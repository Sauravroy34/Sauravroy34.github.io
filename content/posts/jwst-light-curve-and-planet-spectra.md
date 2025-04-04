+++
title = 'Jwst Light Curve and Planet Spectra'
date = 2025-04-05T00:32:11+05:30
desciption = 'Details about my project jwst planet spectra and light curve'
+++

### Wasp-39b light curve and planet spectra
Recenly i made a cool project where i plot the light curve of star WASP-39 where its exoplanet hot jupyter was also witnessed As per nasa data [wasp-39b](https://exoplanetarchive.ipac.caltech.edu/overview/WASP-39#planet_WASP-39-b_collapsible)!  WASP-39b has a mass of about 0.28 times that of Jupiter and a radius about 1.27 times that of Jupiter (91,000 km) It is a hot gas giant planet with a high temperature of 900 °C. The exoplanet orbits very close (7 million km) to WASP-39, its host star, every 4 days. In addition WASP-39b was the first exoplanet found to contain carbon dioxide in its atmosphere,and likewise for sulfur dioxide.WASP-39b is in the constellation Virgo, and is about 700 light-years from Earth. As part of the NameExoWorlds campaigns at the 100th anniversary of the IAU, the planet was named Bocaprins, after the beach Boca Prins in the Arikok National Park of Aruba.The star which this planet is orbiting around is WASP-39 

### Now what is light curve ?
I wont go into details but light curve are a plot of incoming photons count or flux vs time so basically its a plot which shows how much light is coming for given period(which is called exposure) it is observed by a telescope which stares a star one of the cool things about light curves are that one can find and discover exoplanet check this out for more detail [Transit-photometry](https://en.wikipedia.org/wiki/Methods_of_detecting_exoplanets#Transit_photometry)!

### What are planet spectra ?
Telescope which uses [CCD](https://noirlab.edu/public/blog/50-years-ccds/)! provides the ability to user to know the photons arrival time, its energy and counts too through this knowledge one can easily plot the planet spectra which is nothing but plot of flux or photon counts vs the wavelength band [Planet Spectroscopy](https://oxfordre.com/planetaryscience/display/10.1093/acrefore/9780190647926.001.0001/acrefore-9780190647926-e-134)!

### Datasets and project implementation
Datasets was gathered from James webb telescope NIRSpec instrument which was in BOTS mode for more detail check this out [NIRSpec-Bright-Object-Time-Series-Spectroscopy](https://jwst-docs.stsci.edu/jwst-near-infrared-spectrograph/nirspec-observing-modes/nirspec-bright-object-time-series-spectroscopy#gsc.tab=0)! dataset was download from [MAST](https://mast.stsci.edu/portal/Mashup/Clients/Mast/Portal.html)! portal and all the files were in [fits](https://en.wikipedia.org/wiki/FITS)! format which is the most popular in astronomy 

project is made in jupyter notebook and here are some of the intresting plots
#### Light curve and poission regression fit
![Screenshot from 2025-04-05 00-58-57](https://github.com/user-attachments/assets/98ce41e7-a80d-44f8-8ad1-bdd080a7919d)

#### Planet spectra
![Screenshot from 2025-04-05 00-59-26](https://github.com/user-attachments/assets/65e4a4b8-f115-4596-854e-055960f8cc59)

### finally the project repo link 
The project can be found in my github repo [JWST-light-curve-and-Planet-spectra](https://github.com/Sauravroy34/JWST-light-curve-and-spectral-analysis)!
