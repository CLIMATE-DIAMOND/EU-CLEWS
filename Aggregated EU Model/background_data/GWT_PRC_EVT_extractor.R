# ============================================================
# EU27 TACTIC RASTER WORKFLOW
# - Downloads three TACTIC GeoTIFFs (mm/yr, ~1981–2010)
# - Builds EU-27 polygons (excludes overseas territories)
# - Crops/masks the raster stack to EU extent
# - (9) Integrates Copernicus Land Cover 100 m (2019) and
#       computes per-country × land-cover class means + class areas
# - (10) Computes per-country means (all land covers combined)
# - (11) Exports choropleth maps of national means
# - Outputs CSVs; maps
# ============================================================

# -------------------------------
# 0) Repro defaults (optional)
# -------------------------------
options(stringsAsFactors = FALSE)

# -------------------------------
# 1) >>>>>>>> SET YOUR WORKING DIRECTORY (WD) <<<<<<<<
#    - EDIT ROOT to your own folder path.
#    - On Windows, use forward slashes (/).
# -------------------------------
ROOT <- "C:/Users/scarr/OneDrive - Imperial College London/CCG/CLEWS data/Groundwater recharge"  # <-- CHANGE ME
setwd(ROOT)
cat("Working directory set to:\n", getwd(), "\n\n")

# -------------------------------
# 2) Packages: install + load
# -------------------------------
pkgs <- c(
  # core rasters / vectors
  "terra", "sf",
  # EU borders (Eurostat / GISCO)
  "giscoR",
  # data wrangling
  "dplyr", "purrr", "stringr", "tibble", "tidyr",
  # visualization
  "ggplot2", "scales",
  # csv output (optional)
  "readr"
)
to_install <- setdiff(pkgs, rownames(installed.packages()))
if (length(to_install)) install.packages(to_install, repos = "https://cloud.r-project.org")
invisible(lapply(pkgs, require, character.only = TRUE))

# -------------------------------
# 3) Output root and TACTIC dataset URLs
# -------------------------------
dir_out <- "egdi_tactic_eu27"
dir.create(dir_out, showWarnings = FALSE, recursive = TRUE)

# TACTIC GeoTIFFs (EGDI) — long-term means (LTA ~1981–2010), units mm/year
urls <- c(
  peff_biascorr   = "https://data.geus.dk/egdidatasets/tactic/Effective%20Precipitation%20Biascorrected.tif",
  gwrpot_biascorr = "https://data.geus.dk/egdidatasets/tactic/Potential%20Groundwater%20Recharge%20bias%20corrected.tif",
  aet             = "https://data.geus.dk/egdidatasets/tactic/Actual%20Evapotranspiration.tif"
)

# Helper for tidy filenames
safe_name <- function(x) stringr::str_to_lower(gsub("[^A-Za-z0-9]+", "_", x))

# -------------------------------
# 4) Download the three TACTIC GeoTIFFs (idempotent)
# -------------------------------
tif_paths <- purrr::imap(urls, function(url, nm) {
  fp <- file.path(dir_out, paste0(safe_name(nm), ".tif"))
  if (!file.exists(fp)) {
    message("Downloading: ", nm)
    download.file(url, fp, mode = "wb", quiet = FALSE)
  } else {
    message("Exists: ", fp)
  }
  fp
})

# -------------------------------
# 5) Load rasters and build a multi-layer SpatRaster (stack)
#    - Ensures layers share the same CRS/extent/resolution
# -------------------------------
r_peff <- terra::rast(tif_paths$peff_biascorr)
r_gwr  <- terra::rast(tif_paths$gwrpot_biascorr)
r_aet  <- terra::rast(tif_paths$aet)

# Confirm CRS consistency (typically ETRS89-LAEA / EPSG:3035)
stopifnot(
  terra::crs(r_peff) == terra::crs(r_gwr),
  terra::crs(r_peff) == terra::crs(r_aet)
)

# Build a single multi-layer SpatRaster (avoid base::c making a list)
stk <- terra::rast(list(
  peff_biascorr   = r_peff,
  gwrpot_biascorr = r_gwr,
  aet             = r_aet
))
print(stk); cat("\n")

