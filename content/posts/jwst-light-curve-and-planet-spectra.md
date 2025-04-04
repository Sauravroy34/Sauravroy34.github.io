+++
title = "JWST Light Curve and Planet Spectra"  
date = 2025-04-05T00:32:11+05:30  
description = "Details about my project on JWST exoplanet spectra and light curve"  
+++

### WASP-39b Light Curve and Planet Spectra

Recently, I worked on a cool project where I plotted the light curve of the star **WASP-39**, during which its exoplanet — the hot Jupiter **WASP-39b** — was also observed. According to [NASA's exoplanet archive](https://exoplanetarchive.ipac.caltech.edu/overview/WASP-39#planet_WASP-39-b_collapsible), WASP-39b has about **0.28 times the mass of Jupiter** and a **radius 1.27 times that of Jupiter** (~91,000 km).  

It's a hot gas giant with a scorching temperature of around **900 °C**. The planet orbits very close to its host star (about **7 million km away**) and completes one orbit in just **4 days**.  

WASP-39b was the **first exoplanet discovered to contain carbon dioxide in its atmosphere**, and sulfur dioxide was also detected. It lies in the **Virgo** constellation and is about **700 light-years away** from Earth. As part of the NameExoWorlds campaign for the IAU’s 100th anniversary, the planet was officially named **Bocaprins**, after *Boca Prins* beach in Aruba’s Arikok National Park. The star it orbits is **WASP-39**.

---

### What Is a Light Curve?

In simple terms, a **light curve** is a plot of incoming light (photon counts or flux) versus time. It shows how the brightness of a star changes over a period (called exposure time). Telescopes observe these light curves by continuously watching a star.  

One fascinating use of light curves is to detect exoplanets. When a planet passes in front of its star (a transit), it causes a small dip in the light curve — and that’s how astronomers discover new worlds!  
Learn more about this method [here](https://en.wikipedia.org/wiki/Methods_of_detecting_exoplanets#Transit_photometry).

---

### What Are Planet Spectra?

When telescopes use [CCD detectors](https://noirlab.edu/public/blog/50-years-ccds/), they can measure not just when photons arrive, but also their **energy** and **count**. Using this information, we can create a **spectrum** of the planet — which is basically a plot of photon flux (or counts) vs **wavelength**.  

This tells us what elements or molecules are present in the planet’s atmosphere. Want to go deeper? Check out [this article on planetary spectroscopy](https://oxfordre.com/planetaryscience/display/10.1093/acrefore/9780190647926.001.0001/acrefore-9780190647926-e-134).

---

### Datasets and Project Implementation

The dataset for this project came from the **James Webb Space Telescope (JWST)** using its **NIRSpec instrument**, specifically in **Bright Object Time-Series (BOTS)** mode. For more details, visit the [official JWST documentation](https://jwst-docs.stsci.edu/jwst-near-infrared-spectrograph/nirspec-observing-modes/nirspec-bright-object-time-series-spectroscopy#gsc.tab=0).

The data was downloaded from the [MAST Portal](https://mast.stsci.edu/portal/Mashup/Clients/Mast/Portal.html) and came in **FITS format**, which is the standard for astronomy data.

The project was done entirely in a **Jupyter Notebook**, and here are some of the interesting visualizations I generated:

#### Light Curve and Poisson Regression Fit
![Light Curve Plot](https://github.com/user-attachments/assets/98ce41e7-a80d-44f8-8ad1-bdd080a7919d)

#### Planet Spectra
![Spectra Plot](https://github.com/user-attachments/assets/65e4a4b8-f115-4596-854e-055960f8cc59)

---

### Project Repository

You can check out the complete code and analysis on GitHub:  
👉 [JWST Light Curve and Planet Spectra](https://github.com/Sauravroy34/JWST-light-curve-and-spectral-analysis)
