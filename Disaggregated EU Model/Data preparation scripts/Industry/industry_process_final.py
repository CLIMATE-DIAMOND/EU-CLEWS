# -*- coding: utf-8 -*-
"""
Created on Tue Nov  5 17:56:55 2024

@author: m.karmellos
"""


import pandas as pd
import os
from pathlib import Path
from sys import exit
from industry_sectors import industry_sectors_function
import copy

countries_file = 'Country Codes.xlsx'
countries = pd.read_excel(countries_file, header=0, index_col=0)

# Calculate lifetime_range to construct a revised dataframe for efficiency projections
lifetime_range = range(2022,2061)
lifetime_list = []    
for n in lifetime_range:
    lifetime_list.append(n)
lifetime_df = pd.DataFrame(columns=lifetime_list)  

for k in countries.index:
    if __name__ == "__main__":
        print('Data Processing for country: ', k)
        code = countries['Code'].loc[k]
        data_file_path = '' #insert data path
        path_dir_export = data_file_path + code + '/Useful Data/Industry/'
        if not os.path.exists(path_dir_export):
            os.makedirs(path_dir_export)
        for filename in os.listdir(path_dir_export):
            file_path = os.path.join(path_dir_export, filename)
            
            # Check if files exist in the directory and delete them
            if os.path.isfile(file_path):
                os.remove(file_path)
        
        fuels_fec_pj_df, fuels_ued_pj_df = industry_sectors_function(code) # Call function that creates the database with all sectors for each country
        
        if code == 'EU27':
            rev_fuels_fec_pj_df = fuels_fec_pj_df
            rev_fuels_ued_pj_df = fuels_fec_pj_df            
            energy_efficiency_df = rev_fuels_ued_pj_df / rev_fuels_fec_pj_df
            energy_intensity_df = rev_fuels_fec_pj_df / rev_fuels_ued_pj_df
        elif code == 'AT':
            ois_fec = (fuels_fec_pj_df.loc['OIS'] 
                   + fuels_fec_pj_df.loc['NFM']
                   + fuels_fec_pj_df.loc['FBT']
                   + fuels_fec_pj_df.loc['TRE']
                   + fuels_fec_pj_df.loc['MAE']
                   + fuels_fec_pj_df.loc['TEL']
                   + fuels_fec_pj_df.loc['WWP'])
            ois_fec['OIS'] = 'OIS'
            ois_fec.set_index(['OIS'], append=True, inplace=True, drop=True)
            ois_fec.index.names = ['Fuel', 'Sector']
            ois_fec = ois_fec.reorder_levels(['Sector', 'Fuel'])
            ois_ued = (fuels_ued_pj_df.loc['OIS'] 
                   + fuels_ued_pj_df.loc['NFM']
                   + fuels_ued_pj_df.loc['FBT']
                   + fuels_ued_pj_df.loc['TRE']
                   + fuels_ued_pj_df.loc['MAE']
                   + fuels_ued_pj_df.loc['TEL']
                   + fuels_ued_pj_df.loc['WWP'])
            ois_ued['OIS'] = 'OIS'
            ois_ued.set_index(['OIS'], append=True, inplace=True, drop=True)
            ois_ued.index.names = ['Fuel', 'Sector']
            ois_ued = ois_ued.reorder_levels(['Sector', 'Fuel'])          
            
            # Create revised dataframes 
            rev_fuels_fec_pj_df = pd.concat([fuels_fec_pj_df.loc[['ISI']],
                                             fuels_fec_pj_df.loc[['CHI']],
                                             fuels_fec_pj_df.loc[['NMM']],
                                             fuels_fec_pj_df.loc[['PPA']],
                                             ois_fec])
            rev_fuels_ued_pj_df = pd.concat([fuels_ued_pj_df.loc[['ISI']],
                                             fuels_ued_pj_df.loc[['CHI']],
                                             fuels_ued_pj_df.loc[['NMM']],
                                             fuels_ued_pj_df.loc[['PPA']],
                                             ois_ued])
        elif code == 'BE':
            ois_fec = (fuels_fec_pj_df.loc['OIS'] 
                   + fuels_fec_pj_df.loc['NFM']
                   + fuels_fec_pj_df.loc['PPA']
                   + fuels_fec_pj_df.loc['TRE']
                   + fuels_fec_pj_df.loc['MAE']
                   + fuels_fec_pj_df.loc['TEL']
                   + fuels_fec_pj_df.loc['WWP'])
            ois_fec['OIS'] = 'OIS'
            ois_fec.set_index(['OIS'], append=True, inplace=True, drop=True)
            ois_fec.index.names = ['Fuel', 'Sector']
            ois_fec = ois_fec.reorder_levels(['Sector', 'Fuel'])
            ois_ued = (fuels_ued_pj_df.loc['OIS'] 
                   + fuels_ued_pj_df.loc['NFM']
                   + fuels_ued_pj_df.loc['PPA']
                   + fuels_ued_pj_df.loc['TRE']
                   + fuels_ued_pj_df.loc['MAE']
                   + fuels_ued_pj_df.loc['TEL']
                   + fuels_ued_pj_df.loc['WWP'])
            ois_ued['OIS'] = 'OIS'
            ois_ued.set_index(['OIS'], append=True, inplace=True, drop=True)
            ois_ued.index.names = ['Fuel', 'Sector']
            ois_ued = ois_ued.reorder_levels(['Sector', 'Fuel'])
            
            # Create revised dataframes 
            rev_fuels_fec_pj_df = pd.concat([fuels_fec_pj_df.loc[['ISI']],
                                             fuels_fec_pj_df.loc[['CHI']],
                                             fuels_fec_pj_df.loc[['NMM']],
                                             fuels_fec_pj_df.loc[['FBT']],
                                             ois_fec])
            rev_fuels_ued_pj_df = pd.concat([fuels_ued_pj_df.loc[['ISI']],
                                             fuels_ued_pj_df.loc[['CHI']],
                                             fuels_ued_pj_df.loc[['NMM']],
                                             fuels_ued_pj_df.loc[['FBT']],
                                             ois_ued])
        elif code == 'BG':
            ois_fec = (fuels_fec_pj_df.loc['OIS'] 
                   + fuels_fec_pj_df.loc['ISI']
                   + fuels_fec_pj_df.loc['PPA']
                   + fuels_fec_pj_df.loc['TRE']
                   + fuels_fec_pj_df.loc['MAE']
                   + fuels_fec_pj_df.loc['TEL']
                   + fuels_fec_pj_df.loc['WWP'])
            ois_fec['OIS'] = 'OIS'
            ois_fec.set_index(['OIS'], append=True, inplace=True, drop=True)
            ois_fec.index.names = ['Fuel', 'Sector']
            ois_fec = ois_fec.reorder_levels(['Sector', 'Fuel'])
            ois_ued = (fuels_ued_pj_df.loc['OIS'] 
                   + fuels_ued_pj_df.loc['ISI']
                   + fuels_ued_pj_df.loc['PPA']
                   + fuels_ued_pj_df.loc['TRE']
                   + fuels_ued_pj_df.loc['MAE']
                   + fuels_ued_pj_df.loc['TEL']
                   + fuels_ued_pj_df.loc['WWP'])
            ois_ued['OIS'] = 'OIS'
            ois_ued.set_index(['OIS'], append=True, inplace=True, drop=True)
            ois_ued.index.names = ['Fuel', 'Sector']
            ois_ued = ois_ued.reorder_levels(['Sector', 'Fuel'])            
            
            # Create revised dataframes 
            rev_fuels_fec_pj_df = pd.concat([fuels_fec_pj_df.loc[['NFM']],
                                             fuels_fec_pj_df.loc[['CHI']],
                                             fuels_fec_pj_df.loc[['NMM']],
                                             fuels_fec_pj_df.loc[['FBT']],
                                             ois_fec])
            rev_fuels_ued_pj_df = pd.concat([fuels_ued_pj_df.loc[['NFM']],
                                             fuels_ued_pj_df.loc[['CHI']],
                                             fuels_ued_pj_df.loc[['NMM']],
                                             fuels_ued_pj_df.loc[['FBT']],
                                             ois_ued])
        elif code == 'CY':
            ois_fec = (fuels_fec_pj_df.loc['OIS'] 
                   + fuels_fec_pj_df.loc['ISI']
                   + fuels_fec_pj_df.loc['NFM']
                   + fuels_fec_pj_df.loc['CHI']
                   + fuels_fec_pj_df.loc['PPA']
                   + fuels_fec_pj_df.loc['TRE']
                   + fuels_fec_pj_df.loc['MAE']
                   + fuels_fec_pj_df.loc['TEL']
                   + fuels_fec_pj_df.loc['WWP'])
            ois_fec['OIS'] = 'OIS'
            ois_fec.set_index(['OIS'], append=True, inplace=True, drop=True)
            ois_fec.index.names = ['Fuel', 'Sector']
            ois_fec = ois_fec.reorder_levels(['Sector', 'Fuel'])
            ois_ued = (fuels_ued_pj_df.loc['OIS'] 
                   + fuels_ued_pj_df.loc['ISI']
                   + fuels_fec_pj_df.loc['NFM']
                   + fuels_fec_pj_df.loc['CHI']
                   + fuels_ued_pj_df.loc['PPA']
                   + fuels_ued_pj_df.loc['TRE']
                   + fuels_ued_pj_df.loc['MAE']
                   + fuels_ued_pj_df.loc['TEL']
                   + fuels_ued_pj_df.loc['WWP'])
            ois_ued['OIS'] = 'OIS'
            ois_ued.set_index(['OIS'], append=True, inplace=True, drop=True)
            ois_ued.index.names = ['Fuel', 'Sector']
            ois_ued = ois_ued.reorder_levels(['Sector', 'Fuel'])            
            
            # Create revised dataframes 
            rev_fuels_fec_pj_df = pd.concat([fuels_fec_pj_df.loc[['NMM']],
                                             fuels_fec_pj_df.loc[['FBT']],
                                             ois_fec])
            rev_fuels_ued_pj_df = pd.concat([fuels_ued_pj_df.loc[['NMM']],
                                             fuels_ued_pj_df.loc[['FBT']],
                                             ois_ued])
        elif code == 'CZ':
            ois_fec = (fuels_fec_pj_df.loc['OIS'] 
                   + fuels_fec_pj_df.loc['NFM']
                   + fuels_fec_pj_df.loc['FBT']
                   + fuels_fec_pj_df.loc['TRE']
                   + fuels_fec_pj_df.loc['MAE']
                   + fuels_fec_pj_df.loc['TEL']
                   + fuels_fec_pj_df.loc['WWP'])
            ois_fec['OIS'] = 'OIS'
            ois_fec.set_index(['OIS'], append=True, inplace=True, drop=True)
            ois_fec.index.names = ['Fuel', 'Sector']
            ois_fec = ois_fec.reorder_levels(['Sector', 'Fuel'])
            ois_ued = (fuels_ued_pj_df.loc['OIS'] 
                   + fuels_ued_pj_df.loc['NFM']
                   + fuels_ued_pj_df.loc['FBT']
                   + fuels_ued_pj_df.loc['TRE']
                   + fuels_ued_pj_df.loc['MAE']
                   + fuels_ued_pj_df.loc['TEL']
                   + fuels_ued_pj_df.loc['WWP'])
            ois_ued['OIS'] = 'OIS'
            ois_ued.set_index(['OIS'], append=True, inplace=True, drop=True)
            ois_ued.index.names = ['Fuel', 'Sector']
            ois_ued = ois_ued.reorder_levels(['Sector', 'Fuel'])            
            
            # Create revised dataframes 
            rev_fuels_fec_pj_df = pd.concat([fuels_fec_pj_df.loc[['ISI']],
                                             fuels_fec_pj_df.loc[['CHI']],
                                             fuels_fec_pj_df.loc[['NMM']],
                                             fuels_fec_pj_df.loc[['PPA']],
                                             ois_fec])
            rev_fuels_ued_pj_df = pd.concat([fuels_ued_pj_df.loc[['ISI']],
                                             fuels_ued_pj_df.loc[['CHI']],
                                             fuels_ued_pj_df.loc[['NMM']],
                                             fuels_ued_pj_df.loc[['PPA']],
                                             ois_ued])
        elif code == 'DE':
            ois_fec = (fuels_fec_pj_df.loc['OIS'] 
                   + fuels_fec_pj_df.loc['NFM']
                   + fuels_fec_pj_df.loc['FBT']
                   + fuels_fec_pj_df.loc['TRE']
                   + fuels_fec_pj_df.loc['MAE']
                   + fuels_fec_pj_df.loc['TEL']
                   + fuels_fec_pj_df.loc['WWP'])
            ois_fec['OIS'] = 'OIS'
            ois_fec.set_index(['OIS'], append=True, inplace=True, drop=True)
            ois_fec.index.names = ['Fuel', 'Sector']
            ois_fec = ois_fec.reorder_levels(['Sector', 'Fuel'])
            ois_ued = (fuels_ued_pj_df.loc['OIS'] 
                   + fuels_ued_pj_df.loc['NFM']
                   + fuels_ued_pj_df.loc['FBT']
                   + fuels_ued_pj_df.loc['TRE']
                   + fuels_ued_pj_df.loc['MAE']
                   + fuels_ued_pj_df.loc['TEL']
                   + fuels_ued_pj_df.loc['WWP'])
            ois_ued['OIS'] = 'OIS'
            ois_ued.set_index(['OIS'], append=True, inplace=True, drop=True)
            ois_ued.index.names = ['Fuel', 'Sector']
            ois_ued = ois_ued.reorder_levels(['Sector', 'Fuel'])            
            
            # Create revised dataframes 
            rev_fuels_fec_pj_df = pd.concat([fuels_fec_pj_df.loc[['ISI']],
                                             fuels_fec_pj_df.loc[['CHI']],
                                             fuels_fec_pj_df.loc[['NMM']],
                                             fuels_fec_pj_df.loc[['PPA']],
                                             ois_fec])
            rev_fuels_ued_pj_df = pd.concat([fuels_ued_pj_df.loc[['ISI']],
                                             fuels_ued_pj_df.loc[['CHI']],
                                             fuels_ued_pj_df.loc[['NMM']],
                                             fuels_ued_pj_df.loc[['PPA']],
                                             ois_ued])
        elif code == 'DK':
            ois_fec = (fuels_fec_pj_df.loc['OIS'] 
                   + fuels_fec_pj_df.loc['ISI']
                   + fuels_fec_pj_df.loc['NFM']
                   + fuels_fec_pj_df.loc['PPA']
                   + fuels_fec_pj_df.loc['TRE']
                   + fuels_fec_pj_df.loc['TEL']
                   + fuels_fec_pj_df.loc['WWP'])
            ois_fec['OIS'] = 'OIS'
            ois_fec.set_index(['OIS'], append=True, inplace=True, drop=True)
            ois_fec.index.names = ['Fuel', 'Sector']
            ois_fec = ois_fec.reorder_levels(['Sector', 'Fuel'])
            ois_ued = (fuels_ued_pj_df.loc['OIS'] 
                   + fuels_ued_pj_df.loc['ISI']
                   + fuels_ued_pj_df.loc['NFM']
                   + fuels_ued_pj_df.loc['PPA']
                   + fuels_ued_pj_df.loc['TRE']
                   + fuels_ued_pj_df.loc['TEL']
                   + fuels_ued_pj_df.loc['WWP'])
            ois_ued['OIS'] = 'OIS'
            ois_ued.set_index(['OIS'], append=True, inplace=True, drop=True)
            ois_ued.index.names = ['Fuel', 'Sector']
            ois_ued = ois_ued.reorder_levels(['Sector', 'Fuel'])            
            
            # Create revised dataframes 
            rev_fuels_fec_pj_df = pd.concat([fuels_fec_pj_df.loc[['CHI']],
                                             fuels_fec_pj_df.loc[['NMM']],
                                             fuels_fec_pj_df.loc[['FBT']],
                                             fuels_fec_pj_df.loc[['MAE']],
                                             ois_fec])
            rev_fuels_ued_pj_df = pd.concat([fuels_ued_pj_df.loc[['CHI']],
                                             fuels_ued_pj_df.loc[['NMM']],
                                             fuels_ued_pj_df.loc[['FBT']],
                                             fuels_ued_pj_df.loc[['MAE']],
                                             ois_ued])
        elif code == 'EE':
            ois_fec = (fuels_fec_pj_df.loc['OIS'] 
                   + fuels_fec_pj_df.loc['ISI']
                   + fuels_fec_pj_df.loc['NFM']
                   + fuels_fec_pj_df.loc['CHI']
                   + fuels_fec_pj_df.loc['NMM']
                   + fuels_fec_pj_df.loc['TRE']
                   + fuels_fec_pj_df.loc['TEL'])
            ois_fec['OIS'] = 'OIS'
            ois_fec.set_index(['OIS'], append=True, inplace=True, drop=True)
            ois_fec.index.names = ['Fuel', 'Sector']
            ois_fec = ois_fec.reorder_levels(['Sector', 'Fuel'])
            ois_ued = (fuels_ued_pj_df.loc['OIS'] 
                   + fuels_ued_pj_df.loc['ISI']
                   + fuels_ued_pj_df.loc['NFM']
                   + fuels_ued_pj_df.loc['CHI']
                   + fuels_ued_pj_df.loc['NMM']
                   + fuels_ued_pj_df.loc['TRE']
                   + fuels_ued_pj_df.loc['TEL'])
            ois_ued['OIS'] = 'OIS'
            ois_ued.set_index(['OIS'], append=True, inplace=True, drop=True)
            ois_ued.index.names = ['Fuel', 'Sector']
            ois_ued = ois_ued.reorder_levels(['Sector', 'Fuel'])            
            
            # Create revised dataframes 
            rev_fuels_fec_pj_df = pd.concat([fuels_fec_pj_df.loc[['PPA']],
                                             fuels_fec_pj_df.loc[['FBT']],
                                             fuels_fec_pj_df.loc[['MAE']],
                                             fuels_fec_pj_df.loc[['WWP']],
                                             ois_fec])
            rev_fuels_ued_pj_df = pd.concat([fuels_ued_pj_df.loc[['PPA']],
                                             fuels_ued_pj_df.loc[['FBT']],
                                             fuels_ued_pj_df.loc[['MAE']],
                                             fuels_ued_pj_df.loc[['WWP']],
                                             ois_ued])
        elif code == 'EL':
            ois_fec = (fuels_fec_pj_df.loc['OIS'] 
                   + fuels_fec_pj_df.loc['CHI']
                   + fuels_fec_pj_df.loc['PPA']
                   + fuels_fec_pj_df.loc['TRE']
                   + fuels_fec_pj_df.loc['MAE']
                   + fuels_fec_pj_df.loc['TEL']
                   + fuels_fec_pj_df.loc['WWP'])
            ois_fec['OIS'] = 'OIS'
            ois_fec.set_index(['OIS'], append=True, inplace=True, drop=True)
            ois_fec.index.names = ['Fuel', 'Sector']
            ois_fec = ois_fec.reorder_levels(['Sector', 'Fuel'])
            ois_ued = (fuels_ued_pj_df.loc['OIS'] 
                   + fuels_ued_pj_df.loc['CHI']
                   + fuels_ued_pj_df.loc['PPA']
                   + fuels_ued_pj_df.loc['TRE']
                   + fuels_ued_pj_df.loc['MAE']
                   + fuels_ued_pj_df.loc['TEL']
                   + fuels_ued_pj_df.loc['WWP'])
            ois_ued['OIS'] = 'OIS'
            ois_ued.set_index(['OIS'], append=True, inplace=True, drop=True)
            ois_ued.index.names = ['Fuel', 'Sector']
            ois_ued = ois_ued.reorder_levels(['Sector', 'Fuel'])            
            
            # Create revised dataframes 
            rev_fuels_fec_pj_df = pd.concat([fuels_fec_pj_df.loc[['ISI']],
                                             fuels_fec_pj_df.loc[['NFM']],
                                             fuels_fec_pj_df.loc[['NMM']],
                                             fuels_fec_pj_df.loc[['FBT']],
                                             ois_fec])
            rev_fuels_ued_pj_df = pd.concat([fuels_ued_pj_df.loc[['ISI']],
                                             fuels_ued_pj_df.loc[['NFM']],
                                             fuels_ued_pj_df.loc[['NMM']],
                                             fuels_ued_pj_df.loc[['FBT']],
                                             ois_ued])
        elif code == 'ES':
            ois_fec = (fuels_fec_pj_df.loc['OIS'] 
                   + fuels_fec_pj_df.loc['NFM']
                   + fuels_fec_pj_df.loc['PPA']
                   + fuels_fec_pj_df.loc['TRE']
                   + fuels_fec_pj_df.loc['MAE']
                   + fuels_fec_pj_df.loc['TEL']
                   + fuels_fec_pj_df.loc['WWP'])
            ois_fec['OIS'] = 'OIS'
            ois_fec.set_index(['OIS'], append=True, inplace=True, drop=True)
            ois_fec.index.names = ['Fuel', 'Sector']
            ois_fec = ois_fec.reorder_levels(['Sector', 'Fuel'])
            ois_ued = (fuels_ued_pj_df.loc['OIS'] 
                   + fuels_ued_pj_df.loc['NFM']
                   + fuels_ued_pj_df.loc['PPA']
                   + fuels_ued_pj_df.loc['TRE']
                   + fuels_ued_pj_df.loc['MAE']
                   + fuels_ued_pj_df.loc['TEL']
                   + fuels_ued_pj_df.loc['WWP'])
            ois_ued['OIS'] = 'OIS'
            ois_ued.set_index(['OIS'], append=True, inplace=True, drop=True)
            ois_ued.index.names = ['Fuel', 'Sector']
            ois_ued = ois_ued.reorder_levels(['Sector', 'Fuel'])            
            
            # Create revised dataframes 
            rev_fuels_fec_pj_df = pd.concat([fuels_fec_pj_df.loc[['ISI']],
                                             fuels_fec_pj_df.loc[['CHI']],
                                             fuels_fec_pj_df.loc[['NMM']],
                                             fuels_fec_pj_df.loc[['FBT']],
                                             ois_fec])
            rev_fuels_ued_pj_df = pd.concat([fuels_ued_pj_df.loc[['ISI']],
                                             fuels_ued_pj_df.loc[['CHI']],
                                             fuels_ued_pj_df.loc[['NMM']],
                                             fuels_ued_pj_df.loc[['FBT']],
                                             ois_ued])
        elif code == 'FI':
            ois_fec = (fuels_fec_pj_df.loc['OIS'] 
                   + fuels_fec_pj_df.loc['NFM']
                   + fuels_fec_pj_df.loc['NMM']
                   + fuels_fec_pj_df.loc['FBT']
                   + fuels_fec_pj_df.loc['TRE']
                   + fuels_fec_pj_df.loc['MAE']
                   + fuels_fec_pj_df.loc['TEL'])
            ois_fec['OIS'] = 'OIS'
            ois_fec.set_index(['OIS'], append=True, inplace=True, drop=True)
            ois_fec.index.names = ['Fuel', 'Sector']
            ois_fec = ois_fec.reorder_levels(['Sector', 'Fuel'])
            ois_ued = (fuels_ued_pj_df.loc['OIS'] 
                   + fuels_ued_pj_df.loc['NFM']
                   + fuels_ued_pj_df.loc['NMM']
                   + fuels_ued_pj_df.loc['FBT']
                   + fuels_ued_pj_df.loc['TRE']
                   + fuels_ued_pj_df.loc['MAE']
                   + fuels_ued_pj_df.loc['TEL'])
            ois_ued['OIS'] = 'OIS'
            ois_ued.set_index(['OIS'], append=True, inplace=True, drop=True)
            ois_ued.index.names = ['Fuel', 'Sector']
            ois_ued = ois_ued.reorder_levels(['Sector', 'Fuel'])    
            
            # Create revised dataframes 
            rev_fuels_fec_pj_df = pd.concat([fuels_fec_pj_df.loc[['ISI']],
                                             fuels_fec_pj_df.loc[['CHI']],
                                             fuels_fec_pj_df.loc[['PPA']],
                                             fuels_fec_pj_df.loc[['WWP']],
                                             ois_fec])
            rev_fuels_ued_pj_df = pd.concat([fuels_ued_pj_df.loc[['ISI']],
                                             fuels_ued_pj_df.loc[['CHI']],
                                             fuels_ued_pj_df.loc[['PPA']],
                                             fuels_ued_pj_df.loc[['WWP']],
                                             ois_ued])
        elif code == 'FR':
            ois_fec = (fuels_fec_pj_df.loc['OIS'] 
                   + fuels_fec_pj_df.loc['ISI']
                   + fuels_fec_pj_df.loc['NFM']
                   + fuels_fec_pj_df.loc['TRE']
                   + fuels_fec_pj_df.loc['MAE']
                   + fuels_fec_pj_df.loc['TEL']
                   + fuels_fec_pj_df.loc['WWP'])
            ois_fec['OIS'] = 'OIS'
            ois_fec.set_index(['OIS'], append=True, inplace=True, drop=True)
            ois_fec.index.names = ['Fuel', 'Sector']
            ois_fec = ois_fec.reorder_levels(['Sector', 'Fuel'])
            ois_ued = (fuels_ued_pj_df.loc['OIS'] 
                   + fuels_ued_pj_df.loc['ISI']
                   + fuels_ued_pj_df.loc['NFM']
                   + fuels_ued_pj_df.loc['TRE']
                   + fuels_ued_pj_df.loc['MAE']
                   + fuels_ued_pj_df.loc['TEL']
                   + fuels_ued_pj_df.loc['WWP'])
            ois_ued['OIS'] = 'OIS'
            ois_ued.set_index(['OIS'], append=True, inplace=True, drop=True)
            ois_ued.index.names = ['Fuel', 'Sector']
            ois_ued = ois_ued.reorder_levels(['Sector', 'Fuel'])     
            
            # Create revised dataframes 
            rev_fuels_fec_pj_df = pd.concat([fuels_fec_pj_df.loc[['CHI']],
                                             fuels_fec_pj_df.loc[['NMM']],
                                             fuels_fec_pj_df.loc[['PPA']],
                                             fuels_fec_pj_df.loc[['FBT']],
                                             ois_fec])
            rev_fuels_ued_pj_df = pd.concat([fuels_ued_pj_df.loc[['CHI']],
                                             fuels_ued_pj_df.loc[['NMM']],
                                             fuels_ued_pj_df.loc[['PPA']],
                                             fuels_ued_pj_df.loc[['FBT']],
                                             ois_ued])

        elif code == 'HR':
            ois_fec = (fuels_fec_pj_df.loc['OIS'] 
                   + fuels_fec_pj_df.loc['ISI']
                   + fuels_fec_pj_df.loc['NFM']
                   + fuels_fec_pj_df.loc['TRE']
                   + fuels_fec_pj_df.loc['MAE']
                   + fuels_fec_pj_df.loc['TEL']
                   + fuels_fec_pj_df.loc['WWP'])
            ois_fec['OIS'] = 'OIS'
            ois_fec.set_index(['OIS'], append=True, inplace=True, drop=True)
            ois_fec.index.names = ['Fuel', 'Sector']
            ois_fec = ois_fec.reorder_levels(['Sector', 'Fuel'])
            ois_ued = (fuels_ued_pj_df.loc['OIS'] 
                   + fuels_ued_pj_df.loc['ISI']
                   + fuels_ued_pj_df.loc['NFM']
                   + fuels_ued_pj_df.loc['TRE']
                   + fuels_ued_pj_df.loc['MAE']
                   + fuels_ued_pj_df.loc['TEL']
                   + fuels_ued_pj_df.loc['WWP'])
            ois_ued['OIS'] = 'OIS'
            ois_ued.set_index(['OIS'], append=True, inplace=True, drop=True)
            ois_ued.index.names = ['Fuel', 'Sector']
            ois_ued = ois_ued.reorder_levels(['Sector', 'Fuel'])  
            
            # Create revised dataframes 
            rev_fuels_fec_pj_df = pd.concat([fuels_fec_pj_df.loc[['CHI']],
                                             fuels_fec_pj_df.loc[['NMM']],
                                             fuels_fec_pj_df.loc[['PPA']],
                                             fuels_fec_pj_df.loc[['FBT']],
                                             ois_fec])
            rev_fuels_ued_pj_df = pd.concat([fuels_ued_pj_df.loc[['CHI']],
                                             fuels_ued_pj_df.loc[['NMM']],
                                             fuels_ued_pj_df.loc[['PPA']],
                                             fuels_ued_pj_df.loc[['FBT']],
                                             ois_ued])
        elif code == 'HU':
            ois_fec = (fuels_fec_pj_df.loc['OIS'] 
                   + fuels_fec_pj_df.loc['ISI']
                   + fuels_fec_pj_df.loc['NFM']
                   + fuels_fec_pj_df.loc['PPA']
                   + fuels_fec_pj_df.loc['TRE']
                   + fuels_fec_pj_df.loc['TEL']
                   + fuels_fec_pj_df.loc['WWP'])
            ois_fec['OIS'] = 'OIS'
            ois_fec.set_index(['OIS'], append=True, inplace=True, drop=True)
            ois_fec.index.names = ['Fuel', 'Sector']
            ois_fec = ois_fec.reorder_levels(['Sector', 'Fuel'])
            ois_ued = (fuels_ued_pj_df.loc['OIS'] 
                   + fuels_ued_pj_df.loc['ISI']
                   + fuels_ued_pj_df.loc['NFM']
                   + fuels_ued_pj_df.loc['PPA']
                   + fuels_ued_pj_df.loc['TRE']
                   + fuels_ued_pj_df.loc['TEL']
                   + fuels_ued_pj_df.loc['WWP'])
            ois_ued['OIS'] = 'OIS'
            ois_ued.set_index(['OIS'], append=True, inplace=True, drop=True)
            ois_ued.index.names = ['Fuel', 'Sector']
            ois_ued = ois_ued.reorder_levels(['Sector', 'Fuel'])        
            
            # Create revised dataframes 
            rev_fuels_fec_pj_df = pd.concat([fuels_fec_pj_df.loc[['CHI']],
                                             fuels_fec_pj_df.loc[['NMM']],
                                             fuels_fec_pj_df.loc[['FBT']],
                                             fuels_fec_pj_df.loc[['MAE']],
                                             ois_fec])
            rev_fuels_ued_pj_df = pd.concat([fuels_ued_pj_df.loc[['CHI']],
                                             fuels_ued_pj_df.loc[['NMM']],
                                             fuels_ued_pj_df.loc[['FBT']],
                                             fuels_ued_pj_df.loc[['MAE']],
                                             ois_ued])
        elif code == 'IE':
            ois_fec = (fuels_fec_pj_df.loc['OIS'] 
                   + fuels_fec_pj_df.loc['ISI']
                   + fuels_fec_pj_df.loc['PPA']
                   + fuels_fec_pj_df.loc['TRE']
                   + fuels_fec_pj_df.loc['MAE']
                   + fuels_fec_pj_df.loc['TEL']
                   + fuels_fec_pj_df.loc['WWP'])
            ois_fec['OIS'] = 'OIS'
            ois_fec.set_index(['OIS'], append=True, inplace=True, drop=True)
            ois_fec.index.names = ['Fuel', 'Sector']
            ois_fec = ois_fec.reorder_levels(['Sector', 'Fuel'])
            ois_ued = (fuels_ued_pj_df.loc['OIS'] 
                   + fuels_ued_pj_df.loc['ISI']
                   + fuels_ued_pj_df.loc['PPA']
                   + fuels_ued_pj_df.loc['TRE']
                   + fuels_ued_pj_df.loc['MAE']
                   + fuels_ued_pj_df.loc['TEL']
                   + fuels_ued_pj_df.loc['WWP'])
            ois_ued['OIS'] = 'OIS'
            ois_ued.set_index(['OIS'], append=True, inplace=True, drop=True)
            ois_ued.index.names = ['Fuel', 'Sector']
            ois_ued = ois_ued.reorder_levels(['Sector', 'Fuel'])   
            
            # Create revised dataframes 
            rev_fuels_fec_pj_df = pd.concat([fuels_fec_pj_df.loc[['NFM']],
                                             fuels_fec_pj_df.loc[['CHI']],
                                             fuels_fec_pj_df.loc[['NMM']],
                                             fuels_fec_pj_df.loc[['FBT']],
                                             ois_fec])
            rev_fuels_ued_pj_df = pd.concat([fuels_ued_pj_df.loc[['NFM']],
                                             fuels_ued_pj_df.loc[['CHI']],
                                             fuels_ued_pj_df.loc[['NMM']],
                                             fuels_ued_pj_df.loc[['FBT']],
                                             ois_ued])
        elif code == 'IT':
            ois_fec = (fuels_fec_pj_df.loc['OIS'] 
                   + fuels_fec_pj_df.loc['NFM']
                   + fuels_fec_pj_df.loc['PPA']
                   + fuels_fec_pj_df.loc['FBT']
                   + fuels_fec_pj_df.loc['TRE']
                   + fuels_fec_pj_df.loc['TEL']
                   + fuels_fec_pj_df.loc['WWP'])
            ois_fec['OIS'] = 'OIS'
            ois_fec.set_index(['OIS'], append=True, inplace=True, drop=True)
            ois_fec.index.names = ['Fuel', 'Sector']
            ois_fec = ois_fec.reorder_levels(['Sector', 'Fuel'])
            ois_ued = (fuels_ued_pj_df.loc['OIS'] 
                   + fuels_ued_pj_df.loc['NFM']
                   + fuels_ued_pj_df.loc['PPA']
                   + fuels_ued_pj_df.loc['FBT']
                   + fuels_ued_pj_df.loc['TRE']
                   + fuels_ued_pj_df.loc['TEL']
                   + fuels_ued_pj_df.loc['WWP'])
            ois_ued['OIS'] = 'OIS'
            ois_ued.set_index(['OIS'], append=True, inplace=True, drop=True)
            ois_ued.index.names = ['Fuel', 'Sector']
            ois_ued = ois_ued.reorder_levels(['Sector', 'Fuel'])     
            
            # Create revised dataframes 
            rev_fuels_fec_pj_df = pd.concat([fuels_fec_pj_df.loc[['ISI']],
                                             fuels_fec_pj_df.loc[['CHI']],
                                             fuels_fec_pj_df.loc[['NMM']],
                                             fuels_fec_pj_df.loc[['MAE']],
                                             ois_fec])
            rev_fuels_ued_pj_df = pd.concat([fuels_ued_pj_df.loc[['ISI']],
                                             fuels_ued_pj_df.loc[['CHI']],
                                             fuels_ued_pj_df.loc[['NMM']],
                                             fuels_ued_pj_df.loc[['MAE']],
                                             ois_ued])
        elif code == 'LT':
            ois_fec = (fuels_fec_pj_df.loc['OIS'] 
                   + fuels_fec_pj_df.loc['ISI']
                   + fuels_fec_pj_df.loc['NFM']
                   + fuels_fec_pj_df.loc['PPA']
                   + fuels_fec_pj_df.loc['TRE']
                   + fuels_fec_pj_df.loc['MAE']
                   + fuels_fec_pj_df.loc['TEL'])
            ois_fec['OIS'] = 'OIS'
            ois_fec.set_index(['OIS'], append=True, inplace=True, drop=True)
            ois_fec.index.names = ['Fuel', 'Sector']
            ois_fec = ois_fec.reorder_levels(['Sector', 'Fuel'])
            ois_ued = (fuels_ued_pj_df.loc['OIS'] 
                   + fuels_ued_pj_df.loc['ISI']
                   + fuels_ued_pj_df.loc['NFM']
                   + fuels_ued_pj_df.loc['PPA']
                   + fuels_ued_pj_df.loc['TRE']
                   + fuels_ued_pj_df.loc['MAE']
                   + fuels_ued_pj_df.loc['TEL'])
            ois_ued['OIS'] = 'OIS'
            ois_ued.set_index(['OIS'], append=True, inplace=True, drop=True)
            ois_ued.index.names = ['Fuel', 'Sector']
            ois_ued = ois_ued.reorder_levels(['Sector', 'Fuel'])        
            
            # Create revised dataframes 
            rev_fuels_fec_pj_df = pd.concat([fuels_fec_pj_df.loc[['CHI']],
                                             fuels_fec_pj_df.loc[['NMM']],
                                             fuels_fec_pj_df.loc[['FBT']],
                                             fuels_fec_pj_df.loc[['WWP']],
                                             ois_fec])
            rev_fuels_ued_pj_df = pd.concat([fuels_ued_pj_df.loc[['CHI']],
                                             fuels_ued_pj_df.loc[['NMM']],
                                             fuels_ued_pj_df.loc[['FBT']],
                                             fuels_ued_pj_df.loc[['WWP']],
                                             ois_ued])
        elif code == 'LU':
            ois_fec = (fuels_fec_pj_df.loc['OIS'] 
                   + fuels_fec_pj_df.loc['NFM']
                   + fuels_fec_pj_df.loc['CHI']
                   + fuels_fec_pj_df.loc['PPA']
                   + fuels_fec_pj_df.loc['FBT']
                   + fuels_fec_pj_df.loc['TRE']
                   + fuels_fec_pj_df.loc['MAE']
                   + fuels_fec_pj_df.loc['TEL']
                   + fuels_fec_pj_df.loc['WWP'])
            ois_fec['OIS'] = 'OIS'
            ois_fec.set_index(['OIS'], append=True, inplace=True, drop=True)
            ois_fec.index.names = ['Fuel', 'Sector']
            ois_fec = ois_fec.reorder_levels(['Sector', 'Fuel'])
            ois_ued = (fuels_ued_pj_df.loc['OIS'] 
                   + fuels_ued_pj_df.loc['NFM']
                   + fuels_ued_pj_df.loc['CHI']
                   + fuels_ued_pj_df.loc['PPA']
                   + fuels_ued_pj_df.loc['FBT']
                   + fuels_ued_pj_df.loc['TRE']
                   + fuels_ued_pj_df.loc['MAE']
                   + fuels_ued_pj_df.loc['TEL']
                   + fuels_ued_pj_df.loc['WWP'])
            ois_ued['OIS'] = 'OIS'
            ois_ued.set_index(['OIS'], append=True, inplace=True, drop=True)
            ois_ued.index.names = ['Fuel', 'Sector']
            ois_ued = ois_ued.reorder_levels(['Sector', 'Fuel'])            
            
            # Create revised dataframes 
            rev_fuels_fec_pj_df = pd.concat([fuels_fec_pj_df.loc[['ISI']],
                                             fuels_fec_pj_df.loc[['NMM']],
                                             ois_fec])
            rev_fuels_ued_pj_df = pd.concat([fuels_ued_pj_df.loc[['ISI']],
                                             fuels_ued_pj_df.loc[['NMM']],
                                             ois_ued])
        elif code == 'LV':
            ois_fec = (fuels_fec_pj_df.loc['OIS'] 
                   + fuels_fec_pj_df.loc['ISI']
                   + fuels_fec_pj_df.loc['NFM']
                   + fuels_fec_pj_df.loc['CHI']
                   + fuels_fec_pj_df.loc['PPA']
                   + fuels_fec_pj_df.loc['TRE']
                   + fuels_fec_pj_df.loc['MAE']
                   + fuels_fec_pj_df.loc['TEL'])
            ois_fec['OIS'] = 'OIS'
            ois_fec.set_index(['OIS'], append=True, inplace=True, drop=True)
            ois_fec.index.names = ['Fuel', 'Sector']
            ois_fec = ois_fec.reorder_levels(['Sector', 'Fuel'])
            ois_ued = (fuels_ued_pj_df.loc['OIS'] 
                   + fuels_ued_pj_df.loc['ISI']
                   + fuels_ued_pj_df.loc['NFM']
                   + fuels_ued_pj_df.loc['CHI']
                   + fuels_ued_pj_df.loc['PPA']
                   + fuels_ued_pj_df.loc['TRE']
                   + fuels_ued_pj_df.loc['MAE']
                   + fuels_ued_pj_df.loc['TEL'])
            ois_ued['OIS'] = 'OIS'
            ois_ued.set_index(['OIS'], append=True, inplace=True, drop=True)
            ois_ued.index.names = ['Fuel', 'Sector']
            ois_ued = ois_ued.reorder_levels(['Sector', 'Fuel'])            
            # Create revised dataframes 
            rev_fuels_fec_pj_df = pd.concat([fuels_fec_pj_df.loc[['NMM']],
                                             fuels_fec_pj_df.loc[['FBT']],
                                             fuels_fec_pj_df.loc[['WWP']],
                                             ois_fec])
            rev_fuels_ued_pj_df = pd.concat([fuels_ued_pj_df.loc[['NMM']],
                                             fuels_ued_pj_df.loc[['FBT']],
                                             fuels_ued_pj_df.loc[['WWP']],
                                             ois_ued])
        elif code == 'MT':
            ois_fec = fuels_fec_pj_df.groupby(level=1, sort=False).sum()
            ois_fec['OIS'] = 'OIS'
            ois_fec.set_index(['OIS'], append=True, inplace=True, drop=True)
            ois_fec.index.names = ['Fuel', 'Sector']
            ois_fec = ois_fec.reorder_levels(['Sector', 'Fuel'])
            ois_ued = fuels_ued_pj_df.groupby(level=1, sort=False).sum()
            ois_ued['OIS'] = 'OIS'
            ois_ued.set_index(['OIS'], append=True, inplace=True, drop=True)
            ois_ued.index.names = ['Fuel', 'Sector']
            ois_ued = ois_ued.reorder_levels(['Sector', 'Fuel'])            
            # Create revised dataframes 
            rev_fuels_fec_pj_df = ois_fec
            rev_fuels_ued_pj_df = ois_ued
        elif code == 'NL':
            ois_fec = (fuels_fec_pj_df.loc['OIS'] 
                   + fuels_fec_pj_df.loc['NFM']
                   + fuels_fec_pj_df.loc['PPA']
                   + fuels_fec_pj_df.loc['TRE']
                   + fuels_fec_pj_df.loc['MAE']
                   + fuels_fec_pj_df.loc['TEL']
                   + fuels_fec_pj_df.loc['WWP'])
            ois_fec['OIS'] = 'OIS'
            ois_fec.set_index(['OIS'], append=True, inplace=True, drop=True)
            ois_fec.index.names = ['Fuel', 'Sector']
            ois_fec = ois_fec.reorder_levels(['Sector', 'Fuel'])
            ois_ued = (fuels_ued_pj_df.loc['OIS'] 
                   + fuels_ued_pj_df.loc['NFM']
                   + fuels_ued_pj_df.loc['PPA']
                   + fuels_ued_pj_df.loc['TRE']
                   + fuels_ued_pj_df.loc['MAE']
                   + fuels_ued_pj_df.loc['TEL']
                   + fuels_ued_pj_df.loc['WWP'])
            ois_ued['OIS'] = 'OIS'
            ois_ued.set_index(['OIS'], append=True, inplace=True, drop=True)
            ois_ued.index.names = ['Fuel', 'Sector']
            ois_ued = ois_ued.reorder_levels(['Sector', 'Fuel'])            
            # Create revised dataframes 
            rev_fuels_fec_pj_df = pd.concat([fuels_fec_pj_df.loc[['ISI']],
                                             fuels_fec_pj_df.loc[['CHI']],
                                             fuels_fec_pj_df.loc[['NMM']],
                                             fuels_fec_pj_df.loc[['FBT']],
                                             ois_fec])
            rev_fuels_ued_pj_df = pd.concat([fuels_ued_pj_df.loc[['ISI']],
                                             fuels_ued_pj_df.loc[['CHI']],
                                             fuels_ued_pj_df.loc[['NMM']],
                                             fuels_ued_pj_df.loc[['FBT']],
                                             ois_ued])

        elif code == 'PL':
            ois_fec = (fuels_fec_pj_df.loc['OIS'] 
                   + fuels_fec_pj_df.loc['NFM']
                   + fuels_fec_pj_df.loc['PPA']
                   + fuels_fec_pj_df.loc['TRE']
                   + fuels_fec_pj_df.loc['MAE']
                   + fuels_fec_pj_df.loc['TEL']
                   + fuels_fec_pj_df.loc['WWP'])
            ois_fec['OIS'] = 'OIS'
            ois_fec.set_index(['OIS'], append=True, inplace=True, drop=True)
            ois_fec.index.names = ['Fuel', 'Sector']
            ois_fec = ois_fec.reorder_levels(['Sector', 'Fuel'])
            ois_ued = (fuels_ued_pj_df.loc['OIS'] 
                   + fuels_ued_pj_df.loc['NFM']
                   + fuels_ued_pj_df.loc['PPA']
                   + fuels_ued_pj_df.loc['TRE']
                   + fuels_ued_pj_df.loc['MAE']
                   + fuels_ued_pj_df.loc['TEL']
                   + fuels_ued_pj_df.loc['WWP'])
            ois_ued['OIS'] = 'OIS'
            ois_ued.set_index(['OIS'], append=True, inplace=True, drop=True)
            ois_ued.index.names = ['Fuel', 'Sector']
            ois_ued = ois_ued.reorder_levels(['Sector', 'Fuel'])            
            # Create revised dataframes 
            rev_fuels_fec_pj_df = pd.concat([fuels_fec_pj_df.loc[['ISI']],
                                             fuels_fec_pj_df.loc[['CHI']],
                                             fuels_fec_pj_df.loc[['NMM']],
                                             fuels_fec_pj_df.loc[['FBT']],
                                             ois_fec])
            rev_fuels_ued_pj_df = pd.concat([fuels_ued_pj_df.loc[['ISI']],
                                             fuels_ued_pj_df.loc[['CHI']],
                                             fuels_ued_pj_df.loc[['NMM']],
                                             fuels_ued_pj_df.loc[['FBT']],
                                             ois_ued])

        elif code == 'PT':
            ois_fec = (fuels_fec_pj_df.loc['OIS'] 
                   + fuels_fec_pj_df.loc['ISI']
                   + fuels_fec_pj_df.loc['NFM']
                   + fuels_fec_pj_df.loc['TRE']
                   + fuels_fec_pj_df.loc['MAE']
                   + fuels_fec_pj_df.loc['TEL']
                   + fuels_fec_pj_df.loc['WWP'])
            ois_fec['OIS'] = 'OIS'
            ois_fec.set_index(['OIS'], append=True, inplace=True, drop=True)
            ois_fec.index.names = ['Fuel', 'Sector']
            ois_fec = ois_fec.reorder_levels(['Sector', 'Fuel'])
            ois_ued = (fuels_ued_pj_df.loc['OIS'] 
                   + fuels_ued_pj_df.loc['ISI']
                   + fuels_ued_pj_df.loc['NFM']
                   + fuels_ued_pj_df.loc['TRE']
                   + fuels_ued_pj_df.loc['MAE']
                   + fuels_ued_pj_df.loc['TEL']
                   + fuels_ued_pj_df.loc['WWP'])
            ois_ued['OIS'] = 'OIS'
            ois_ued.set_index(['OIS'], append=True, inplace=True, drop=True)
            ois_ued.index.names = ['Fuel', 'Sector']
            ois_ued = ois_ued.reorder_levels(['Sector', 'Fuel'])            
            # Create revised dataframes 
            rev_fuels_fec_pj_df = pd.concat([fuels_fec_pj_df.loc[['CHI']],
                                             fuels_fec_pj_df.loc[['NMM']],
                                             fuels_fec_pj_df.loc[['PPA']],
                                             fuels_fec_pj_df.loc[['FBT']],
                                             ois_fec])
            rev_fuels_ued_pj_df = pd.concat([fuels_ued_pj_df.loc[['CHI']],
                                             fuels_ued_pj_df.loc[['NMM']],
                                             fuels_ued_pj_df.loc[['PPA']],
                                             fuels_ued_pj_df.loc[['FBT']],
                                             ois_ued])
        elif code == 'RO':
            ois_fec = (fuels_fec_pj_df.loc['OIS'] 
                   + fuels_fec_pj_df.loc['PPA']
                   + fuels_fec_pj_df.loc['FBT']
                   + fuels_fec_pj_df.loc['TRE']
                   + fuels_fec_pj_df.loc['MAE']
                   + fuels_fec_pj_df.loc['TEL']
                   + fuels_fec_pj_df.loc['WWP'])
            ois_fec['OIS'] = 'OIS'
            ois_fec.set_index(['OIS'], append=True, inplace=True, drop=True)
            ois_fec.index.names = ['Fuel', 'Sector']
            ois_fec = ois_fec.reorder_levels(['Sector', 'Fuel'])
            ois_ued = (fuels_ued_pj_df.loc['OIS'] 
                   + fuels_ued_pj_df.loc['PPA']
                   + fuels_ued_pj_df.loc['FBT']
                   + fuels_ued_pj_df.loc['TRE']
                   + fuels_ued_pj_df.loc['MAE']
                   + fuels_ued_pj_df.loc['TEL']
                   + fuels_ued_pj_df.loc['WWP'])
            ois_ued['OIS'] = 'OIS'
            ois_ued.set_index(['OIS'], append=True, inplace=True, drop=True)
            ois_ued.index.names = ['Fuel', 'Sector']
            ois_ued = ois_ued.reorder_levels(['Sector', 'Fuel'])            
            # Create revised dataframes 
            rev_fuels_fec_pj_df = pd.concat([fuels_fec_pj_df.loc[['ISI']],
                                             fuels_fec_pj_df.loc[['NFM']],
                                             fuels_fec_pj_df.loc[['CHI']],
                                             fuels_fec_pj_df.loc[['NMM']],
                                             ois_fec])
            rev_fuels_ued_pj_df = pd.concat([fuels_ued_pj_df.loc[['ISI']],
                                             fuels_ued_pj_df.loc[['NFM']],
                                             fuels_ued_pj_df.loc[['CHI']],
                                             fuels_ued_pj_df.loc[['NMM']],
                                             ois_ued])
        elif code == 'SE':
            ois_fec = (fuels_fec_pj_df.loc['OIS'] 
                   + fuels_fec_pj_df.loc['NFM']
                   + fuels_fec_pj_df.loc['NMM']
                   + fuels_fec_pj_df.loc['TRE']
                   + fuels_fec_pj_df.loc['MAE']
                   + fuels_fec_pj_df.loc['TEL']
                   + fuels_fec_pj_df.loc['WWP'])
            ois_fec['OIS'] = 'OIS'
            ois_fec.set_index(['OIS'], append=True, inplace=True, drop=True)
            ois_fec.index.names = ['Fuel', 'Sector']
            ois_fec = ois_fec.reorder_levels(['Sector', 'Fuel'])
            ois_ued = (fuels_ued_pj_df.loc['OIS'] 
                   + fuels_ued_pj_df.loc['NFM']
                   + fuels_ued_pj_df.loc['NMM']
                   + fuels_ued_pj_df.loc['TRE']
                   + fuels_ued_pj_df.loc['MAE']
                   + fuels_ued_pj_df.loc['TEL']
                   + fuels_ued_pj_df.loc['WWP'])
            ois_ued['OIS'] = 'OIS'
            ois_ued.set_index(['OIS'], append=True, inplace=True, drop=True)
            ois_ued.index.names = ['Fuel', 'Sector']
            ois_ued = ois_ued.reorder_levels(['Sector', 'Fuel'])            
            # Create revised dataframes 
            rev_fuels_fec_pj_df = pd.concat([fuels_fec_pj_df.loc[['ISI']],
                                             fuels_fec_pj_df.loc[['CHI']],
                                             fuels_fec_pj_df.loc[['PPA']],
                                             fuels_fec_pj_df.loc[['FBT']],
                                             ois_fec])
            rev_fuels_ued_pj_df = pd.concat([fuels_ued_pj_df.loc[['ISI']],
                                             fuels_ued_pj_df.loc[['CHI']],
                                             fuels_ued_pj_df.loc[['PPA']],
                                             fuels_ued_pj_df.loc[['FBT']],
                                             ois_ued])
        elif code == 'SI':
            ois_fec = (fuels_fec_pj_df.loc['OIS'] 
                   + fuels_fec_pj_df.loc['NFM']
                   + fuels_fec_pj_df.loc['PPA']
                   + fuels_fec_pj_df.loc['FBT']
                   + fuels_fec_pj_df.loc['TRE']
                   + fuels_fec_pj_df.loc['TEL']
                   + fuels_fec_pj_df.loc['WWP'])
            ois_fec['OIS'] = 'OIS'
            ois_fec.set_index(['OIS'], append=True, inplace=True, drop=True)
            ois_fec.index.names = ['Fuel', 'Sector']
            ois_fec = ois_fec.reorder_levels(['Sector', 'Fuel'])
            ois_ued = (fuels_ued_pj_df.loc['OIS'] 
                   + fuels_ued_pj_df.loc['NFM']
                   + fuels_ued_pj_df.loc['PPA']
                   + fuels_ued_pj_df.loc['FBT']
                   + fuels_ued_pj_df.loc['TRE']
                   + fuels_ued_pj_df.loc['TEL']
                   + fuels_ued_pj_df.loc['WWP'])
            ois_ued['OIS'] = 'OIS'
            ois_ued.set_index(['OIS'], append=True, inplace=True, drop=True)
            ois_ued.index.names = ['Fuel', 'Sector']
            ois_ued = ois_ued.reorder_levels(['Sector', 'Fuel'])            
            # Create revised dataframes 
            rev_fuels_fec_pj_df = pd.concat([fuels_fec_pj_df.loc[['ISI']],
                                             fuels_fec_pj_df.loc[['CHI']],
                                             fuels_fec_pj_df.loc[['NMM']],
                                             fuels_fec_pj_df.loc[['MAE']],
                                             ois_fec])
            rev_fuels_ued_pj_df = pd.concat([fuels_ued_pj_df.loc[['ISI']],
                                             fuels_ued_pj_df.loc[['CHI']],
                                             fuels_ued_pj_df.loc[['NMM']],
                                             fuels_ued_pj_df.loc[['MAE']],
                                             ois_ued])
        elif code == 'SK':
            ois_fec = (fuels_fec_pj_df.loc['OIS'] 
                   + fuels_fec_pj_df.loc['NFM']
                   + fuels_fec_pj_df.loc['FBT']
                   + fuels_fec_pj_df.loc['TRE']
                   + fuels_fec_pj_df.loc['MAE']
                   + fuels_fec_pj_df.loc['TEL']
                   + fuels_fec_pj_df.loc['WWP'])
            ois_fec['OIS'] = 'OIS'
            ois_fec.set_index(['OIS'], append=True, inplace=True, drop=True)
            ois_fec.index.names = ['Fuel', 'Sector']
            ois_fec = ois_fec.reorder_levels(['Sector', 'Fuel'])
            ois_ued = (fuels_ued_pj_df.loc['OIS'] 
                   + fuels_ued_pj_df.loc['NFM']
                   + fuels_ued_pj_df.loc['FBT']
                   + fuels_ued_pj_df.loc['TRE']
                   + fuels_ued_pj_df.loc['MAE']
                   + fuels_ued_pj_df.loc['TEL']
                   + fuels_ued_pj_df.loc['WWP'])
            ois_ued['OIS'] = 'OIS'
            ois_ued.set_index(['OIS'], append=True, inplace=True, drop=True)
            ois_ued.index.names = ['Fuel', 'Sector']
            ois_ued = ois_ued.reorder_levels(['Sector', 'Fuel'])            
            # Create revised dataframes 
            rev_fuels_fec_pj_df = pd.concat([fuels_fec_pj_df.loc[['ISI']],
                                             fuels_fec_pj_df.loc[['CHI']],
                                             fuels_fec_pj_df.loc[['NMM']],
                                             fuels_fec_pj_df.loc[['PPA']],
                                             ois_fec])
            rev_fuels_ued_pj_df = pd.concat([fuels_ued_pj_df.loc[['ISI']],
                                             fuels_ued_pj_df.loc[['CHI']],
                                             fuels_ued_pj_df.loc[['NMM']],
                                             fuels_ued_pj_df.loc[['PPA']],
                                             ois_ued])
        else:
            print('Error: wrong country codes. Country: ', k)
     
    rev_fuels_fec_pj_df = rev_fuels_fec_pj_df.astype(float).round(4)
    rev_fuels_fec_pj_df.sort_index(level=0, inplace=True)
    rev_fuels_fec_pj_df.to_csv(path_dir_export + '/Final_Energy.csv')
    
    rev_fuels_ued_pj_df = rev_fuels_ued_pj_df.astype(float).round(4)
    rev_fuels_ued_pj_df.sort_index(level=0, inplace=True)
    rev_fuels_ued_pj_df.to_csv(path_dir_export + '/Useful_Energy.csv')   
     
    energy_efficiency_df = rev_fuels_ued_pj_df / rev_fuels_fec_pj_df
    energy_efficiency_df = energy_efficiency_df.astype(float).round(4)
    energy_efficiency_df.index.names = ['Energy Efficiency', 'Fuel']
    energy_efficiency_df.sort_index(level=0, inplace=True)
    energy_efficiency_df.to_csv(path_dir_export + '/Energy_Efficiency.csv')
            
    energy_intensity_df = rev_fuels_fec_pj_df / rev_fuels_ued_pj_df
    energy_intensity_df = energy_intensity_df.astype(float).round(4)
    energy_intensity_df.index.names = ['Energy Efficiency', 'Fuel']
    energy_intensity_df.sort_index(level=0, inplace=True)
    energy_intensity_df.to_csv(path_dir_export + '/Energy_Intensity.csv')
        
    # Intensity projections
    path_dir_sup = '' # Insert respective path
    supplemantary_data_file = 'Supplementary data for industry projections.xlsx'
    sheet_efficiency = 'Efficiency'
    
    intensity_projection_industry = pd.read_excel(path_dir_sup + supplemantary_data_file, sheet_name=sheet_efficiency, skiprows=445, header=0, index_col=3)
    intensity_projection_industry.drop(intensity_projection_industry.iloc[:,0:18], axis=1, inplace=True)
    intensity_projection_industry.drop(intensity_projection_industry.iloc[:,40:], axis=1, inplace=True)
    intensity_projection_industry.loc['Hydrogen boiler/combustion'] = intensity_projection_industry.loc['Gas boiler/combustion']
    intensity_projection_industry.index.names = ['Fuel']
    
    #Fix intensity_projection_industry to match the other dataframes
    intensity_projection_industry.rename(
        index={'Oil boiler/combustion' : 'Oil', 'Coal boiler/combustion' : 'Coal',
               'Coal boiler/combustion with CCS' : 'Coal (CCS)',
               'Gas boiler/combustion' : 'Natural gas',
               'Gas boiler/combustion with CCS' : 'Natural gas (CCS)',
               'Biomass/biofuels/biogas boiler/combustion' : 'Biomass/Biofuels',
               'Hydrogen boiler/combustion' : 'Hydrogen', 'Solar thermal' : 'Solar'},
        inplace=True)

    # Create a revised dataframe of energy intensity
    energy_intensity_df_copy = copy.deepcopy(energy_intensity_df)
    
    energy_intensity_df_rev = pd.concat([energy_intensity_df_copy, lifetime_df], axis=1)
    energy_intensity_df_rev_index = energy_intensity_df_rev.index.get_level_values(0)
    for i in energy_intensity_df_rev_index:
        energy_intensity_df_rev.loc[(i, 'Hydrogen'),:] = energy_intensity_df_rev.loc[(i, 'Natural gas'),:]
        energy_intensity_df_rev.loc[(i, 'Coal (CCS)'),:] = energy_intensity_df_rev.loc[(i, 'Coal'),:]
        energy_intensity_df_rev.loc[(i, 'Natural gas (CCS)'),:] = energy_intensity_df_rev.loc[(i, 'Natural gas'),:]
    energy_intensity_df_rev.sort_index(level=0, inplace=True)
    energy_intensity_df_rev.index.names = ['Energy intensity', 'Fuel']

    for z in lifetime_range:
        energy_intensity_df_rev.loc[:, z] = energy_intensity_df_rev.loc[:, 2021] * intensity_projection_industry.loc[:,z]

    energy_intensity_df_rev = energy_intensity_df_rev.astype(float).round(4)        
    energy_intensity_df_rev.to_csv(path_dir_export+'/Energy_Intensity_Projections.csv')