# -------------------------------
# 6) Get EU-27 borders (GISCO) in EPSG:3035
#    - Robust to column-name differences across giscoR versions
# -------------------------------
eu_raw <- giscoR::gisco_get_countries(
  year = "2024",
  epsg = "3035",
  resolution = "20",   # 1:20M general-purpose
  spatialtype = "RG",  # country regions
  region = "EU"        # EU members (27 as of 2024)
) |>
  sf::st_make_valid()

nm <- names(eu_raw)
pick_first <- function(candidates, nm) {
  m <- intersect(candidates, nm)
  if (length(m) == 0) NA_character_ else m[1]
}
code_col <- pick_first(c("CNTR_CODE", "CNTR_ID", "ISO2_CODE", "ISO3_CODE"), nm)
name_col <- pick_first(c("NAME_ENGL", "NAME_EN", "NAME_ENG", "NAME_ENGLISH", "NAME"), nm)
if (is.na(code_col) || is.na(name_col)) {
  stop("Could not find expected columns for country code or name. Available: ", paste(nm, collapse = ", "))
}

eu27 <- eu_raw |>
  dplyr::rename(CNTR_CODE = !!code_col, NAME_ENGL = !!name_col) |>
  dplyr::select(CNTR_CODE, NAME_ENGL, geometry) |>
  dplyr::arrange(CNTR_CODE)

cat("EU-27 country codes:\n", paste(eu27$CNTR_CODE, collapse = ", "), "\n\n")

# -------------------------------
# 7) Exclude overseas territories (keep continental-Europe neighborhood)
#    - Drops FR/ES/PT outermost regions (Caribbean, Indian Ocean, Azores/Madeira/Canary, etc.)
#    - Optionally drops Spanish enclaves Ceuta/Melilla (North Africa)
# -------------------------------
# 7.1 Explode to individual polygons
eu27_parts <- eu27 |>
  sf::st_cast("MULTIPOLYGON", warn = FALSE) |>
  sf::st_cast("POLYGON", warn = FALSE)

# 7.2 Centroids in WGS84 to apply a geographic filter window
cent_wgs84 <- eu27_parts |>
  sf::st_centroid() |>
  sf::st_transform(4326)
coords <- sf::st_coordinates(cent_wgs84)
eu27_parts$lon <- coords[, "X"]
eu27_parts$lat <- coords[, "Y"]

# 7.3 Keep polygons whose centroid sits inside a "European neighborhood" box
#     lon ∈ [-11, 36], lat ∈ [34, 72]
keep_in_europe <- eu27_parts$lon >= -11 & eu27_parts$lon <= 36 &
  eu27_parts$lat >=  34 & eu27_parts$lat <= 72
eu27_parts_kept <- eu27_parts[keep_in_europe, , drop = FALSE]

# 7.4 Optional: drop Ceuta/Melilla (TRUE to exclude; FALSE to retain)
drop_ceuta_melilla <- TRUE
if (isTRUE(drop_ceuta_melilla)) {
  eu27_parts_kept <- eu27_parts_kept[!(
    eu27_parts_kept$CNTR_CODE == "ES" &
      eu27_parts_kept$lat < 36 & eu27_parts_kept$lat > 34 &
      eu27_parts_kept$lon > -6  & eu27_parts_kept$lon < -1
  ), , drop = FALSE]
}

# 7.5 Re-assemble per-country multipolygons (filtered EU-27)
eu27 <- eu27_parts_kept |>
  dplyr::select(CNTR_CODE, NAME_ENGL, geometry) |>
  dplyr::group_by(CNTR_CODE, NAME_ENGL) |>
  dplyr::summarise(geometry = sf::st_union(geometry), .groups = "drop") |>
  sf::st_make_valid()

cat("Filtered EU-27 retained (after removing overseas territories):\n",
    paste(eu27$CNTR_CODE, collapse = ", "), "\n\n")

