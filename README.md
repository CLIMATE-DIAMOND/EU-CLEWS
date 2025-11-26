# CLEWS-EU
This repository contains the CLEWs-EU model development work carried out under the Horizon-DIAMOND project. It has two main sections: (1) the Aggregated CLEWs-EU model, and (2) the Disaggregated CLEWs-EU model.

Zenodo link to CLEWs-EU releases: https://doi.org/10.5281/zenodo.16537821
Detailed model documentation available at: https://eu-clews.readthedocs.io/en/latest/index.html

# Structure of CLEWs-EU

The CLEWs-EU model is developed within the OSeMOSYS (Open-Source Energy Systems Model) modelling framework. OSeMOSYS is a long-term cost-optimisation energy system model ([Howells et al., 2011](https://www.sciencedirect.com/science/article/abs/pii/S0301421511004897)). OSeMOSYS has been used in numerous studies with focus ranging from a global, regional and national scale. It is a bottom-up technoeconomic model that is demand-driven, which means the exogenously defined demand has to be met, no matter the cost. The choice of technologies and energy mix is based on the adopted technoeconomic assumptions (e.g., fuel costs, technology costs, resource availability, emission limits). The model’s objective function is the minimisation of the total discounted system cost over the entire modelling horizon.

The CLEWs-EU model builds on the structure of the [Global CLEWs model](https://www.sciencedirect.com/science/article/pii/S1364815221001341), with several enhancements being implemented in this release. Two separate main modules, namely i) energy; and ii) land with water, have been developed with several interlinkages between them. Greenhouse gas emissions are tracked across the modules, while these are in turn affected by climate assumptions; for instance, temperature affects water demand in agriculture and heating and cooling demand in buildings, while precipitation affects hydropower output and crop yield. In the energy module, a large set of technologies are used to represent primary energy supply, electricity generation, transport, buildings and industry. In addition, the suite of technologies has been expanded to include a broader range of decarbonisation options. For instance, use of hydrogen – either imported or locally produced – is an option that was not available in the Global CLEWs but is included in this version of the CLEWs-EU model. In the land module, the available land resources for crop production, livestock grazing and other uses are being defined at the EU level and for each country individually, assessing the impact of policies and climate on water and energy. Furthermore, whereas the Global CLEWs model employs a simple accounting approach to calculate water requirements throughout the system, the CLEWs-EU model has a more explicit representation of water demand and supply. More information on the structure of each module is provided in the subsequent sections. 

Two levels of geographical resolution are adopted: 

**a.	Aggregated regional model**, in which the EU is represented as a single node, serving as an engagement model, upon which capacity development activities on EU climate policy can be developed due to its simplified structure and low computational effort. Coupled with the adoption of a user-friendly interface, enabling direct changes in model parameters and visualisation of the system dynamics, it allows the exploration of climate change mitigation pathways by a broad range of stakeholders. This will ensure consistency with the philosophy behind the initial development of the Global CLEWs model. 

**b.	Disaggregated model**, in which the level of spatial resolution has been extended to the national level, to be used for the more extensive analyses foreseen within DIAMOND (e.g., through soft-links in WP4). Unlike the high-level focus of the aggregated model, the disaggregated model is able to provide more focused insights and can be used to support development of national policies within the context of mutual EU obligations/targets. As expected, development of the disaggregated model has entailed a larger volume of input data compared to the aggregated model. Most of this data has been implemented in the draft version of the national-detail CLEWs-EU model, especially for the energy module. For the land and water module, most of the country level data has been incorporated in the draft version. However, in certain cases like groundwater usage shares, livestock numbers (to name a few), EU-27 averages have been used for countries which do not report explicit numbers. These assumptions will be revisited after this release and towards the final version of the model, and country-specific data will be updated wherever possible.

## Energy module
Five overarching sectors are developed to represent the broader energy system. Each of these will include a large set of technologies to capture the current status of energy mix, as well as future technology options for decarbonisation. A simplified representation of the structure of the energy module is provided in Figure 1. Specifically, the following sectors will be modelled:

a)	**Primary energy supply** – this relates to fossil fuel supply, nuclear fuel supply, renewable energy potential and hydrogen imports. Primary energy supply and transformation infrastructure (e.g., gas pipelines, LNG regasification terminals, oil refineries, etc.) will not be modelled explicitly, with the only exception of electricity interconnectors between countries in the disaggregated version of the CLEWs-EU model. Supply of biomass into the energy system will occur via an interlinkage with the land module of the model.

b)	**Electricity and heat generation** – fossil fuel, nuclear and renewable energy technologies will be represented, along with a simplified representation of grid networks to capture associated losses. Additional technology options to be represented include electricity storage, use of Carbon Capture and Storage (CCS) technologies, electrolysers for the production of green hydrogen; hydrogen production will also be possible through steam methane reforming (i.e., using natural gas as feedstock) with or without CCS. 

c)	**Transport** – the transport sector will include road transport, which will be further broken down to passenger (passenger cars and buses) and freight (light commercial vans and heavy trucks), rail transport (passenger and freight), aviation and shipping. 

