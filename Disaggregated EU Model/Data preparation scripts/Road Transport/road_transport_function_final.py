# -*- coding: utf-8 -*-
"""
Created on Fri Nov  1 16:16:04 2024

@author: m.karmellos
"""

def road_transport_function(country, code):

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
    data_path = ' ' # define the path for input data
    data_file = data_path + country_abb + '/JRC-IDEES-2021_Transport_'+ country_abb +'.xlsx'
    sheet_act = 'TrRoad_act'
    sheet_energy = 'TrRoad_ene'

    path_dir_sup = '04 Data/Transport/' # define the path for supplementary data
    supplemantary_data_file = 'Supplementary data for transport projections.xlsx'
    sheet_efficiency = 'Efficiency'
    sheet_capital_cost = 'Capital Cost'

    path_dir_passenger_cars = '04 Data/Transport/Passenger Cars/Passenger Cars by type ' # define the path for supplementary data for passenger cars
    path_dir_lorries = '04 Data/Transport/Lorries/lorries by type ' # define the path for supplementary data for lorries

    # Export path
    path_dir_export = data_path + country_abb + '/Useful Data/Road Transport/' # define an export path f

    if not os.path.exists(path_dir_export):
        os.makedirs(path_dir_export)
        
    for filename in os.listdir(path_dir_export):
            file_path = os.path.join(path_dir_export, filename)
            
            # Check if a file exists in the folder and delete it
            if os.path.isfile(file_path):
                os.remove(file_path)
                
    ## Read the excel file with road transport
    road_transport = pd.read_excel(data_file, sheet_name=sheet_act, header=0, index_col=0)
    year_keys = list(range(2018,2022))

    ## Pull data for mileage
    mileage = road_transport.iloc[165:191, 18:22]
    mileage.index.names = ['Mileage [km/vehicle]']

    # Breakdown mileage into dataframes for different type using year as key
    mileage_passenger = mileage.iloc[4:10]
    mileage_coaches = mileage.iloc[11:16]
    mileage_lcv = mileage.iloc[18:23]
    mileage_heavy = mileage.iloc[23].to_frame().transpose()

    vehicle_types_keys = ['Passenger', 'Coaches', 'LCV', 'HGV']
    vehicle_types_mileage = [mileage_passenger, mileage_coaches, mileage_lcv, mileage_heavy]
    vehicle_types_mileage_dict = dict(zip(vehicle_types_keys, vehicle_types_mileage)) # Dictionary of mileage per car type

    # Create a revised mileage list
    rev_vehicle_types_mileage_dict = copy.deepcopy(vehicle_types_mileage_dict)

    rev_vehicle_types_mileage_dict['Passenger'].loc['Hybrid electric-petrol'] = rev_vehicle_types_mileage_dict['Passenger'].loc['Gasoline engine']
    rev_vehicle_types_mileage_dict['Passenger'].loc['Hybrid electric-diesel'] = rev_vehicle_types_mileage_dict['Passenger'].loc['Diesel oil engine']
    rev_vehicle_types_mileage_dict['LCV'].loc['Hybrid electric-petrol'] = rev_vehicle_types_mileage_dict['LCV'].loc['Gasoline engine']
    rev_vehicle_types_mileage_dict['LCV'].loc['Hybrid electric-diesel'] = rev_vehicle_types_mileage_dict['LCV'].loc['Diesel oil engine']
    rev_vehicle_types_mileage_dict['LCV'].drop(index = 'LPG engine', inplace = True)
    rev_vehicle_types_mileage_dict['HGV'].rename(index={'Heavy goods vehicles' : 'Diesel oil engine'}, inplace=True)
    rev_vehicle_types_mileage_dict['Coaches'].drop(index=['LPG engine', 'Gasoline engine'], inplace = True)

    for z in vehicle_types_keys:
        rev_vehicle_types_mileage_dict[z].to_csv(path_dir_export+'Revised_Mileage_'+str(z)+'.csv')


    ## Stock of vehicles

    # Pull data from the excel file
    vehicles_stock = road_transport.iloc[55:81, 18:22]
    vehicles_stock.index.names = ['Vehicles']

    vehicles_stock_passenger = vehicles_stock.iloc[4:10]
    vehicles_stock_coaches = vehicles_stock.iloc[11:16]
    vehicles_stock_lcv = vehicles_stock.iloc[18:23]
    vehicles_stock_heavy = vehicles_stock.iloc[23].to_frame().transpose()

    vehicle_types_stock = [vehicles_stock_passenger, vehicles_stock_coaches, vehicles_stock_lcv, vehicles_stock_heavy]
    vehicle_types_stock_dict = dict(zip(vehicle_types_keys, vehicle_types_stock)) # Dictionary of stock per car type

    # Pull eurostat data for passenger cars and lorries to make revised calculations

    passenger_cars_eu = []
    for z in year_keys:
        passenger_cars_eu_file = Path(path_dir_passenger_cars + str(z) + '.csv')
        passenger_cars_eu_data = pd.read_csv(passenger_cars_eu_file, index_col=0)
        passenger_cars_eu.append(passenger_cars_eu_data)

    passenger_cars_eu_dict = dict(zip(year_keys, passenger_cars_eu)) # Final dictionary of cars for the specific years

    lorries_eu = []
    for z in year_keys:
        lorries_file = Path(path_dir_lorries + str(z) + '.csv')
        lorries_data = pd.read_csv(lorries_file, index_col=0)
        lorries_eu.append(lorries_data)

    lorries_eu_dict = dict(zip(year_keys, lorries_eu)) # Final dictionary of lorries for the specific years

    # MAKE REVISIONS IN Vehicles Stock
    # Add hybrid cars to the main stock dictionary for passenger cars

    passenger_hybrid_petrol_list = []
    passenger_hybrid_diesel_list = []
    for z in year_keys:
        if country in passenger_cars_eu_dict[z].index:
            passenger_cars_eu_hybrid_petrol_aux = passenger_cars_eu_dict[z].loc[[country], ['Hybrid electric-petrol']]
            passenger_cars_eu_hybrid_diesel_aux = passenger_cars_eu_dict[z].loc[[country], ['Hybrid diesel-electric']]
            passenger_hybrid_petrol_list.append(passenger_cars_eu_hybrid_petrol_aux)
            passenger_hybrid_diesel_list.append(passenger_cars_eu_hybrid_diesel_aux)
        else:
            passenger_cars_eu_hybrid_petrol_aux = pd.Series(0)
            passenger_cars_eu_hybrid_diesel_aux = pd.Series(0)
            passenger_hybrid_petrol_list.append(passenger_cars_eu_hybrid_petrol_aux)
            passenger_hybrid_diesel_list.append(passenger_cars_eu_hybrid_diesel_aux)

    passengers_hybrid_petrol_ep_row = pd.concat(passenger_hybrid_petrol_list, axis=1)
    passengers_hybrid_petrol_ep_row.columns = year_keys
    passengers_hybrid_petrol_ep_row.index = ['Hybrid electric-petrol']

    passengers_hybrid_diesel_ep_row = pd.concat(passenger_hybrid_diesel_list, axis=1)
    passengers_hybrid_diesel_ep_row.columns = year_keys
    passengers_hybrid_diesel_ep_row.index = ['Hybrid electric-diesel']

    vehicle_types_stock_dict['Passenger'] = pd.concat([vehicle_types_stock_dict['Passenger'], passengers_hybrid_petrol_ep_row, passengers_hybrid_diesel_ep_row], axis=0)

    # Add hybrid lorries to the stock of LCV vehicles
    lorries_hybrid_petrol_list =[]
    lorries_hybrid_diesel_list =[]

    for z in year_keys:
        if country in lorries_eu_dict[z].index:
            vehicles_stock_lorries_gasoline = vehicle_types_stock_dict['LCV'].loc[['Gasoline engine'], z]
            lorries_cars_eu_hybrid_petrol_aux = lorries_eu_dict[z].loc[[country], ['Hybrid electric-petrol']]
            lorries_cars_eu_hybrid_diesel_aux = lorries_eu_dict[z].loc[[country], ['Hybrid diesel-electric']]
            lorries_hybrid_petrol_list.append(lorries_cars_eu_hybrid_petrol_aux)
            lorries_hybrid_diesel_list.append(lorries_cars_eu_hybrid_diesel_aux)
        else:
            lorries_cars_eu_hybrid_petrol_aux = pd.Series(0)
            lorries_cars_eu_hybrid_diesel_aux = pd.Series(0)
            lorries_hybrid_petrol_list.append(lorries_cars_eu_hybrid_petrol_aux)
            lorries_hybrid_diesel_list.append(lorries_cars_eu_hybrid_diesel_aux)

    lorries_hybrid_petrol_ep_row = pd.concat(lorries_hybrid_petrol_list, axis=1)
    lorries_hybrid_petrol_ep_row.columns = year_keys
    lorries_hybrid_petrol_ep_row.index = ['Hybrid electric-petrol']

    lorries_hybrid_diesel_ep_row = pd.concat(lorries_hybrid_diesel_list, axis=1)
    lorries_hybrid_diesel_ep_row.columns = year_keys
    lorries_hybrid_diesel_ep_row.index = ['Hybrid electric-diesel']

    vehicle_types_stock_dict['LCV'] = pd.concat([vehicle_types_stock_dict['LCV'], lorries_hybrid_petrol_ep_row, lorries_hybrid_diesel_ep_row], axis=0)

    # Replace values in stock of vehicles

    # Replace gasoline values in passenger cars
    vehicle_types_stock_dict['Passenger'].loc['Gasoline engine'] = vehicle_types_stock_dict['Passenger'].loc['Gasoline engine'] - vehicle_types_stock_dict['Passenger'].loc['Hybrid electric-petrol'] 
    vehicle_types_stock_dict['Passenger'].loc['Diesel oil engine'] = vehicle_types_stock_dict['Passenger'].loc['Diesel oil engine'] - vehicle_types_stock_dict['Passenger'].loc['Hybrid electric-diesel'] 

    # Replace gasoline values in lorries and add lpg 
    vehicle_types_stock_dict['LCV'].loc['Gasoline engine'] = vehicle_types_stock_dict['LCV'].loc['Gasoline engine'] + vehicle_types_stock_dict['LCV'].loc['LPG engine'] - vehicle_types_stock_dict['LCV'].loc['Hybrid electric-petrol']
    vehicle_types_stock_dict['LCV'].loc['Diesel oil engine'] = vehicle_types_stock_dict['LCV'].loc['Diesel oil engine'] - vehicle_types_stock_dict['LCV'].loc['Hybrid electric-diesel']
    vehicle_types_stock_dict['LCV'].drop(index=['LPG engine'], inplace = True)

    # Revision of diesel engine in coaches category to include gasoline and lpg
    vehicle_types_stock_dict['Coaches'].loc['Diesel oil engine'] = vehicle_types_stock_dict['Coaches'].loc['Diesel oil engine'] + vehicle_types_stock_dict['Coaches'].loc['Gasoline engine'] + vehicle_types_stock_dict['Coaches'].loc['LPG engine']
    vehicle_types_stock_dict['Coaches'].drop(index=['LPG engine', 'Gasoline engine'], inplace = True)

    # Revision of heavy good vehicles to represent diesel engines
    vehicle_types_stock_dict['HGV'].loc['Diesel oil engine'] = vehicle_types_stock_dict['HGV'].loc['Heavy goods vehicles']
    vehicle_types_stock_dict['HGV'].drop(index=['Heavy goods vehicles'], inplace = True)

    # Extract vechicle stock
    for z in vehicle_types_keys:
        vehicle_types_stock_dict[z].to_csv(path_dir_export+'Vehicles Stock_'+str(z)+'.csv')

    vehicle_types_stock_dict_copy = copy.deepcopy(vehicle_types_stock_dict)

    # Calculate existing capacity in Gveh-km

    existing_capacity = []
    for z in vehicle_types_keys:
        existing_capacity_aux = vehicle_types_stock_dict_copy[z] * rev_vehicle_types_mileage_dict[z] / pow(10,9)
        existing_capacity_aux.index.names = ['Capacity [Gveh-km]']
        existing_capacity.append(existing_capacity_aux)

    existing_capacity_dict = dict(zip(vehicle_types_keys, existing_capacity))

    # Revise existing capacity of technologies

    lifetime_dict = {'Passenger':12, 'Coaches':10, 'LCV':12, 'HGV': 15}
    lifetime_range = range(2022,2071)
    lifetime_list = []

    for n in lifetime_range:
        lifetime_list.append(n)
    lifetime_df = pd.DataFrame(columns=lifetime_list)

    # Create a revised stock of vehicles for decomissioning
    decom_capacity_dict = copy.deepcopy(existing_capacity_dict)

    for z in vehicle_types_keys:
        decom_capacity_dict[z] = pd.concat([decom_capacity_dict[z], lifetime_df], axis=1)
        for k in range(1,lifetime_dict[z] + 1):
            decom_capacity_dict[z].iloc[:, 3+k] = (1 - k/lifetime_dict[z]) * decom_capacity_dict[z].iloc[:,3] 
        decom_capacity_dict[z] = decom_capacity_dict[z].fillna(0)
        decom_capacity_dict[z].to_csv(path_dir_export+'/Capacity_'+str(z)+'.csv')

    # Energy consumption
    energy_consumption = pd.read_excel(data_file, sheet_name=sheet_energy, header=0, index_col=0)
    energy_consumption.index.names = ['Total energy consumption [ktoe]']

    # Pull data for total energy consumption and convert to PJ
    total_energy_consumption = energy_consumption.iloc[15:55,18:22]
    total_energy_consumption_passenger = total_energy_consumption.iloc[5:16]
    total_energy_consumption_passenger.rename(index={'Plug-in hybrid electric (Gasoline and electricity)':'Plug-in hybrid electric'},inplace=True)
    total_energy_consumption_coaches = total_energy_consumption.iloc[17:25]
    total_energy_consumption_lcv = total_energy_consumption.iloc[27:35]
    total_energy_consumption_heavy = total_energy_consumption.iloc[36:40]

    total_energy_consumption_type = [total_energy_consumption_passenger, total_energy_consumption_coaches, total_energy_consumption_lcv, total_energy_consumption_heavy]
    total_energy_consumption_dict = dict(zip(vehicle_types_keys, total_energy_consumption_type))

    # Process energy consumption data in new units and calculate biofuels ratio
    ktoe_pj = 23.8845897 # convert ktoe to PJ by dividing with this value
    total_energy_consumption_pj_dict = copy.deepcopy(total_energy_consumption_dict)

    total_energy_consumption_pj_list = []
    for z in vehicle_types_keys:
        total_energy_consumption_pj = total_energy_consumption_pj_dict[z] / ktoe_pj
        total_energy_consumption_pj.index.names = ['Total energy consumption [PJ]']
        total_energy_consumption_pj_list.append(total_energy_consumption_pj)
    total_energy_consumption_pj_dict = dict(zip(vehicle_types_keys, total_energy_consumption_pj_list))

    # Revise energy consumption by types of vehicles

    total_energy_consumption_pj_dict['LCV'].loc['Gasoline engine'] = total_energy_consumption_pj_dict['LCV'].loc['Gasoline engine'] + total_energy_consumption_pj_dict['LCV'].loc['LPG engine'] 
    total_energy_consumption_pj_dict['LCV'].drop(index=['LPG engine'], inplace = True)

    total_energy_consumption_pj_dict['Coaches'].loc['Diesel oil engine'] = total_energy_consumption_pj_dict['Coaches'].loc['Diesel oil engine'] + total_energy_consumption_pj_dict['Coaches'].loc['Gasoline engine'] + total_energy_consumption_pj_dict['Coaches'].loc['LPG engine']
    total_energy_consumption_pj_dict['Coaches'] = total_energy_consumption_pj_dict['Coaches'].groupby(total_energy_consumption_pj_dict['Coaches'].index, sort=False).sum()
    total_energy_consumption_pj_dict['Coaches'].drop(index=['Gasoline engine', 'LPG engine'], inplace = True)
    total_energy_consumption_pj_dict['Coaches'] = total_energy_consumption_pj_dict['Coaches'].reindex(['Diesel oil engine', 'of which biofuels', 'Natural gas engine', 'of which biogas', 'Battery electric vehicles'])

    total_energy_consumption_pj_dict['HGV'].loc['Diesel oil engine'] = total_energy_consumption_pj_dict['HGV'].loc['Domestic']+ total_energy_consumption_pj_dict['HGV'].loc['International']
    total_energy_consumption_pj_dict['HGV'].drop(index=['Domestic', 'International'], inplace = True)
    total_energy_consumption_pj_dict['HGV'] = total_energy_consumption_pj_dict['HGV'].groupby(total_energy_consumption_pj_dict['HGV'].index, sort=False).sum()
    total_energy_consumption_pj_dict['HGV'] = total_energy_consumption_pj_dict['HGV'].reindex(['Diesel oil engine', 'of which biofuels'])

    # Calculate biofuels ratio

    total_energy_consumption_bio_ratio_dict = copy.deepcopy(total_energy_consumption_pj_dict)
    for z in vehicle_types_keys:
        total_energy_consumption_bio_ratio_dict[z].index.names = ['Biofuel/Biogas ratio']
        
    total_energy_consumption_bio_ratio_dict['Passenger'].loc['Gasoline engine'] = total_energy_consumption_bio_ratio_dict['Passenger'].iloc[1,:] / total_energy_consumption_bio_ratio_dict['Passenger'].loc['Gasoline engine']
    total_energy_consumption_bio_ratio_dict['Passenger'].loc['Diesel oil engine'] = total_energy_consumption_bio_ratio_dict['Passenger'].iloc[3,:] / total_energy_consumption_bio_ratio_dict['Passenger'].loc['Diesel oil engine']
    total_energy_consumption_bio_ratio_dict['Passenger'].loc['Natural gas engine'] = total_energy_consumption_bio_ratio_dict['Passenger'].iloc[6,:] / total_energy_consumption_bio_ratio_dict['Passenger'].loc['Natural gas engine']
    total_energy_consumption_bio_ratio_dict['Passenger'].loc['Plug-in hybrid electric'] = total_energy_consumption_bio_ratio_dict['Passenger'].iloc[8,:] / total_energy_consumption_bio_ratio_dict['Passenger'].loc['Plug-in hybrid electric']
    total_energy_consumption_bio_ratio_dict['Passenger'].drop(index=['of which biofuels', 'LPG engine', 'of which biogas', 'of which electricity', 'Battery electric vehicles'], inplace = True)

    total_energy_consumption_bio_ratio_dict['LCV'].loc['Gasoline engine'] = total_energy_consumption_bio_ratio_dict['LCV'].iloc[1,:] / total_energy_consumption_bio_ratio_dict['LCV'].loc['Gasoline engine']
    total_energy_consumption_bio_ratio_dict['LCV'].loc['Diesel oil engine'] = total_energy_consumption_bio_ratio_dict['LCV'].iloc[3,:] / total_energy_consumption_bio_ratio_dict['LCV'].loc['Diesel oil engine']
    total_energy_consumption_bio_ratio_dict['LCV'].loc['Natural gas engine'] = total_energy_consumption_bio_ratio_dict['LCV'].iloc[5,:] / total_energy_consumption_bio_ratio_dict['LCV'].loc['Natural gas engine']
    total_energy_consumption_bio_ratio_dict['LCV'].drop(index=['of which biofuels', 'of which biogas', 'Battery electric vehicles'], inplace = True)

    total_energy_consumption_bio_ratio_dict['Coaches'].loc['Diesel oil engine'] = total_energy_consumption_bio_ratio_dict['Coaches'].iloc[1,:] / total_energy_consumption_bio_ratio_dict['Coaches'].loc['Diesel oil engine']
    total_energy_consumption_bio_ratio_dict['Coaches'].loc['Natural gas engine'] = total_energy_consumption_bio_ratio_dict['Coaches'].iloc[3,:] / total_energy_consumption_bio_ratio_dict['Coaches'].loc['Natural gas engine']
    total_energy_consumption_bio_ratio_dict['Coaches'].drop(index=['of which biofuels', 'of which biogas'], inplace = True)

    total_energy_consumption_bio_ratio_dict['HGV'].loc['Diesel oil engine'] = total_energy_consumption_bio_ratio_dict['HGV'].iloc[1,:] / total_energy_consumption_bio_ratio_dict['HGV'].loc['Diesel oil engine']
    total_energy_consumption_bio_ratio_dict['HGV'].drop(index=['of which biofuels'], inplace = True)

    for z in vehicle_types_keys:
        total_energy_consumption_bio_ratio_dict[z].to_csv(path_dir_export+'/Biofuel_Ratio_'+str(z)+'.csv')
        
    # Create a restructured dataframe for total energy consumption without biofuels
    rev_total_energy_consumption_dict = copy.deepcopy(total_energy_consumption_pj_dict)

    rev_total_energy_consumption_dict['Passenger'].drop(index=['of which biofuels', 'of which biogas', 'of which electricity'], inplace = True)
    rev_total_energy_consumption_dict['LCV'].drop(index=['of which biofuels', 'of which biogas'], inplace = True)
    rev_total_energy_consumption_dict['Coaches'].drop(index=['of which biofuels', 'of which biogas'], inplace = True)
    rev_total_energy_consumption_dict['HGV'].drop(index=['of which biofuels'], inplace = True)


    # Calculate energy consumption by vehicle type to include hybrids
    vehicle_energy_consumption = energy_consumption.iloc[112:138,18:22]
    vehicle_energy_consumption.index.names = ['Energy consumption per vehicle annum (kgoe/vehicle)']
    vehicle_energy_consumption_passenger = vehicle_energy_consumption.iloc[4:10]
    vehicle_energy_consumption_coaches = vehicle_energy_consumption.iloc[11:16]
    vehicle_energy_consumption_lcv = vehicle_energy_consumption.iloc[18:23]
    vehicle_energy_consumption_heavy = vehicle_energy_consumption.iloc[24:26]

    vehicle_energy_consumption_type = [vehicle_energy_consumption_passenger, vehicle_energy_consumption_coaches, vehicle_energy_consumption_lcv, vehicle_energy_consumption_heavy]
    vehicle_energy_consumption_dict = dict(zip(vehicle_types_keys, vehicle_energy_consumption_type))

    vehicle_energy_consumption_pj_dict = copy.deepcopy(vehicle_energy_consumption_dict)

    for z in vehicle_types_keys:
        vehicle_energy_consumption_pj_dict[z] = vehicle_energy_consumption_pj_dict[z] / pow(10,6) / ktoe_pj
        vehicle_energy_consumption_pj_dict[z].index.names = ['Energy consumption per vehicle annum (PJ/vehicle)']

    hybrid_to_engine = 0.6612 # energy consumption of hybrids compared to conventional engines

    vehicle_energy_consumption_pj_dict['Passenger'].loc['Hybrid electric-petrol'] = vehicle_energy_consumption_pj_dict['Passenger'].loc['Gasoline engine'] * hybrid_to_engine
    vehicle_energy_consumption_pj_dict['Passenger'].loc['Hybrid electric-diesel'] = vehicle_energy_consumption_pj_dict['Passenger'].loc['Diesel oil engine'] * hybrid_to_engine

    vehicle_energy_consumption_pj_dict['LCV'].loc['Gasoline engine'] = vehicle_energy_consumption_pj_dict['LCV'].loc['Gasoline engine'] + vehicle_energy_consumption_pj_dict['LCV'].loc['LPG engine'] 
    vehicle_energy_consumption_pj_dict['LCV'].loc['Hybrid electric-petrol'] = vehicle_energy_consumption_pj_dict['LCV'].loc['Gasoline engine'] * hybrid_to_engine
    vehicle_energy_consumption_pj_dict['LCV'].loc['Hybrid electric-diesel'] = vehicle_energy_consumption_pj_dict['LCV'].loc['Diesel oil engine'] * hybrid_to_engine
    vehicle_energy_consumption_pj_dict['LCV'].drop(index=['LPG engine'], inplace = True)

    vehicle_energy_consumption_pj_dict['Coaches'].loc['Diesel oil engine'] = vehicle_energy_consumption_pj_dict['Coaches'].loc['Diesel oil engine'] + vehicle_energy_consumption_pj_dict['Coaches'].loc['Gasoline engine'] + vehicle_energy_consumption_pj_dict['Coaches'].loc['LPG engine']
    vehicle_energy_consumption_pj_dict['Coaches'].drop(index=['Gasoline engine', 'LPG engine'], inplace = True)

    vehicle_energy_consumption_pj_dict['HGV'].loc['Diesel oil engine'] = vehicle_energy_consumption_pj_dict['HGV'].loc['Domestic']+  vehicle_energy_consumption_pj_dict['HGV'].loc['International']
    vehicle_energy_consumption_pj_dict['HGV'].drop(index=['Domestic', 'International'], inplace = True)

    # Calculate revised total energy consumption in PJ
    copy_vehicle_energy_consumption_pj_dict = copy.deepcopy(vehicle_energy_consumption_pj_dict)
    copy_vehicle_types_stock_dict = copy.deepcopy(vehicle_types_stock_dict)

    ## AUXILIARY TABLE - IGNORE VALUES OTHER THAN HYBRID

    new_total_energy_consumption_pj_list = []
    for z in vehicle_types_keys:
        new_total_energy_consumption_pj_aux = copy_vehicle_energy_consumption_pj_dict[z] * copy_vehicle_types_stock_dict[z]
        new_total_energy_consumption_pj_aux.index.names = ['Total energy consumption [PJ]']
        new_total_energy_consumption_pj_list.append(new_total_energy_consumption_pj_aux)

    new_total_energy_consumption_dict = dict(zip(vehicle_types_keys, new_total_energy_consumption_pj_list))

    # Important - Fix rev total energy consumption with data only for hybrid vehicles calculated
    # in new_total_energy_consumption. IGNORE OTHER VALUES

    rev_total_energy_consumption_dict['Passenger'].loc['Hybrid electric-petrol'] = new_total_energy_consumption_dict['Passenger'].loc['Hybrid electric-petrol']
    rev_total_energy_consumption_dict['Passenger'].loc['Hybrid electric-diesel'] = new_total_energy_consumption_dict['Passenger'].loc['Hybrid electric-diesel']
    rev_total_energy_consumption_dict['LCV'].loc['Hybrid electric-petrol'] = new_total_energy_consumption_dict['LCV'].loc['Hybrid electric-petrol']
    rev_total_energy_consumption_dict['LCV'].loc['Hybrid electric-diesel'] = new_total_energy_consumption_dict['LCV'].loc['Hybrid electric-diesel']

    copy_rev_total_energy_consumption_dict = copy.deepcopy(rev_total_energy_consumption_dict)
    copy_existing_capacity_dict = copy.deepcopy(existing_capacity_dict)

    ## Calculate vehicle efficiency in [PJ/Gveh-km]
    vehicle_efficiency = []
    for z in vehicle_types_keys:
        vehicle_efficiency_aux = copy_rev_total_energy_consumption_dict[z] / copy_existing_capacity_dict[z]
        vehicle_efficiency_aux.index.names = ['Vehicle efficiency [PJ/Gveh-km]']
        copy_rev_total_energy_consumption_dict[z].index.names = ['Total energy consumption [PJ]']
        vehicle_efficiency.append(vehicle_efficiency_aux)

    vehicle_efficiency_dict = dict(zip(vehicle_types_keys, vehicle_efficiency))

    # Read efficiency projections
    efficiency_projection = pd.read_excel(path_dir_sup + supplemantary_data_file, sheet_name=sheet_efficiency, skiprows=447, header=0, index_col=[2,3])
    efficiency_projection.drop(efficiency_projection.iloc[:,0:18], axis=1, inplace=True)
    efficiency_projection_passenger = efficiency_projection.iloc[0:7].reset_index(level='Shipping/Maritime', drop=True)

    efficiency_projection_coaches = efficiency_projection.iloc[8:11].reset_index(level='Shipping/Maritime', drop=True)
    efficiency_projection_lcv = efficiency_projection.iloc[12:18].reset_index(level='Shipping/Maritime', drop=True)
    efficiency_projection_freight = efficiency_projection.iloc[19].to_frame().transpose().reset_index(level=0, drop=True)

    efficiency_projection_list = [efficiency_projection_passenger, efficiency_projection_coaches, efficiency_projection_lcv, efficiency_projection_freight]
    efficiency_projection_dict = dict(zip(vehicle_types_keys, efficiency_projection_list))

    for z in vehicle_types_keys:
        efficiency_projection_dict[z].index.names = ['Efficiency']

    # Fix efficiency_data_dict to match the other dataframes
    efficiency_projection_dict['Passenger'].rename(index = {'Gasoline vehicles' : 'Gasoline engine', 'Diesel vehicles' : 'Diesel oil engine', 
                                                   'CNG/LNG vehicles' : 'Natural gas engine', 'LPG vehicles' : 'LPG engine', 
                                                   'Hybrid electric vehicles' : 'Hybrid electric-petrol', 'Plug-in electric vehicles' : 'Plug-in hybrid electric' 
                                                   }, inplace=True)
    efficiency_projection_dict['Passenger'].loc['Hybrid electric-diesel'] = efficiency_projection_dict['Passenger'].loc['Hybrid electric-petrol']

    efficiency_projection_dict['LCV'].rename(index = {'Gasoline light trucks' : 'Gasoline engine', 'Diesel light trucks' : 'Diesel oil engine', 
                                                   'CNG/LNG light trucks' : 'Natural gas engine', 'Hybrid electric light trucks' : 'Hybrid electric-petrol',  
                                                   'Battery electric light trucks' : 'Battery electric vehicles'}, inplace=True)
    efficiency_projection_dict['LCV'].loc['Hybrid electric-diesel'] = efficiency_projection_dict['Passenger'].loc['Hybrid electric-petrol']
    efficiency_projection_dict['LCV'].drop(index = 'Plug-in electric light trucks', inplace=True)

    efficiency_projection_dict['Coaches'].rename(index = {'Diesel bus' : 'Diesel oil engine', 'CNG bus' : 'Natural gas engine', 'LPG vehicles' : 'LPG engine', 
                                                   'Electric bus' : 'Battery electric vehicles' 
                                                   }, inplace=True)

    efficiency_projection_dict['HGV'].rename(index = {'Diesel heavy trucks' : 'Diesel oil engine'}, inplace=True)

    # Create a revised stock of vehicles for efficency
    rev_vehicle_efficiency_dict = copy.deepcopy(vehicle_efficiency_dict)

    for z in vehicle_types_keys:
        rev_vehicle_efficiency_dict[z] = pd.concat([vehicle_efficiency_dict[z], lifetime_df], axis=1)
        for k in lifetime_range:
            rev_vehicle_efficiency_dict[z].loc[:, k] = rev_vehicle_efficiency_dict[z].loc[:,2021] * efficiency_projection_dict[z].loc[:,k]
        rev_vehicle_efficiency_dict[z].index.names = ['Vehicle efficiency [PJ/Gveh-km]']
        rev_vehicle_efficiency_dict[z].to_csv(path_dir_export+'/Vehicle_Efficiency_'+str(z)+'.csv')

    ## Maximum number registrations
    registrations_data = road_transport.iloc[109:135, 18:22]
    registrations_data_2021 = road_transport.iloc[109:135, 21]

    # Calculate a the share of hybrid vehicles for passenger and LCV for year 2021

    if vehicle_types_stock_dict['Passenger'][2021].loc['Gasoline engine'] > 0:
        passenger_hybrid_petrol_2021 = vehicle_types_stock_dict['Passenger'][2021].loc['Hybrid electric-petrol']/vehicle_types_stock_dict['Passenger'][2021].loc['Gasoline engine']
    else:
        passenger_hybrid_petrol_2021 = 0
        
    if vehicle_types_stock_dict['Passenger'][2021].loc['Diesel oil engine'] > 0:
        passenger_hybrid_diesel_2021 = vehicle_types_stock_dict['Passenger'][2021].loc['Hybrid electric-diesel']/vehicle_types_stock_dict['Passenger'][2021].loc['Diesel oil engine']
    else:
        passenger_hybrid_diesel_2021 = 0
        
    if vehicle_types_stock_dict['LCV'][2021].loc['Gasoline engine'] > 0 :
        lcv_hybrid_petrol_2021 = vehicle_types_stock_dict['LCV'][2021].loc['Hybrid electric-petrol']/vehicle_types_stock_dict['LCV'][2021].loc['Gasoline engine']
    else:
        lcv_hybrid_petrol_2021 = 0

    if vehicle_types_stock_dict['LCV'][2021].loc['Diesel oil engine'] > 0 :
        lcv_hybrid_diesel_2021 = vehicle_types_stock_dict['LCV'][2021].loc['Hybrid electric-diesel']/vehicle_types_stock_dict['LCV'][2021].loc['Diesel oil engine']
    else:
        lcv_hybrid_diesel_2021 = 0

    # Reshape vehicle technologies for each categories
    registrations_data_2021_passenger = registrations_data_2021.iloc[4:10]
    registrations_data_2021_coaches = registrations_data_2021.iloc[11:16]
    registrations_data_2021_lcv = registrations_data_2021.iloc[18:23]
    registrations_data_2021_heavy = registrations_data_2021.iloc[24:26]

    registrations_data_2021_list = [registrations_data_2021_passenger, registrations_data_2021_coaches, registrations_data_2021_lcv, registrations_data_2021_heavy]
    registrations_data_2021_dict = dict(zip(vehicle_types_keys, registrations_data_2021_list))

    registrations_data_2021_dict['Passenger'].loc['Hybrid electric-petrol'] = registrations_data_2021_dict['Passenger'].loc['Gasoline engine'] * passenger_hybrid_petrol_2021
    registrations_data_2021_dict['Passenger'].loc['Hybrid electric-diesel'] = registrations_data_2021_dict['Passenger'].loc['Diesel oil engine'] * passenger_hybrid_diesel_2021
    registrations_data_2021_dict['LCV'].loc['Hybrid electric-petrol'] = registrations_data_2021_dict['LCV'].loc['Gasoline engine'] * lcv_hybrid_petrol_2021
    registrations_data_2021_dict['LCV'].loc['Hybrid electric-diesel'] = registrations_data_2021_dict['LCV'].loc['Diesel oil engine'] * lcv_hybrid_diesel_2021


    # Replace gasoline values in passenger cars
    registrations_data_2021_dict['Passenger'].loc['Gasoline engine'] = registrations_data_2021_dict['Passenger'].loc['Gasoline engine'] - registrations_data_2021_dict['Passenger'].loc['Hybrid electric-petrol'] 
    registrations_data_2021_dict['Passenger'].loc['Diesel oil engine'] = registrations_data_2021_dict['Passenger'].loc['Diesel oil engine'] - registrations_data_2021_dict['Passenger'].loc['Hybrid electric-diesel'] 

    # Replace gasoline values in lorries and add lpg 
    registrations_data_2021_dict['LCV'].loc['Gasoline engine'] = registrations_data_2021_dict['LCV'].loc['Gasoline engine'] + registrations_data_2021_dict['LCV'].loc['LPG engine'] - registrations_data_2021_dict['LCV'].loc['Hybrid electric-petrol'] - registrations_data_2021_dict['LCV'].loc['Hybrid electric-diesel']
    registrations_data_2021_dict['LCV'].drop(index=['LPG engine'], inplace = True)

    # Revision of diesel engine in coaches category to include gasoline and lpg
    registrations_data_2021_dict['Coaches'].loc['Diesel oil engine'] = registrations_data_2021_dict['Coaches'].loc['Diesel oil engine'] + registrations_data_2021_dict['Coaches'].loc['Gasoline engine'] + registrations_data_2021_dict['Coaches'].loc['LPG engine']
    registrations_data_2021_dict['Coaches'].drop(index=['LPG engine', 'Gasoline engine'], inplace = True)

    # Revision of heavy good vehicles to represent diesel engines
    registrations_data_2021_dict['HGV'].loc['Diesel oil engine'] = registrations_data_2021_dict['HGV'].loc['Domestic']+ registrations_data_2021_dict['HGV'].loc['International']
    registrations_data_2021_dict['HGV'].drop(index=['Domestic', 'International'], inplace = True)

    for z in vehicle_types_keys:
        registrations_data_2021_dict[z].to_csv(path_dir_export+'/Registrations_2021_'+str(z)+'.csv')

    # Calculate capacity in Gveh - km
    capacity_2022_list = []
    for z in vehicle_types_keys:
        capacity_2022 = registrations_data_2021_dict[z] * rev_vehicle_types_mileage_dict[z][2021] / pow(10,9)
        capacity_2022.index.names = ['Capacity [Gveh-km]']
        capacity_2022_df = capacity_2022.to_frame()
        capacity_2022_df.to_csv(path_dir_export+'/Capacity_2022_'+str(z)+'.csv')
        capacity_2022_list.append(capacity_2022_df)
    capacity_2022_dict = dict(zip(vehicle_types_keys, capacity_2022_list))

    ## Capital cost
    # Read Data
    capital_cost = pd.read_excel(path_dir_sup+supplemantary_data_file, sheet_name=sheet_capital_cost, skiprows=2, header=0, index_col=[3,4])
    capital_cost.drop(capital_cost.iloc[:,0:5], axis=1, inplace=True)

    capital_cost_passenger = capital_cost.iloc[0:8].reset_index(level='Type', drop=True)
    capital_cost_coaches = capital_cost.iloc[8:12].reset_index(level='Type', drop=True)
    capital_cost_lcv = capital_cost.iloc[12:19].reset_index(level='Type', drop=True)
    capital_cost_freight = capital_cost.iloc[19:24].reset_index(level='Type', drop=True)

    capital_cost_list = [capital_cost_passenger, capital_cost_coaches, capital_cost_lcv, capital_cost_freight]
    capital_cost_dict = dict(zip(vehicle_types_keys, capital_cost_list))

    for z in vehicle_types_keys:
        capital_cost_dict[z].index.names = ['Capital Cost [EUR2015/veh]']

    # Fix capital_cost_dict to match the other dataframes
    capital_cost_dict['Passenger'].rename(index = {'Gasoline vehicles' : 'Gasoline engine', 'Diesel vehicles' : 'Diesel oil engine', 
                                                   'CNG/LNG vehicles' : 'Natural gas engine', 'LPG vehicles' : 'LPG engine', 
                                                   'Hybrid electric vehicles' : 'Hybrid electric-petrol', 'Plug-in electric vehicles' : 'Plug-in hybrid electric' 
                                                   }, inplace=True)
    capital_cost_dict['Passenger'].loc['Hybrid electric-diesel'] = capital_cost_dict['Passenger'].loc['Hybrid electric-petrol']

    capital_cost_dict['LCV'].rename(index = {'Gasoline light trucks' : 'Gasoline engine', 'Diesel light trucks' : 'Diesel oil engine', 
                                                   'CNG/LNG light trucks' : 'Natural gas engine', 'Hybrid electric light trucks' : 'Hybrid electric-petrol',  
                                                   'Battery electric light trucks' : 'Battery electric vehicles'}, inplace=True)
    capital_cost_dict['LCV'].loc['Hybrid electric-diesel'] = capital_cost_dict['Passenger'].loc['Hybrid electric-petrol']

    capital_cost_dict['Coaches'].rename(index = {'Diesel bus' : 'Diesel oil engine', 'CNG bus' : 'Natural gas engine', 'LPG vehicles' : 'LPG engine', 
                                                   'Electric bus' : 'Battery electric vehicles' 
                                                   }, inplace=True)

    capital_cost_dict['HGV'].rename(index = {'Diesel heavy trucks' : 'Diesel oil engine'}, inplace=True)

    # Calculate Capital Cost in MillionEUR2018/Gvehkm
    euro_2018_2015_conv = 1.0357 # euro conversion

    capital_cost_copy_dict = copy.deepcopy(capital_cost_dict)
    new_vehicle_types_mileage_dict = copy.deepcopy(rev_vehicle_types_mileage_dict)

    new_vehicle_types_mileage_dict['Passenger'].loc['Hydrogen fuel cell vehicles'] = new_vehicle_types_mileage_dict['Passenger'].loc['Gasoline engine']
    new_vehicle_types_mileage_dict['LCV'].loc['Plug-in electric light trucks'] = new_vehicle_types_mileage_dict['LCV'].loc['Gasoline engine']
    new_vehicle_types_mileage_dict['LCV'].loc['Hydrogen fuel cell light trucks'] = new_vehicle_types_mileage_dict['LCV'].loc['Gasoline engine']
    new_vehicle_types_mileage_dict['Coaches'].loc['Hydrogen fuel cell bus'] = new_vehicle_types_mileage_dict['Coaches'].loc['Diesel oil engine']
    new_vehicle_types_mileage_dict['HGV'].loc['CNG/LNG heavy trucks'] = new_vehicle_types_mileage_dict['HGV'].loc['Diesel oil engine']
    new_vehicle_types_mileage_dict['HGV'].loc['Hybrid electric heavy trucks'] = new_vehicle_types_mileage_dict['HGV'].loc['Diesel oil engine']
    new_vehicle_types_mileage_dict['HGV'].loc['Battery electric heavy trucks'] = new_vehicle_types_mileage_dict['HGV'].loc['Diesel oil engine']
    new_vehicle_types_mileage_dict['HGV'].loc['Hydrogen fuel cell heavy trucks'] = new_vehicle_types_mileage_dict['HGV'].loc['Diesel oil engine']

    new_vehicle_types_mileage_reindexed_list = []
    for z in vehicle_types_keys:
        new_vehicle_types_mileage_reindexed = new_vehicle_types_mileage_dict[z].reindex(capital_cost_copy_dict[z].index)
        new_vehicle_types_mileage_reindexed.index.names = ['Mileage [km/vehicle]']
        new_vehicle_types_mileage_reindexed_list.append(new_vehicle_types_mileage_reindexed)
    new_vehicle_types_mileage_reindexed_dict = dict(zip(vehicle_types_keys, new_vehicle_types_mileage_reindexed_list))

    cost_per_capacity_list = []
    for z in vehicle_types_keys:
        cost_per_capacity = capital_cost_copy_dict[z].div(new_vehicle_types_mileage_reindexed_dict[z][2018], axis=0) * pow(10,3) * euro_2018_2015_conv
        cost_per_capacity.index.names = ['Cost [MEUR2018/Gveh-km]']
        cost_per_capacity.to_csv(path_dir_export+'/Cost_Capacity_'+str(z)+'.csv')
        cost_per_capacity_list.append(cost_per_capacity)
    cost_per_capacity_dict = dict(zip(vehicle_types_keys, cost_per_capacity_list))