# -------------------------------
# 8) Crop & mask the raster stack to EU-27 extent (speeds up subsequent ops)
# -------------------------------
eu_union   <- sf::st_union(eu27)
eu_union_v <- terra::vect(eu_union)

stk_eu <- terra::crop(stk, eu_union_v, snap = "out")
stk_eu <- terra::mask(stk_eu, eu_union_v)
print(stk_eu); cat("\n")

# ======================================================================
# 9) Land Cover integration (CGLS LC100 v3, epoch 2019, discrete map)
#    Goal: per-country × land-cover class means (mm/yr) + class area (km²)
# ======================================================================

# 9.1 Download (robust) ------------------------------------------------
lc_dir <- file.path(dir_out, "landcover")
dir.create(lc_dir, showWarnings = FALSE, recursive = TRUE)

lc_url <- "https://zenodo.org/records/3939050/files/PROBAV_LC100_global_v3.0.1_2019-nrt_Discrete-Classification-map_EPSG-4326.tif?download=1"
lc_tif <- file.path(lc_dir, "CGLS_LC100_2019_discrete_epsg4326.tif")

if (!file.exists(lc_tif)) {
  message("Downloading CGLS LC100 2019 (≈1.7 GB). This can take a while…")
  old_to <- getOption("timeout"); options(timeout = max(3600, old_to))
  ok <- FALSE
  
  if (requireNamespace("curl", quietly = TRUE)) {
    # via curl package (supports resume)
    try({
      h <- curl::new_handle()
      curl::handle_setopt(h, followlocation = TRUE, connecttimeout = 300,
                          low_speed_time = 120, low_speed_limit = 1024)
      tmp <- paste0(lc_tif, ".part")
      if (file.exists(tmp)) curl::handle_setopt(h, resume_from = file.size(tmp))
      curl::curl_download(lc_url, destfile = tmp, handle = h, mode = "wb")
      file.rename(tmp, lc_tif)
      ok <- TRUE
    }, silent = TRUE)
  }
  if (!ok && nzchar(Sys.which("curl"))) {
    # system curl with resume
    cmd <- sprintf('curl -L --retry 10 --retry-delay 10 -C - -o "%s" "%s"', lc_tif, lc_url)
    ok <- system(cmd) == 0 && file.exists(lc_tif)
  }
  options(timeout = old_to)
  if (!ok) stop("Land-cover download failed after retries. Try again later (or install 'curl').")
} else {
  message("Exists: ", lc_tif)
}

# 9.2 Read, project to stk_eu grid (EPSG:3035), crop/mask to EU ----------
lc_raw  <- terra::rast(lc_tif)                              # EPSG:4326, integer codes
lc_3035 <- terra::project(lc_raw, stk_eu, method = "near")  # keep integer classes
eu_un   <- terra::vect(sf::st_union(eu27))
lc_eu   <- terra::mask(terra::crop(lc_3035, eu_un, snap = "out"), eu_un)

# Optional: save aligned EU LC raster for reuse
terra::writeRaster(lc_eu, file.path(lc_dir, "CGLS_LC100_2019_discrete_epsg3035_EU.tif"), overwrite = TRUE)

# 9.3 Per-country × land-cover class means (mm/yr) ----------------------
zonal_country_means <- function(ctry_row) {
  code <- ctry_row$CNTR_CODE; name <- ctry_row$NAME_ENGL
  poly <- terra::vect(sf::st_geometry(ctry_row))
  
  # crop/mask variables & zones to country
  x_ctry <- terra::mask(terra::crop(stk_eu, poly, snap = "out"), poly)  # 3 layers
  z_ctry <- terra::mask(terra::crop(lc_eu,  poly, snap = "out"), poly)  # class codes
  
  # mean for each variable by LC class
  mean_by_class <- function(v) {
    z <- terra::zonal(x_ctry[[v]], z_ctry, fun = "mean", na.rm = TRUE)
    names(z) <- c("lc_class_code", paste0(v, "_mean_mm_yr"))
    z
  }
  
  out <- Reduce(function(a, b) merge(a, b, by = "lc_class_code", all = TRUE),
                list(mean_by_class("peff_biascorr"),
                     mean_by_class("gwrpot_biascorr"),
                     mean_by_class("aet")))
  
  out <- out[!is.na(out$lc_class_code) & out$lc_class_code > 0, , drop = FALSE]
  out$CNTR_CODE <- code; out$NAME_ENGL <- name
  out[, c("CNTR_CODE","NAME_ENGL","lc_class_code",
          "peff_biascorr_mean_mm_yr","gwrpot_biascorr_mean_mm_yr","aet_mean_mm_yr")]
}
lc_stats <- dplyr::bind_rows(purrr::map(split(eu27, seq_len(nrow(eu27))), zonal_country_means))

