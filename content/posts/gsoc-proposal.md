+++
title = 'GSoC Proposal'
date = 2025-04-05T12:40:00+05:30
description = 'My GSoC journey'
+++

It's been around 8 months since I discovered the Stingray project. My first pull request to the Stingray software involved implementing [pre-commit hooks](https://github.com/StingraySoftware/stingray/pull/847), which was merged on September 30, 2024. Since then, I’ve found this package fascinating and have contributed a few more PRs.

Before this, I didn’t know about Stingray or even the role of Python in astronomy. To be honest, learning how the package works was overwhelming at first, but the journey has been incredibly rewarding. Here's what I’ve learned so far:

- The physics of black holes and X-ray binaries  
- How light curves and power spectra are used in analysis  
- Various statistical and signal processing methods like correlation and Fourier transforms  
- Different states of black holes and the radio jets they emit during transitions from soft to hard states (and vice versa)  
- Tools used in astronomy like HEASOFT  
- How CCDs in telescopes work, and much more  

I’m proud that I was able to learn all of this while still pursuing my B.Tech!

### GSoC Project

The project I'm interested in is [Interactive Database for X-ray Binary Observations](https://openastronomy.org/gsoc/gsoc2025/#/projects?project=interactive_database_for_x-ray_observations), a 350-hour GSoC project. The goal is to build a catalog of black hole binaries where users can track their evolution using a [Hardness-Intensity Diagram (HID)](https://www.researchgate.net/figure/The-hardness-intensity-diagram-showing-the-added-information-gained-when-including-the_fig1_230595369#:~:text=The%20hardness%2Dintensity%20diagram%20showing%20the%20added%20information%20gained%20when,and%20darker%20to%20lower%20flux.)—a plot showing photon intensity and the ratio of counts across specific energy bands (e.g., [2–4 keV]/[4–12 keV]).

The database would include Fourier and timing products like light curves, power spectra, and energy spectra for each observation. Currently, most analyses focus on individual observations, which is useful for estimating spin and mass, but this project aims to provide a complete overview of a black hole's evolution over time.

### My Proposal

After two months of trial and error—learning, exploring, and refining—the proposal is finally ready! This is my first time writing such a detailed technical document. I plan to submit it soon, as the deadline is April 8, 2025.

Fingers crossed! Let's hope for the best! 🙌
