+++
title = 'Setting Up HEASOFT'
date = 2025-04-05T18:37:50+05:30
description = 'Pain in setting up HEASOFT on my computer'
+++

### Setting Up HEASOFT: A Frustrating but Rewarding Experience

First of all, I had no idea that setting up HEASOFT would be *so* painful. The official documentation didn’t help much, and I needed HEASOFT for my GSoC project with Stingray, where it’s used for Level 1 data processing.

### What is HEASOFT?

HEASoft (High Energy Astrophysics Software) is a unified package that includes:

- **FTOOLS**: Tools to manipulate FITS files, both general-purpose and mission-specific.
- **XANADU**: A set of high-level, multi-mission tasks for analyzing X-ray spectral, timing, and imaging data.

and lot more !!!
It bundles everything you need to work with X-ray astronomical data. You can download either the source code or precompiled executables depending on your system. It even has a web-based interface called [sciserver](https://heasarc.gsfc.nasa.gov/docs/sciserver/)!.

### How I Finally Got HEASOFT to Work

The official documentation didn’t really help me much, so I had to hunt around online. Thankfully, I found an amazing YouTube channel: [Nick Space Cowboy](https://www.youtube.com/@nspace-cowboy)! He has a complete, step-by-step guide on installing HEASOFT, and following it made the process *so* much easier.

It took about an hour to fully install everything, and to my surprise, he also had tutorials on analyzing NICER data, which is super helpful for my project.

So far, I’ve managed to:

- Set up HEASOFT successfully
- Configure the NICER CALDB (Calibration Database)
- Add geomagnetic files required for preprocessing

If you're struggling like I was, I *highly* recommend checking out Nick’s channel. It might save you hours of frustration.