# 9.4 Add class area per country (km²) ---------------------------------
area_m2 <- terra::cellSize(stk_eu, unit = "m")[[1]]  # equal-area grid ⇒ one band is enough

lc_area_country <- function(ctry_row) {
  code <- ctry_row$CNTR_CODE; name <- ctry_row$NAME_ENGL
  poly <- terra::vect(sf::st_geometry(ctry_row))
  
  a_ctry <- terra::mask(terra::crop(area_m2, poly, snap = "out"), poly)  # m²
  z_ctry <- terra::mask(terra::crop(lc_eu,   poly, snap = "out"), poly)  # LC classes
  
  ta <- terra::zonal(a_ctry, z_ctry, fun = "sum", na.rm = TRUE)         # m² per class
  names(ta) <- c("lc_class_code","area_m2")
  ta <- ta[!is.na(ta$lc_class_code) & ta$lc_class_code > 0, , drop = FALSE]
  
  transform(ta,
            CNTR_CODE = code, NAME_ENGL = name,
            class_area_km2 = area_m2 / 1e6)[, c("CNTR_CODE","NAME_ENGL","lc_class_code","class_area_km2")]
}
areas_tbl <- dplyr::bind_rows(purrr::map(split(eu27, seq_len(nrow(eu27))), lc_area_country))

# 9.5 Attach class names (robust to unknown codes) ----------------------
# Force integer key to avoid type-mismatch joins
lc_stats$lc_class_code  <- as.integer(lc_stats$lc_class_code)
areas_tbl$lc_class_code <- as.integer(areas_tbl$lc_class_code)

present_codes <- sort(unique(lc_stats$lc_class_code))
present_codes <- present_codes[!is.na(present_codes) & present_codes > 0]

known_map <- c(
  `10`="Tree cover", `20`="Shrubland", `30`="Herbaceous vegetation", `40`="Cropland",
  `50`="Built-up",   `60`="Bare / sparse vegetation", `70`="Snow & ice",
  `80`="Permanent water bodies", `90`="Herbaceous wetland", `95`="Mangroves",
  `100`="Moss & lichen",
  `111`="Closed forest — evergreen needleleaf", `112`="Closed forest — evergreen broadleaf",
  `113`="Closed forest — deciduous needleleaf", `114`="Closed forest — deciduous broadleaf",
  `115`="Closed forest — mixed", `116`="Closed forest — unknown",
  `121`="Open forest — evergreen needleleaf", `122`="Open forest — evergreen broadleaf",
  `123`="Open forest — deciduous needleleaf", `124`="Open forest — deciduous broadleaf",
  `125`="Open forest — mixed", `126`="Open forest — unknown",
  `200`="Open sea"
)

lc_legend <- tibble::tibble(
  lc_class_code = as.integer(present_codes),
  lc_class_name = dplyr::recode(as.character(present_codes), !!!known_map,
                                .default = paste0("Class ", present_codes))
)

# 9.6 Merge means + areas + names; write CSV ----------------------------
lc_stats_with_area <- lc_stats |>
  dplyr::left_join(areas_tbl, by = c("CNTR_CODE","NAME_ENGL","lc_class_code")) |>
  dplyr::left_join(lc_legend, by = "lc_class_code") |>
  dplyr::relocate(CNTR_CODE, NAME_ENGL, lc_class_code, lc_class_name, class_area_km2)

