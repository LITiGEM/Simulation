# LIT Simulations

This repository contains all the modelling code of the UCL 2017 IGEM team.

## File description

The UCL iGEM 2017 team spent its summer developing a range of models that simulate and optimize parameters that affect cellular mechanisms in different areas of light induced technologies (LIT).
Four models were developed by the team. The codes contained in this file have been created using the programming languages Python and MATLAB.
This file contains the following models:

LIT Barchitecture Model

Optimization of rate kinetics for the expression of a surface protein (intimin).
The construct is induced with blue light (450 nm), the effect of light induction is tested in 2 ways: light intensity used and light pulsing.
- 10minplse.py
- india.py
- Intensity intimin expression.py
- Pulsing.py
- Rate kinetics.py
- Sensitivity Analysis.py

Game of LIT

Variation of Conway’s Game of Life
Visual representation of the cell adhesion; where the two binding partners SpyTag and SpyCatcher bind to each other.
- GameOfLit.m
- LOGO.m
- run_GameOfLit.m
- run_LOGO.m

LIT Tissue Regeneration Model

Optimization of rate kinetics for the photoactivation of the dCAS9 – p65 construct. The system is induced by the photo cleaving of the linker PhoCl with violet light.
- mammalian light intensity.py
- mammalian rate kinetics.py

LIT bulb Model

This model optimizes the dimensions of the LIT bulb. Parameters were optimized to allow for the highest rate of sugar production within the light bulb, as this would maximise the amount of luminescence emitted from the bulb. The following parameters are optimized: diameter of the LIT bulb, incoming Photon Flux Density and biomass concentration of cyanobacteria. 
- bulbST.m
- Cyano.mat
- OptimiseCx.m
- OptimiseDiameter.m
- OptimiseIph0.m
- PAR_Norm.mat

LIT UCL iGEM would like to thank Dr Christopher Barnes (UCL, Department of Cell & Developmental Biology), Dr Alexandros Kiparissides (UCL, Department of Biochemical Engineering), Behzad Karkaria (PhD student, UCL, Department of Cell & Developmental Biology), and Maximilien Rothier Bautzer (MRes, UCL, Department of Biochemical Engineering) for the support and assistance they gave to the modelling team throughout the summer.  

