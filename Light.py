rom scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt


def diff_eqs(y, t):
    '''This function contains the differential equations'''

    """Unpacking y"""
    EL222F= y[0] #free
    EL222B= y[1] #bound
    mRNA= y[2]
    P = y[3]

    """Set rate constants"""
    k1 = 1 # Light induction for EL222F to bind to promoter
    k_1= 0.5 # EL22B unbinds to form EL222F
    k2 = 3 # Transcription of EL222B to form mRNA
    k3 = 4 # Translation to form the autotransporter
    d1=  5 # Degradation of mRNA
    d2=  6 # Degradation of protein
    L=   1 #Light on then L=1; Light off hten L=0

    # this is me and I`m a rebel

    # Rate of change of EL222F
    dEL222F_dt = -(k1 * EL222F * L) + (k_1* EL222B)


    # Rate of change of EL222B
    dEL222B_dt = (k1 * EL222F) - (k_1 * EL222B)


    # Rate of change of Transcription
    dmRNA_dt = (k2*EL222B) - (d1*mRNA)

    # Rate of change of Translation to the protein
    dP_dt = (k3 * mRNA)-(d2*P)

    """Repack solution in same order as y"""
    sol = [dEL222F_dt, dEL222B_dt, dmRNA_dt, dP_dt]

    return sol

if __name__ == "__main__":
    time_steps = 1000 # Number of timepoints to simulate
    t = np.linspace(0, 800, time_steps)  # Set the timeframe (start_time, stop_time, step)

    '''Set initial species concentration values'''
    EL222F_0 =500          # Starting EL22F concentration
    EL222B_0 = 0        # Starting EL222B concentration
    mRNA_0=0            # Starting mRNA concentration
    P_0 = 0             # Starting protein concentration

    '''Pack intial conditions into an array'''
    y0 = [EL222F_0, EL222B_0, mRNA_0, P_0]

    sol = odeint(diff_eqs, y0, t)

    """plot output"""
    plt.plot(t, sol[:, 0], label='EL222F')
    plt.plot(t, sol[:, 1], label='EL222B')
    plt.plot(t, sol[:, 2], label='mRNA')
    plt.plot(t, sol[:, 3], label='P')
    plt.legend(loc=1, borderaxespad=0)
    plt.show()
