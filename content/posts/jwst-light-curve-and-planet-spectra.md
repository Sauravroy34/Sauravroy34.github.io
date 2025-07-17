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
## Transmission Spectroscopy

When a planet transits, some starlight passes through its atmosphere. Different wavelengths of light are absorbed by atmospheric molecules, causing variations in the transit depth. Plotting these variations against wavelength produces a transmission spectrum, which reveals details about the atmosphere’s composition. For a clear explanation, watch this [video](https://www.youtube.com/watch?v=ZnLg4YFMfDQ&ab_channel=MartianColonist).

### Transmission Spectrum of WASP-39b

![Transmission Spectrum](https://github.com/user-attachments/assets/66baeb9c-f64f-4c27-a1e9-f8a0d4cc22d4)


The spectrum above shows how WASP-39b’s atmosphere affects light at different wavelengths.

## Detecting Atmospheric Composition

To determine the atmospheric composition, we use atmospheric retrieval. This involves comparing observed data to model spectra generated with known compositions. The model that best fits the data indicates the likely atmospheric makeup. For more insights, refer to this [video](https://www.youtube.com/watch?v=ZnLg4YFMfDQ&ab_channel=MartianColonist).

![Model Fit](https://github.com/user-attachments/assets/5efc277a-e584-465d-a986-0e71490eb463)

## Composition of WASP-39b’s Atmosphere

As a hot Jupiter, WASP-39b is expected to contain gases like methane and carbon dioxide. Analysis confirms the presence of water, sulfur dioxide, methane, and carbon dioxide. A distinct bump in the transmission spectrum between 4–5 µm confirms carbon dioxide.

![Molecular Contributions](https://github.com/user-attachments/assets/e8355d1c-d8f0-4439-9119-03fb3b6278e4)

## Pressure-Temperature Profile

The retrieval process assumes a [Guillot pressure-temperature profile](https://www.aanda.org/articles/aa/pdf/2010/12/aa13396-09.pdf) to model the atmosphere’s temperature structure.

![Pressure-Temperature Profile](https://github.com/user-attachments/assets/dcdc5ea5-c144-445e-8c7c-2e1c59e9e020)

## Molecular Abundance

The abundance of molecules like water, methane, carbon dioxide, and sulfur dioxide varies with atmospheric pressure, as shown below.

![Pressure vs. Abundance](https://github.com/user-attachments/assets/c709a606-6ba8-4fbd-9932-38365baae326)

The transmission spectrum highlights specific absorption features for each molecule.

![Chemical Lines](https://github.com/user-attachments/assets/af1bfc59-19cb-4ed1-849d-48ad3108ddeb)

REEFRENCES:
1) https://www.youtube.com/watch?v=ZnLg4YFMfDQ
2) https://petitradtrans.readthedocs.io/en/latest/
---

### Project Repository

You can check out the complete code and analysis on GitHub:  
👉 [JWST Light Curve and Planet Spectra](https://github.com/Sauravroy34/JWST-light-curve-and-spectral-analysis)
