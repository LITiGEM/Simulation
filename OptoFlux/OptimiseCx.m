%source of equations:Janssen M. Microalgal Photosynthesis and Growth in Mass Culture. Photobioreaction Engineering. 2016;:185-256.
qsm= 1.25 *10^-4; %mol(s)*mol(X)^-1s^-1
Iph0=0.5*10^-3; %mol(ph)*m^-2*s^-1
d=0.03;
Cx = 50; %mol/m^3
Cx = 50:50:800;
for i=1:size(Cx, 2)
[qs_av(i),Ysph_av(i)]=whitechlorellaST(Iph0,d,Cx(i));
end
[hex2,hl1,hl2]=plotyy(Cx, qs_av, Cx, Ysph_av)
xlabel('Biomass Concentration (Cx) [mol*m^3]')
%title('Sugar Production as a function of Biomass Concentration-WhiteLED, Chlamy')
ylabel(hex2(1),'qs_a_v[mol_smol_X^-^1s^-^1]')
ylabel(hex2(2),'Y_s_/_p_h[mol_smol_p_h^-^1]')
hl1.LineWidth=2.5;
hl2.LineWidth=2.5;