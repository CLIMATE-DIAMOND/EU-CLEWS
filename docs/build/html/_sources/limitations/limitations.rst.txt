Overview
==========================

Several weaknesses were identified during the development of the final version of the CLEWs-EU model. 
The following points summarise the main items that can be addressed either within the DIAMOND project’s 
lifetime or in future model updates:

a) **Computational intensity**  
   The disaggregated CLEWs-EU model is highly computationally intensive.  
   The underlying OSeMOSYS code could be revised to reduce computational effort, which would allow 
   additional detail to be incorporated where necessary.

b) **Model documentation**  
   The available documentation will continue to be improved to provide more detail on:
   
   - the structure of each individual sector,  
   - adopted input data and assumptions, and  
   - detailed guidelines for using the model.  

   These improvements will be guided by feedback from the broader OSeMOSYS and CLEWs communities.

The subsections below provide further detail on potential improvements to the disaggregated CLEWs-EU 
model within each of the two main modules.

Energy module
===============
The following weaknesses have been identified in the energy module.

• Dependence of the base year definition on the JRC-IDEES 2021 database has in certain cases limited the level of detail included in the model. For instance, in the road transport sector no differentiation between gasoline and gasoline-hybrid vehicles is given in the database; only plug-in hybrid vehicles are separately mentioned. To address this, data from Eurostat have also been used. However, in other cases, such as for industrial energy demand, no differentiation between biomass and waste is provided. Even though, national energy balances provide more detailed information on the final energy demand by fuel type and sector, the equivalent information regarding useful energy demand was not readily available, so the team kept the aggregated category “biomass and waste”.

• The results of the baseline scenario do not show considerable investments in electricity storage, with the exception of Cyprus, which currently operates an isolated grid system. This may be due to the low temporal resolution within each year, which potentially does not adequately capture peaks in demand and variable renewable energy generation. The team has tested the model with a considerably lower capital cost to see if the technologies appear in the solution, and indeed they do so. As such, the adopted cost assumptions may be too high or due to the fact that we have not forced the model to fully decarbonise, the storage requirements are deemed to be low. At the same time, it is possible that the rise in the production of hydrogen through electrolysis has contributed to the lower need for storage investments.

• The non-energy greenhouse gas emissions of industrial processes are not captured by the adopted structure of the CLEWs-EU model. Since the required level of detail is difficult to implement, we do not attempt to make projections that would be highly uncertain.

• As the CLEWs-EU model is developed in the OSeMOSYS modelling framework, it relies on exogenous demand projections. This means that future demand for energy services (e.g., mobility, space cooling/heating, useful heat in industry etc.) has to be provided either by another model or be estimated by the CLEWs-EU modelling team based on a set of assumptions.


Land and Water module
======================

We’ve identified the following limitations in the land and water module; they point to opportunities to strengthen the module and increase the accuracy of its outputs.

• Land use costs need to be improved to represent a country-specific outlook. In some cases, having crop-specific costs (possible in some countries) helps in improving the marginal cost at which a crop can be produced.

• We have deliberately excluded the import and export of crops to simplify the computation load. However, the model has provisions to easily include this setup. This will require detailed data on how the different crops are converted into their final products and exported. For example, Grapes are produced in a country that exports both the primary crop (grapes) and wine, which is a product of grapes.

• The model has been calibrated to account for energy inputs to the agriculture and forestry sector, but the factors have not been evenly distributed across the land cover types. This is because the JRC energy balance also provides the numbers in a consolidated manner per country.

• The share of sources of water supply is the same as in the base year. The model could be improved to provide flexibility for including other splits in the supply shares.

• The livestock demand projections could be improved. Currently, we incorporate projections from the EU agricultural outlook, which are uniform across all countries.

• We do not account for animal feed production and its associated water and energy inputs in this model.

• We include crop-specific fertiliser application rates by country. However, there is not enough clarity on how much of these fertilisers are imported (from within and outside the EU-27 countries).

• The share of agricultural land under irrigation is available on a country level, and very little data exists on crop-specific numbers. Though the model has the provision to implement these modalities, the data inputs will need improvement.

• The model has the provision to implement the changes in crop yields for different climate scenarios. However, the data pipeline needs to be streamlined for implementation.

• The hydrological component in CLEWS-EU does not have water routing, like in a hydrological model. This is an area that will need significant rethinking of modelling methodology. However, when done, it will facilitate the analysis of climate-induced variations in water availability.


References
==========

Avitabile, V., Pilli, R., Migliavacca, M., Duveiller, G., Camia, A., Blujdea, V., Adolt, R., Alberdi, I., Barreiro, S., Bender, S., Borota, D., Bosela, M., Bouriaud, O., Breidenbach, J., Cañellas, I., Čavlović, J., Colin, A., Di Cosmo, L., Donis, J., … Mubareka, S. (2024). Harmonised statistics and maps of forest biomass and increment in Europe. *Scientific Data*, 11(1), 274. https://doi.org/10.1038/s41597-023-02868-8

