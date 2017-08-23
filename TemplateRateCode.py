#This is a program we developed to allow future iGEM teams to easily model the transfer of proteins to the surface of cells

from __future__ import division
from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt

#Here the rate at which our Transcription takes place is light dependant, therefore the rate at which our transcription factor is transferred to the promoter
#of the plasmid is a function of light

k1_rate_array = []

# k1: Rate at which EL222 becomes activated with light to bind to the promoter

def light(k, L, n, K1):
    a = # Basal expression level of the promoter (microM)

    # k: Maximum expression due to induction (a.u.)
    # K1:Hill constant (W/m^2)
    # n: Hill coefficient
    # a: Basal expression level of the promoter (microM)
    # L: Light intensity (W)

    k1 = a + ((k * (L) ^ n) / ((k) ^ n + (L) ^ n))

    k1_rate_array.append(k1)

    return k1


print (k1_rate_array)


def diff_eqs(y, t):
    '''This function contains the differential equations'''

    """Unpacking y"""
    B = y[0]  # Bound EL222 to the promoter (microM/L)
    mRNA = y[1]  # Transcrption (microM/L)
    P = y[2]  # Translation (microM/L)
    S = y[3]  # Expression on surface (microM/L)

    """Set rate constants"""  # we made these numbers up we are now looking into fixing them and adding rate equations for the k values

    k2 = # Rate of transcription per transcript (1/s)
    k3 = # Rate of translation (1/hr)
    d1 = # Degradation of transcript (1/hr)
    d2 = # Degradation of protein (Half-life of E.coli) (1/hr)

    # Rate of EL222 being activated by light and binding to the promoter
    dB_dt = (light_intensity * (I) ** 2) - (k2 * B)

    # Rate of transcription
    dmRNA_dt = (k2 * B) - (d1 * mRNA) - (k3 * mRNA)

    # Rate at which the protein is transferred to the surface of the cell
    Km =  # (microM/L)
    v =  # Based on the rate at which mRNA is transferred from within the nucleus of a mammalian cell to its cytoplasm (1/hr)
    n = 1 - (S / ())  # Representing the space available for more proteins on the surface of the cell in the form of a ratio (Dimensionless)
    b = (P / (P + Km)) * n * v  # Rate at which the protein is transferred to the surface of the cell (1/s)

    # Rate of translation
    dP_dt = (k3 * mRNA) - (d2 * P) - (b * P)

    # Rate of expression of the protein
    dS_dt = (b * P)

    """Repack solution in same order as y"""
    sol = [dB_dt, dmRNA_dt, dP_dt, dS_dt]

    return sol

if __name__ == "__main__":
    time_steps = 100000  # Number of timepoints to simulate
    t = np.linspace(0, 200, time_steps)  # Set the time frame (start_time, stop_time, step)

    '''Set initial species concentration values'''
    I = # Initial concentration of EL222 (microM/L)
    B_0 = # Starting concentration of EL222 bound to the promoter (microM/L)
    mRNA_0 = # Starting mRNA concentration (microM/L)
    P_0 = # Starting protein concentration (microM/L)
    S_0 = # Starting concentration of protein expressed on the surface of the cell (microM/L)

    '''Pack intial conditions into an array'''
    y0 = [B_0, mRNA_0, P_0, S_0]


#Here we are defining the light intensity of the light hitting our cells
    L_range = []

    for L in L_range:
        print(L)
        light_intensity = light(1545, L, 2, 6.554)
        sol = odeint(diff_eqs, y0, t)

        """plot output"""
        asfont = {'fontname': 'Arial'}
        hfont = {'fontname': 'Helvetica'}

        plt.plot(t, sol[:, 0])
        plt.plot(t, sol[:, 1])
        plt.plot(t, sol[:, 2])
        plt.plot(t, sol[:, 3])
        plt.legend(['EL222 bound to promoter', 'mRNA', 'Translated protein', 'Surface-expressed protein', ], loc='lower right')


        #plt.title('Figure 1: Rate kinetics of cellular mechanisms with a light intensity of 14 W/$m^2$',**asfont)
        plt.ylabel('Concentration (uM)', **asfont)
        plt.xlabel('Time (hr)', **asfont)
        plt.legend(loc=1, borderaxespad=0)
        plt.title('Figure 1: Rate kinetics of cellular mechanisms induced with a light intensity of 14 W/$m^2$',
                  fontsize=10, y=1.08)
        plt.ticklabel_format(style='sci', axis='Y', scilimits=(0, 0))

    plt.show()