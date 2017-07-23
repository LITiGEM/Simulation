from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt

import matplotlib.pyplot as plt

k1_rate_array = []


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

for L in range (0,15):
    light_intensity = light( 1545, L, 2, 6.554)

print k1_rate_array

EI=200 #initial concentration of EL222

def diff_eqs(y, t):
    '''This function contains the differential equations'''

    """Unpacking y"""
EHB= y[0] #bound EL222 to the promoter
mRNA= y[1] #transcrption
P= y[2] #translation
PA= y[3] #expression on surface

"""Set rate constants""" #we made these numbers up we are now looking into fixing them and adding rate equations for the k values

k2=0.5 # EL22B unbinds to form EL222F
k3=1  # Translation to form the autotransporter
d1=2 # Degradation of mRNA
d2=3 # Degradation of protein
b=4 # Rate of transport of the protein to the membrane

    # Rate of EL222 being activated by light and binding to the promoter
dEHB_dt = (light_intensity * EI ) - (k2* EHB)

    # Rate of transcription
dmRNA_dt = (k2*EHB) - (d1*mRNA)-(k3*mRNA)

    # Rate of translation
dP_dt = (k3 * mRNA)-(d2*P)-b

    #Rate of expression of the protie
dPA_dt= b*P

"""Repack solution in same order as y"""
sol = [dEHB_dt, dmRNA_dt, dP_dt, dPA_dt]

return sol

if __name__ == "__main__":
    time_steps = 1000 # Number of timepoints to simulate
    t = np.linspace(0, 800, time_steps)  # Set the timeframe (start_time, stop_time, step)

    '''Set initial species concentration values'''
    EI_0=500          # Starting EL222 concentration in its inactive conformation
    EHB_0=0           # Starting concentration of EL222
    mRNA_0=0            # Starting mRNA concentration
    P_0 = 0             # Starting protein concentration
    PA_0=0              #Starting protein expressed on the surface of the

    '''Pack intial conditions into an array'''
    y0 = [EHB_0, mRNA_0, P_0, PA_0]

    sol = odeint(diff_eqs, y0, t)

    """plot output"""
    plt.plot(t, sol[:, 0], label='EHB')
    plt.plot(t, sol[:, 1], label='mRNA')
    plt.plot(t, sol[:, 2], label='P')
    plt.plot(t, sol[:, 3], label='PA')
    plt.legend(loc=1, borderaxespad=0)
    plt.show()



