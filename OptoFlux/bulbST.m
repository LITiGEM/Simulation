%source of equations:Janssen M. Microalgal Photosynthesis and Growth in Mass Culture. Photobioreaction Engineering. 2016;:185-256.
function[qs_av,Ysph_av]=bulbST(Iph0,d,Cx);
AF = 5;              % dimensionless (accumulation factor)
qsm = 2.7;           % mol(s)*mol(X)^-1*s^-1
Ysphm = 0.10;        % dimensionless (Yield)
ms = 3*10^-6;        % mol(s)*mol(X)^-1*s^-1
Yxs = 0.65;          % mol(s)*mol(X)^-1
Mx = 24;             % gDCW*mol(X)^-1
Vr = 0.000075;       % m^3
% Cx = 1;            % mol/m^3
% Iph0=0.5*10^-3
% d=0.03
% In how many "slices" do you want to split your lightbulb in order to study how light intensity changes throughout the 
numzones = 500;
% Load the characteristics of the Light source and algae considered 
% In this case you need to load your data for the corresponding EnL values
% for your cells and the PAR norm light spectrum you are evaluating 
% axL: Absorption coefficient per nm
load('PAR_Norm');
load('Cyano');
% Name the parameters you added as 'EnL' and 'Cyano' 
EnL = PAR_Norm;
axL = Cyano;
% Compute the Sugar Production rate in the chloroplast % Incoming photon flux per nm
Iphl0 = Iph0*EnL(:,2);
% Initialize the iterative procedure
z = 0;
zstep = d/numzones; 
for i=1:numzones
IphlzF(:,1) = Iphl0.*exp(-axL(:,2).*Cx.*(z+zstep/2).*AF); 
IphlzB(:,1) = Iphl0.*exp(-axL(:,2).*Cx.*(z-zstep/2).*AF); 
Iphlz(:,1) = (IphlzF + IphlzB)/2;
% Evaluate the sums over all wavelengths
IphzF(i,1) = sum(IphlzF);
IphzB(i,1) = sum(IphlzB);
Iphz(i,1) = sum(Iphlz);
% Calculate the specific photon uptake rate 
qphz(i,1) = -(IphzF(i,1) - IphzB(i,1))/(Cx*zstep);
% Calculate the sugar production rate for each zone 
qs(i,1) = qsm * tanh(Ysphm*qphz(i)/qsm);
% Yield of sugar on photons
z = z + zstep;
Y= qs(i,1)./Iphz;
Ysph(i)=(qs(i)/qphz(i));
end
qs_av = mean(qs);
Ysph_av = mean(Ysph);
end