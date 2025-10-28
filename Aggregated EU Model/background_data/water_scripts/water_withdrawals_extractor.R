# =====================================================================
# EU27 national water use from Zenodo NetCDFs (exact_extract sums)
# Outputs -> to your chosen file directory
# QA: checks country-level domestic/industrial withdrawals (ww) and consumption (wc) sum to EU27 total
#
# What this script does:
#  1) Loads required packages.
#  2) Sets your designated folder as the working location and prepares subfolders.
#  3) Builds clean EU27 country polygons (sf) from GISCO (2024).
#  4) Defines the list of 10 NetCDF files to download (historical + SSPs; domestic + industrial).
#  5) Extracts national totals for each year and metric using exactextractr::exact_extract(..., "sum"),
#     which splits boundary cells proportionally by area overlap with each country polygon.
#  6) Runs QA that compares the EU union total for a metric with the sum of the 27 countries
#     for that same metric and year (they should match ~exactly).
#  7) Saves three tidy CSVs: long format, EU totals, and a country-year wide format.
# =====================================================================

# ---------------------------------------------------------------------
# 1) Load packages (quietly). If you’re missing any, uncomment install line.
# ---------------------------------------------------------------------
# install.packages(c("sf","terra","exactextractr","giscoR","countrycode",
#                    "dplyr","purrr","readr","stringr","tidyr","tibble"))

suppressPackageStartupMessages({
  library(sf)            # vector (polygon) geodata handling
  library(terra)         # raster/NetCDF reading
  library(exactextractr) # area-weighted raster extraction by polygons
  library(giscoR)        # EU country boundaries from GISCO
  library(countrycode)   # ISO2 -> ISO3 conversions
  library(dplyr)         # data wrangling
  library(purrr)         # mapping over lists/years
  library(readr)         # fast CSV read/write
  library(stringr)       # string helpers
  library(tidyr)         # reshaping data
  library(tibble)        # tidy tibbles
})

# ---------------------------------------------------------------------
# 2) Set base directories (Windows) and ensure they exist
# ---------------------------------------------------------------------
# >>> REQUIRED: Set your local base folder (where NetCDFs download and CSVs are written).
# Use a path you can write to. Examples:
#   Windows: "C:/Users/<you>/Documents/EU27_water"
#   macOS/Linux: "/Users/<you>/EU27_water"
# If using OneDrive/Dropbox, point to a folder inside it.

base_dir <- normalizePath("C:/Users/scarr/OneDrive - Imperial College London/CCG/CLEWS data")
data_dir <- file.path(base_dir, "data_nc")  # where NetCDFs will be stored
out_dir  <- file.path(base_dir, "out")      # where CSV outputs will be written

dir.create(data_dir, showWarnings = FALSE, recursive = TRUE)
dir.create(out_dir,  showWarnings = FALSE, recursive = TRUE)

# ---------------------------------------------------------------------
# 3) Build EU27 polygons (returns an sf with 27 country features)
#    - Pulls GISCO countries at 2024 vintage, EPSG:4326 (lon/lat)
#    - Normalizes Greece code (EL -> GR), attaches ISO3 and name
#    - Ensures geometries are valid and each country is a single (multi)polygon
# ---------------------------------------------------------------------
build_eu27 <- function() {
  # ISO2 codes of current EU27
  eu27_iso2 <- c("AT","BE","BG","HR","CY","CZ","DK","EE","FI","FR","DE","GR","HU","IE",
                 "IT","LV","LT","LU","MT","NL","PL","PT","RO","SK","SI","ES","SE")
  
  # Download country boundaries (resolution "1" ~ coarse but light; good for national aggregation)
  g0 <- giscoR::gisco_get_countries(resolution = "1", year = "2024", epsg = 4326)
  
  # Locate the relevant attributes (GISCO field names sometimes differ by version)
  iso2_col <- if ("ISO2_CODE" %in% names(g0)) "ISO2_CODE" else if ("CNTR_ID" %in% names(g0)) "CNTR_ID" else NA
  name_col <- if ("NAME_ENGL" %in% names(g0)) "NAME_ENGL" else if ("CNTR_NAME" %in% names(g0)) "CNTR_NAME" else NA
  stopifnot(!is.na(iso2_col), !is.na(name_col))
  
  # Normalize ISO2 (GISCO uses "EL" for Greece; convert to "GR")
  iso2_std <- ifelse(g0[[iso2_col]] == "EL", "GR", g0[[iso2_col]])
  
  # Keep only the columns we need (name, ISO2, ISO3, geometry), fix invalid geometries
  g <- g0 |>
    mutate(
      iso2 = iso2_std,
      iso3 = countrycode::countrycode(iso2_std, "iso2c", "iso3c", warn = FALSE),
      name = .data[[name_col]]
    ) |>
    dplyr::select(name, iso2, iso3, geometry) |>
    st_make_valid()
  
  # Filter to EU27 and consolidate geometry per country
  eu <- g |>
    filter(iso2 %in% eu27_iso2) |>
    st_cast("MULTIPOLYGON", warn = FALSE) |>
    group_by(iso2, iso3, name) |>
    summarise(geometry = st_union(geometry), .groups = "drop") |>
    st_make_valid()
  
  # Sanity check: we must end with 27 rows/features
  stopifnot(nrow(eu) == 27)
  eu
}

