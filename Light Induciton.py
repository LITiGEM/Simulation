from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt

EI=

def diff_eqs(y, t):
    '''This function contains the differential equations'''

    """Unpacking y"""
    EHB= y[0] #free
    mRNA= y[1] #bound
    P= y[2]
    PA= y[3]

    """Set rate constants""" #we made these numbers up we are now looking into fixing them and adding rate equations for the k values
    #k1 = 1 # Light induction for EL222F to bind to promoter

k1_rate_array = []

k2=0.5 # EL22B unbinds to form EL222F
k3=1  # Translation to form the autotransporter
d1=2 # Degradation of mRNA
d2=3# Degradation of protein
b= x #rate of transport of the protein to the membrane

    # this is me and I`m a rebel

    # Rate of change of EL222F
dEHB_dt = (k1 * EI ) - (k2* EHB)

    # Rate of change of Transcription
dmRNA_dt = (k2*EHB) - (d1*mRNA)-(k3*mRNA)

    # Rate of change of Translation to the protein
dP_dt = (k3 * mRNA)-(d2*P)-b

    #Rate of protein expressed on the surface of the membrane
dPA_dt= b*P

"""Repack solution in same order as y"""
sol = [dEHB_dt, dmRNA_dt, dmP_dt, dPA_dt]

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
    y0 = [EI_0, EHB_0, mRNA_0, P_0]

    sol = odeint(diff_eqs, y0, t)

    """plot output"""
    plt.plot(t, sol[:, 0], label='EL222F')
    plt.plot(t, sol[:, 1], label='EL222B')
    plt.plot(t, sol[:, 2], label='mRNA')
    plt.plot(t, sol[:, 3], label='P')
    plt.legend(loc=1, borderaxespad=0)
    plt.show()