lc_csv_area <- file.path(dir_out, "eu27_landcover_class_means_mm_per_year_2019_WITH_AREA.csv")
if (requireNamespace("readr", quietly = TRUE)) {
  readr::write_csv(lc_stats_with_area, lc_csv_area)
} else {
  write.csv(lc_stats_with_area, lc_csv_area, row.names = FALSE)
}
cat("Wrote land-cover class means + area -> ", normalizePath(lc_csv_area), "\n\n")

# ======================================================================
# 10) National means + consistency check against LC-weighted means
#     (Outputs: national means CSV, comparison CSV)
# ======================================================================

# 10.1 National means (direct from raster; mm/yr) -----------------------
stats_mat <- terra::extract(
  stk_eu, terra::vect(eu27),
  fun = mean, na.rm = TRUE, ID = FALSE
)
stats_tbl <- tibble::as_tibble(stats_mat)

meta_tbl <- sf::st_drop_geometry(eu27) |>
  dplyr::select(CNTR_CODE, NAME_ENGL)

stats <- dplyr::bind_cols(meta_tbl, stats_tbl) |>
  dplyr::relocate(CNTR_CODE, NAME_ENGL)

print(stats)

csv_out <- file.path(dir_out, "eu27_country_means_mm_per_year.csv")
if (requireNamespace("readr", quietly = TRUE)) {
  readr::write_csv(stats, csv_out)
} else {
  write.csv(stats, csv_out, row.names = FALSE)
}
cat("10.1 ✓ Wrote national means CSV -> ", normalizePath(csv_out), "\n\n")

# 10.2 Consistency check:
#      LC class means weighted by VALID area (per variable) vs direct national means
#      This uses, for each country & class, the count of non-NA pixels in each variable
#      as weights, which matches the denominator used by terra::extract(..., na.rm=TRUE).

# helper to count valid pixels by class for a given variable in one country
.valid_counts_by_class <- function(x_ctry_band, z_ctry) {
  # Logical raster of non-NA pixels; TRUE=1, NA stays NA -> zonal(sum, na.rm=TRUE) counts valids
  ok <- !is.na(x_ctry_band)
  cnt <- terra::zonal(ok, z_ctry, fun = "sum", na.rm = TRUE)   # count of valid cells per class
  names(cnt) <- c("lc_class_code", "n_valid")
  cnt$lc_class_code <- as.integer(cnt$lc_class_code)
  cnt
}

# compute weighted means per country using valid counts as weights
wgt_means_valid <- purrr::map_dfr(
  split(eu27, seq_len(nrow(eu27))),
  function(ctry_row) {
    code <- ctry_row$CNTR_CODE; name <- ctry_row$NAME_ENGL
    poly <- terra::vect(sf::st_geometry(ctry_row))
    
    # crop/mask once per country
    x_ctry <- terra::mask(terra::crop(stk_eu, poly, snap = "out"), poly)  # peff/gwr/aet
    z_ctry <- terra::mask(terra::crop(lc_eu,  poly, snap = "out"), poly)  # LC classes
    
    # valid counts per class for each variable
    cnt_peff <- .valid_counts_by_class(x_ctry[["peff_biascorr"]],   z_ctry)
    cnt_gwr  <- .valid_counts_by_class(x_ctry[["gwrpot_biascorr"]], z_ctry)
    cnt_aet  <- .valid_counts_by_class(x_ctry[["aet"]],             z_ctry)
    
    # class means for this country (already computed in Step 9)
    lc_means_ctry <- dplyr::filter(lc_stats, CNTR_CODE == code) |>
      dplyr::select(lc_class_code,
                    peff_biascorr_mean_mm_yr,
                    gwrpot_biascorr_mean_mm_yr,
                    aet_mean_mm_yr)
    
    # join counts to class means; compute weighted mean = sum(mean * n_valid) / sum(n_valid)
    j_peff <- dplyr::left_join(lc_means_ctry, cnt_peff, by = "lc_class_code")
    j_gwr  <- dplyr::left_join(lc_means_ctry, cnt_gwr,  by = "lc_class_code", suffix = c("", "_gwr"))
    j_aet  <- dplyr::left_join(lc_means_ctry, cnt_aet,  by = "lc_class_code", suffix = c("", "_aet"))
    
    wm_peff <- with(j_peff, stats::weighted.mean(peff_biascorr_mean_mm_yr, n_valid, na.rm = TRUE))
    wm_gwr  <- with(j_gwr,  stats::weighted.mean(gwrpot_biascorr_mean_mm_yr, n_valid, na.rm = TRUE))
    wm_aet  <- with(j_aet,  stats::weighted.mean(aet_mean_mm_yr,             n_valid, na.rm = TRUE))
    
    tibble::tibble(
      CNTR_CODE = code, NAME_ENGL = name,
      peff_biascorr_wmean_mm_yr   = wm_peff,
      gwrpot_biascorr_wmean_mm_yr = wm_gwr,
      aet_wmean_mm_yr             = wm_aet
    )
  }
)

