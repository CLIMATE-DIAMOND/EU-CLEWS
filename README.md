# EU-CLEWS
This repository contains the EU-CLEWs model development work carried out under the Horizon-DIAMOND project. At the moment, it is a private repository. We can make it public when needed after adding the necessary licenses.



# Land-Water Modules

I've just uplodaed the a template of the Land-Water Modules (aggragated EU model) for use with Otoole
Currenlty only Technologies and Fuels have been added (and there input-output relationship) 
Soem uncertainites with the model structure:

- Do we need a potential for crop land land technology if we already have specific crop land technologies? (currently exlcuded from the template)
- which crops for biofuel? (we currently have technologies for both biodiesal and bioethanal) 
- I have excluded the technology and realted fuels 'land for protected tree cover' for now 
- please check if Seawater techs and fuels are coherent in the technology list/ Reference diagram - see docs in the diamond shared drive

I have also uploaded a couple of python scripts to aid populating the template quicker 

# GAEZ

I have successfully extracted GAEZ data via the steps outlined on the OSeMOSYS/CLEWs_GAEZ directory on github
My test case was Germany (national boundary only/ RCP 4.5)- see the summery data under the GAEZ folder here. ALthough haven't quite got to grips with the data produced, it's there for us to experiment with. It takes about 40mins (my laptop) to complete the script to extract the data.

I suggest we divide the countries up between us and do it that way.....
Also - I think it would take a lot of work to adapt the script to do the whole the EU......which is needed for the aggragaetd model?




