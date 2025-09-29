# Aggregated EU-CLEWs model

This folder contains the model, data files and associated scripts that are used for setting up the Aggregated EU-CLEWs model. please refer to the individual folders for the respective contents.

This is a work in Progress. The model is in its final stages of development with . The draft version will be ready by July 2025 and the final version by November 2025.



## How to run the Aggregated EU-CLEWs model

> Please choose the relevant model file from either one of the following three folders.This selection is important if you want to run the individual modules or the integrated Energy, Land and water module.
> - Energy
> - Land and Water
> - Integrated_CLEWs

The data is constructed in a excel file with multiple worksheets. Each worksheet corresponds to a particular SET or Parameter in the OSeMOSYS model. A python package, [Otoole](https://github.com/OSeMOSYS/otoole), is used handle all the data manipulations required for running the EU CLEWs model. Please make sure you have the latest version of Otoole installed in your computer along with the latest stable version of [Python](https://www.python.org/). To use Otoole, a configuration file (YAML) is required. A YAML file has been specifically developed for this project and it can be found in the [model_files](https://github.com/vignesh1987/EU-CLEWS/tree/main/Aggregated%20EU%20Model/model_files) folder. Additionally, an optimisation solver is required to run the model. Please refer to any one of the following and install the latest version of anyone of the solvers. Some solvers are proprietary and some are free and open source. Please select one based on your needs. 

* [CBC](https://github.com/coin-or/Cbc)

* [GLPSOL](https://www.gnu.org/software/glpk/) 
    - This is mandatory as GLPSOL is part of GLPK and it is mandatory for creating the matrix)

* [CPLEX](https://www.ibm.com/products/ilog-cplex-optimization-studio/cplex-optimizer)

* [GUROBI](https://www.gurobi.com/)


## Steps
1. First we convert the OSeMOSYS model file from Excel data format to a text file
2. Use GLPK to create the LP file version of our model
3. Optimise the LP file using anyone of the solvers. Write the solution file
4. Use Otoole to write the results from the optimised solution file to result-CSVs
5. The users can open the CSVS to view the results. At a later stage, visualization scripts will be developed to automatically view results in an interactive format.

### Please refer to the [examples](https://otoole.readthedocs.io/en/latest/examples.html) page of the [Otoole documentation](https://otoole.readthedocs.io/en/latest/index.html) for the syntax used to carry out the previous steps.


