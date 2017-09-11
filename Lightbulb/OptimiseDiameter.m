qsm= 1.25 *10^-4; % mol(s)*mol(X)^-1s^-1
Cx=1;% mol*m^3
Iph0=0.0005; % mol/m^2*s^-1
d=0.03; % m
d=0.3:0.05:0.5; % m
for i=1:size(d, 2)
[qs_av(i),Ysph_av(i)]=bulbST(Iph0,d(i),Cx);
end
[hex2,hl1,hl2]=plotyy(d, qs_av, d, Ysph_av)
xlabel('Reactor Dimensions (d) [m]')
title('Figure 2: Sugar Production as a function of reactor dimensions')
ylabel(hex2(1),'qs_a_v[mol_smol_X^-^1s^-^1]')
ylabel(hex2(2),'Y_s_/_p_h[mol_smol_p_h^-^1]')
hl1.LineWidth=2.5;
hl2.LineWidth=2.5;