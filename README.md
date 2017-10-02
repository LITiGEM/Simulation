 
#LIT simulation
This repository contains all the modelling code of the UCL 2017 iGEM team
##File Description
The UCL iGEM 2017 team developed a range of models that simulate and optimize parameters that affect cellular mechanisms in different areas of light induced technologies (LIT). All the work will be presented in November 2017 at the international Jamboree in Boston. 
Four models were developed by the team. The codes contained in this file have been created using the programming languages Python and MATLAB.
This file contains the following models:
LIT Barchitecture Model (LEGIT Model) 
Optimization of rate kinetics for the expression of a surface protein (intimin).
The construct is induced with blue light (450 nm), the effect of light induction is tested in 2 ways: light intensity used and light pulsing. This directory includes parameter optimisation (i.e. Sensitivity Analysis and Parameter Sampling) as well as a cost analysis. 
- 10minplse.py
- india.py
- Intensity intimin expression.py
- Pulsing.py
- Rate kinetics.py
- Sensitivity Analysis.py

Game of LIT Model (GOLIT Model) 
Variation of Conway’s Game of Life
Visual representation of the cell adhesion; where the two binding partners SpyTag and SpyCatcher bind to each other. Implementation of genetic algorithm to determine the optimal starting condition before running the game. 
- GameOfLit.m
- LOGO.m
- run_GameOfLit.m
- run_LOGO.m
- LIT.py

LIT Mammalian Cells Model (LAME Model) 
Optimization of rate kinetics for the photoactivation of the dCAS9 – p65 construct. The system is induced by the photo cleaving of the linker PhoCl with violet light. 
- 2hourpulses.py
- Costing_BestLightIntensities.py
- Costing_Optimized.py
- Costing_Pulsing.py
- mammalian light intensity.py
- mammalian rate kinetics.py
- Optimised conditions.py
- ParamSamp_Degradation.py
- ParamSamp_Translocation.py
- Pulsing.py
- Sensitivity_Degradation.py
- Sensitivity_Translocation.py


LIT bulb Model  (OptoFlux Model) 
This model optimizes the dimensions of the LIT bulb. Parameters were optimized to allow for the highest rate of sugar production within the light bulb, as this would maximise the amount of luminescence emitted from the bulb. The following parameters are optimized: diameter of the LIT bulb, incoming Photon Flux Density and biomass concentration of cyanobacteria. 
- bulbST.m
- Cyano.mat
- OptimiseCx.m
- OptimiseDiameter.m
- OptimiseIph0.m
- PAR_Norm.mat


LIT UCL iGEM would like to thank Dr Christopher Barnes (UCL, Department of Cell & Developmental Biology), Dr Darren Nesbeth (UCL, Department of Biochemical Engineering) Dr Alexandros Kiparissides (UCL, Department of Biochemical Engineering), Behzad Karkaria (PhD student, UCL, Department of Cell & Developmental Biology), and Maximilien Rothier Bautzer (MRes, UCL, Department of Biochemical Engineering) for the support and assistance they gave to the modelling team throughout the summer.  

