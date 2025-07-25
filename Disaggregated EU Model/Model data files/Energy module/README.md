# Energy module
Five overarching sectors are developed to represent the broader energy system. Each of these includes a large set of technologies to capture the status of the current energy mix, as well as future technology options for decarbonisation. Specifically, the following sectors are modelled:

**a)**	Primary energy supply – this relates to fossil fuel supply, nuclear fuel supply, renewable energy potential and hydrogen imports. Primary energy supply and transformation infrastructure (e.g., gas pipelines, LNG regasification terminals, oil refineries, etc.) is not modelled explicitly, with the only exception of electricity interconnectors between countries in the disaggregated version of the CLEWs-EU model and hydrogen production. Supply of biomass into the energy system occurs via an interlinkage with the land module of the model.

**b)**	Electricity and heat generation – fossil fuel, nuclear and renewable energy technologies are represented, along with a simplified representation of grid networks to capture associated losses. Additional technology options represented include electricity storage, use of Carbon Capture and Storage (CCS) technologies, hydrogen production through electrolysers to produce green hydrogen and steam methane reforming (i.e., using natural gas as feedstock) with or without CCS to produce blue and grey hydrogen respectively. 

**c)**	Transport – the transport sector includes road transport, which is further broken down to passenger (passenger cars and buses) and freight (light commercial vans and heavy trucks), rail transport (passenger and freight), aviation and shipping. 

**d)**	Buildings – this sector basically comprises of the households and service sectors. It is broken down into end-use services (i.e., space heating, space cooling, cooking, sanitary hot water, lighting and appliances).

**e)**	Industry –up to four distinct industries, based on the most energy-consuming sectors, are represented separately for each country, while the rest of the industries are lumped together in a fifth category. The output of each of the industries is represented in generic energy terms (i.e., PJ of useful energy services).

In this folder the energy module is provided, which combines the relevant sectoral modules of the energy system into a single entity. Even though the sectoral models have an annual resolution for the entire period 2018-2055, the energy module uses a different outlook. Specifically, an annual resolution is used for the period 2018-2022, followed by 2025 and subsequent 5-year time steps until 2055. This approach is adopted to address the computational intensity of the integrated energy system model.
