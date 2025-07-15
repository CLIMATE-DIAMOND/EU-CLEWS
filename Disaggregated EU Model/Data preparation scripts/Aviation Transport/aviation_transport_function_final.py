# -*- coding: utf-8 -*-
"""
Created on Fri Nov  1 16:16:04 2024

@author: m.karmellos
"""

def aviation_transport_function(country, code):

    import pandas as pd
    from pathlib import Path
    import copy
    from sys import exit
    import os

    ## Define the country
    country_abb = code
    country = country

    ## Path 
    ## Data files and import path# Breakdown mileage into dataframes for passenger and freight rails

    data_path_file = '' # Insert relative path
    data_file = data_path_file + country_abb+'/JRC-IDEES-2021_Transport_'+ country_abb +'.xlsx'
    sheet_act = 'TrAvia_act'
    sheet_energy = 'TrAvia_ene'

    path_dir_sup = '' # path for supplementary files
    supplemantary_data_file = 'Supplementary data for transport projections.xlsx'
    sheet_efficiency = 'Efficiency'
    sheet_capital_cost = 'Capital Cost'


    # Export path
    path_dir_export = data_path_file + country_abb + '/Useful Data/Aviation Transport/' # Insert relative path for export

    if not os.path.exists(path_dir_export):
        os.makedirs(path_dir_export)
            
    ## Read the excel file with road transport
    aviation_transport = pd.read_excel(data_file, sheet_name=sheet_act, header=0, index_col=0)
    year_keys = list(range(2018,2022))

    ## Stock of aircrafts

    # Pull data from the excel file
    aviation_stock = aviation_transport.iloc[41:42, 18:22]
    aviation_stock.index.names = ['Stock']
    aviation_stock.rename(index={'Stock of aircrafts - total' : 'Aircrafts (total)'}, inplace=True)

    fuel_index_aircraft = pd.DataFrame({'Jet Fuel'}, columns=['Fuel'])
    aviation_stock = aviation_stock.set_index(fuel_index_aircraft['Fuel'], append=True)

    aviation_stock.to_csv(path_dir_export+'Aviation_Stock.csv')

    ## Calculate existing capacity in Mvkm

    existing_capacity = aviation_transport.iloc[11:12, 18:22]
    existing_capacity.index.names = ['Existing Capacity [Mvkm]']
    existing_capacity.rename(index={'Vehicle-km (mio km)' : 'Aircrafts (total)'}, inplace=True)
    existing_capacity = existing_capacity.set_index(fuel_index_aircraft['Fuel'], append=True)


    # Revise existing capacity of technologies

    lifetime_duration = 30
    lifetime_range = range(2022,2071)
    lifetime_list = []

    for n in lifetime_range:
        lifetime_list.append(n)
    lifetime_df = pd.DataFrame(columns=lifetime_list)

    # Create a revised capacity
    decom_capacity = copy.deepcopy(existing_capacity)
    decom_capacity_rev = pd.concat([decom_capacity, lifetime_df], axis=1)

    for k in range(1, lifetime_duration + 1):
        decom_capacity_rev.iloc[:, 3+k] = (1 - k/lifetime_duration) * decom_capacity_rev.iloc[:,3] 
    decom_capacity_rev = decom_capacity_rev.fillna(0)
    decom_capacity_rev.index.set_names(['Capacity [Mvkm]', 'Fuel'], inplace=True)
    decom_capacity_rev.to_csv(path_dir_export+'/Decommissioned_Capacity.csv')

    ## Calculate mileage in Mvkm/year
    existing_capacity_copy = copy.deepcopy(existing_capacity)
    aviation_stock_copy = copy.deepcopy(aviation_stock)   

    mileage = existing_capacity_copy / aviation_stock_copy
    mileage.index.rename({'Capacity [Mvkm]' : 'Mileage [Mvkm/year]'}, inplace=True)
    mileage.to_csv(path_dir_export+'Mileage.csv')

    ## Energy consumption
    energy_consumption = pd.read_excel(data_file, sheet_name=sheet_energy, header=0, index_col=0)

    # Pull data for total energy consumption and convert to PJ
    total_energy_consumption = energy_consumption.iloc[1:2,18:22]
    total_energy_consumption.rename(index={'Energy consumption (ktoe)':'Aircrafts (total)'},inplace=True)
    total_energy_consumption.index.names = ['Total energy consumption [ktoe]']
    total_energy_consumption = total_energy_consumption.set_index(fuel_index_aircraft['Fuel'], append=True)


    # Process energy consumption data in new units 
    ktoe_pj = 23.8845897 # convert ktoe to PJ by dividing with this value
    total_energy_consumption_rev_pj = copy.deepcopy(total_energy_consumption)

    total_energy_consumption_rev_pj = total_energy_consumption_rev_pj / ktoe_pj
    total_energy_consumption_rev_pj.index.rename({'Total energy consumption [ktoe]' : 'Total energy consumption [PJ]'}, inplace=True)

    ## Calculate aircracft efficiency in [PJ/Mvkm]
    total_energy_consumption_rev_pj_copy = copy.deepcopy(total_energy_consumption_rev_pj)
    existing_capacity_rev_copy = copy.deepcopy(existing_capacity)

    aircraft_efficiency = total_energy_consumption_rev_pj_copy / existing_capacity_rev_copy
    aircraft_efficiency.index.rename({'Total energy consumption [PJ]' : 'Aircraft efficiency [PJ/Mvkm]'}, inplace=True)

    # Read efficiency projections
    efficiency_projection = pd.read_excel(path_dir_sup + supplemantary_data_file, sheet_name=sheet_efficiency, skiprows=447, header=0, index_col=[2,3])
    efficiency_projection.drop(efficiency_projection.iloc[:,0:18], axis=1, inplace=True)
    efficiency_projection_aircraft = efficiency_projection.iloc[28:29]
    efficiency_projection_aircraft.index.rename(['Efficiency Coefficient','Type'], inplace=True)

    #Fix efficiency_data_dict to match the other dataframes
    efficiency_projection_aircraft.rename(index={'Aviation' : 'Aircrafts (total)', 'Kerosene planes' : 'Jet Fuel'},
                                       inplace=True)

    # Create a revised database of train efficiency
    aircraft_efficiency_copy = copy.deepcopy(aircraft_efficiency)

    aircraft_efficiency_rev = pd.concat([aircraft_efficiency_copy, lifetime_df], axis=1)

    for k in lifetime_range:
        aircraft_efficiency_rev.loc[:, k] = aircraft_efficiency_rev.loc[:,2021] * efficiency_projection_aircraft.loc[:,k]
    aircraft_efficiency_rev.index.names = (['Aircraft efficiency [PJ/Mvkm]', 'Type'])

    aircraft_efficiency_rev = aircraft_efficiency_rev.astype('float64')
    aircraft_efficiency_rev.to_csv(path_dir_export+'/Aircraft_efficiency.csv')

    ## Maximum number registrations
    registrations_data_2021 = aviation_transport.iloc[51:52, 21].to_frame()
    registrations_data_2021.index.names = ['Registrations']
    registrations_data_2021 = registrations_data_2021.set_index(fuel_index_aircraft['Fuel'], append=True)
    registrations_data_2021.rename(index={'New aircrafts':'Aircrafts (total)'},inplace=True)
    registrations_data_2021.to_csv(path_dir_export+'/Registrations_2021.csv')

    # Calculate capacity in Gpkm or Gtkm
    registrations_data_2021_copy = copy.deepcopy(registrations_data_2021)
    mileage_copy = copy.deepcopy(mileage)
    mileage_2021_copy = mileage_copy[2021].to_frame()
    capacity_2022 = registrations_data_2021 * mileage_2021_copy 
    capacity_2022.index.names = (['Capacity [Mvkm]', 'Type', ]) 
    capacity_2022.to_csv(path_dir_export+'/Capacity_2022.csv')


    ## Capital cost
    # Read Data
    capital_cost = pd.read_excel(path_dir_sup + supplemantary_data_file, sheet_name=sheet_capital_cost, skiprows=2, header=0, index_col=[3,4])
    capital_cost.drop(capital_cost.iloc[:,0:5], axis=1, inplace=True)
    capital_cost_aircraft = capital_cost.iloc[28:31]
    capital_cost_aircraft.index.names = (['Capital Cost [MEUR2015/unit]','Type'])
    capital_cost_aircraft.rename(index={'Aviation' : 'Aircrafts (total)', 'Kerosene planes' : 'Jet Fuel'}, inplace=True)

    # Calculate Capital Cost in MillionEUR2018/Gvehkm
    euro_2018_2015_conv = 1.0357 # euro conversion
    capital_cost_aircraft_copy = copy.deepcopy(capital_cost_aircraft)
    cost_per_capacity = capital_cost_aircraft_copy.div(mileage_copy[2018].values[0], axis=0)  * euro_2018_2015_conv
    cost_per_capacity.index.names = (['Cost [MEUR2018/Gveh-km]','Type'])
    cost_per_capacity.to_csv(path_dir_export+'/Cost_Capacity.csv')