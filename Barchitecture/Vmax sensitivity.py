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
    d1 = 60 / 20  # Degradation of transcript (1/hr)
    d2 = 60 / 20  # Degradation of protein (Half-life of E.coli) (1/hr)
    a = ((20 / 100) * (3.5 * (10 ** -1)))  #basal promoter expression  # We modelled it at 0.2 of the maximal expression rate

    # Rate of EL222 being activated by light, dimerizing and binding to the promoter
    dEL222dimer_dt = a + (light_intensity * (EL222inactive) ** 2) - (k2 * EL222dimer)

    # Rate of transcription
    dmRNA_dt = (k2 * EL222dimer) - (d1 * mRNA) - (k3 * mRNA)

    # Rate at which the protein is transferred to the surface of the cell
    Km=1
    #v = 115200 / 10  # Based on the rate at which mRNA is transferred from within the nucleus of a mammalian cell to
    # its cytoplasm (1/hr)
    n = 1 - (Intiminsurface / (1.24))  # Representing the space available for more proteins on the surface

    dIntiminintracellular_dt = ((((Intiminintracellular)**2)*(-d2-v)*n)+(Intiminintracellular*((mRNA*k3)-(d2*Km)))+((mRNA*k3)*Km))/(Km+Intiminintracellular)

    # Rate of expression of the protein on the surface of the cell
    dIntiminsurface_dt = (((Intiminintracellular*v / (Intiminintracellular + Km)) * n)* Intiminintracellular) -d2*(Intiminsurface)

    """Repack solution in same order as y"""

    sol = [dEL222dimer_dt, dmRNA_dt, dIntiminintracellular_dt, dIntiminsurface_dt]

    return sol

if __name__ == "__main__":
    time_steps = 1000  # Number of timepoints to simulate
    t = np.linspace(0, 5, time_steps)  # Set the time frame (start_time, stop_time, step) time frames are equally spaced within the two limits
    #Km_array=[1,2,3,4,5,6,7,8,9,10]

    v_array=[ 2160, 36000, 57960, 17863200, 648000000, 2160000000]

    '''Set initial species concentration values'''
    EL222inactive = 0.032  # Initial concentration of EL222 (microM/L)
    EL222dimer_0 = 0  # Starting concentration of EL222 bound to the promoter (microM/L)
    mRNA_0 = 0  # Starting mRNA concentration (microM/L)
    Intiminintracellular_0 = 0  # Starting protein concentration (microM/L)
    Intiminsurface_0 = 0  # Starting concentration of protein expressed on the surface of the cell (microM/L)

    '''Pack intial conditions into an array'''
    y0 = [EL222dimer_0, mRNA_0, Intiminintracellular_0, Intiminsurface_0]

    # Once we selected our range of light intensities we inputted them into our initial function to calculate the value
    # of k1 and then inputted the values of k1 into our differential equations

    L_range = [70]

    for L in L_range:
        print(L)
        light_intensity = light(1545, L, 2, int(6.554))
        #print(light_intensity)
    #for i in Km_array:
    #   Km =i

    v_arrayLabels = []

    for i in v_array:
        v =i
        sol = odeint(diff_eqs,y0,t)
        plt.style.use('ggplot')
        plt.plot(t, sol[:, 3])

        v1 = v / 3600
        v2 = "{0:0.1E}".format(v1)
        v_arrayLabels.append(str(v2) + ' 1/s')

    """plot output"""
    # We set the font we wanted for our graphs
    asfont = {'fontname': 'Arial'}
    # We then annotaed our graphs axis, legends and set minimum and maximum ranges for them
    #plt.legend(['6E+01 1/s', '1E+02 1/s', '1.6E+02 1/s', '4E+04 1/s', '1.8E+05 1/s', '6E+06 1/s'], loc='center left', bbox_to_anchor=(1, 0.5))
    plt.legend(v_arrayLabels, loc='center left', bbox_to_anchor=(1, 0.5))
    plt.ylabel('Concentration (uM)',**asfont)
    plt.xlabel('Time (hr)',**asfont)
    #plt.title('Effect changing Vmax has on the rate of intimin expression on the cell surface ', fontsize=10, y=1.08)
    plt.ticklabel_format(style='sci', axis='y', scilimits=(0, 0))
    plt.xlim((0, 5))
    #plt.ylim((0, 0.000007))
    plt.show()