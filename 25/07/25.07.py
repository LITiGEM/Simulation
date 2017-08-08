from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt

import matplotlib.pyplot as plt

k1_rate_array = []

#k1: rate at which EL222 becomes activated with light to bind to the promoter

def light(k,L,n,K1):

    a=444.6

    # k:  Maximum expression due to induction
    # K1: Hill constant
    # n: Hill coefficient
    # a: basal expression level of the promoter
    # L: light intensity (W/m^2)

    k1 =a+((k*(L)^n)/((k)^n+(L)^n))

    k1_rate_array.append(k1)

    return k1



print k1_rate_array

EI=200 #initial concentration of EL222


def lag(x,k,n)




def diff_eqs(y, t):
    '''This function contains the differential equations'''

    """Unpacking y"""
    EI = y[0]
    EHB= y[1] #bound EL222 to the promoter
    mRNA= y[2] #transcrption
    P= y[3] #translation
    PA= y[4] #expression on surface

    """Set rate constants""" #we made these numbers up we are now looking into fixing them and adding rate equations for the k values

    k2= (666/360) #rate of transcription (nucleotides/min)
    k3= 0.001 #rate of translation (/min)
    d1= 1/5
    d2= 1/5 #Degradation of transcript (mRNA)(/min)
    d3= 1/20 #Degradation of protein (Half-life of E.coli) (/min)
    b= 0.03 #Rate of transport of the protein to the surface of the membrane

    dEI_dt =-(light_intensity * EI )

    # Rate of EL222 being activated by light and binding to the promoter
    dEHB_dt = (light_intensity * EI )-(k2* EHB)-(d1*EHB)

    # Rate of transcription
    dmRNA_dt = (k2*EHB) - (d2*mRNA)-(k3*mRNA)

    # Rate of translation
    dP_dt = (k3 * mRNA)-(d3*P)-(b*P)

    #Rate of expression of the protein
    dPA_dt= b*P

    """Repack solution in same order as y"""
    sol = [dEI_dt, dEHB_dt, dmRNA_dt, dP_dt, dPA_dt]

    return sol

if __name__ == "__main__":
    time_steps = 1000 # Number of timepoints to simulate
    t = np.linspace(0, 1200, time_steps)  # Set the timeframe (start_time, stop_time, step)

    '''Set initial species concentration values'''
    EI_0=0.00001          # Starting EL222 concentration in its inactive conformation in the cell
    EHB_0=0           # Starting concentration of EL222 bound to the promoter
    mRNA_0=0            # Starting mRNA concentration
    P_0 = 0             # Starting protein concentration
    PA_0=0              #Starting concentration of protein expressed on the surface of the

    '''Pack intial conditions into an array'''
    y0 = [EI_0, EHB_0, mRNA_0, P_0, PA_0]

    L_range = [2]

    for L in L_range:
        print(L)
        light_intensity = light(1545, L, 2, 6.554)
        sol = odeint(diff_eqs, y0, t)

        """plot output"""
        plt.plot(t, sol[:, 0], label='EI')
        plt.plot(t, sol[:, 1], label='EHB')
        plt.plot(t, sol[:, 2], label='mRNA')
        plt.plot(t, sol[:, 3], label='P')
        plt.plot(t, sol[:, 4], label='PA')
        plt.ylabel('Concentration of PA (mM)')
        plt.xlabel('Time (s)')
        plt.legend(loc=1, borderaxespad=0)

    plt.show()