# EU-CLEWS
This repository contains the EU-CLEWs model development work carried out under the Horizon-DIAMOND project. 
The repository is a work in progress. It has two main sections: The Aggregated EU CLEWs model and the Diaggregated EU CLEWs model. The later, a detailed country level modelling work, is yet to be started. The former, a single node aggregated model for the EU27 countries, is being developed and is its final stages of development.

# Structure of CLEWs-EU

The CLEWs-EU model will have a similar structure to the [Global CLEWs model](https://www.sciencedirect.com/science/article/pii/S1364815221001341), but several enhancements are foreseen. Two separate modules: one for energy ands another for land and water – will be developed with several interlinkages between them (Figure 1). Greenhouse gas emissions are tracked across the three modules, while these are in turn affected by climate assumptions; for instance, temperature affects water demand in agriculture and heating and cooling demand in buildings, while precipitation affects hydropower output and crop yield. In the energy module, a large set of technologies will be used to represent primary energy supply, electricity generation, transport, buildings and industry. In addition, the suite of technologies will be expanded to include a broader range of decarbonisation options. For instance, use of hydrogen – either imported or locally produced – is an option that was not available in the Global CLEWs but will be included in the CLEWs-EU model. In the land module, the available land resources for crop production, livestock grazing and other uses will be defined at the EU level and for each country individually, assessing the impact of policies and climate on water and energy. Furthermore, whereas the Global CLEWs model employs a simple accounting approach to calculate water requirements throughout the system, the CLEWs-EU model will have a more explicit representation of water demand and supply. 

Two levels of geographical resolution will be adopted: 

**a.	Aggregated regional model**, in which the EU will be represented as a single node, serving as an engagement model, upon which capacity development activities on EU climate policy can be developed due to its simplified structure and low computational effort. Coupled with the adoption of a user-friendly interface, enabling direct changes in model parameters and visualisation of the system dynamics, it will allow the exploration of climate change mitigation pathways by a broad range of stakeholders. This will ensure consistency with the philosophy behind the initial development of the Global CLEWs model. 

**b.	Disaggregated model**, in which the level of spatial resolution will extend to the national level, to be used for more extensive analyses. Unlike the high-level focus of the aggregated model, the disaggregated model will be able to provide more focused insights and can be used to support development of national policies within the context of mutual EU obligations/targets. As expected, the disaggregated model will require a larger volume of input data compared to the aggregated model.

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