Background guide for the calculation of land carbon stocks in the biofuels sustainability scheme: Drawing on the 2006 IPCC guidelines for National Greenhouse Gas Inventories. (2010). Publications Office of the European Union. https://data.europa.eu/doi/10.2788/34463

Beltramo, A., Ramos, E. P., Taliotis, C., Howells, M., & Usher, W. (2021). The Global Least-cost user-friendly CLEWs Open-Source Exploratory model. *Environmental Modelling & Software*, 143, 105091. https://doi.org/10.1016/j.envsoft.2021.105091

De, L. V., Galli, A., & Sala, S. (2022). Modelling the land footprint of EU consumption. European Commission, Joint Research Centre. https://doi.org/10.2760/97417

DG Agriculture and Rural Development,. (2024). EU agricultural outlook (p. 82) [Agricultural Outlook]. European Commission. https://agriculture.ec.europa.eu/data-and-analysis/markets/outlook/medium-term_en

EEA. (2021). Greenhouse gas emissions by source sector-EU [GHG inventory]. https://ec.europa.eu/eurostat/databrowser/product/page/env_air_gge__custom_18155525

ENTSO-E. (n.d.). Power Statistics. European Network of Transmission System Operators for Electricity (ENTSO-E). Retrieved 6 July 2025, from https://www.entsoe.eu/data/power-stats/

European Commission. (n.d.). National energy and climate plans 2021-2030. Retrieved 2 July 2025, from https://commission.europa.eu/energy-climate-change-environment/implementation-eu-countries/energy-and-climate-governance-and-reporting/national-energy-and-climate-plans_en#national-energy-and-climate-plans-2021-2030

European Commission. (2025). *The EU agricultural outlook 2024-2035* (p. 82) [Annual Outlook]. European Commission. https://agriculture.ec.europa.eu/data-and-analysis/markets/outlook/medium-term_en

European Commission - DG CLIMA. (2024). EC recommended parameters for GHG projections 2025. Eionet Portal. https://epanet.eea.europa.eu/Eionet/reportnet/docs/govreg/projections/govregart18_ec_parameters_projections_2021.zip/view

European Commission - Directorate General for Energy., European Commission - Directorate General for Climate Action., & European Commission - Directorate General for Mobility and Transport. (2021). *EU Reference Scenario 2020: Energy, Transport and GHG emissions : Trends to 2050.* Publications Office. https://data.europa.eu/doi/10.2833/35750

European Commission - Directorate-General for Energy. (n.d.-a). ETS2: Buildings, road transport and additional sectors - Climate Action. Retrieved 15 October 2025, from https://climate.ec.europa.eu/eu-action/carbon-markets/ets2-buildings-road-transport-and-additional-sectors_en

European Commission - Directorate-General for Energy. (n.d.-b). Weekly Oil Bulletin. Retrieved 15 October 2025, from https://energy.ec.europa.eu/data-and-analysis/weekly-oil-bulletin_en

Eurostat. (n.d.). [nrg_pc_204] Electricity prices for household consumers—Bi-annual data (from 2007 onwards). Retrieved 15 October 2025, from https://ec.europa.eu/eurostat/databrowser/view/nrg_pc_204/default/table?lang=en

Eurostat. (2019). Share of irrigable and irrigated areas in utilised agricultural area (UAA) [Data set]. Eurostat. https://ec.europa.eu/eurostat/databrowser/view/aei_ef_ir/default/table?lang=en

Eurostat. (2025). Land cover overview by NUTS 2 region [Data set]. https://ec.europa.eu/eurostat/databrowser/view/lan_lcv_ovw/default/table?lang=en

FAO. (2024). Agricultural production statistics 2010–2023. FAO. https://openknowledge.fao.org/handle/20.500.14283/cd3755en

Fischer, G. (2021). *Global Agro-Ecological Zones v4 – Model documentation* (1st edn). FAO. https://doi.org/10.4060/cb4744en

Fridman, D., Burek, P., Palazzo, A., Wada, Y., & Kahil, T. (2024). SSP-aligned projected European water withdrawal/consumption at 5 arcminutes [Data set]. Zenodo. https://doi.org/10.5281/zenodo.13767595

Gardumi, F., Shivakumar, A., Morrison, R., Taliotis, C., Broad, O., Beltramo, A., Sridharan, V., Howells, M., Hörsch, J., Niet, T., Almulla, Y., Ramos, E., Burandt, T., Balderrama, G. P., Pinto de Moura, G. N., Zepeda, E., & Alfstad, T. (2018). From the development of an open-source energy modelling tool to its application and the creation of communities of practice: The example of OSeMOSYS. *Energy Strategy Reviews*, 20, 209–228. https://doi.org/10.1016/j.esr.2018.03.005

