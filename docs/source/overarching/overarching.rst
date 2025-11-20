Time horizon and temporal resolution
====================================
Considering the climate neutrality goal of the European Union by 2050, analysis by the model is performed up to 2050 . The extension of the modelling horizon beyond this point implies great uncertainty as to the technological advances and relevant cost assumptions, climatic conditions and energy demand projections required as input in the CLEWs-EU model. The base period is 2018-2021, with statistics up to 2021/2022 accounted for, and these years are calibrated accordingly, wherever possible. To reduce the computational effort required to run CLEWs-EU, a modified OSeMOSYS code version has been developed to allow scenario development with multi-year steps instead of adopting an annual resolution (e.g., one could choose to adopt an annual resolution for the period 2018-2035, and then the years 2040, 2045 and 2050). This same OSeMOSYS code can also be used for an outlook with annual resolution and is made available on the GitHub repository. The individual sectoral models of the disaggregated CLEWs-EU version are built with an annual resolution. However, the integrated CLEWs-EU model represents 2021 as a base year, then 2025 and the remaining horizon is in 5-year time-steps, due to the computational effort entailed; in the case of the energy module, the years 2018-2020 are also included in the reference period.
The temporal resolution of the model is enhanced from the 3 intra-annual parts adopted in the GLUCOSE (i.e., Global CLEWs) model to **16 annual timesteps**, consisting of **4 seasons** (i.e., winter, spring, summer, autumn) represented by a typical day; each consisting of 4 intra-day parts (Table 23). The goal is to capture the daily characteristics of variability across electricity demand and variable renewable electricity generation. Initially, the model is developed with this temporal resolution, but in case the computational effort during the model optimisation permits further enhancement, this will be explored in future stages of model development. Such an enhancement would strengthen the model’s capability to provide valuable insights regarding variable renewable energy integration. In this sense, the data collection process for time-variable statistics (e.g., electricity demand variability, renewable energy generation profiles, heating and cooling demand profiles etc.) considered this plausibility.

.. raw:: html

    <div style="font-size:13px; margin-top:20px; margin-bottom:8px; text-align:center;">
        <b>Table 23.</b> Intra-year temporal breakdown of CLEWs-EU.
    </div>

.. list-table::
   :header-rows: 1
   :widths: 20 20 20 20 20
   :align: center

   * - **Seasons**
     - **Winter**
     - **Spring**
     - **Summer**
     - **Autumn**

   * - 
     - December–February
     - March–May
     - June–August
     - September–October

   * - **Day parts (UTC time)**
     - 00:00–07:00
     - 07:00–17:00
     - 17:00–21:00
     - 21:00–00:00

   * - **Day part duration (hours)**
     - 7
     - 10
     - 4
     - 3

Emissions accounting
=====================
The CLEWs-EU model accounts for key greenhouse gas (GHG) emissions (CO2, CH4, N2O) separately, but also in terms of carbon dioxide equivalent (CO2eq). In the context of the European Union legislation, it is important to differentiate between GHG emissions that fall under the Emissions Trading System (ETS) and those that are part of the Effort Sharing Regulation (ESR), as different carbon pricing mechanisms are in place, while these will also change with the introduction of the new ETS. As such, a distinction is made in the model on the sectors that are relevant to ETS or ESR. Price projections for the existing and the new ETS are taken from a communication of the European Commission on the “Recommended parameters for reporting on GHG projections in 2025” (European Commission - DG CLIMA, 2024), which was used by member states in the preparation of the final revisions of their National Energy and Climate Plans (NECPs) (European Commission, n.d.). Accounting for GHG emissions in the energy module of CLEWs-EU occurs either at the fuel supply level or the use level (i.e., technology). Negative GHG emission rates are included in Carbon Capture and Storage (CCS) technologies, which are available for investment in electricity & heat generation, as well as industry.  
Emissions in the Land module are captured at multiple levels. All land cover categories have an emission activity ratio corresponding to their CO2, CH4, N2O & CO2eq emissions. Livestock emissions pertaining to enteric fermentation and manure management are obtained from the European GHG inventory (EEA, 2021) and divided by the total live heads of livestock in the base year to compute emission activity ratios for each type of livestock per EU-27 member state. Similarly, emissions from other AFOLU sectors are also sourced from the same source, and the factors are calculated by dividing the total GHG emissions by the area under the emitting/sequestering land cover category. The EU also declares the amount of GHG that is stored in harvested wood products. We represent this category as exogenous emission in the model. For land that has been under forest or grassland cover for a long time and changes to another land cover category (such as agriculture), an emission change factor has been implemented to specify the carbon stocks that will be released when land cover changes (Background Guide for the Calculation of Land Carbon Stocks in the Biofuels Sustainability Scheme, 2010). These emission activity ratios and the calculation are available in the GitHub repository.


Naming Convention
==================