# Build the EU27 layer once (used by all extractions)
eu_countries <- build_eu27()
message("EU27 features: ", nrow(eu_countries))  # expect 27

# ---------------------------------------------------------------------
# 4) Helper: derive the list of years a file contains
#    - Uses filename (e.g., "..._1960_2020.nc") if present, else falls back to #layers
# ---------------------------------------------------------------------
.file_years <- function(r, nc_path) {
  m <- regmatches(nc_path, regexec("(\\d{4})_(\\d{4})\\.nc$", nc_path))[[1]]
  if (length(m) == 3) {
    seq.int(as.integer(m[2]), as.integer(m[3]))
  } else {
    seq_len(terra::nlyr(r))
  }
}

# ---------------------------------------------------------------------
# 5) List the 10 NetCDF targets and download if missing
#    - Each file has a 'dom' or 'ind' sector and a scenario (historical or SSPx)
# ---------------------------------------------------------------------
base <- "https://zenodo.org/records/13767595/files"
targets <- tribble(
  ~scenario,   ~sector, ~file,
  "historical","dom",   "historical_dom_year_millionm3_5min_Europe_1960_2020.nc",
  "historical","ind",   "historical_ind_year_millionm3_5min_Europe_1960_2020.nc",
  "ssp1",      "dom",   "ssp1_dom_year_millionm3_5min_Europe_2020_2100.nc",
  "ssp1",      "ind",   "ssp1_ind_year_millionm3_5min_Europe_2020_2100.nc",
  "ssp2",      "dom",   "ssp2_dom_year_millionm3_5min_Europe_2020_2100.nc",
  "ssp2",      "ind",   "ssp2_ind_year_millionm3_5min_Europe_2020_2100.nc",
  "ssp3",      "dom",   "ssp3_dom_year_millionm3_5min_Europe_2020_2100.nc",
  "ssp3",      "ind",   "ssp3_ind_year_millionm3_5min_Europe_2020_2100.nc",
  "ssp5",      "dom",   "ssp5_dom_year_millionm3_5min_Europe_2020_2100.nc",
  "ssp5",      "ind",   "ssp5_ind_year_millionm3_5min_Europe_2020_2100.nc"
) |>
  mutate(
    url  = file.path(base, file),        # download URL
    dest = file.path(data_dir, file)     # local destination path
  )

# Download any file that’s not present locally
for (i in seq_len(nrow(targets))) {
  if (!file.exists(targets$dest[i])) {
    message(sprintf("Downloading (%d/%d): %s", i, nrow(targets), targets$file[i]))
    utils::download.file(targets$url[i], targets$dest[i], mode = "wb", quiet = TRUE)
  }
}