Howells, M., Rogner, H., Strachan, N., Heaps, C., Huntington, H., Kypreos, S., Hughes, A., Silveira, S., DeCarolis, J., Bazillian, M., & Roehrl, A. (2011). OSeMOSYS: The Open Source Energy Modeling System. *Energy Policy*, 39(10), 5850–5870. https://doi.org/10.1016/j.enpol.2011.06.033

IEA ETSAP. (2010). *Technology Brief E04—Combined Heat and Power.* https://iea-etsap.org/E-TechDS/PDF/E04-CHP-GS-gct_ADfinal.pdf

IEA ETSAP. (2012). *Technology Brief R02—Space Heating and Cooling.* https://iea-etsap.org/E-TechDS/PDF/R02%20Heating%20and%20cooling%20FINAL_GSOK.pdf

Leip, A., & Weiss, F. (2010). *Evaluation of the livestock sector’s contribution to the EU greenhouse gas emissions* (p. 32). European Commission, Joint Research Centre. https://agriculture.ec.europa.eu/system/files/2020-02/ext-study-livestock-gas-exec-sum_2010_en_0.pdf

NREL. (2024). *Electricity Annual Technology Baseline (ATB) Data.* https://atb.nrel.gov/electricity/2024/data

Paraschiv, S., Paraschiv, L. S., & Serban, A. (2023). An overview of energy intensity of drinking water production and wastewater treatment. *Energy Reports*, 9, 118–123. https://doi.org/10.1016/j.egyr.2023.08.074

Peña Balderrama, J., Alfstad, T., Taliotis, C., Hesamzadeh, M., Howells, M., Peña Balderrama, J. G., Alfstad, T., Taliotis, C., Hesamzadeh, M. R., & Howells, M. (2018). A Sketch of Bolivia’s Potential Low-Carbon Power System Configurations. *Energies*, 11(10), 2738. https://doi.org/10.3390/en11102738

Pfenninger, S., & Staffell, I. (n.d.). *Renewables.ninja*. Retrieved 19 May 2022, from https://www.renewables.ninja/

Plappally, A. K., & Lienhard V, J. H. (2012). Energy requirements for water production, treatment, end use, reclamation, and disposal. *Renewable and Sustainable Energy Reviews*, 16(7), 4818–4848. https://doi.org/10.1016/j.rser.2012.05.022

Regulation (EU) 2023/2405 … ReFuelEU Aviation. http://data.europa.eu/eli/reg/2023/2405/2023-10-31/eng

Rózsai, M., Jaxa-Rozen, M., Salvucci, R., Sikora, P., Tattini, J., & Neuwahl, F. (2024). *JRC-IDEES-2021*. Publications Office of the European Union. https://data.europa.eu/doi/10.2760/614599

Ruiz, P., Nijs, W., Tarvydas, D., Sgobbi, A., Zucker, A., Pilli, R., Jonsson, R., Camia, A., Thiel, C., Hoyer-Klick, C., Dalla Longa, F., Kober, T., Badger, J., Volker, P., Elbersen, B. S., Brosowski, A., & Thrän, D. (2019). ENSPRESO … *Energy Strategy Reviews*, 26, 100379. https://doi.org/10.1016/j.esr.2019.100379

Scarlat, N., Dallemand, J.-F., Taylor, N., & Banja, M. (2019). *Brief on biomass for energy in the European Union*. https://doi.org/10.2760/546943

Schiller, G., & Dirlich, S. (2015). Applications of Life-Cycle Cost Analysis in Water and Wastewater Projects. In *Governing the Nexus* (pp. 131–151). Springer. https://doi.org/10.1007/978-3-319-05747-7_7

Singhal, D., Sridharan, V., & Hawkes, A. (2024). *Biomass Energy Potential Mapping and Analysis Tool (BEPMAT).* Zenodo. https://doi.org/10.5281/zenodo.10927219

Sridharan, V., Broad, O., Shivakumar, A., Howells, M., Boehlert, B., Groves, D. G., Rogner, H.-H., Taliotis, C., Neumann, J. E., Strzepek, K. M., Lempert, R., Joyce, B., Huber-Lee, A., & Cervigni, R. (2019). Resilience of the Eastern African electricity sector … *Nature Communications*, 10(1), 302. https://doi.org/10.1038/s41467-018-08275-7

Urban waste water directive treatment plants data viewer. (2017). https://www.eea.europa.eu/en/analysis/maps-and-charts/urban-waste-water-directive-treatment-data-viewer-urban-wastewater-treatment-directive-1

Vladimir Tesnière, M. J. A. M., & Ivan Haščič. (2024). Monitoring land cover change to understand biodiversity pressures. OECD. https://www.oecd.org/en/publications/monitoring-land-cover-change-to-understand-biodiversity-pressures_441a7a6c-en.html
