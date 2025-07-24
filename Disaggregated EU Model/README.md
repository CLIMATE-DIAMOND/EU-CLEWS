# Disaggregated CLEWs-EU model
This folder contains the model, data files and associated scripts that are used for setting up the disaggregated version of the CLEWs-EU model. Please refer to the individual folders for the respective contents. 
This is a work in Progress. The Disaggregated model is currently in its draft version. The baseline setup of the model is still undergoing its final validation procedures. The final version of the model will be ready by November 2025.

## Using the CLEWs-EU model
The procedure to run the CLEWs-EU model is the same as for any other OSeMOSYS model. Specifically, the following steps should be followed:
1)	First, using [Otoole](https://otoole.readthedocs.io/en/latest/index.html), convert the OSeMOSYS data file from Excel data format to a text file. Users should refer to the examples page of the Otoole documentation for the syntax used to carry out the previous steps.
2)	Use GLPK to create the LP file version of our model (.lp file format), using the data file and the OSeMOSYS code as input (both in .txt format). This step creates the matrix of the problem by loading the data into the relevant OSeMOSYS equations.
3)	Optimise the LP file using anyone of the suggested solvers. Once an optimal solution is found, the user should write the solution file (.sol file format).
4)	Use Otoole to write the results from the optimised solution file to result CSV files.
5)	The users can open the CSV files to view the results in a tabular format. At a later stage, visualisation scripts will be developed to automatically view results in an interactive format.