# ---------------------------------------------------------------------
# 6) Core extractor: national totals from a NetCDF (exact_extract sums)
#    - Reads the 'ww' (withdrawals) and 'wc' (consumption) subdatasets
#    - For each year/layer: sums the raster within each country polygon
#    - exact_extract(..., "sum") splits partial cells by overlap fraction,
#      so boundary cells are allocated proportionally to each country
# ---------------------------------------------------------------------
extract_country_totals_exact <- function(nc_path, scenario, sector, countries_sf,
                                         test_mode = FALSE) {
  # Basic checks
  stopifnot(file.exists(nc_path))
  stopifnot(inherits(countries_sf, "sf"), all(c("name","iso3") %in% names(countries_sf)))
  
  # Identify the netCDF variable names for this sector
  var_ww <- paste0(sector, "ww")  # e.g., "domww" or "indww"
  var_wc <- paste0(sector, "wc")  # e.g., "domwc" or "indwc"
  
  # Open as SpatRaster (terra reads NetCDF subdatasets via 'subds')
  r_ww <- terra::rast(nc_path, subds = var_ww)
  r_wc <- terra::rast(nc_path, subds = var_wc)
  
  # If CRS metadata is absent, assume geographic lon/lat WGS84
  if (is.na(terra::crs(r_ww))) terra::crs(r_ww) <- "EPSG:4326"
  
  # Which years are in the file?
  years_all <- .file_years(r_ww, nc_path)
  lyr_ids   <- seq_along(years_all)
  if (isTRUE(test_mode)) lyr_ids <- head(lyr_ids, 5)  # fast trial run
  
  # Compute EU union geometry once (s2 on for robust geodesic union)
  old_s2 <- sf::sf_use_s2(TRUE)
  eu_union <- sf::st_union(sf::st_transform(countries_sf, 4326))
  sf::sf_use_s2(old_s2)
  
  # Helper: extract sums for one raster stack (ww or wc)
  extract_stack <- function(r_stack, metric_label) {
    map_dfr(lyr_ids, function(i) {
      if (i %% 5 == 1) message(sprintf("  • %s year %d/%d", metric_label, i, length(lyr_ids)))
      lyr <- r_stack[[i]]
      
      # Country totals (vector of length 27). exact_extract returns area-weighted sums.
      vals_ctry <- as.numeric(exactextractr::exact_extract(lyr, countries_sf, "sum"))
      
      # One-time sanity print (compare EU union vs sum of all countries for this metric)
      if (i == min(lyr_ids)) {
        union_sum <- exactextractr::exact_extract(lyr, eu_union, "sum")[[1]]
        cat(sprintf("[check %s y=%d] union=%.2f  sum(countries)=%.2f  rel_diff=%.3f%%\n",
                    metric_label, years_all[i], union_sum, sum(vals_ctry, na.rm = TRUE),
                    100 * (sum(vals_ctry, na.rm = TRUE) / union_sum - 1)))
      }
      
      # Return a tidy table for this year and metric
      tibble(
        country = countries_sf$name,
        iso3    = countries_sf$iso3,
        year    = years_all[i],
        metric  = metric_label,                # "ww" or "wc"
        value_million_m3 = vals_ctry           # units from file (million m3 per year)
      )
    })
  }
  
  # Build the long table for both metrics, add file/scenario/sector labels
  bind_rows(
    extract_stack(r_ww, "ww"),
    extract_stack(r_wc, "wc")
  ) |>
    mutate(
      source_file = basename(nc_path),
      scenario = scenario,
      sector   = sector
    ) |>
    relocate(source_file, country, iso3, year, scenario, sector, metric, value_million_m3)
}

