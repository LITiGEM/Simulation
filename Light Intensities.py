from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt

# k1: Rate at which EL222 becomes activated with light to bind to the promoter
# Here we create express k1 in terms of a function of light intensity

k1_rate_array = []
#The array was created to add the values of k1 as different light intensities are examined

def light(k, L, n, K1):
    a = 444.6  # Basal expression level of the promoter (microM)

    # k: Maximum expression due to induction (a.u.)
    # K1:Hill constant (W/m^2)
    # n: Hill coefficient
    # a: Basal expression level of the promoter (microM)
    # L: Light intensity (W)

    k1 = a + ((k * (L) ^ n) / ((k) ^ n + (L) ^ n))

    k1_rate_array.append(k1)

    return k1

def diff_eqs(y, t):
    '''This function contains the differential equations'''

    """Unpacking y"""
    B = y[0]  # Bound EL222 to the promoter (microM/L)
    mRNA = y[1]  # Transcrption (microM/L)
    P = y[2]  # Translation (microM/L)
    S = y[3]  # Expression on surface (microM/L)

    """Set rate constants"""  # we made these numbers up we are now looking into fixing them and adding rate equations for the k values

    k2 = (108/25)  # Rate of transcription per transcript (1/hr)
    k3 = (3600 / 660)  # Rate of translation (1/hr)
    d1 = 60 / 300  # Degradation of transcript (1/hr)
    d2 = 60 / 20  # Degradation of protein (Half-life of E.coli) (1/hr)

    # Rate of EL222 being activated by light and binding to the promoter
    dB_dt = (light_intensity * (T) ** 2) - (k2 * B)

    # Rate of transcription
    dmRNA_dt = (k2 * B) - (d1 * mRNA) - (k3 * mRNA)

    # Rate at which the protein is transferred to the surface of the cell
    Km = 5  # (microM/L)
    v = 115200/ 10  # Based on the rate at which mRNA is transferred from within the nucleus of a mammalian cell to its cytoplasm (1/hr)
    n = 1 - (S / (6.48 * 10 ** -6))  # Representing the space available for more proteins on the surface of the cell in the form of a ratio (Dimensionless)
    b = (P / (P + Km)) * n * v  # Rate at which the protein is transferred to the surface of the cell (1/s)

    # Rate of translation
    dP_dt = (k3 * mRNA) - (d2 * P) - (b * P)

    # Rate of expression of the protein
    dS_dt = (b * P)

    """Repack solution in same order as y"""
    sol = [dB_dt, dmRNA_dt, dP_dt, dS_dt]

    return sol

if __name__ == "__main__":
    time_steps = 1000  # Number of timepoints to simulate
    t = np.linspace(0, 200, time_steps)  # Set the time frame (start_time, stop_time, step) time frames are equally spaced within the two limits

    '''Set initial species concentration values'''
    T = 2.37 * (10 ** -4)  # Initial concentration of EL222 (microM/L)
    B_0 = 0  # Starting concentration of EL222 bound to the promoter (microM/L)
    mRNA_0 = 0  # Starting mRNA concentration (microM/L)
    P_0 = 0  # Starting protein concentration (microM/L)
    S_0 = 0  # Starting concentration of protein expressed on the surface of the cell (microM/L)

    '''Pack intial conditions into an array'''
    y0 = [B_0, mRNA_0, P_0, S_0]

    L_range = [0,2,8,14]
    # These are the range of light intensities who's effect was evaluated on the rate of 'k1'

    for L in L_range:
        print(L)
        light_intensity = light(1545, L, 2, 6.554)
        #print(light_intensity)
        sol = odeint(diff_eqs, y0, t)

        """plot output"""
        asfont = {'fontname': 'Arial'}
        hfont = {'fontname': 'Helvetica'}

        #plt.plot(t, sol[:, 0])
        #plt.plot(t, sol[:, 1])
        #plt.plot(t, sol[:, 2])
        plt.plot(t, sol[:, 3])
        #plt.legend(['EL222 bound to promoter', 'mRNA', 'Translated protein', 'Surface-expressed protein',], bbox_to_anchor=(1, 0.5))

        plt.legend(['0 W/$m^2$', '2 W/$m^2$', '8 W/$m^2$', '14 W/$m^2$'], loc='lower right')
        #plt.title('Figure 2: Effect light intensity has on the rate of intimin expression on the cell surface',**asfont )
        plt.ylabel('Concentration (uM)',**asfont)
        plt.xlabel('Time (hr)',**asfont)
        plt.title('Figure 2: Effect light intensity has on the rate of intimin expression on the cell surface ', fontsize=10, y=1.08)
        plt.legend(loc=1, borderaxespad=0)
        plt.ticklabel_format(style='sci', axis='y', scilimits=(0, 0))

    plt.show()