As the CLEWs-EU model has been built from scratch, the way in which technologies and commodities would be represented within the model and hence, the short codes abbreviating these had to be formulated. This would facilitate the standardisation and automation of data entry and results extraction and visualisation. A 12-character naming convention was followed for technologies, while a 6-character naming convention was adopted for commodities. Table 24 shows an extract of the naming convention adopted for the energy module, while Table 25 and Table 26 highlight the naming convention implemented for the land and water modules. The full explanation of the naming convention is available as part of the model documentation in the model’s GitHub repository. As further additions are made, the relevant documentation will be updated accordingly. 

.. raw:: html

    <div style="font-size:13px; margin-top:20px; margin-bottom:8px; text-align:center;">
        <b>Table 24.</b> Naming convention sample for technologies and commodities in the energy module (CLEWs-EU).
    </div>

.. list-table::
   :header-rows: 1
   :widths: 20 15 15 15 15 15 15
   :align: center

   * - **Technology**
     - **Country/Region (2 Characters)**
     - **Module (1 Character)**
     - **Sector (2 Characters)**
     - **Fuel (3 Characters)**
     - **Technology / Destination (2 Characters)**
     - **Type (2 Characters)**

   * - EUEPTVPGSLPH  
       Gasoline-fired plug-in hybrid passenger car in the EU
     - EU  
       (European Union)
     - E  
       (Energy)
     - PT  
       (Passenger Transport)
     - GSL  
       (Gasoline)
     - VP  
       (Passenger vehicle)
     - PH  
       (Plug-in hybrid)

   * - ATEGNELCDEIC  
       Electricity interconnector between Austria and Germany
     - AT  
       (Austria)
     - E  
       (Energy)
     - GN  
       (Grid Networks)
     - ELC  
       (Electricity)
     - DE  
       (Germany)
     - IC  
       (Inter-connector)

   * - PLEEGCOAPPCS  
       Coal power plant with CCS in Poland
     - PL  
       (Poland)
     - E  
       (Energy)
     - EG  
       (Electricity Generation)
     - COA  
       (Electricity)
     - PP  
       (Power Plant)
     - CS  
       (Carbon Capture and Storage)


.. raw:: html

    <div style="font-size:13px; margin-top:20px; margin-bottom:8px; text-align:center;">
        <b>Table 25.</b> Naming convention sample for technologies in the land module (CLEWs-EU).
    </div>

.. list-table::
   :header-rows: 1
   :widths: 18 18 12 12 12 12 12 12
   :align: center

   * - **Technology**
     - **Country/Region (2 Characters)**
     - **Module (1 Character)**
     - **Identifier 1 (3 Characters)**
     - **Identifier 2 (3 Characters)**
     - **Input Level (1 Character)**
     - **Water supply (1 Character)**
     - **Dummy (1 Character)**

   * - EULIMPWHE000  
       Wheat imports in the EU
     - EU  
       (Europe)
     - L  
       (Land)
     - IMP  
       (Imports)
     - WHE  
       (Wheat)
     - 0  
       (Dummy)
     - 0  
       (Dummy)
     - 0  
       (Dummy)

   * - EUL000WAT000  
       Land cover under water bodies
     - EU  
       (Europe)
     - L  
       (Land)
     - 000  
       (Dummy)
     - WAT  
       (Water)
     - 0  
       (Dummy)
     - 0  
       (Dummy)
     - 0  
       (Dummy)

   * - EUL000MAIHR0  
       Potential for rainfed maize cultivation under high input level
     - EU  
       (Europe)
     - L  
       (Land)
     - 000  
       (Dummy)
     - MAI  
       (Maize)
     - H  
       (High Input Level)
     - R  
       (Rainfed type)
     - 0  
       (Dummy)


.. raw:: html

    <div style="font-size:13px; margin-top:20px; margin-bottom:8px; text-align:center;">
        <b>Table 26.</b> Naming convention sample for technologies in the water module (CLEWs-EU).
    </div>

.. list-table::
   :header-rows: 1
   :widths: 20 18 15 15 15 15
   :align: center

   * - **Technology**
     - **Country/Region (2 Characters)**
     - **Module (1 Character)**
     - **Identifier 1 (3 Characters)**
     - **Identifier 2 (3 Characters)**
     - **Identifier 3 (3 Characters)**

   * - EUWDEMPUBGWT  
       Ground water supply technology for public use
     - EU  
       (Europe)
     - W  
       (Water)
     - DEM  
       (Demand)
     - PUB  
       (Public supply)
     - GWT  
       (Groundwater)

   * - EUWDEMAGRSUR  
       Surface water supply technology for agricultural use
     - EU  
       (Europe)
     - W  
       (Water)
     - DEM  
       (Demand)
     - AGR  
       (Agricultural Use)
     - SUR  
       (Surface water)

   * - EUWMIN000PRC  
       Technology to produce water from precipitation
     - EU  
       (Europe)
     - W  
       (Water)
     - MIN  
       (Resource Technology)
     - 000  
       (Dummy)
     - PRC  
       (Precipitation)