# ---------------------------------------------------------------------
# 7) QA: metric-aware union vs. sum(countries)
#    - For selected years, calculates EU union total and compares only
#      to the country totals for the SAME metric (ww or wc)
#    - Prints rows for both metrics so mixups are obvious
# ---------------------------------------------------------------------
qa_assert_exact_both <- function(nc_path, sector, scenario, eu_sf, results_df,
                                 years_to_check = NULL, tol_pct = 0.1) {
  # Open both subdatasets for this sector
  r_ww <- terra::rast(nc_path, subds = paste0(sector, "ww"))
  r_wc <- terra::rast(nc_path, subds = paste0(sector, "wc"))
  if (is.na(terra::crs(r_ww))) terra::crs(r_ww) <- "EPSG:4326"
  
  # Choose which years to check (default: first four)
  years_all <- .file_years(r_ww, nc_path)
  if (is.null(years_to_check)) years_to_check <- head(years_all, 4)
  idx <- match(years_to_check, years_all); stopifnot(!anyNA(idx))
  
  # EU union geometry
  old_s2 <- sf::sf_use_s2(TRUE)
  eu_union <- sf::st_union(sf::st_transform(eu_sf, 4326))
  sf::sf_use_s2(old_s2)
  
  # If results_df contains multiple files, keep only rows from this one
  if ("source_file" %in% names(results_df)) {
    results_df <- dplyr::filter(results_df, .data$source_file == basename(nc_path))
  }
  
  # Helper that checks a single metric stack (ww or wc)
  one_metric <- function(r, metric_label) {
    purrr::map_dfr(seq_along(idx), function(k) {
      i <- idx[k]; y <- years_all[i]
      
      # EU union: area-weighted sum
      union_sum <- exactextractr::exact_extract(r[[i]], eu_union, "sum")[[1]]
      
      # Sum of country totals for this metric/year/scenario/sector
      res_sum <- results_df %>%
        dplyr::filter(year == y, scenario == scenario, sector == sector, metric == metric_label) %>%
        dplyr::summarise(val = sum(value_million_m3, na.rm = TRUE), .groups = "drop") %>%
        dplyr::pull(val)
      
      tibble::tibble(
        metric = metric_label,
        year = y,
        union = union_sum,
        sum_countries = res_sum,
        rel_diff_pct = 100 * (res_sum / union_sum - 1)
      )
    })
  }
  
  # Build the QA table for both metrics and print
  out <- dplyr::bind_rows(
    one_metric(r_ww, "ww"),
    one_metric(r_wc, "wc")
  )
  print(out)
  
  # Enforce tolerance: all rows must be within ±tol_pct
  stopifnot(all(abs(out$rel_diff_pct) < tol_pct))
  invisible(out)
}

# ---------------------------------------------------------------------
# 8) RUN: iterate through all 10 files, extract results, run QA, save CSVs
#    - Set TEST_MODE <- TRUE to process only the first 5 years of each file
# ---------------------------------------------------------------------
TEST_MODE <- FALSE  # change to TRUE for a quick, partial run

results <- pmap_dfr(targets, function(scenario, sector, file, url, dest) {
  message("Processing: ", file)
  
  # Extract country totals for both metrics
  df <- extract_country_totals_exact(dest, scenario, sector, eu_countries, test_mode = TEST_MODE)
  
  # Ensure one row per (file, country, year, scenario, sector, metric)
  df <- df |>
    group_by(source_file, country, iso3, year, scenario, sector, metric) |>
    summarise(value_million_m3 = sum(value_million_m3, na.rm = TRUE), .groups = "drop")
  
  # QA on a few years: checks ww and wc separately
  ycheck <- if (scenario == "historical") c(1960, 1980, 2000, 2020) else c(2020, 2050, 2100)
  qa_assert_exact_both(dest, sector, scenario, eu_countries, df, years_to_check = intersect(ycheck, df$year))
  
  df
})

# ---------------------------------------------------------------------
# 9) Save outputs (long, EU totals, and wide)
# ---------------------------------------------------------------------

# Long format: one row per (file, country, iso3, year, scenario, sector, metric)
write_csv(results, file.path(out_dir, "EU27_water_ww_wc_by_country_year.csv"))

# EU27 totals: sum over countries (useful for quick EU checks/plots)
eu_totals <- results |>
  group_by(source_file, year, scenario, sector, metric) |>
  summarise(value_million_m3 = sum(value_million_m3, na.rm = TRUE), .groups = "drop")
write_csv(eu_totals, file.path(out_dir, "EU27_totals_by_year_sector_metric.csv"))

# Wide format: country-year with columns like historical_domww, ssp1_indwc, etc.
wide <- results |>
  select(-source_file) |>
  unite("var", sector, metric, remove = TRUE) |>
  pivot_wider(names_from = c(scenario, var), values_from = value_million_m3)
write_csv(wide, file.path(out_dir, "EU27_country_year_wide.csv"))

message("Done. CSVs in: ", out_dir)

# =====================================================================
# End of script
# =====================================================================

