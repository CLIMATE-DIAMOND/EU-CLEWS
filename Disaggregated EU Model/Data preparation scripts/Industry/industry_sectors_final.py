# -*- coding: utf-8 -*-
"""
Created on Fri Nov  1 16:16:04 2024

@author: m.karmellos
"""
def industry_sectors_function(code):
    import pandas as pd
    from pathlib import Path
    import copy
    from sys import exit
    import os
    
    ## Path 
    ## Data files and import path
    country_abb = code
    data_file_path = '' # Insert data file path
    data_file = data_file_path + country_abb + '/JRC-IDEES-2021_Industry_'+ country_abb +'.xlsx'
    sheet_isi_fec = 'ISI_fec'
    sheet_isi_ued = 'ISI_ued'
    sheet_nfm_fec = 'NFM_fec'
    sheet_nfm_ued = 'NFM_ued'
    sheet_chi_fec = 'CHI_fec'
    sheet_chi_ued = 'CHI_ued'
    sheet_nmm_fec = 'NMM_fec'
    sheet_nmm_ued = 'NMM_ued'
    sheet_ppa_fec = 'PPA_fec'
    sheet_ppa_ued = 'PPA_ued'
    sheet_fbt_fec = 'FBT_fec'
    sheet_fbt_ued = 'FBT_ued'
    sheet_tre_fec = 'TRE_fec'
    sheet_tre_ued = 'TRE_ued'
    sheet_mae_fec = 'MAE_fec'
    sheet_mae_ued = 'MAE_ued'
    sheet_tel_fec = 'TEL_fec'
    sheet_tel_ued = 'TEL_ued'
    sheet_wwp_fec = 'WWP_fec'
    sheet_wwp_ued = 'WWP_ued'
    sheet_ois_fec = 'OIS_fec'
    sheet_ois_ued = 'OIS_ued'
    
    ## Calculations for ISI
    isi_data_fec = pd.read_excel(data_file, sheet_name = sheet_isi_fec, header=0, index_col=0, usecols=[0,19,20,21,22])
    df_index = pd.DataFrame(range(len(isi_data_fec)), columns = ['Counter'])
    isi_data_fec.set_index(df_index['Counter'], append=True, inplace=True)
    
    isi_data_ued = pd.read_excel(data_file, sheet_name = sheet_isi_ued, header=0, index_col=0, usecols=[0,19,20,21,22])
    df_index = pd.DataFrame(range(len(isi_data_ued)), columns = ['Counter'])
    isi_data_ued.set_index(df_index['Counter'], append=True, inplace=True)
    
    ## Calculations for NFM
    nfm_data_fec = pd.read_excel(data_file, sheet_name = sheet_nfm_fec, header=0, index_col=0, usecols=[0,19,20,21,22])
    df_index = pd.DataFrame(range(len(nfm_data_fec)), columns = ['Counter'])
    nfm_data_fec.set_index(df_index['Counter'], append=True, inplace=True)
    
    nfm_data_ued = pd.read_excel(data_file, sheet_name = sheet_nfm_ued, header=0, index_col=0, usecols=[0,19,20,21,22])
    df_index = pd.DataFrame(range(len(nfm_data_ued)), columns = ['Counter'])
    nfm_data_ued.set_index(df_index['Counter'], append=True, inplace=True)
    
    ## Calculations for CHI
    chi_data_fec = pd.read_excel(data_file, sheet_name = sheet_chi_fec, header=0, index_col=0, usecols=[0,19,20,21,22])
    df_index = pd.DataFrame(range(len(chi_data_fec)), columns = ['Counter'])
    chi_data_fec.set_index(df_index['Counter'], append=True, inplace=True)
    
    chi_data_ued = pd.read_excel(data_file, sheet_name = sheet_chi_ued, header=0, index_col=0, usecols=[0,19,20,21,22])
    df_index = pd.DataFrame(range(len(chi_data_ued)), columns = ['Counter'])
    chi_data_ued.set_index(df_index['Counter'], append=True, inplace=True)
    
    ## Calculations for NMM
    nmm_data_fec = pd.read_excel(data_file, sheet_name = sheet_nmm_fec, header=0, index_col=0, usecols=[0,19,20,21,22])
    df_index = pd.DataFrame(range(len(nmm_data_fec)), columns = ['Counter'])
    nmm_data_fec.set_index(df_index['Counter'], append=True, inplace=True)
    
    nmm_data_ued = pd.read_excel(data_file, sheet_name = sheet_nmm_ued, header=0, index_col=0, usecols=[0,19,20,21,22])
    df_index = pd.DataFrame(range(len(nmm_data_ued)), columns = ['Counter'])
    nmm_data_ued.set_index(df_index['Counter'], append=True, inplace=True)
    
    ## Calculations for PPA
    ppa_data_fec = pd.read_excel(data_file, sheet_name = sheet_ppa_fec, header=0, index_col=0, usecols=[0,19,20,21,22])
    df_index = pd.DataFrame(range(len(ppa_data_fec)), columns = ['Counter'])
    ppa_data_fec.set_index(df_index['Counter'], append=True, inplace=True)
    
    ppa_data_ued = pd.read_excel(data_file, sheet_name = sheet_ppa_ued, header=0, index_col=0, usecols=[0,19,20,21,22])
    df_index = pd.DataFrame(range(len(ppa_data_ued)), columns = ['Counter'])
    ppa_data_ued.set_index(df_index['Counter'], append=True, inplace=True)
    
    ## Calculations for FBT
    fbt_data_fec = pd.read_excel(data_file, sheet_name = sheet_fbt_fec, header=0, index_col=0, usecols=[0,19,20,21,22])
    df_index = pd.DataFrame(range(len(fbt_data_fec)), columns = ['Counter'])
    fbt_data_fec.set_index(df_index['Counter'], append=True, inplace=True)
    
    fbt_data_ued = pd.read_excel(data_file, sheet_name = sheet_fbt_ued, header=0, index_col=0, usecols=[0,19,20,21,22])
    df_index = pd.DataFrame(range(len(fbt_data_ued)), columns = ['Counter'])
    fbt_data_ued.set_index(df_index['Counter'], append=True, inplace=True)
    
    ## Calculations for TRE
    tre_data_fec = pd.read_excel(data_file, sheet_name = sheet_tre_fec, header=0, index_col=0, usecols=[0,19,20,21,22])
    df_index = pd.DataFrame(range(len(tre_data_fec)), columns = ['Counter'])
    tre_data_fec.set_index(df_index['Counter'], append=True, inplace=True)
    
    tre_data_ued = pd.read_excel(data_file, sheet_name = sheet_tre_ued, header=0, index_col=0, usecols=[0,19,20,21,22])
    df_index = pd.DataFrame(range(len(tre_data_ued)), columns = ['Counter'])
    tre_data_ued.set_index(df_index['Counter'], append=True, inplace=True)
    
    ## Calculations for MAE
    mae_data_fec = pd.read_excel(data_file, sheet_name = sheet_mae_fec, header=0, index_col=0, usecols=[0,19,20,21,22])
    df_index = pd.DataFrame(range(len(mae_data_fec)), columns = ['Counter'])
    mae_data_fec.set_index(df_index['Counter'], append=True, inplace=True)
    
    mae_data_ued = pd.read_excel(data_file, sheet_name = sheet_mae_ued, header=0, index_col=0, usecols=[0,19,20,21,22])
    df_index = pd.DataFrame(range(len(mae_data_ued)), columns = ['Counter'])
    mae_data_ued.set_index(df_index['Counter'], append=True, inplace=True)
    
    ## Calculations for TEL
    tel_data_fec = pd.read_excel(data_file, sheet_name = sheet_tel_fec, header=0, index_col=0, usecols=[0,19,20,21,22])
    df_index = pd.DataFrame(range(len(tel_data_fec)), columns = ['Counter'])
    tel_data_fec.set_index(df_index['Counter'], append=True, inplace=True)
    
    tel_data_ued = pd.read_excel(data_file, sheet_name = sheet_tel_ued, header=0, index_col=0, usecols=[0,19,20,21,22])
    df_index = pd.DataFrame(range(len(tel_data_ued)), columns = ['Counter'])
    tel_data_ued.set_index(df_index['Counter'], append=True, inplace=True)
    
    ## Calculations for WWP
    wwp_data_fec = pd.read_excel(data_file, sheet_name = sheet_wwp_fec, header=0, index_col=0, usecols=[0,19,20,21,22])
    df_index = pd.DataFrame(range(len(wwp_data_fec)), columns = ['Counter'])
    wwp_data_fec.set_index(df_index['Counter'], append=True, inplace=True)
    
    wwp_data_ued = pd.read_excel(data_file, sheet_name = sheet_wwp_ued, header=0, index_col=0, usecols=[0,19,20,21,22])
    df_index = pd.DataFrame(range(len(wwp_data_ued)), columns = ['Counter'])
    wwp_data_ued.set_index(df_index['Counter'], append=True, inplace=True)
    
    ## Calculations for OIS
    ois_data_fec = pd.read_excel(data_file, sheet_name = sheet_ois_fec, header=0, index_col=0, usecols=[0,19,20,21,22])
    df_index = pd.DataFrame(range(len(ois_data_fec)), columns = ['Counter'])
    ois_data_fec.set_index(df_index['Counter'], append=True, inplace=True)
    
    ois_data_ued = pd.read_excel(data_file, sheet_name = sheet_ois_ued, header=0, index_col=0, usecols=[0,19,20,21,22])
    df_index = pd.DataFrame(range(len(ois_data_ued)), columns = ['Counter'])
    ois_data_ued.set_index(df_index['Counter'], append=True, inplace=True)
    
    ## Create dictionary
    sectors_fec_dic = dict(ISI = isi_data_fec, NFM = nfm_data_fec, CHI = chi_data_fec,
                           NMM = nmm_data_fec, PPA = ppa_data_fec, FBT = fbt_data_fec,
                           TRE = tre_data_fec, MAE = mae_data_fec, TEL = tel_data_fec,
                           WWP = wwp_data_fec, OIS = ois_data_fec)
    
    sectors_ued_dic = dict(ISI = isi_data_ued, NFM = nfm_data_ued, CHI = chi_data_ued,
                           NMM = nmm_data_ued, PPA = ppa_data_ued, FBT = fbt_data_ued,
                           TRE = tre_data_ued, MAE = mae_data_ued, TEL = tel_data_ued,
                           WWP = wwp_data_ued, OIS = ois_data_ued)
    sectors_fec_keys = sectors_fec_dic.keys()
    sectors_ued_keys = sectors_ued_dic.keys()
    
    ## Construct tables for each sector for final energy demand
    
    fec_list = []
    for z in sectors_fec_keys:
        if z == 'ISI':
            # Coal
            coal = (sectors_fec_dic[z].iloc[15] + sectors_fec_dic[z].iloc[21:23].sum()
                    + sectors_fec_dic[z].iloc[39] + sectors_fec_dic[z].iloc[64]
                    + sectors_fec_dic[z].iloc[83])
            coal = coal.to_frame().transpose()
            coal.rename(index={0:'Coal'}, inplace=True)
            # Oil
            oil = (sectors_fec_dic[z].iloc[9] + sectors_fec_dic[z].iloc[16] + sectors_fec_dic[z].iloc[23] 
                   + sectors_fec_dic[z].iloc[28:31].sum(axis=0) + sectors_fec_dic[z].iloc[35] 
                   + sectors_fec_dic[z].iloc[36] + sectors_fec_dic[z].iloc[40:45].sum() 
                   + sectors_fec_dic[z].iloc[58] + sectors_fec_dic[z].iloc[65] + sectors_fec_dic[z].iloc[72:75].sum() 
                   + sectors_fec_dic[z].iloc[79] + sectors_fec_dic[z].iloc[80] + sectors_fec_dic[z].iloc[84:89].sum())
            oil = oil.to_frame().transpose()
            oil.rename(index={0:'Oil'}, inplace=True)
            # Natural gas
            nat_gas = (sectors_fec_dic[z].iloc[10] + sectors_fec_dic[z].iloc[17] + sectors_fec_dic[z].iloc[18] 
                       + sectors_fec_dic[z].iloc[24] + sectors_fec_dic[z].iloc[25] + sectors_fec_dic[z].iloc[31] 
                       + sectors_fec_dic[z].iloc[37] + sectors_fec_dic[z].iloc[45] + sectors_fec_dic[z].iloc[46] 
                       + sectors_fec_dic[z].iloc[59] + sectors_fec_dic[z].iloc[66] + sectors_fec_dic[z].iloc[67] 
                       + sectors_fec_dic[z].iloc[75] + sectors_fec_dic[z].iloc[81] + sectors_fec_dic[z].iloc[89] 
                       + sectors_fec_dic[z].iloc[90])
            nat_gas = nat_gas.to_frame().transpose()
            nat_gas.rename(index={0:'Natural gas'}, inplace=True)
            # Biomass/biofuels
            biofuels = sectors_fec_dic[z].iloc[47] + sectors_fec_dic[z].iloc[91] 
            biofuels = biofuels.to_frame().transpose()
            biofuels.rename(index={0:'Biomass/Biofuels'}, inplace=True)
            # Solar
            solar = sectors_fec_dic[z].iloc[11] + sectors_fec_dic[z].iloc[60] 
            solar = solar.to_frame().transpose()
            solar.rename(index={0:'Solar'}, inplace=True)        
            # Distributed heat
            dist_heat = sectors_fec_dic[z].iloc[48] + sectors_fec_dic[z].iloc[92] 
            dist_heat = dist_heat.to_frame().transpose()
            dist_heat.rename(index={0:'Distributed heat'}, inplace=True)  
            # Electricity (heat)
            elec_heat = (sectors_fec_dic[z].iloc[13] + sectors_fec_dic[z].iloc[19] + sectors_fec_dic[z].iloc[32] 
                         + sectors_fec_dic[z].iloc[49] + sectors_fec_dic[z].iloc[62] + sectors_fec_dic[z].iloc[69] 
                         + sectors_fec_dic[z].iloc[76] + sectors_fec_dic[z].iloc[93])
            elec_heat = elec_heat.to_frame().transpose()
            elec_heat.rename(index={0:'Electricity (heat)'}, inplace=True)
            # Electricity (lighting, motors etc)
            elec_other = sectors_fec_dic[z].iloc[4:8].sum() + sectors_fec_dic[z].iloc[53:57].sum() 
            elec_other = elec_other.to_frame().transpose()
            elec_other.rename(index={0:'Electricity (lighting, motors etc)'}, inplace=True)
            # Combine in a single dataframe
            fuels = pd.concat([coal, oil, nat_gas, biofuels, solar, dist_heat, elec_heat, elec_other])
            fuels.index.names = [z]
            fec_list.append(fuels)
        elif z == 'NFM': 
            # Coal
            coal = (sectors_fec_dic[z].iloc[15] + sectors_fec_dic[z].iloc[57] + sectors_fec_dic[z].iloc[101]
                    + sectors_fec_dic[z].iloc[126] + sectors_fec_dic[z].iloc[145])
            coal = coal.to_frame().transpose()
            coal.rename(index={0:'Coal'}, inplace=True)
            # Oil
            oil = (sectors_fec_dic[z].iloc[9] + sectors_fec_dic[z].iloc[16:21].sum() + sectors_fec_dic[z].iloc[26:29].sum()
                   + sectors_fec_dic[z].iloc[38] + sectors_fec_dic[z].iloc[46:49].sum() + sectors_fec_dic[z].iloc[53]
                   + sectors_fec_dic[z].iloc[54] + sectors_fec_dic[z].iloc[58:63].sum() + sectors_fec_dic[z].iloc[76] 
                   + sectors_fec_dic[z].iloc[83:86].sum() + sectors_fec_dic[z].iloc[90:93].sum() + sectors_fec_dic[z].iloc[97] 
                   + sectors_fec_dic[z].iloc[98] + sectors_fec_dic[z].iloc[102:107].sum() + sectors_fec_dic[z].iloc[119] 
                   + sectors_fec_dic[z].iloc[127:130].sum() + sectors_fec_dic[z].iloc[134:137].sum() + sectors_fec_dic[z].iloc[141] 
                   + sectors_fec_dic[z].iloc[142] + sectors_fec_dic[z].iloc[146:151].sum())
            oil = oil.to_frame().transpose()
            oil.rename(index={0:'Oil'}, inplace=True)
            # Natural gas
            nat_gas = (sectors_fec_dic[z].iloc[10] + sectors_fec_dic[z].iloc[21] + sectors_fec_dic[z].iloc[22] 
                       + sectors_fec_dic[z].iloc[29] + sectors_fec_dic[z].iloc[39] + sectors_fec_dic[z].iloc[49] 
                       + sectors_fec_dic[z].iloc[55] + sectors_fec_dic[z].iloc[63] + sectors_fec_dic[z].iloc[64] 
                       + sectors_fec_dic[z].iloc[77] + sectors_fec_dic[z].iloc[86] + sectors_fec_dic[z].iloc[93] 
                       + sectors_fec_dic[z].iloc[99] + sectors_fec_dic[z].iloc[107] + sectors_fec_dic[z].iloc[108] 
                       + sectors_fec_dic[z].iloc[120] + sectors_fec_dic[z].iloc[130] + sectors_fec_dic[z].iloc[137] 
                       + sectors_fec_dic[z].iloc[143] + sectors_fec_dic[z].iloc[151] + sectors_fec_dic[z].iloc[152])
            nat_gas = nat_gas.to_frame().transpose()
            nat_gas.rename(index={0:'Natural gas'}, inplace=True)
            # Biomass/biofuels
            biofuels = sectors_fec_dic[z].iloc[[23, 65, 109, 153]].sum()
            biofuels = biofuels.to_frame().transpose()
            biofuels.rename(index={0:'Biomass/Biofuels'}, inplace=True)
            # Solar
            solar = sectors_fec_dic[z].iloc[[11, 40, 78, 121]].sum()
            solar = solar.to_frame().transpose()
            solar.rename(index={0:'Solar'}, inplace=True)        
            # Distributed heat
            dist_heat = sectors_fec_dic[z].iloc[[24, 66, 110, 154]].sum()
            dist_heat = dist_heat.to_frame().transpose()
            dist_heat.rename(index={0:'Distributed heat'}, inplace=True)  
            # Electricity (heat)
            elec_heat = sectors_fec_dic[z].iloc[[13, 30, 42, 43, 50, 67, 80, 87, 94, 111, 123, 131, 138, 155]].sum()
            elec_heat = elec_heat.to_frame().transpose()
            elec_heat.rename(index={0:'Electricity (heat)'}, inplace=True)
            # Electricity (lighting, motors etc)
            elec_other = (sectors_fec_dic[z].iloc[4:8].sum() + sectors_fec_dic[z].iloc[33:37].sum() 
                          + sectors_fec_dic[z].iloc[71:75].sum() + sectors_fec_dic[z].iloc[114:118].sum())
            elec_other = elec_other.to_frame().transpose()
            elec_other.rename(index={0:'Electricity (lighting, motors etc)'}, inplace=True)
            # Combine in a single dataframe
            fuels = pd.concat([coal, oil, nat_gas, biofuels, solar, dist_heat, elec_heat, elec_other])
            fuels.index.names = [z]
            fec_list.append(fuels)
        elif z == 'CHI': 
            # Coal
            coal = sectors_fec_dic[z].iloc[[24, 36, 45, 72, 85, 94, 121, 134, 143]].sum()
            coal = coal.to_frame().transpose()
            coal.rename(index={0:'Coal'}, inplace=True)
            # Oil
            oil = (sectors_fec_dic[z].iloc[9] + sectors_fec_dic[z].iloc[25:30].sum() + sectors_fec_dic[z].iloc[37:40].sum()
                   + sectors_fec_dic[z].iloc[46:50].sum() +  sectors_fec_dic[z].iloc[65] + sectors_fec_dic[z].iloc[73:78].sum()
                   + sectors_fec_dic[z].iloc[86:89].sum() + sectors_fec_dic[z].iloc[95:100].sum() + sectors_fec_dic[z].iloc[114]
                   + sectors_fec_dic[z].iloc[122:127].sum() + sectors_fec_dic[z].iloc[135:138].sum() + sectors_fec_dic[z].iloc[144:149].sum())
            oil = oil.to_frame().transpose()
            oil.rename(index={0:'Oil'}, inplace=True)
            # Natural gas
            nat_gas = sectors_fec_dic[z].iloc[[10, 30, 31, 40, 43, 51, 52, 66, 78, 79, 89, 92, 100, 101, 115, 127, 128, 138, 141, 149, 150]].sum()
            nat_gas = nat_gas.to_frame().transpose()
            nat_gas.rename(index={0:'Natural gas'}, inplace=True)
            # Biomass/biofuels
            biofuels = sectors_fec_dic[z].iloc[[32, 53, 80, 102, 129, 151]].sum()
            biofuels = biofuels.to_frame().transpose()
            biofuels.rename(index={0:'Biomass/Biofuels'}, inplace=True)
            # Solar
            solar = sectors_fec_dic[z].iloc[[11, 67, 116]].sum()
            solar = solar.to_frame().transpose()
            solar.rename(index={0:'Solar'}, inplace=True)        
            # Distributed heat
            dist_heat = sectors_fec_dic[z].iloc[[33, 54, 81, 103, 130, 152]].sum()
            dist_heat = dist_heat.to_frame().transpose()
            dist_heat.rename(index={0:'Distributed heat'}, inplace=True)  
            # Electricity (heat)
            elec_heat = sectors_fec_dic[z].iloc[[13, 41, 55, 69, 82, 90, 104, 118, 131, 139, 153]].sum()
            elec_heat = elec_heat.to_frame().transpose()
            elec_heat.rename(index={0:'Electricity (heat)'}, inplace=True)
            # Electricity (lighting, motors etc)
            elec_other = (sectors_fec_dic[z].iloc[4:8].sum() + sectors_fec_dic[z].iloc[56]
                          + sectors_fec_dic[z].iloc[60:64].sum() + sectors_fec_dic[z].iloc[105] 
                          + sectors_fec_dic[z].iloc[109:113].sum() + sectors_fec_dic[z].iloc[154]) 
            elec_other = elec_other.to_frame().transpose()
            elec_other.rename(index={0:'Electricity (lighting, motors etc)'}, inplace=True)
            # Combine in a single dataframe
            fuels = pd.concat([coal, oil, nat_gas, biofuels, solar, dist_heat, elec_heat, elec_other])
            fuels.index.names = [z]
            fec_list.append(fuels)        
        elif z == 'NMM': 
            # Coal
            coal = sectors_fec_dic[z].iloc[[16, 24, 34, 60, 66, 79, 89, 110, 119]].sum()
            coal = coal.to_frame().transpose()
            coal.rename(index={0:'Coal'}, inplace=True)
            # Oil
            oil = (sectors_fec_dic[z].iloc[9] + sectors_fec_dic[z].iloc[17:21].sum() + sectors_fec_dic[z].iloc[25:29].sum()
                   + sectors_fec_dic[z].iloc[35:40].sum() +  sectors_fec_dic[z].iloc[52] + sectors_fec_dic[z].iloc[61:64].sum()
                   + sectors_fec_dic[z].iloc[67:72].sum() + sectors_fec_dic[z].iloc[80:84].sum() + sectors_fec_dic[z].iloc[90:93].sum()
                   + sectors_fec_dic[z].iloc[103] + sectors_fec_dic[z].iloc[111:114].sum() + sectors_fec_dic[z].iloc[120:123].sum())
            oil = oil.to_frame().transpose()
            oil.rename(index={0:'Oil'}, inplace=True)
            # Natural gas
            nat_gas = sectors_fec_dic[z].iloc[[10, 21, 29, 40, 41, 53, 64, 72, 73, 84, 93, 104, 114, 123]].sum()
            nat_gas = nat_gas.to_frame().transpose()
            nat_gas.rename(index={0:'Natural gas'}, inplace=True)
            # Biomass/biofuels
            biofuels = sectors_fec_dic[z].iloc[[22, 30, 42, 74, 85]].sum()
            biofuels = biofuels.to_frame().transpose()
            biofuels.rename(index={0:'Biomass/Biofuels'}, inplace=True)
            # Solar
            solar = sectors_fec_dic[z].iloc[[11, 54, 105]].sum()
            solar = solar.to_frame().transpose()
            solar.rename(index={0:'Solar'}, inplace=True)        
            # Distributed heat
            dist_heat = sectors_fec_dic[z].iloc[[43, 75]].sum()
            dist_heat = dist_heat.to_frame().transpose()
            dist_heat.rename(index={0:'Distributed heat'}, inplace=True)  
            # Electricity (heat)
            elec_heat = sectors_fec_dic[z].iloc[[13, 56, 76, 86, 94, 107, 115, 124]].sum()
            elec_heat = elec_heat.to_frame().transpose()
            elec_heat.rename(index={0:'Electricity (heat)'}, inplace=True)
            # Electricity (lighting, motors etc)
            elec_other = (sectors_fec_dic[z].iloc[4:8].sum() + sectors_fec_dic[z].iloc[14]
                          + sectors_fec_dic[z].iloc[32] + sectors_fec_dic[z].iloc[47:51].sum() 
                          + sectors_fec_dic[z].iloc[57] + sectors_fec_dic[z].iloc[98:102].sum()
                          + sectors_fec_dic[z].iloc[116] + sectors_fec_dic[z].iloc[125])  
            elec_other = elec_other.to_frame().transpose()
            elec_other.rename(index={0:'Electricity (lighting, motors etc)'}, inplace=True)
            # Combine in a single dataframe
            fuels = pd.concat([coal, oil, nat_gas, biofuels, solar, dist_heat, elec_heat, elec_other])
            fuels.index.names = [z]
            fec_list.append(fuels)        
        elif z == 'PPA': 
            # Coal
            coal = sectors_fec_dic[z].iloc[[17, 43, 56, 69]].sum()
            coal = coal.to_frame().transpose()
            coal.rename(index={0:'Coal'}, inplace=True)
            # Oil
            oil = (sectors_fec_dic[z].iloc[9] + sectors_fec_dic[z].iloc[18:23].sum() + sectors_fec_dic[z].iloc[36]
                   + sectors_fec_dic[z].iloc[44:49].sum() + sectors_fec_dic[z].iloc[57:62].sum()
                   + sectors_fec_dic[z].iloc[70:75].sum() + sectors_fec_dic[z].iloc[87])
            oil = oil.to_frame().transpose()
            oil.rename(index={0:'Oil'}, inplace=True)
            # Natural gas
            nat_gas = sectors_fec_dic[z].iloc[[10, 23, 24, 37, 49, 50, 62, 63, 75, 76, 88]].sum()
            nat_gas = nat_gas.to_frame().transpose()
            nat_gas.rename(index={0:'Natural gas'}, inplace=True)
            # Biomass/biofuels
            biofuels = sectors_fec_dic[z].iloc[[25, 51, 64, 77]].sum()
            biofuels = biofuels.to_frame().transpose()
            biofuels.rename(index={0:'Biomass/Biofuels'}, inplace=True)
            # Solar
            solar = sectors_fec_dic[z].iloc[[11, 38, 89]].sum()
            solar = solar.to_frame().transpose()
            solar.rename(index={0:'Solar'}, inplace=True)        
            # Distributed heat
            dist_heat = sectors_fec_dic[z].iloc[[26, 52, 65, 78]].sum()
            dist_heat = dist_heat.to_frame().transpose()
            dist_heat.rename(index={0:'Distributed heat'}, inplace=True)  
            # Electricity (heat)
            elec_heat = sectors_fec_dic[z].iloc[[13, 27, 40, 53, 66, 79, 91]].sum()
            elec_heat = elec_heat.to_frame().transpose()
            elec_heat.rename(index={0:'Electricity (heat)'}, inplace=True)
            # Electricity (lighting, motors etc)
            elec_other = (sectors_fec_dic[z].iloc[4:8].sum() + sectors_fec_dic[z].iloc[14]
                          + sectors_fec_dic[z].iloc[28] + sectors_fec_dic[z].iloc[31:35].sum() 
                          + sectors_fec_dic[z].iloc[82:86].sum() + sectors_fec_dic[z].iloc[92])  
            elec_other = elec_other.to_frame().transpose()
            elec_other.rename(index={0:'Electricity (lighting, motors etc)'}, inplace=True)
            # Combine in a single dataframe
            fuels = pd.concat([coal, oil, nat_gas, biofuels, solar, dist_heat, elec_heat, elec_other])
            fuels.index.names = [z]
            fec_list.append(fuels)
        elif z == 'FBT': 
            # Coal
            coal = sectors_fec_dic[z].iloc[[16, 25, 33, 45, 51, 67]].sum()
            coal = coal.to_frame().transpose()
            coal.rename(index={0:'Coal'}, inplace=True)
            # Oil
            oil = (sectors_fec_dic[z].iloc[9] + sectors_fec_dic[z].iloc[17:20].sum() 
                   + sectors_fec_dic[z].iloc[26:29].sum() + sectors_fec_dic[z].iloc[34:39].sum()
                   + sectors_fec_dic[z].iloc[46:49].sum() + sectors_fec_dic[z].iloc[52:57].sum()
                   + sectors_fec_dic[z].iloc[68:73].sum())
            oil = oil.to_frame().transpose()
            oil.rename(index={0:'Oil'}, inplace=True)
            # Natural gas
            nat_gas = sectors_fec_dic[z].iloc[[10, 20, 29, 39, 40, 49, 57, 58, 65, 73, 74]].sum()
            nat_gas = nat_gas.to_frame().transpose()
            nat_gas.rename(index={0:'Natural gas'}, inplace=True)
            # Biomass/biofuels
            biofuels = sectors_fec_dic[z].iloc[[41, 59, 75]].sum()
            biofuels = biofuels.to_frame().transpose()
            biofuels.rename(index={0:'Biomass/Biofuels'}, inplace=True)
            # Solar
            solar = sectors_fec_dic[z].iloc[11]
            solar = solar.to_frame().transpose()
            solar = solar.reset_index(drop=True)
            solar.rename(index={0:'Solar'}, inplace=True)        
            # Distributed heat
            dist_heat = sectors_fec_dic[z].iloc[[42, 60, 76]].sum()
            dist_heat = dist_heat.to_frame().transpose()
            dist_heat.rename(index={0:'Distributed heat'}, inplace=True)  
            # Electricity (heat)
            elec_heat = (sectors_fec_dic[z].iloc[[13, 21, 22, 30, 31]].sum()
                         + sectors_fec_dic[z].iloc[61:64].sum()
                         + sectors_fec_dic[z].iloc[77])
            elec_heat = elec_heat.to_frame().transpose()
            elec_heat.rename(index={0:'Electricity (heat)'}, inplace=True)
            # Electricity (lighting, motors etc)
            elec_other = (sectors_fec_dic[z].iloc[4:8].sum() + sectors_fec_dic[z].iloc[78])  
            elec_other = elec_other.to_frame().transpose()
            elec_other.rename(index={0:'Electricity (lighting, motors etc)'}, inplace=True)
            # Combine in a single dataframe
            fuels = pd.concat([coal, oil, nat_gas, biofuels, solar, dist_heat, elec_heat, elec_other])
            fuels.index.names = [z]
            fec_list.append(fuels) 
        elif z == 'TRE': 
            # Coal 
            coal = sectors_fec_dic[z].iloc[[16, 27, 34]].sum()
            coal = coal.to_frame().transpose()
            coal.rename(index={0:'Coal'}, inplace=True)
            # Oil
            oil = (sectors_fec_dic[z].iloc[9] + sectors_fec_dic[z].iloc[17:20].sum() 
                   + sectors_fec_dic[z].iloc[28:31].sum() + sectors_fec_dic[z].iloc[35:40].sum())
            oil = oil.to_frame().transpose()
            oil.rename(index={0:'Oil'}, inplace=True)
            # Natural gas
            nat_gas = sectors_fec_dic[z].iloc[[10, 20, 23, 31, 40, 41]].sum()
            nat_gas = nat_gas.to_frame().transpose()
            nat_gas.rename(index={0:'Natural gas'}, inplace=True)
            # Biomass/biofuels
            biofuels = sectors_fec_dic[z].iloc[42]
            biofuels = biofuels.to_frame().transpose()
            biofuels = biofuels.reset_index(drop=True)
            biofuels.rename(index={0:'Biomass/Biofuels'}, inplace=True)
            # Solar
            solar = sectors_fec_dic[z].iloc[11]
            solar = solar.to_frame().transpose()
            solar = solar.reset_index(drop=True)
            solar.rename(index={0:'Solar'}, inplace=True)        
            # Distributed heat
            dist_heat = sectors_fec_dic[z].iloc[43]
            dist_heat = dist_heat.to_frame().transpose()
            dist_heat = dist_heat.reset_index(drop=True)
            dist_heat.rename(index={0:'Distributed heat'}, inplace=True)  
            # Electricity (heat)
            elec_heat = (sectors_fec_dic[z].iloc[[13, 21, 24, 32]].sum())
            elec_heat = elec_heat.to_frame().transpose()
            elec_heat.rename(index={0:'Electricity (heat)'}, inplace=True)
            # Electricity (lighting, motors etc)
            elec_other = (sectors_fec_dic[z].iloc[4:8].sum() + sectors_fec_dic[z].iloc[44]
                          + sectors_fec_dic[z].iloc[45])  
            elec_other = elec_other.to_frame().transpose()
            elec_other.rename(index={0:'Electricity (lighting, motors etc)'}, inplace=True)
            # Combine in a single dataframe
            fuels = pd.concat([coal, oil, nat_gas, biofuels, solar, dist_heat, elec_heat, elec_other])
            fuels.index.names = [z]
            fec_list.append(fuels) 
        elif z == 'MAE': 
            # Coal 
            coal = sectors_fec_dic[z].iloc[[16, 27, 34]].sum()
            coal = coal.to_frame().transpose()
            coal.rename(index={0:'Coal'}, inplace=True)
            # Oil
            oil = (sectors_fec_dic[z].iloc[9] + sectors_fec_dic[z].iloc[17:20].sum() 
                   + sectors_fec_dic[z].iloc[28:31].sum() + sectors_fec_dic[z].iloc[35:40].sum())
            oil = oil.to_frame().transpose()
            oil.rename(index={0:'Oil'}, inplace=True)
            # Natural gas
            nat_gas = sectors_fec_dic[z].iloc[[10, 20, 23, 31, 40, 41]].sum()
            nat_gas = nat_gas.to_frame().transpose()
            nat_gas.rename(index={0:'Natural gas'}, inplace=True)
            # Biomass/biofuels
            biofuels = sectors_fec_dic[z].iloc[42]
            biofuels = biofuels.to_frame().transpose()
            biofuels = biofuels.reset_index(drop=True)
            biofuels.rename(index={0:'Biomass/Biofuels'}, inplace=True)
            # Solar
            solar = sectors_fec_dic[z].iloc[11]
            solar = solar.to_frame().transpose()
            solar = solar.reset_index(drop=True)
            solar.rename(index={0:'Solar'}, inplace=True)        
            # Distributed heat
            dist_heat = sectors_fec_dic[z].iloc[43]
            dist_heat = dist_heat.to_frame().transpose()
            dist_heat = dist_heat.reset_index(drop=True)
            dist_heat.rename(index={0:'Distributed heat'}, inplace=True)  
            # Electricity (heat)
            elec_heat = (sectors_fec_dic[z].iloc[[13, 21, 24, 32]].sum())
            elec_heat = elec_heat.to_frame().transpose()
            elec_heat.rename(index={0:'Electricity (heat)'}, inplace=True)
            # Electricity (lighting, motors etc)
            elec_other = (sectors_fec_dic[z].iloc[4:8].sum() + sectors_fec_dic[z].iloc[44]
                          + sectors_fec_dic[z].iloc[45])  
            elec_other = elec_other.to_frame().transpose()
            elec_other.rename(index={0:'Electricity (lighting, motors etc)'}, inplace=True)
            # Combine in a single dataframe
            fuels = pd.concat([coal, oil, nat_gas, biofuels, solar, dist_heat, elec_heat, elec_other])
            fuels.index.names = [z]
            fec_list.append(fuels) 
        elif z == 'TEL': 
            # Coal 
            coal = sectors_fec_dic[z].iloc[[15, 26, 39, 45]].sum()
            coal = coal.to_frame().transpose()
            coal.rename(index={0:'Coal'}, inplace=True)
            # Oil
            oil = (sectors_fec_dic[z].iloc[9] + sectors_fec_dic[z].iloc[16:21].sum() 
                   + sectors_fec_dic[z].iloc[27:32].sum() + sectors_fec_dic[z].iloc[40:43].sum()
                   + sectors_fec_dic[z].iloc[46:51].sum())
            oil = oil.to_frame().transpose()
            oil.rename(index={0:'Oil'}, inplace=True)
            # Natural gas
            nat_gas = sectors_fec_dic[z].iloc[[10, 21, 22, 32, 33, 43, 51, 52]].sum()
            nat_gas = nat_gas.to_frame().transpose()
            nat_gas.rename(index={0:'Natural gas'}, inplace=True)
            # Biomass/biofuels
            biofuels = sectors_fec_dic[z].iloc[[23, 34, 53]].sum()
            biofuels = biofuels.to_frame().transpose()
            biofuels.rename(index={0:'Biomass/Biofuels'}, inplace=True)
            # Solar
            solar = sectors_fec_dic[z].iloc[11]
            solar = solar.to_frame().transpose()
            solar = solar.reset_index(drop=True)
            solar.rename(index={0:'Solar'}, inplace=True)        
            # Distributed heat
            dist_heat = sectors_fec_dic[z].iloc[[24, 35, 54]].sum()
            dist_heat = dist_heat.to_frame().transpose()
            dist_heat.rename(index={0:'Distributed heat'}, inplace=True)  
            # Electricity (heat)
            elec_heat = (sectors_fec_dic[z].iloc[[13, 55, 56]].sum())
            elec_heat = elec_heat.to_frame().transpose()
            elec_heat.rename(index={0:'Electricity (heat)'}, inplace=True)
            # Electricity (lighting, motors etc)
            elec_other = (sectors_fec_dic[z].iloc[4:8].sum() + sectors_fec_dic[z].iloc[36]
                          + sectors_fec_dic[z].iloc[57])  
            elec_other = elec_other.to_frame().transpose()
            elec_other.rename(index={0:'Electricity (lighting, motors etc)'}, inplace=True)
            # Combine in a single dataframe
            fuels = pd.concat([coal, oil, nat_gas, biofuels, solar, dist_heat, elec_heat, elec_other])
            fuels.index.names = [z]
            fec_list.append(fuels)
        elif z == 'WWP': 
            # Coal 
            coal = sectors_fec_dic[z].iloc[[15, 28, 34]].sum()
            coal = coal.to_frame().transpose()
            coal.rename(index={0:'Coal'}, inplace=True)
            # Oil
            oil = (sectors_fec_dic[z].iloc[9] + sectors_fec_dic[z].iloc[16:21].sum() 
                   + sectors_fec_dic[z].iloc[30:32].sum() + sectors_fec_dic[z].iloc[35:40].sum())
            oil = oil.to_frame().transpose()
            oil.rename(index={0:'Oil'}, inplace=True)
            # Natural gas
            nat_gas = sectors_fec_dic[z].iloc[[10, 21, 22, 32, 40, 41]].sum()
            nat_gas = nat_gas.to_frame().transpose()
            nat_gas.rename(index={0:'Natural gas'}, inplace=True)
            # Biomass/biofuels
            biofuels = sectors_fec_dic[z].iloc[[23, 42]].sum()
            biofuels = biofuels.to_frame().transpose()
            biofuels.rename(index={0:'Biomass/Biofuels'}, inplace=True)
            # Solar
            solar = sectors_fec_dic[z].iloc[11]
            solar = solar.to_frame().transpose()
            solar = solar.reset_index(drop=True)
            solar.rename(index={0:'Solar'}, inplace=True)        
            # Distributed heat
            dist_heat = sectors_fec_dic[z].iloc[[24, 43]].sum()
            dist_heat = dist_heat.to_frame().transpose()
            dist_heat.rename(index={0:'Distributed heat'}, inplace=True)  
            # Electricity (heat)
            elec_heat = (sectors_fec_dic[z].iloc[[13, 44, 45]].sum())
            elec_heat = elec_heat.to_frame().transpose()
            elec_heat.rename(index={0:'Electricity (heat)'}, inplace=True)
            # Electricity (lighting, motors etc)
            elec_other = (sectors_fec_dic[z].iloc[4:8].sum() + sectors_fec_dic[z].iloc[25]
                          + sectors_fec_dic[z].iloc[43])  
            elec_other = elec_other.to_frame().transpose()
            elec_other.rename(index={0:'Electricity (lighting, motors etc)'}, inplace=True)
            # Combine in a single dataframe
            fuels = pd.concat([coal, oil, nat_gas, biofuels, solar, dist_heat, elec_heat, elec_other])
            fuels.index.names = [z]
            fec_list.append(fuels)         
        elif z == 'OIS': 
            # Coal 
            coal = sectors_fec_dic[z].iloc[[15, 27, 35, 41, 55]].sum()
            coal = coal.to_frame().transpose()
            coal.rename(index={0:'Coal'}, inplace=True)
            # Oil
            oil = (sectors_fec_dic[z].iloc[9] + sectors_fec_dic[z].iloc[16:21].sum() 
                   + sectors_fec_dic[z].iloc[28:31].sum() + sectors_fec_dic[z].iloc[36:39].sum()
                   + sectors_fec_dic[z].iloc[42:47].sum() + sectors_fec_dic[z].iloc[56:61].sum()
                   + sectors_fec_dic[z].iloc[66])
            oil = oil.to_frame().transpose()
            oil.rename(index={0:'Oil'}, inplace=True)
            # Natural gas
            nat_gas = sectors_fec_dic[z].iloc[[10, 21, 22, 31, 39, 47, 48, 53, 61, 62]].sum()
            nat_gas = nat_gas.to_frame().transpose()
            nat_gas.rename(index={0:'Natural gas'}, inplace=True)
            # Biomass/biofuels
            biofuels = sectors_fec_dic[z].iloc[[23, 49, 63]].sum()
            biofuels = biofuels.to_frame().transpose()
            biofuels.rename(index={0:'Biomass/Biofuels'}, inplace=True)
            # Solar
            solar = sectors_fec_dic[z].iloc[11]
            solar = solar.to_frame().transpose()
            solar = solar.reset_index(drop=True)
            solar.rename(index={0:'Solar'}, inplace=True)        
            # Distributed heat
            dist_heat = sectors_fec_dic[z].iloc[[24, 50, 64]].sum()
            dist_heat = dist_heat.to_frame().transpose()
            dist_heat.rename(index={0:'Distributed heat'}, inplace=True)  
            # Electricity (heat)
            elec_heat = (sectors_fec_dic[z].iloc[[13, 32, 51, 65]].sum())
            elec_heat = elec_heat.to_frame().transpose()
            elec_heat.rename(index={0:'Electricity (heat)'}, inplace=True)
            # Electricity (lighting, motors etc)
            elec_other = (sectors_fec_dic[z].iloc[4:8].sum() + sectors_fec_dic[z].iloc[67])  
            elec_other = elec_other.to_frame().transpose()
            elec_other.rename(index={0:'Electricity (lighting, motors etc)'}, inplace=True)
            # Combine in a single dataframe
            fuels = pd.concat([coal, oil, nat_gas, biofuels, solar, dist_heat, elec_heat, elec_other])
            fuels.index.names = [z]
            fec_list.append(fuels)   
    fuels_fec_dic = dict(zip(sectors_fec_keys, fec_list)) # Create dictionary for each sector
    #fuels_fec_df = pd.concat(fec_list, keys= sectors_fec_keys) # Create a single dataframe
    #fuels_fec_df.index.names = ['Sector', 'Fuel']
    
    ued_list = []
    for z in sectors_ued_keys:
        if z == 'ISI':
            # Coal
            coal = (sectors_ued_dic[z].iloc[15] + sectors_ued_dic[z].iloc[21:23].sum()
                    + sectors_ued_dic[z].iloc[39] + sectors_ued_dic[z].iloc[64]
                    + sectors_ued_dic[z].iloc[83])
            coal = coal.to_frame().transpose()
            coal.rename(index={0:'Coal'}, inplace=True)
            # Oil
            oil = (sectors_ued_dic[z].iloc[9] + sectors_ued_dic[z].iloc[16] + sectors_ued_dic[z].iloc[23] 
                   + sectors_ued_dic[z].iloc[28:31].sum(axis=0) + sectors_ued_dic[z].iloc[35] 
                   + sectors_ued_dic[z].iloc[36] + sectors_ued_dic[z].iloc[40:45].sum() 
                   + sectors_ued_dic[z].iloc[58] + sectors_ued_dic[z].iloc[65] + sectors_ued_dic[z].iloc[72:75].sum() 
                   + sectors_ued_dic[z].iloc[79] + sectors_ued_dic[z].iloc[80] + sectors_ued_dic[z].iloc[84:89].sum())
            oil = oil.to_frame().transpose()
            oil.rename(index={0:'Oil'}, inplace=True)
            # Natural gas
            nat_gas = (sectors_ued_dic[z].iloc[10] + sectors_ued_dic[z].iloc[17] + sectors_ued_dic[z].iloc[18] 
                       + sectors_ued_dic[z].iloc[24] + sectors_ued_dic[z].iloc[25] + sectors_ued_dic[z].iloc[31] 
                       + sectors_ued_dic[z].iloc[37] + sectors_ued_dic[z].iloc[45] + sectors_ued_dic[z].iloc[46] 
                       + sectors_ued_dic[z].iloc[59] + sectors_ued_dic[z].iloc[66] + sectors_ued_dic[z].iloc[67] 
                       + sectors_ued_dic[z].iloc[75] + sectors_ued_dic[z].iloc[81] + sectors_ued_dic[z].iloc[89] 
                       + sectors_ued_dic[z].iloc[90])
            nat_gas = nat_gas.to_frame().transpose()
            nat_gas.rename(index={0:'Natural gas'}, inplace=True)
            # Biomass/biofuels
            biofuels = sectors_ued_dic[z].iloc[47] + sectors_ued_dic[z].iloc[91] 
            biofuels = biofuels.to_frame().transpose()
            biofuels.rename(index={0:'Biomass/Biofuels'}, inplace=True)
            # Solar
            solar = sectors_ued_dic[z].iloc[11] + sectors_ued_dic[z].iloc[60] 
            solar = solar.to_frame().transpose()
            solar.rename(index={0:'Solar'}, inplace=True)        
            # Distributed heat
            dist_heat = sectors_ued_dic[z].iloc[48] + sectors_ued_dic[z].iloc[92] 
            dist_heat = dist_heat.to_frame().transpose()
            dist_heat.rename(index={0:'Distributed heat'}, inplace=True)  
            # Electricity (heat)
            elec_heat = (sectors_ued_dic[z].iloc[13] + sectors_ued_dic[z].iloc[19] + sectors_ued_dic[z].iloc[32] 
                         + sectors_ued_dic[z].iloc[49] + sectors_ued_dic[z].iloc[62] + sectors_ued_dic[z].iloc[69] 
                         + sectors_ued_dic[z].iloc[76] + sectors_ued_dic[z].iloc[93])
            elec_heat = elec_heat.to_frame().transpose()
            elec_heat.rename(index={0:'Electricity (heat)'}, inplace=True)
            # Electricity (lighting, motors etc)
            elec_other = sectors_ued_dic[z].iloc[4:8].sum() + sectors_ued_dic[z].iloc[53:57].sum() 
            elec_other = elec_other.to_frame().transpose()
            elec_other.rename(index={0:'Electricity (lighting, motors etc)'}, inplace=True)
            # Combine in a single dataframe
            fuels = pd.concat([coal, oil, nat_gas, biofuels, solar, dist_heat, elec_heat, elec_other])
            fuels.index.names = [z]
            ued_list.append(fuels)
        elif z == 'NFM': 
            # Coal
            coal = (sectors_ued_dic[z].iloc[15] + sectors_ued_dic[z].iloc[57] + sectors_ued_dic[z].iloc[101]
                    + sectors_ued_dic[z].iloc[126] + sectors_ued_dic[z].iloc[145])
            coal = coal.to_frame().transpose()
            coal.rename(index={0:'Coal'}, inplace=True)
            # Oil
            oil = (sectors_ued_dic[z].iloc[9] + sectors_ued_dic[z].iloc[16:21].sum() + sectors_ued_dic[z].iloc[26:29].sum()
                   + sectors_ued_dic[z].iloc[38] + sectors_ued_dic[z].iloc[46:49].sum() + sectors_ued_dic[z].iloc[53]
                   + sectors_ued_dic[z].iloc[54] + sectors_ued_dic[z].iloc[58:63].sum() + sectors_ued_dic[z].iloc[76] 
                   + sectors_ued_dic[z].iloc[83:86].sum() + sectors_ued_dic[z].iloc[90:93].sum() + sectors_ued_dic[z].iloc[97] 
                   + sectors_ued_dic[z].iloc[98] + sectors_ued_dic[z].iloc[102:107].sum() + sectors_ued_dic[z].iloc[119] 
                   + sectors_ued_dic[z].iloc[127:130].sum() + sectors_ued_dic[z].iloc[134:137].sum() + sectors_ued_dic[z].iloc[141] 
                   + sectors_ued_dic[z].iloc[142] + sectors_ued_dic[z].iloc[146:151].sum())
            oil = oil.to_frame().transpose()
            oil.rename(index={0:'Oil'}, inplace=True)
            # Natural gas
            nat_gas = (sectors_ued_dic[z].iloc[10] + sectors_ued_dic[z].iloc[21] + sectors_ued_dic[z].iloc[22] 
                       + sectors_ued_dic[z].iloc[29] + sectors_ued_dic[z].iloc[39] + sectors_ued_dic[z].iloc[49] 
                       + sectors_ued_dic[z].iloc[55] + sectors_ued_dic[z].iloc[63] + sectors_ued_dic[z].iloc[64] 
                       + sectors_ued_dic[z].iloc[77] + sectors_ued_dic[z].iloc[86] + sectors_ued_dic[z].iloc[93] 
                       + sectors_ued_dic[z].iloc[99] + sectors_ued_dic[z].iloc[107] + sectors_ued_dic[z].iloc[108] 
                       + sectors_ued_dic[z].iloc[120] + sectors_ued_dic[z].iloc[130] + sectors_ued_dic[z].iloc[137] 
                       + sectors_ued_dic[z].iloc[143] + sectors_ued_dic[z].iloc[151] + sectors_ued_dic[z].iloc[152])
            nat_gas = nat_gas.to_frame().transpose()
            nat_gas.rename(index={0:'Natural gas'}, inplace=True)
            # Biomass/biofuels
            biofuels = sectors_ued_dic[z].iloc[[23, 65, 109, 153]].sum()
            biofuels = biofuels.to_frame().transpose()
            biofuels.rename(index={0:'Biomass/Biofuels'}, inplace=True)
            # Solar
            solar = sectors_ued_dic[z].iloc[[11, 40, 78, 121]].sum()
            solar = solar.to_frame().transpose()
            solar.rename(index={0:'Solar'}, inplace=True)        
            # Distributed heat
            dist_heat = sectors_ued_dic[z].iloc[[24, 66, 110, 154]].sum()
            dist_heat = dist_heat.to_frame().transpose()
            dist_heat.rename(index={0:'Distributed heat'}, inplace=True)  
            # Electricity (heat)
            elec_heat = sectors_ued_dic[z].iloc[[13, 30, 42, 43, 50, 67, 80, 87, 94, 111, 123, 131, 138, 155]].sum()
            elec_heat = elec_heat.to_frame().transpose()
            elec_heat.rename(index={0:'Electricity (heat)'}, inplace=True)
            # Electricity (lighting, motors etc)
            elec_other = (sectors_ued_dic[z].iloc[4:8].sum() + sectors_ued_dic[z].iloc[33:37].sum() 
                          + sectors_ued_dic[z].iloc[71:75].sum() + sectors_ued_dic[z].iloc[114:118].sum())
            elec_other = elec_other.to_frame().transpose()
            elec_other.rename(index={0:'Electricity (lighting, motors etc)'}, inplace=True)
            # Combine in a single dataframe
            fuels = pd.concat([coal, oil, nat_gas, biofuels, solar, dist_heat, elec_heat, elec_other])
            fuels.index.names = [z]
            ued_list.append(fuels)
        elif z == 'CHI': 
            # Coal
            coal = sectors_ued_dic[z].iloc[[24, 36, 45, 72, 85, 94, 121, 134, 143]].sum()
            coal = coal.to_frame().transpose()
            coal.rename(index={0:'Coal'}, inplace=True)
            # Oil
            oil = (sectors_ued_dic[z].iloc[9] + sectors_ued_dic[z].iloc[25:30].sum() + sectors_ued_dic[z].iloc[37:40].sum()
                   + sectors_ued_dic[z].iloc[46:50].sum() +  sectors_ued_dic[z].iloc[65] + sectors_ued_dic[z].iloc[73:78].sum()
                   + sectors_ued_dic[z].iloc[86:89].sum() + sectors_ued_dic[z].iloc[95:100].sum() + sectors_ued_dic[z].iloc[114]
                   + sectors_ued_dic[z].iloc[122:127].sum() + sectors_ued_dic[z].iloc[135:138].sum() + sectors_ued_dic[z].iloc[144:149].sum())
            oil = oil.to_frame().transpose()
            oil.rename(index={0:'Oil'}, inplace=True)
            # Natural gas
            nat_gas = sectors_ued_dic[z].iloc[[10, 30, 31, 40, 43, 51, 52, 66, 78, 79, 89, 92, 100, 101, 115, 127, 128, 138, 141, 149, 150]].sum()
            nat_gas = nat_gas.to_frame().transpose()
            nat_gas.rename(index={0:'Natural gas'}, inplace=True)
            # Biomass/biofuels
            biofuels = sectors_ued_dic[z].iloc[[32, 53, 80, 102, 129, 151]].sum()
            biofuels = biofuels.to_frame().transpose()
            biofuels.rename(index={0:'Biomass/Biofuels'}, inplace=True)
            # Solar
            solar = sectors_ued_dic[z].iloc[[11, 67, 116]].sum()
            solar = solar.to_frame().transpose()
            solar.rename(index={0:'Solar'}, inplace=True)        
            # Distributed heat
            dist_heat = sectors_ued_dic[z].iloc[[33, 54, 81, 103, 130, 152]].sum()
            dist_heat = dist_heat.to_frame().transpose()
            dist_heat.rename(index={0:'Distributed heat'}, inplace=True)  
            # Electricity (heat)
            elec_heat = sectors_ued_dic[z].iloc[[13, 41, 55, 69, 82, 90, 104, 118, 131, 139, 153]].sum()
            elec_heat = elec_heat.to_frame().transpose()
            elec_heat.rename(index={0:'Electricity (heat)'}, inplace=True)
            # Electricity (lighting, motors etc)
            elec_other = (sectors_ued_dic[z].iloc[4:8].sum() + sectors_ued_dic[z].iloc[56]
                          + sectors_ued_dic[z].iloc[60:64].sum() + sectors_ued_dic[z].iloc[105] 
                          + sectors_ued_dic[z].iloc[109:113].sum() + sectors_ued_dic[z].iloc[154]) 
            elec_other = elec_other.to_frame().transpose()
            elec_other.rename(index={0:'Electricity (lighting, motors etc)'}, inplace=True)
            # Combine in a single dataframe
            fuels = pd.concat([coal, oil, nat_gas, biofuels, solar, dist_heat, elec_heat, elec_other])
            fuels.index.names = [z]
            ued_list.append(fuels)        
        elif z == 'NMM': 
            # Coal
            coal = sectors_ued_dic[z].iloc[[16, 24, 34, 60, 66, 79, 89, 110, 119]].sum()
            coal = coal.to_frame().transpose()
            coal.rename(index={0:'Coal'}, inplace=True)
            # Oil
            oil = (sectors_ued_dic[z].iloc[9] + sectors_ued_dic[z].iloc[17:21].sum() + sectors_ued_dic[z].iloc[25:29].sum()
                   + sectors_ued_dic[z].iloc[35:40].sum() +  sectors_ued_dic[z].iloc[52] + sectors_ued_dic[z].iloc[61:64].sum()
                   + sectors_ued_dic[z].iloc[67:72].sum() + sectors_ued_dic[z].iloc[80:84].sum() + sectors_ued_dic[z].iloc[90:93].sum()
                   + sectors_ued_dic[z].iloc[103] + sectors_ued_dic[z].iloc[111:114].sum() + sectors_ued_dic[z].iloc[120:123].sum())
            oil = oil.to_frame().transpose()
            oil.rename(index={0:'Oil'}, inplace=True)
            # Natural gas
            nat_gas = sectors_ued_dic[z].iloc[[10, 21, 29, 40, 41, 53, 64, 72, 73, 84, 93, 104, 114, 123]].sum()
            nat_gas = nat_gas.to_frame().transpose()
            nat_gas.rename(index={0:'Natural gas'}, inplace=True)
            # Biomass/biofuels
            biofuels = sectors_ued_dic[z].iloc[[22, 30, 42, 74, 85]].sum()
            biofuels = biofuels.to_frame().transpose()
            biofuels.rename(index={0:'Biomass/Biofuels'}, inplace=True)
            # Solar
            solar = sectors_ued_dic[z].iloc[[11, 54, 105]].sum()
            solar = solar.to_frame().transpose()
            solar.rename(index={0:'Solar'}, inplace=True)        
            # Distributed heat
            dist_heat = sectors_ued_dic[z].iloc[[43, 75]].sum()
            dist_heat = dist_heat.to_frame().transpose()
            dist_heat.rename(index={0:'Distributed heat'}, inplace=True)  
            # Electricity (heat)
            elec_heat = sectors_ued_dic[z].iloc[[13, 56, 76, 86, 94, 107, 115, 124]].sum()
            elec_heat = elec_heat.to_frame().transpose()
            elec_heat.rename(index={0:'Electricity (heat)'}, inplace=True)
            # Electricity (lighting, motors etc)
            elec_other = (sectors_ued_dic[z].iloc[4:8].sum() + sectors_ued_dic[z].iloc[14]
                          + sectors_ued_dic[z].iloc[32] + sectors_ued_dic[z].iloc[47:51].sum() 
                          + sectors_ued_dic[z].iloc[57] + sectors_ued_dic[z].iloc[98:102].sum()
                          + sectors_ued_dic[z].iloc[116] + sectors_ued_dic[z].iloc[125])  
            elec_other = elec_other.to_frame().transpose()
            elec_other.rename(index={0:'Electricity (lighting, motors etc)'}, inplace=True)
            # Combine in a single dataframe
            fuels = pd.concat([coal, oil, nat_gas, biofuels, solar, dist_heat, elec_heat, elec_other])
            fuels.index.names = [z]
            ued_list.append(fuels)        
        elif z == 'PPA': 
            # Coal
            coal = sectors_ued_dic[z].iloc[[17, 43, 56, 69]].sum()
            coal = coal.to_frame().transpose()
            coal.rename(index={0:'Coal'}, inplace=True)
            # Oil
            oil = (sectors_ued_dic[z].iloc[9] + sectors_ued_dic[z].iloc[18:23].sum() + sectors_ued_dic[z].iloc[36]
                   + sectors_ued_dic[z].iloc[44:49].sum() + sectors_ued_dic[z].iloc[57:62].sum()
                   + sectors_ued_dic[z].iloc[70:75].sum() + sectors_ued_dic[z].iloc[87])
            oil = oil.to_frame().transpose()
            oil.rename(index={0:'Oil'}, inplace=True)
            # Natural gas
            nat_gas = sectors_ued_dic[z].iloc[[10, 23, 24, 37, 49, 50, 62, 63, 75, 76, 88]].sum()
            nat_gas = nat_gas.to_frame().transpose()
            nat_gas.rename(index={0:'Natural gas'}, inplace=True)
            # Biomass/biofuels
            biofuels = sectors_ued_dic[z].iloc[[25, 51, 64, 77]].sum()
            biofuels = biofuels.to_frame().transpose()
            biofuels.rename(index={0:'Biomass/Biofuels'}, inplace=True)
            # Solar
            solar = sectors_ued_dic[z].iloc[[11, 38, 89]].sum()
            solar = solar.to_frame().transpose()
            solar.rename(index={0:'Solar'}, inplace=True)        
            # Distributed heat
            dist_heat = sectors_ued_dic[z].iloc[[26, 52, 65, 78]].sum()
            dist_heat = dist_heat.to_frame().transpose()
            dist_heat.rename(index={0:'Distributed heat'}, inplace=True)  
            # Electricity (heat)
            elec_heat = sectors_ued_dic[z].iloc[[13, 27, 40, 53, 66, 79, 91]].sum()
            elec_heat = elec_heat.to_frame().transpose()
            elec_heat.rename(index={0:'Electricity (heat)'}, inplace=True)
            # Electricity (lighting, motors etc)
            elec_other = (sectors_ued_dic[z].iloc[4:8].sum() + sectors_ued_dic[z].iloc[14]
                          + sectors_ued_dic[z].iloc[28] + sectors_ued_dic[z].iloc[31:35].sum() 
                          + sectors_ued_dic[z].iloc[82:86].sum() + sectors_ued_dic[z].iloc[92])  
            elec_other = elec_other.to_frame().transpose()
            elec_other.rename(index={0:'Electricity (lighting, motors etc)'}, inplace=True)
            # Combine in a single dataframe
            fuels = pd.concat([coal, oil, nat_gas, biofuels, solar, dist_heat, elec_heat, elec_other])
            fuels.index.names = [z]
            ued_list.append(fuels)
        elif z == 'FBT': 
            # Coal
            coal = sectors_ued_dic[z].iloc[[16, 25, 33, 45, 51, 67]].sum()
            coal = coal.to_frame().transpose()
            coal.rename(index={0:'Coal'}, inplace=True)
            # Oil
            oil = (sectors_ued_dic[z].iloc[9] + sectors_ued_dic[z].iloc[17:20].sum() 
                   + sectors_ued_dic[z].iloc[26:29].sum() + sectors_ued_dic[z].iloc[34:39].sum()
                   + sectors_ued_dic[z].iloc[46:49].sum() + sectors_ued_dic[z].iloc[52:57].sum()
                   + sectors_ued_dic[z].iloc[68:73].sum())
            oil = oil.to_frame().transpose()
            oil.rename(index={0:'Oil'}, inplace=True)
            # Natural gas
            nat_gas = sectors_ued_dic[z].iloc[[10, 20, 29, 39, 40, 49, 57, 58, 65, 73, 74]].sum()
            nat_gas = nat_gas.to_frame().transpose()
            nat_gas.rename(index={0:'Natural gas'}, inplace=True)
            # Biomass/biofuels
            biofuels = sectors_ued_dic[z].iloc[[41, 59, 75]].sum()
            biofuels = biofuels.to_frame().transpose()
            biofuels.rename(index={0:'Biomass/Biofuels'}, inplace=True)
            # Solar
            solar = sectors_ued_dic[z].iloc[11]
            solar = solar.to_frame().transpose()
            solar = solar.reset_index(drop=True)
            solar.rename(index={0:'Solar'}, inplace=True)        
            # Distributed heat
            dist_heat = sectors_ued_dic[z].iloc[[42, 60, 76]].sum()
            dist_heat = dist_heat.to_frame().transpose()
            dist_heat.rename(index={0:'Distributed heat'}, inplace=True)  
            # Electricity (heat)
            elec_heat = (sectors_ued_dic[z].iloc[[13, 21, 22, 30, 31]].sum()
                         + sectors_ued_dic[z].iloc[61:64].sum()
                         + sectors_ued_dic[z].iloc[77])
            elec_heat = elec_heat.to_frame().transpose()
            elec_heat.rename(index={0:'Electricity (heat)'}, inplace=True)
            # Electricity (lighting, motors etc)
            elec_other = (sectors_ued_dic[z].iloc[4:8].sum() + sectors_ued_dic[z].iloc[78])  
            elec_other = elec_other.to_frame().transpose()
            elec_other.rename(index={0:'Electricity (lighting, motors etc)'}, inplace=True)
            # Combine in a single dataframe
            fuels = pd.concat([coal, oil, nat_gas, biofuels, solar, dist_heat, elec_heat, elec_other])
            fuels.index.names = [z]
            ued_list.append(fuels) 
        elif z == 'TRE': 
            # Coal 
            coal = sectors_ued_dic[z].iloc[[16, 27, 34]].sum()
            coal = coal.to_frame().transpose()
            coal.rename(index={0:'Coal'}, inplace=True)
            # Oil
            oil = (sectors_ued_dic[z].iloc[9] + sectors_ued_dic[z].iloc[17:20].sum() 
                   + sectors_ued_dic[z].iloc[28:31].sum() + sectors_ued_dic[z].iloc[35:40].sum())
            oil = oil.to_frame().transpose()
            oil.rename(index={0:'Oil'}, inplace=True)
            # Natural gas
            nat_gas = sectors_ued_dic[z].iloc[[10, 20, 23, 31, 40, 41]].sum()
            nat_gas = nat_gas.to_frame().transpose()
            nat_gas.rename(index={0:'Natural gas'}, inplace=True)
            # Biomass/biofuels
            biofuels = sectors_ued_dic[z].iloc[42]
            biofuels = biofuels.to_frame().transpose()
            biofuels = biofuels.reset_index(drop=True)
            biofuels.rename(index={0:'Biomass/Biofuels'}, inplace=True)
            # Solar
            solar = sectors_ued_dic[z].iloc[11]
            solar = solar.to_frame().transpose()
            solar = solar.reset_index(drop=True)
            solar.rename(index={0:'Solar'}, inplace=True)        
            # Distributed heat
            dist_heat = sectors_ued_dic[z].iloc[43]
            dist_heat = dist_heat.to_frame().transpose()
            dist_heat = dist_heat.reset_index(drop=True)
            dist_heat.rename(index={0:'Distributed heat'}, inplace=True)  
            # Electricity (heat)
            elec_heat = (sectors_ued_dic[z].iloc[[13, 21, 24, 32]].sum())
            elec_heat = elec_heat.to_frame().transpose()
            elec_heat.rename(index={0:'Electricity (heat)'}, inplace=True)
            # Electricity (lighting, motors etc)
            elec_other = (sectors_ued_dic[z].iloc[4:8].sum() + sectors_ued_dic[z].iloc[44]
                          + sectors_ued_dic[z].iloc[45])  
            elec_other = elec_other.to_frame().transpose()
            elec_other.rename(index={0:'Electricity (lighting, motors etc)'}, inplace=True)
            # Combine in a single dataframe
            fuels = pd.concat([coal, oil, nat_gas, biofuels, solar, dist_heat, elec_heat, elec_other])
            fuels.index.names = [z]
            ued_list.append(fuels) 
        elif z == 'MAE': 
            # Coal 
            coal = sectors_ued_dic[z].iloc[[16, 27, 34]].sum()
            coal = coal.to_frame().transpose()
            coal.rename(index={0:'Coal'}, inplace=True)
            # Oil
            oil = (sectors_ued_dic[z].iloc[9] + sectors_ued_dic[z].iloc[17:20].sum() 
                   + sectors_ued_dic[z].iloc[28:31].sum() + sectors_ued_dic[z].iloc[35:40].sum())
            oil = oil.to_frame().transpose()
            oil.rename(index={0:'Oil'}, inplace=True)
            # Natural gas
            nat_gas = sectors_ued_dic[z].iloc[[10, 20, 23, 31, 40, 41]].sum()
            nat_gas = nat_gas.to_frame().transpose()
            nat_gas.rename(index={0:'Natural gas'}, inplace=True)
            # Biomass/biofuels
            biofuels = sectors_ued_dic[z].iloc[42]
            biofuels = biofuels.to_frame().transpose()
            biofuels = biofuels.reset_index(drop=True)
            biofuels.rename(index={0:'Biomass/Biofuels'}, inplace=True)
            # Solar
            solar = sectors_ued_dic[z].iloc[11]
            solar = solar.to_frame().transpose()
            solar = solar.reset_index(drop=True)
            solar.rename(index={0:'Solar'}, inplace=True)        
            # Distributed heat
            dist_heat = sectors_ued_dic[z].iloc[43]
            dist_heat = dist_heat.to_frame().transpose()
            dist_heat = dist_heat.reset_index(drop=True)
            dist_heat.rename(index={0:'Distributed heat'}, inplace=True)  
            # Electricity (heat)
            elec_heat = (sectors_ued_dic[z].iloc[[13, 21, 24, 32]].sum())
            elec_heat = elec_heat.to_frame().transpose()
            elec_heat.rename(index={0:'Electricity (heat)'}, inplace=True)
            # Electricity (lighting, motors etc)
            elec_other = (sectors_ued_dic[z].iloc[4:8].sum() + sectors_ued_dic[z].iloc[44]
                          + sectors_ued_dic[z].iloc[45])  
            elec_other = elec_other.to_frame().transpose()
            elec_other.rename(index={0:'Electricity (lighting, motors etc)'}, inplace=True)
            # Combine in a single dataframe
            fuels = pd.concat([coal, oil, nat_gas, biofuels, solar, dist_heat, elec_heat, elec_other])
            fuels.index.names = [z]
            ued_list.append(fuels) 
        elif z == 'TEL': 
            # Coal 
            coal = sectors_ued_dic[z].iloc[[15, 26, 39, 45]].sum()
            coal = coal.to_frame().transpose()
            coal.rename(index={0:'Coal'}, inplace=True)
            # Oil
            oil = (sectors_ued_dic[z].iloc[9] + sectors_ued_dic[z].iloc[16:21].sum() 
                   + sectors_ued_dic[z].iloc[27:32].sum() + sectors_ued_dic[z].iloc[40:43].sum()
                   + sectors_ued_dic[z].iloc[46:51].sum())
            oil = oil.to_frame().transpose()
            oil.rename(index={0:'Oil'}, inplace=True)
            # Natural gas
            nat_gas = sectors_ued_dic[z].iloc[[10, 21, 22, 32, 33, 43, 51, 52]].sum()
            nat_gas = nat_gas.to_frame().transpose()
            nat_gas.rename(index={0:'Natural gas'}, inplace=True)
            # Biomass/biofuels
            biofuels = sectors_ued_dic[z].iloc[[23, 34, 53]].sum()
            biofuels = biofuels.to_frame().transpose()
            biofuels.rename(index={0:'Biomass/Biofuels'}, inplace=True)
            # Solar
            solar = sectors_ued_dic[z].iloc[11]
            solar = solar.to_frame().transpose()
            solar = solar.reset_index(drop=True)
            solar.rename(index={0:'Solar'}, inplace=True)        
            # Distributed heat
            dist_heat = sectors_ued_dic[z].iloc[[24, 35, 54]].sum()
            dist_heat = dist_heat.to_frame().transpose()
            dist_heat.rename(index={0:'Distributed heat'}, inplace=True)  
            # Electricity (heat)
            elec_heat = (sectors_ued_dic[z].iloc[[13, 55, 56]].sum())
            elec_heat = elec_heat.to_frame().transpose()
            elec_heat.rename(index={0:'Electricity (heat)'}, inplace=True)
            # Electricity (lighting, motors etc)
            elec_other = (sectors_ued_dic[z].iloc[4:8].sum() + sectors_ued_dic[z].iloc[36]
                          + sectors_ued_dic[z].iloc[57])  
            elec_other = elec_other.to_frame().transpose()
            elec_other.rename(index={0:'Electricity (lighting, motors etc)'}, inplace=True)
            # Combine in a single dataframe
            fuels = pd.concat([coal, oil, nat_gas, biofuels, solar, dist_heat, elec_heat, elec_other])
            fuels.index.names = [z]
            ued_list.append(fuels)
        elif z == 'WWP': 
            # Coal 
            coal = sectors_ued_dic[z].iloc[[15, 28, 34]].sum()
            coal = coal.to_frame().transpose()
            coal.rename(index={0:'Coal'}, inplace=True)
            # Oil
            oil = (sectors_ued_dic[z].iloc[9] + sectors_ued_dic[z].iloc[16:21].sum() 
                   + sectors_ued_dic[z].iloc[30:32].sum() + sectors_ued_dic[z].iloc[35:40].sum())
            oil = oil.to_frame().transpose()
            oil.rename(index={0:'Oil'}, inplace=True)
            # Natural gas
            nat_gas = sectors_ued_dic[z].iloc[[10, 21, 22, 32, 40, 41]].sum()
            nat_gas = nat_gas.to_frame().transpose()
            nat_gas.rename(index={0:'Natural gas'}, inplace=True)
            # Biomass/biofuels
            biofuels = sectors_ued_dic[z].iloc[[23, 42]].sum()
            biofuels = biofuels.to_frame().transpose()
            biofuels.rename(index={0:'Biomass/Biofuels'}, inplace=True)
            # Solar
            solar = sectors_ued_dic[z].iloc[11]
            solar = solar.to_frame().transpose()
            solar = solar.reset_index(drop=True)
            solar.rename(index={0:'Solar'}, inplace=True)        
            # Distributed heat
            dist_heat = sectors_ued_dic[z].iloc[[24, 43]].sum()
            dist_heat = dist_heat.to_frame().transpose()
            dist_heat.rename(index={0:'Distributed heat'}, inplace=True)  
            # Electricity (heat)
            elec_heat = (sectors_ued_dic[z].iloc[[13, 44, 45]].sum())
            elec_heat = elec_heat.to_frame().transpose()
            elec_heat.rename(index={0:'Electricity (heat)'}, inplace=True)
            # Electricity (lighting, motors etc)
            elec_other = (sectors_ued_dic[z].iloc[4:8].sum() + sectors_ued_dic[z].iloc[25]
                          + sectors_ued_dic[z].iloc[43])  
            elec_other = elec_other.to_frame().transpose()
            elec_other.rename(index={0:'Electricity (lighting, motors etc)'}, inplace=True)
            # Combine in a single dataframe
            fuels = pd.concat([coal, oil, nat_gas, biofuels, solar, dist_heat, elec_heat, elec_other])
            fuels.index.names = [z]
            ued_list.append(fuels)         
        elif z == 'OIS': 
            # Coal 
            coal = sectors_ued_dic[z].iloc[[15, 27, 35, 41, 55]].sum()
            coal = coal.to_frame().transpose()
            coal.rename(index={0:'Coal'}, inplace=True)
            # Oil
            oil = (sectors_ued_dic[z].iloc[9] + sectors_ued_dic[z].iloc[16:21].sum() 
                   + sectors_ued_dic[z].iloc[28:31].sum() + sectors_ued_dic[z].iloc[36:39].sum()
                   + sectors_ued_dic[z].iloc[42:47].sum() + sectors_ued_dic[z].iloc[56:61].sum()
                   + sectors_ued_dic[z].iloc[66])
            oil = oil.to_frame().transpose()
            oil.rename(index={0:'Oil'}, inplace=True)
            # Natural gas
            nat_gas = sectors_ued_dic[z].iloc[[10, 21, 22, 31, 39, 47, 48, 53, 61, 62]].sum()
            nat_gas = nat_gas.to_frame().transpose()
            nat_gas.rename(index={0:'Natural gas'}, inplace=True)
            # Biomass/biofuels
            biofuels = sectors_ued_dic[z].iloc[[23, 49, 63]].sum()
            biofuels = biofuels.to_frame().transpose()
            biofuels.rename(index={0:'Biomass/Biofuels'}, inplace=True)
            # Solar
            solar = sectors_ued_dic[z].iloc[11]
            solar = solar.to_frame().transpose()
            solar = solar.reset_index(drop=True)
            solar.rename(index={0:'Solar'}, inplace=True)        
            # Distributed heat
            dist_heat = sectors_ued_dic[z].iloc[[24, 50, 64]].sum()
            dist_heat = dist_heat.to_frame().transpose()
            dist_heat.rename(index={0:'Distributed heat'}, inplace=True)  
            # Electricity (heat)
            elec_heat = (sectors_ued_dic[z].iloc[[13, 32, 51, 65]].sum())
            elec_heat = elec_heat.to_frame().transpose()
            elec_heat.rename(index={0:'Electricity (heat)'}, inplace=True)
            # Electricity (lighting, motors etc)
            elec_other = (sectors_ued_dic[z].iloc[4:8].sum() + sectors_ued_dic[z].iloc[67])  
            elec_other = elec_other.to_frame().transpose()
            elec_other.rename(index={0:'Electricity (lighting, motors etc)'}, inplace=True)
            # Combine in a single dataframe
            fuels = pd.concat([coal, oil, nat_gas, biofuels, solar, dist_heat, elec_heat, elec_other])
            fuels.index.names = [z]
            ued_list.append(fuels)   
    fuels_ued_dic = dict(zip(sectors_ued_keys, ued_list)) # Create dictionary for each sector
    #fuels_ued_df = pd.concat(ued_list, keys= sectors_ued_keys) # Create a single dataframe
    #fuels_ued_df.index.names = ['Sector', 'Fuel']
    
    # Convert ktoe to PJ and calculate energy efficiency and intensity
    ktoe_pj = 23.8845897 
    
    fec_list_pj = []
    ued_list_pj = []
    energy_efficiency_list = []
    energy_intensity_list = []
    for z in sectors_fec_keys:
        fuels_fec_pj = fuels_fec_dic[z] / ktoe_pj
        fec_list_pj.append(fuels_fec_pj)
        fuels_ued_pj = fuels_ued_dic[z] / ktoe_pj
        ued_list_pj.append(fuels_ued_pj)

    
    fuels_fec_pj_dic = dict(zip(sectors_fec_keys, fec_list_pj))
    fuels_fec_pj_df = pd.concat(fec_list_pj, keys = sectors_fec_keys) # Create a single dataframe
    fuels_fec_pj_df.index.names = ['Final Energy [PJ]', 'Fuel']
    
    fuels_ued_pj_dic = dict(zip(sectors_ued_keys, ued_list_pj))
    fuels_ued_pj_df = pd.concat(ued_list_pj, keys= sectors_ued_keys) # Create a single dataframe
    fuels_ued_pj_df.index.names = ['Useful Energy [PJ]', 'Fuel']


    return fuels_fec_pj_df, fuels_ued_pj_df
