from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt

import matplotlib.pyplot as plt

k1_rate_array = []

#k1: Rate at which EL222 becomes activated with light to bind to the promoter

def light(k,L,n,K1):

    a=444.6 #Basal expression level of the promoter (microM)

    #k: Maximum expression due to induction (a.u.)
    #K1:Hill constant (W/m^2)
    #n: Hill coefficient
    #a: Basal expression level of the promoter (microM)
    #L: Light intensity (W/m^2)

    k1 =a+((k*(L)^n)/((k)^n+(L)^n))

    k1_rate_array.append(k1)

    return k1

print k1_rate_array

EI= 1.59*(10^(-9)) #Initial concentration of EL222 (microM/L)

def diff_eqs(y, t):
    '''This function contains the differential equations'''

    """Unpacking y"""
    EHB= y[0] #Bound EL222 to the promoter (microM/L)
    mRNA= y[1] #Transcrption (microM/L)
    P= y[2] #Translation (microM/L)
    PS= y[3] #Expression on surface (microM/L)

    """Set rate constants""" #we made these numbers up we are now looking into fixing them and adding rate equations for the k values

    k2= (60/660) #Rate of transcription per transcript (1/s)
    k3= (60/660) #Rate of translation (1/s)
    d1= 1/10 #Rate of dimer dissociation (1/s)
    d2= 1/300 #Degradation of transcript (1/s)
    d3= 1/20 #Degradation of protein (Half-life of E.coli) (1/s)

    #Rate of EL222 being activated by light and binding to the promoter
    dEHB_dt = (light_intensity * EI )-(k2* EHB)-(d1*EHB)

    #Rate of transcription
    dmRNA_dt = (k2*EHB) - (d2*mRNA)-(k3*mRNA)

    #Rate of translation
    dP_dt = (k3 * mRNA)-(d3*P)

    #Rate at which the protein is transferred to the surface of the cell

    Km = 5 * ((10)^-3) #(microM/L)
    v = 1/100 #Based on the rate at which mRNA is transferred from within the nucleus of a mammalian cell to its cytoplasm (1/s)
    n=1-(P/2) #Dimensionless 
    b = (P / (P + Km)) * n * v #Rate at which the protein is transferred to the surface of the cell

    #Rate of expression of the protein
    dPS_dt= b*P

    """Repack solution in same order as y"""
    sol = [dEHB_dt, dmRNA_dt, dP_dt, dPS_dt]

    return sol

if __name__ == "__main__":
    time_steps = 1000 #Number of timepoints to simulate
    t = np.linspace(0, 5000, time_steps)  #Set the time frame (start_time, stop_time, step)

    '''Set initial species concentration values'''
    EHB_0=0           #Starting concentration of EL222 bound to the promoter (microM/L)
    mRNA_0=0          #Starting mRNA concentration (microM/L)
    P_0 = 0           #Starting protein concentration (microM/L)
    PS_0=0            #Starting concentration of protein expressed on the surface of the cell (microM/L)

    '''Pack intial conditions into an array'''
    y0 = [EHB_0, mRNA_0, P_0, PS_0]

    L_range = [2]

    for L in L_range:
        print(L)
        light_intensity = light(1545, L, 2, 6.554)
        sol = odeint(diff_eqs, y0, t)

        """plot output"""
        plt.plot(t, sol[:, 0], label='EHB')
        plt.plot(t, sol[:, 1], label='mRNA')
        plt.plot(t, sol[:, 2], label='P')
        plt.plot(t, sol[:, 3], label='PS')
        plt.ylabel('Concentration of PS (microM)')
        plt.xlabel('Time (min)')
        plt.legend(loc=1, borderaxespad=0)

    plt.show()