d)	**Buildings** – this sector basically comprises of the households and service sectors. It will be broken down into end-use services (i.e., space heating, space cooling, cooking, sanitary hot water, lighting and appliances).

e)	**Industry** – the five most energy intensive industries – a considerable variation exists according to the latest energy balances – will be represented separately for each country, while the rest of the industries will be lumped together in a sixth category . The output of each of the industries will be represented in generic terms (i.e., PJ of energy services).

![image](https://github.com/vignesh1987/EU-CLEWS/assets/148845953/663686cc-87ab-4ef3-be1b-286e56236da5)

**Figure 1.** Simplified representation of CLEWs-EU energy module.

## Land and water module
The water and land use modules are effectively interlinked in nature. Though we have different naming conventions and technologies to represent the two modules inside CLEWs-EU, their inputs and outputs are interdependent. The water module will represent the different primary sources, namely water from precipitation and snow melt, water from existing surface and ground water sources, water from neighbouring geographies by transboundary river exchanges, as well as secondary sources like water from treatment plants in some countries. In the land module, the total land available in the continent (in the engagement model) and in each country (in the disaggregated model) is divided into nine major land categories based on the European Space Agency’s land cover classifications. They are namely: grassland, cropland, snow cover, water bodies, shrubland, forest cover, built up land, barren land, other land (includes mangroves, lichens and wetlands). Representing land and water systems in a generic systems optimisation setup involves using relevant assumptions to simplify their characterisation and at the same time ensuring not a lot of the essential detail is lost. Effectively the land and water modules represent the balance of the two resources (i.e., land and water) in the respective systems. Despite accounting for the balance of these resources, some components like groundwater storage are not considered in these modules as it involves detailed sub surface flow modelling, which is outside the scope of the project. In the following section, a sample of the technology representation in the land and water modules is presented, along with some common data sources. 
Figure 2 represents a diagrammatic illustration of the land component within a general CLEWs systems framework. The diagram breaks down "Total land" into various land uses and their subsequent products or services.

**Land Uses:** 

This includes various classifications of land such as Cropland, Barren land, Forests, Pastures/Grasslands, Built-up land, and Water bodies. Each category of land use is dedicated to a specific type of production or ecosystem service.

**Production:**

From each type of land use, there is also a corresponding output:

•	Cropland is associated with the production of agricultural commodities like Maize, Rice, Coffee, Sugarcane, Bananas, and other crops.

•	Forests contribute to the production of wood and other forest products.

•	Pastures and Grasslands are tied to the production of meat and dairy, implying livestock farming.

•	Built-up land is related to residential, industrial, commercial, and transport services, indicating areas of human development and infrastructure.
The arrows indicate the flow from land use to the type of production. The diagram encapsulates the interconnectedness of land use with various economic and environmental outputs, emphasizing the integrated approach of the CLEWs framework where changes or policies affecting land use have cascading effects on food, energy, water, and ecosystem services.

![image](https://github.com/vignesh1987/EU-CLEWS/assets/148845953/98c9b0bf-5dec-4366-9d62-425e961a800b)

**Figure 2.** Primary level of land categories breakdown in the land module.

The systems diagram is illustrated in Figure 3 and portrays how the CLEWs-EU land and water modules will be represented, along with key interactions with the energy module. The diagram is organised into several columns, each representing different components of the CLEWs systems:

•	Land Use (left-most column): This column lists various types of land uses such as agricultural land (which will be divided into up to 10 different crop types), barren land, forests, built-up land, and water bodies. Each land type is linked to specific outputs, i.e., specific crops and the different aspects of the water system. 

•	Precipitation and Sea Water (bottom rows and centre columns): This section details the sources (precipitation and sea water) and uses of water, distinguishing between surface water and groundwater, and their respective uses in agriculture, power generation (PWR), and other needs.

•	Energy Supply and Use (top right box): The diagram includes simplified forms of electricity generation, to show how these energy sources contribute to meeting the demands of different sectors, including transport, meat processing, and the transport and distribution (T&D) of water resources.

•	Interlinkages (arrows and lines): The arrows and lines represent the flow of resources and interconnections between the land, water, and energy components. For example, water from different sources is used for land irrigation, electricity generation requires water for cooling, and agriculture produces biofuels.

![image](https://github.com/vignesh1987/EU-CLEWS/assets/148845953/2716755e-5f45-4781-8196-ebfa53832f5d)

**Figure 3.** Simplified representation of CLEWs-EU land and water modules and illustration of key interactions with the energy module.