# Join with direct national means and compute differences
compare_means <- stats |>
  dplyr::left_join(wgt_means_valid, by = c("CNTR_CODE","NAME_ENGL")) |>
  dplyr::mutate(
    # absolute differences (weighted - direct), mm/yr
    peff_diff_mm = peff_biascorr_wmean_mm_yr   - peff_biascorr,
    gwr_diff_mm  = gwrpot_biascorr_wmean_mm_yr - gwrpot_biascorr,
    aet_diff_mm  = aet_wmean_mm_yr             - aet,
    # relative differences (% of direct)
    peff_diff_pct = dplyr::if_else(is.finite(peff_biascorr) & peff_biascorr != 0,
                                   100 * peff_diff_mm / peff_biascorr, NA_real_),
    gwr_diff_pct  = dplyr::if_else(is.finite(gwrpot_biascorr) & gwrpot_biascorr != 0,
                                   100 * gwr_diff_mm  / gwrpot_biascorr, NA_real_),
    aet_diff_pct  = dplyr::if_else(is.finite(aet) & aet != 0,
                                   100 * aet_diff_mm  / aet, NA_real_)
  ) |>
  dplyr::relocate(CNTR_CODE, NAME_ENGL)

print(compare_means)

# Summary table: largest absolute % differences (should be tiny)
summary_diffs <- compare_means |>
  tidyr::pivot_longer(c(peff_diff_pct, gwr_diff_pct, aet_diff_pct),
                      names_to = "variable", values_to = "diff_pct") |>
  dplyr::group_by(CNTR_CODE, NAME_ENGL) |>
  dplyr::summarise(max_abs_diff_pct = max(abs(diff_pct), na.rm = TRUE), .groups = "drop") |>
  dplyr::arrange(dplyr::desc(max_abs_diff_pct))

cat("10.2 ✓ Max absolute % difference by country (valid-area weights):\n")
print(summary_diffs, n = 27)

# ======================================================================
# 11) Maps — national choropleths of mean values
# ======================================================================

eu27_stats <- eu27 |>
  dplyr::left_join(stats, by = c("CNTR_CODE","NAME_ENGL"))

nice_names <- c(
  peff_biascorr   = "Effective Precipitation (bias-corr.)",
  gwrpot_biascorr = "Potential Groundwater Recharge (bias-corr.)",
  aet             = "Actual Evapotranspiration"
)

maps_dir <- file.path(dir_out, "maps")
dir.create(maps_dir, showWarnings = FALSE, recursive = TRUE)

# Minimal, publication-friendly map theme
theme_map <- function() {
  ggplot2::theme_void(base_size = 12) +
    ggplot2::theme(
      plot.title = ggplot2::element_text(face = "bold", hjust = 0),
      plot.subtitle = ggplot2::element_text(color = "grey20"),
      legend.position = "right",
      legend.title = ggplot2::element_text(size = 10),
      legend.text  = ggplot2::element_text(size = 9),
      panel.grid.major = ggplot2::element_line(color = "grey92", linewidth = 0.2)
    )
}

