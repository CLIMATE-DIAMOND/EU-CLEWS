# -*- coding: utf-8 -*-
"""
Created on Fri Nov  1 16:16:04 2024

@author: m.karmellos
"""

def rail_transport_function(country, code):

    import pandas as pd
    from pathlib import Path
    import copy
    from sys import exit
    import os
    
    ## Define the country
    country_abb =  code
    country = country
    
    ## Path 
    ## Data files and import path
    data_file_path = '' # Define path
    data_file = data_file_path + country_abb+'/JRC-IDEES-2021_Transport_' + country_abb +'.xlsx'
    sheet_act = 'TrRail_act'
    sheet_energy = 'TrRail_ene'
    
    path_dir_sup = '' # Define path for supplementary transport files
    supplemantary_data_file = 'Supplementary data for transport projections.xlsx'
    sheet_efficiency = 'Efficiency'
    sheet_capital_cost = 'Capital Cost'
    
    
    # Export path
    path_dir_export = data_file_path + country_abb + '/Useful Data/Rail Transport/'
    
    if not os.path.exists(path_dir_export):
        os.makedirs(path_dir_export)
    
    ## Read the excel file with road transport
    rail_transport = pd.read_excel(data_file, sheet_name=sheet_act, header=0, index_col=0)
    year_keys = list(range(2018,2022))
    
    ## Stock of vehicles
    
    # Pull data from the excel file
    rail_stock = rail_transport.iloc[24:33, 18:22]
    rail_stock.index.names = ['Stock (representative configuration)']
    
    rail_stock_passenger = rail_stock.iloc[1:6]
    rail_stock_freight = rail_stock.iloc[7:]
    
    rows_passenger = rail_stock_passenger.shape[0]
    rows_freight = rail_stock_freight.shape[0]
    
    index_list_passenger = []
    for z in range(rows_passenger):
        index_list_passenger.append('Passenger')
    df_index_list_passenger = pd.DataFrame(index_list_passenger, columns=['Type'])
    
    index_list_freight = []
    for z in range(rows_freight):
        index_list_freight.append('Freight')
    df_index_list_freight = pd.DataFrame(index_list_freight, columns=['Type'])
    
    rail_stock_passenger = rail_stock_passenger.set_index(df_index_list_passenger['Type'], append=True)
    rail_stock_freight = rail_stock_freight.set_index(df_index_list_freight['Type'], append=True)
    
    rail_stock_rev = pd.concat([rail_stock_passenger, rail_stock_freight])
    rail_stock_rev_index = rail_stock_rev.index.swaplevel(0,1)
    rail_stock_rev.set_index(rail_stock_rev_index, inplace=True)
    
    rail_stock_rev.loc['Passenger', 'Electric'] = rail_stock_rev.loc['Passenger', 'Electric'] + rail_stock_rev.loc['Passenger', 'Metro and tram, urban light rail']  + rail_stock_rev.loc['Passenger', 'High speed passenger trains'] 
    rail_stock_rev.drop(index = ['Conventional passenger trains',
                                 'Metro and tram, urban light rail',
                                 'High speed passenger trains'], level = 1, axis=0, inplace=True)
    
    rail_stock_rev.to_csv(path_dir_export+'Rail_Stock.csv')
    
    # Calculate existing capacity in Gpkm or Gtkm
    
    existing_capacity = rail_transport.iloc[2:11, 18:22]
    existing_capacity.index.names = ['Existing Capacity [Gpkm or Gtkm]']
    
    # Breakdown mileage into dataframes for passenger and freight rails
    
    existing_capacity.rename(index={'Passenger transport (mio pkm)':'Passenger',
                            'Freight transport (mio tkm)':'Freight',
                             'Diesel':'Diesel oil'},
                             inplace=True)
    
    existing_capacity_passenger = existing_capacity.iloc[1:6] / pow(10,3)
    existing_capacity_freight = existing_capacity.iloc[7:] / pow(10,3)
    
    existing_capacity_passenger = existing_capacity_passenger.set_index(df_index_list_passenger['Type'], append=True)
    existing_capacity_freight = existing_capacity_freight.set_index(df_index_list_freight['Type'], append=True)
    
    existing_capacity_rev = pd.concat([existing_capacity_passenger, existing_capacity_freight])
    existing_capacity_index = existing_capacity_rev.index.swaplevel(0,1)
    existing_capacity_rev.set_index(existing_capacity_index, inplace=True)
    
    existing_capacity_rev.loc['Passenger', 'Electric'] = existing_capacity_rev.loc['Passenger', 'Electric'] + existing_capacity_rev.loc['Passenger', 'Metro and tram, urban light rail']  + existing_capacity_rev.loc['Passenger', 'High speed passenger trains'] 
    existing_capacity_rev.drop(index = ['Conventional passenger trains',
                                 'Metro and tram, urban light rail',
                                 'High speed passenger trains'], level = 1, axis=0, inplace=True)
    
    existing_capacity_rev.to_csv(path_dir_export+'Existing Capacity.csv')
    
    ## Calculate mileage into dataframes for passenger and freight rails
    
    existing_capacity_rev_copy = copy.deepcopy(existing_capacity_rev)
    rail_stock_rev_copy = copy.deepcopy(rail_stock_rev)   
    
    mileage_rev = existing_capacity_rev_copy / rail_stock_rev_copy * pow(10,9)
    mileage_rev.index.rename({'Existing Capacity [Gpkm or Gtkm]' : 'Mileage [Pkm or tkm / vehicle]'}, inplace=True)
    mileage_rev.to_csv(path_dir_export+'Mileage.csv')
    
    # Revise existing capacity of technologies
    
    lifetime_duration = 35
    lifetime_range = range(2022,2071)
    lifetime_list = []
    
    for n in lifetime_range:
        lifetime_list.append(n)
    lifetime_df = pd.DataFrame(columns=lifetime_list)
    
    # Create a revised caopacity
    decom_capacity = copy.deepcopy(existing_capacity_rev)
    
    decom_capacity_rev = pd.concat([decom_capacity, lifetime_df], axis=1)
    
    for k in range(1,lifetime_duration + 1):
        decom_capacity_rev.iloc[:, 3+k] = (1 - k/lifetime_duration) * decom_capacity_rev.iloc[:,3] 
    decom_capacity_rev = decom_capacity_rev.fillna(0)
    decom_capacity_rev.index.set_names(['Type', 'Capacity [Gpkm or Gtkm]'], inplace=True)
    decom_capacity_rev.to_csv(path_dir_export+'/Decommissioned_Capacity.csv')
    
    
    ## Energy consumption
    energy_consumption = pd.read_excel(data_file, sheet_name=sheet_energy, header=0, index_col=0)
    
    # Pull data for total energy consumption and convert to PJ
    total_energy_consumption = energy_consumption.iloc[9:18,18:22]
    total_energy_consumption.rename(index={'Diesel oil (incl. biofuels)':'Diesel oil'},inplace=True)
    total_energy_consumption.index.names = ['Total energy consumption [ktoe]']
    total_energy_consumption_passenger = total_energy_consumption.iloc[1:6]
    total_energy_consumption_freight = total_energy_consumption.iloc[7:]
    
    total_energy_consumption_passenger = total_energy_consumption_passenger.set_index(df_index_list_passenger['Type'], append=True)
    total_energy_consumption_freight = total_energy_consumption_freight.set_index(df_index_list_freight['Type'], append=True)
    
    total_energy_consumption_rev = pd.concat([total_energy_consumption_passenger, total_energy_consumption_freight])
    total_energy_consumption_index = total_energy_consumption_rev.index.swaplevel(0,1)
    total_energy_consumption_rev.set_index(total_energy_consumption_index, inplace=True)
    
    total_energy_consumption_rev.loc['Passenger', 'Electric'] = total_energy_consumption_rev.loc['Passenger', 'Electric'] + total_energy_consumption_rev.loc['Passenger', 'Metro and tram, urban light rail']  + total_energy_consumption_rev.loc['Passenger', 'High speed passenger trains'] 
    total_energy_consumption_rev.drop(index = ['Conventional passenger trains',
                                 'Metro and tram, urban light rail',
                                 'High speed passenger trains'], level = 1, axis=0, inplace=True)
    
    # Process energy consumption data in new units and calculate biofuels ratio
    ktoe_pj = 23.8845897 # convert ktoe to PJ by dividing with this value
    total_energy_consumption_rev_pj = copy.deepcopy(total_energy_consumption_rev)
    
    total_energy_consumption_rev_pj = total_energy_consumption_rev_pj / ktoe_pj
    total_energy_consumption_rev_pj.index.rename({'Total energy consumption [ktoe]' : 'Total energy consumption [PJ]'}, inplace=True)
    
    # Calculate biofuels ratio
    energy_consumption_by_fuel = energy_consumption.iloc[2:7,18:22]
    total_energy_consumption_bio_ratio = copy.deepcopy(total_energy_consumption_rev)
    total_energy_consumption_bio_ratio.drop(index = ['Electric'], level = 1, axis=0, inplace=True)
    total_energy_consumption_bio_ratio = energy_consumption_by_fuel.loc['blended liquid biofuels'] / total_energy_consumption_bio_ratio
    total_energy_consumption_bio_ratio.index.rename({'Total energy consumption [ktoe]' : 'Biofuels Ratio'}, inplace=True)
    
    total_energy_consumption_bio_ratio.to_csv(path_dir_export+'/Biofuel_Ratio.csv')
    
    ## Calculate train efficiency in [PJ/Gveh-km]
    total_energy_consumption_rev_pj_copy = copy.deepcopy(total_energy_consumption_rev_pj)
    existing_capacity_rev_copy = copy.deepcopy(existing_capacity_rev)
    
    train_efficiency = total_energy_consumption_rev_pj_copy / existing_capacity_rev_copy
    train_efficiency.index.rename({'Total energy consumption [PJ]' : 'Train efficiency [PJ/Gpkm or PJ/Gtkm]'}, inplace=True)
        
    # Read efficiency projections
    efficiency_projection = pd.read_excel(path_dir_sup + supplemantary_data_file, sheet_name=sheet_efficiency, skiprows=447, header=0, index_col=[2,3])
    efficiency_projection.drop(efficiency_projection.iloc[:,0:18], axis=1, inplace=True)
    efficiency_projection_train = efficiency_projection.iloc[24:28]
    efficiency_projection_train.index.rename(['Type', 'Efficiency Coefficient'], inplace=True)
    
    #Fix efficiency_data_dict to match the other dataframes
    efficiency_projection_train.rename(index={'Passenger rail' : 'Passenger', 'Freight rail' : 'Freight',
                                              'Electric train' : 'Electric', 'Diesel train' : 'Diesel oil'},
                                       inplace=True)
    
    # Create a revised database of train efficiency
    train_efficiency_copy = copy.deepcopy(train_efficiency)
    
    train_efficiency_rev = pd.concat([train_efficiency_copy, lifetime_df], axis=1)
    
    for k in lifetime_range:
        train_efficiency_rev.loc[:, k] = train_efficiency_rev.loc[:,2021] * efficiency_projection_train.loc[:,k]
    train_efficiency_rev.index.names = (['Type', 'Train efficiency [PJ/Gpkm or PJ/Gtkm]'])
    
    train_efficiency_rev = train_efficiency_rev.astype('float64')
    train_efficiency_rev.to_csv(path_dir_export+'/Train_efficiency.csv')
    
    ## Maximum number registrations
    registrations_data_2021 = rail_transport.iloc[35:44, 21].to_frame()
    registrations_data_2021.index.names = ['Registrations']
    registrations_data_2021_passenger = registrations_data_2021.iloc[1:6]
    registrations_data_2021_freight = registrations_data_2021.iloc[7:]
    
    registrations_data_2021_passenger = registrations_data_2021_passenger.set_index(df_index_list_passenger['Type'], append=True)
    registrations_data_2021_freight = registrations_data_2021_freight.set_index(df_index_list_freight['Type'], append=True)
    
    registrations_data_2021_rev = pd.concat([registrations_data_2021_passenger, registrations_data_2021_freight])
    registrations_data_2021_index = registrations_data_2021_rev.index.swaplevel(0,1)
    registrations_data_2021_rev.set_index(registrations_data_2021_index, inplace=True)
    
    registrations_data_2021_rev.loc['Passenger', 'Electric'] = registrations_data_2021_rev.loc['Passenger', 'Electric'] + registrations_data_2021_rev.loc['Passenger', 'Metro and tram, urban light rail']  + registrations_data_2021_rev.loc['Passenger', 'High speed passenger trains'] 
    registrations_data_2021_rev.drop(index = ['Conventional passenger trains',
                                 'Metro and tram, urban light rail',
                                 'High speed passenger trains'], level = 1, axis=0, inplace=True)
    
    registrations_data_2021_rev.to_csv(path_dir_export+'/Registrations_2021.csv')
    
    # Calculate capacity in Gpkm or Gtkm
    registrations_data_2021_rev_copy = copy.deepcopy(registrations_data_2021_rev)
    mileage_rev_copy = copy.deepcopy(mileage_rev)
    mileage_rev_2021_copy = mileage_rev_copy[2021].to_frame()
    capacity_2022 = registrations_data_2021_rev_copy * mileage_rev_2021_copy / pow(10,9)
    capacity_2022.index.names = (['Type', 'Capacity [Gpkm or Gtkm]']) 
    capacity_2022.to_csv(path_dir_export+'/Capacity_2022.csv')
    
    
    ## Capital cost
    # Read Data
    capital_cost = pd.read_excel(path_dir_sup+supplemantary_data_file, sheet_name=sheet_capital_cost, skiprows=2, header=0, index_col=[3,4])
    capital_cost.drop(capital_cost.iloc[:,0:5], axis=1, inplace=True)
    
    capital_cost_passenger = capital_cost.iloc[24:26]
    capital_cost_freight = capital_cost.iloc[26:28]
    
    capital_cost_rev = pd.concat([capital_cost_passenger, capital_cost_freight], axis=0)
    
    capital_cost_rev.index.names = (['Type','Capital Cost [MEUR2015/unit]'])
    
    # Fix capital_cost_dict to match the other dataframes
    capital_cost_rev.rename(index = {'Passenger rail' : 'Passenger', 'Diesel train' : 'Diesel oil', 
                                                   'Freight rail' : 'Freight', 'Electric train' : 'Electric'}, inplace=True)
    
    
    # Calculate Capital Cost in MillionEUR2018/Gvehkm
    euro_2018_2015_conv = 1.0357 # euro conversion
    
    capital_cost_rev_copy = copy.deepcopy(capital_cost_rev)
    
    cost_per_capacity = capital_cost_rev_copy.div(mileage_rev_copy[2018], axis=0) * pow(10,9) * euro_2018_2015_conv
    cost_per_capacity.index.names = (['Type','Cost [MEUR2018/Gveh-km]'])
    cost_per_capacity.to_csv(path_dir_export+'/Cost_Capacity.csv')