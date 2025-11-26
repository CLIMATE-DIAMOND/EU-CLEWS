Software and hardware requirements
====================================

The input data files for the CLEWs-EU model are constructed in an Excel file with multiple worksheets. 
Each worksheet corresponds to a particular **SET** or **Parameter** in the OSeMOSYS model. 

A Python package, **Otoole**, is used to handle all data manipulations required for running the model. 
Users should ensure they have:

- the latest stable version of **Python**, and  
- the latest version of **Otoole** installed.

To use Otoole, a **YAML configuration file** is required. A project-specific YAML file has been prepared for CLEWs-EU and is available in the ``model_files`` folder of the model’s GitHub repository.

An optimisation solver is also required to run the model. Any of the following options may be used:

- **GLPSOL** – mandatory, as it is part of the GLPK package and required to generate the model matrix.  
  Note: the disaggregated CLEWs-EU model is computationally intensive; GLPSOL should *not* be used for the optimisation step.
- **GUROBI** – proprietary (academic licence available)
- **CPLEX** – proprietary (academic licence available)
- **CBC** – open-source

As the CLEWs-EU model was developed in parallel modules, computational intensity varies depending on whether:

- the **fully integrated model** is run, or  
- only an **individual sectoral module** is executed.

The primary limiting factor is the **amount of available memory**.

The disaggregated version of the integrated CLEWs-EU model is computationally intensive and is therefore not run with annual time steps; instead, **5-year steps** are used. In contrast, **annual resolution** is maintained in each standalone sectoral model.

As indicated in **Table 27**, the disaggregated integrated CLEWs-EU model requires **~260 GB of memory** to run.  
By comparison, the aggregated version requires only **~8 GB**, despite using annual resolution, due to its significantly lower structural complexity, making it suitable for stakeholder engagement.

.. raw:: html

    <div style="font-size:13px; margin-top:20px; margin-bottom:8px; text-align:center;">
        <b>Table 27.</b> Key hardware requirements to run the disaggregated version of the CLEWs-EU model and its sectoral components
    </div>

.. list-table::
   :header-rows: 1
   :widths: 40 20
   :align: center

   * - **CLEWs-EU sectoral model**
     - **Memory requirements (GB RAM)**

   * - Energy module
     - 170 GB

   * - Electricity supply
     - 38 GB

   * - Buildings
     - 12 GB

   * - Industry
     - 34 GB

   * - Transport
     - 32 GB

   * - Land & Water module
     - 180 GB

   * - **Integrated CLEWs-EU model**
     - **260 GB**


Model setup
===========

The `GitHub repository <https://github.com/CLIMATE-DIAMOND/EU-CLEWS>`_ provides the following material:


a) **OSeMOSYS code**  
   This is the version of the OSeMOSYS code developed specifically for this project. 
   Three separate files are provided, depending on which model is used (i.e., 
   the individual sectoral models or the integrated CLEWs-EU model).  
   These files are plain-text and include all parameters, variables, and constraints 
   that describe the relationship between input data (parameters) and model outputs (variables).

b) **CLEWs-EU model data files**  
   Model data files are provided as Excel spreadsheets for:
   
   - the energy module and its sub-components,  
   - the land and water module,  
   - and the integrated CLEWs-EU model (energy + land + water).

   These files contain the full model structure in the form of **Sets**  
   (e.g., years, fuels/commodities, technologies, emissions, etc.)  
   as well as all associated **techno-economic assumptions**  
   (e.g., energy service demand projections, costs, efficiencies, and so on).

c) **Supporting data**  
   This folder contains additional information needed by future CLEWs-EU users.  
   The **naming convention** files are included here, along with more detailed input data 
   and modelling assumptions for the final version of the model.

d) **Data preparation scripts**  
   These scripts automate the extraction of required data from external databases 
   (e.g., JRC-IDEES 2021).  
   They have been developed for the **transport** and **industrial** sectors and may be 
   extended to other sectors in future releases.  
   The scripts are included for transparency and to support potential future 
   updates to model detail.


Using the CLEWs-EU model
==========================

The procedure to run the CLEWs-EU model is the same as for any other OSeMOSYS model. 
Specifically, the following steps should be followed:

1. Using **Otoole**, convert the OSeMOSYS data file from Excel format to a text data file.  
   Users may refer to the examples page of the Otoole documentation for the exact syntax.

2. Use **GLPK** to create the LP version of the model (``.lp`` file), using as input:
   
   - the OSeMOSYS data file (``.txt``), and  
   - the OSeMOSYS code file (``.txt``).  

   This step generates the problem matrix by loading the data into the OSeMOSYS equations.

3. Optimise the ``.lp`` file using any of the recommended solvers.  
   Once an optimal solution is found, write the **solution file** (``.sol`` format).

4. Use **Otoole** to export the results from the solution file into **CSV result files**.

5. Open the CSV files to inspect results in tabular form.  
   At a later stage, visualisation scripts will be developed to allow automatic and interactive result exploration.