# Single-variable map saver
plot_var <- function(var, file) {
  gg <- ggplot2::ggplot(eu27_stats) +
    ggplot2::geom_sf(ggplot2::aes(fill = .data[[var]]), color = "white", linewidth = 0.2) +
    ggplot2::scale_fill_viridis_c(
      name = paste0(nice_names[[var]], " (mm/yr)"),
      na.value = "grey85",
      labels = scales::label_number(accuracy = 1)
    ) +
    ggplot2::labs(
      title = nice_names[[var]],
      subtitle = "EU-27 national means, 1981–2010",
      caption = "Rasters: TACTIC (EGDI). Boundaries: © EuroGeographics (GISCO/Eurostat)."
    ) +
    ggplot2::coord_sf(crs = sf::st_crs(3035)) +
    theme_map()
  
  ggplot2::ggsave(file, gg, width = 9, height = 7, dpi = 300, bg = "white")
  message("Saved map: ", file)
}

# Save the three choropleths
plot_var("peff_biascorr",   file.path(maps_dir, "eu27_mean_peff_biascorr.png"))
plot_var("gwrpot_biascorr", file.path(maps_dir, "eu27_mean_gwrpot_biascorr.png"))
plot_var("aet",             file.path(maps_dir, "eu27_mean_aet.png"))

# Faceted overview (all variables in one figure)
eu27_long <- eu27_stats |>
  tidyr::pivot_longer(
    cols = c("peff_biascorr","gwrpot_biascorr","aet"),
    names_to = "variable", values_to = "value"
  ) |>
  dplyr::mutate(variable = factor(variable, levels = names(nice_names), labels = unname(nice_names)))

gg_facets <- ggplot2::ggplot(eu27_long) +
  ggplot2::geom_sf(ggplot2::aes(fill = value), color = "white", linewidth = 0.2) +
  ggplot2::scale_fill_viridis_c(
    name = "mm/yr",
    na.value = "grey85",
    labels = scales::label_number(accuracy = 1)
  ) +
  ggplot2::labs(
    title = "EU-27 national mean values",
    subtitle = "1981–2010",
    caption = "Rasters: TACTIC (EGDI). Boundaries: © EuroGeographics (GISCO/Eurostat)."
  ) +
  ggplot2::coord_sf(crs = sf::st_crs(3035)) +
  ggplot2::facet_wrap(~ variable, ncol = 1) +
  theme_map() +
  ggplot2::theme(legend.position = "right")

facet_out <- file.path(maps_dir, "eu27_means_faceted.png")
ggplot2::ggsave(facet_out, gg_facets, width = 9, height = 18, dpi = 300, bg = "white")
cat("11 ✓ Saved maps ->", normalizePath(maps_dir), "\n\n")

# -------------------------------
# 12) Done
# -------------------------------
cat("All outputs in:\n", normalizePath(dir_out), "\n\n")

cat("Attribution:\n",
    "  • Rasters (climate): TACTIC (EGDI).\n",
    "  • Boundaries: © EuroGeographics (GISCO/Eurostat).\n",
    "  • Land cover: Copernicus Global Land Service — Land Cover 100 m (CGLS-LC100), ",
    "Collection 3, epoch 2019, discrete classification (CGLS-LC100 v3). ",
    "© European Union; produced by the Copernicus Programme (ESA and partners). ",
    "Downloaded from Zenodo, reprojected to ETRS89-LAEA (EPSG:3035) and clipped to the EU-27 footprint for this analysis.\n",
    sep = "")

cat("\nLand-cover notes:\n",
    "  - Native resolution: 100 m; aligned to the TACTIC grid via nearest-neighbour resampling (to preserve class codes).\n",
    "  - Classes: LCCS-based discrete classes; see columns `lc_class_code` and `lc_class_name` in the CSV output.\n",
    "  - Saved raster (aligned to EU extent): ",
    normalizePath(file.path(dir_out, "landcover", "CGLS_LC100_2019_discrete_epsg3035_EU.tif")),
    "\n",
    sep = ""
)
