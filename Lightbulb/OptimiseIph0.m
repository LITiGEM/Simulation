qsm= 1.25 *10^-4; % mol(s)*mol(X)^-1s^-1
Cx=1; % mol*m^3
d=0.03;
%Iph0 = 0.0005; % mol/m^2*s^-1
Iph0 = 0.0005:0.0005:0.008;
for i=1:size(Iph0, 2)
[qs_av(i),Ysph_av(i)]=bulbST(Iph0(i),d,Cx);
end
[hex2,hl1,hl2]=plotyy(Iph0, qs_av, Iph0, Ysph_av);
xlabel('Incoming Photon Flux Density (I_p_h) [mol_p_hm^-^2s^-^1]')
title('Sugar Production as a function of Light Intensity')
ylabel(hex2(1),'qs_a_v[mol_smol_X^-^1s^-^1]')
ylabel(hex2(2),'Y_s_/_p_h[mol_smol_p_h^-^1]')
hl1.LineWidth=2.5;
hl2.LineWidth=2.5;