from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt

# k1: Rate at which EL222 becomes activated with light to bind to the promoter
# Here we express k1 in terms of a function of light intensity

k1_rate_array = []
# The array was created to add the values of k1 as different light intensities are examined

def light(k, L, n, K1):

    # k: Maximum expression due to induction (a.u.)
    # K1:Hill constant (W/m^2)
    # n: Hill coefficient (dimensionless)
    # a: Basal expression level of the promoter (a. u)
    # L: Light intensity (W)

    k1 = ((k * (L) ^ n) / ((K1) ^ n + (L) ^ n))

    k1_rate_array.append(k1)

    return k1

def diff_eqs(y, t):
    '''This function contains the differential equations'''

    """Unpacking y"""
    EL222dimer = y[0]  # EL222 dimerisation and binding to the promoter (microM/L)
    mRNA = y[1]  # Transcrption (microM/L)
    Intiminintracellular = y[2]  # Translation (microM/L)
    Intiminsurface = y[3]  # Expression of Intimin on the surface of the cells (microM/L)

    """Set rate constants""" # Most values were collected from papers, we are finessing them by adding
    # values our Wet Lab obtained from our experiments

    k2 = (108 / 25)  # Rate of transcription per transcript (1/hr)
    k3 = (3600 / 660)  # Rate of translation (1/hr)
    d1 = 60 / 300  # Degradation of transcript (1/hr)
    d2 = 60 / 20  # Degradation of protein (Half-life of E.coli) (1/hr)

    # Rate of EL222 being activated by light, dimerizing and binding to the promoter
    a = ((20 / 100) * (3.5 * (10 ** -1))) #basal promoter expression
    #a=4.5**-6

    dEL222dimer_dt = a+(light_intensity * (EL222inactive) ** 2) - (k2 * EL222dimer)

    # Rate of transcription
    dmRNA_dt = (k2 * EL222dimer) - (d1 * mRNA) - (k3 * mRNA)

    # Rate at which the protein is transferred to the surface of the cell
    Km = 5  # (microM/L)
    v = 10000   # Based on the rate at which mRNA is transferred from within the nucleus of a mammalian cell to
    # its cytoplasm (1/hr)
    n = 1 - (Intiminsurface / (1.24))  # Representing the space available for more proteins on the surface
    # of the cell in the form of a ratio (Dimensionless)
    b = (Intiminintracellular / (Intiminintracellular + Km)) * n * v  # Rate at which the protein is transferred to the
    # surface of the cell (1/s)

    # Rate of translation
    dIntiminintracellular_dt = (k3 * mRNA) - (d2 * Intiminintracellular) - (b * Intiminintracellular)

    # Rate of expression of the protein on the surface of the cell
    dIntiminsurface_dt = (b * Intiminintracellular) -d2*(Intiminsurface)

    print(Intiminsurface)

    """Repack solution in same order as y"""

    sol = [dEL222dimer_dt, dmRNA_dt, dIntiminintracellular_dt, dIntiminsurface_dt]

    return sol

if __name__ == "__main__":
    time_steps = 100# Number of timepoints to simulate
    time_stop = 10
    t = np.linspace(0, time_stop, time_steps)  # Set the time frame (start_time, stop_time, step) time frames are equally spaced within the two limits

    '''Set initial species concentration values'''
    EL222inactive = 0.032 # Initial concentration of EL222 (microM/L)
    EL222dimer_0 = 0  # Starting concentration of EL222 bound to the promoter (microM/L)
    mRNA_0 = 0  # Starting mRNA concentration (microM/L)
    Intiminintracellular_0 = 0  # Starting protein concentration (microM/L)
    Intiminsurface_0 = 0  # Starting concentration of protein expressed on the surface of the cell (microM/L)

    '''Pack intial conditions into an array'''
    y0 = [EL222dimer_0, mRNA_0, Intiminintracellular_0, Intiminsurface_0]

    # Once we selected our range of light intensities we inputted them into our initial function to calculate the value
    # of k1 and then inputted the values of k1 into our differential equations

    L_range = [0,18,35,53,70]


    for L in L_range:
        print(L)
        light_intensity = light(1545, L, 2, int(6.554))
        print(light_intensity)
        sol = odeint(diff_eqs, y0, t)
        plt.style.use('ggplot')
        plt.plot(t, sol[:, 3])
    """plot output"""
    # We set the font we wanted for our graphs
    asfont = {'fontname': 'Arial'}

    # We then annotaed our graphs axis, legends and set minimum and maximum ranges for them
    plt.legend(['0 W/$cm^2$', '18 W/$cm^2$', '35 W/$cm^2$', '53 W/$cm^2$', '70 W/$cm^2$'], loc='center left', bbox_to_anchor=(1, 0.5))
    plt.ylabel('Concentration (uM)',**asfont)
    plt.xlabel('Time (hr)',**asfont)
    #plt.title('Effect of light intensity on the rate of intimin expression on the cell surface ', fontsize=10, y=1.08)
    plt.legend(loc=1, borderaxespad=0)
    plt.ticklabel_format(style='sci', axis='y', scilimits=(0, 0))
    plt.xlim((0,time_stop))
    #plt.ylim((0,0.002))

    plt.show()