from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt
import math


# k1: Rate at which EL222 becomes activated with light to bind to the promoter
# Here we express k1 in terms of a function of light intensity

k1_rate_array = []
# The array was created to add the values of k1 as different light intensities are examined

def light(k, L, n, K1):
    # k: Maximum expression due to induction (a.u.)
    # K1:Hill constant (W/m^2)
    # n: Hill coefficient (dimensionless)
    # a: Basal expression level of the promoter (microM)
    # L: Light intensity (W)

    k1 =((k * ((L)) ^ n) / ((K1) ^ n + ((L)) ^ n))

    k1_rate_array.append(k1)

    return k1

def diff_eqs(y,t):
    '''This function contains our differential equations'''

    """Unpacking y"""
    EL222dimer = y[0]  # EL222 dimerisation and binding to the promoter (microM/L)
    mRNA = y[1]  # Transcrption (microM/L)
    Intiminintracellular = y[2]  # Translation (microM/L)
    Intiminsurface = y[3]  # Expression of Intimin on the surface of the cells (microM/L)

    """Set rate constants"""  # Most values were collected from papers, we are finessing them by adding
    # values our Wet Lab obtained from our experiments

    k2 = (108/25)  # Rate of transcription per transcript (1/hr)
    k3 = (3600 / 660)  # Rate of translation (1/hr)
    d1 = 60 / 300  # Degradation of transcript (1/hr)
    d2 = 60 / 20  # Degradation of protein (Half-life of E.coli) (1/hr)

    a = ((400 / 2000) * (5 * (10 ** -10))) / 100  # Basal promoter expression

    # Rate of EL222 being activated by light, dimerizing and binding to the promoter
    dEL222dimer_dt = a + (light_intensity * (EL222inactive) ** 2) - (k2 * EL222dimer)

    # Rate of transcription
    dmRNA_dt = (k2 * EL222dimer) - (d1 * mRNA) - (k3 * mRNA)

    # Rate at which the protein is transferred to the surface of the cell
    Km=0.0147
    # its cytoplasm (1/hr)
    n = 1 - (Intiminsurface / (6.48 * 10 ** -6))  # Representing the space available for more proteins on the surface

    dIntiminintracellular_dt =(((((Intiminintracellular) ** 2) * (-d2 - v) * n) + (Intiminintracellular * ((mRNA * k3) - (d2 * Km))) + ((mRNA * k3) * Km)) / (Km + Intiminintracellular))

    # Rate of expression of the protein on the surface of the cell

    dIntiminsurface_dt =((((Intiminintracellular * v / (Intiminintracellular + Km)) * n) * Intiminintracellular) - d2 * (Intiminsurface))

    type(dIntiminsurface_dt)

    """Repack solution in same order as y"""
    sol = [dEL222dimer_dt, dmRNA_dt, dIntiminintracellular_dt, dIntiminsurface_dt]

    return sol

# For good programming practice we created a function to allow us to randomly obtain values of light intensities
# within a certain range, through using normal distributions.This saved us time and allowed us to plot multiple
# light intensities on the same graph simultaneously
def SampleParam (paramValue,sigma, paramNum):

    samples = np.random.normal(paramValue,sigma,paramNum)

    return samples.astype(int)
# We returned our Light intensities as an integer type, as the function was returning our values in the format of
# normal distribution arrays, which we could not concatenate with our other arrays

if __name__ == "__main__":

    #We defined the time for which we would like our cellular mechanisms to run for
    runTime = 2 #hours
    time_steps = 1000  # Number of timepoints to simulate
    t = np.linspace(0, runTime, time_steps)  # Set the time frame (start_time, stop_time, step) time frames are equally

    '''Set initial species concentration values'''
    EL222inactive = 2.37 * (10 ** -4)  # Initial concentration of inactive EL222 monomers (microM/L)
    EL222dimer_0 = 0  # Starting concentration of dimerised EL222 bound to the promoter (microM/L)
    mRNA_0 = 0  # Starting mRNA concentration (microM/L)
    Intiminintracellular_0 = 0  # Starting intimin concentration in the cells (microM/L)
    Intiminsurface_0 = 0  # Starting concentration of intimin expressed on the surface of the cell (microM/L)

    '''Pack intial conditions into an array'''
    y0 = [EL222dimer_0, mRNA_0, Intiminintracellular_0, Intiminsurface_0]

    # We then called the function we created to randomly select light intensities with normal distribution

    L_range=[70]

    for L in L_range:

        light_intensity = light(1545, L, 2, int(6.55))

    v_array= (SampleParam(510, 250, 10))*100
    
    #50% of the actual value is my standard deviation

    #print(Km_array)

    v_arrayLabels = []

    for i in v_array:
        v=i
        sol = odeint(diff_eqs, y0, t)

        plt.style.use("ggplot")

    # Once we selected our range of light intensities we inputted them into our initial function to calculate the value
    # of k1 and then inputted the values of k1 into our differential equations

        plt.plot(t, sol[:,3])

        v1 = v/3600

        v2 = "{0:0.1E}".format(v1)

        v_arrayLabels.append(str(v2) + ' 1/s')

    """plot output"""
    #We set the fonts we wanted for our graphs
    asfont = {'fontname': 'Arial'}
    hfont = {'fontname': 'Helvetica'}

    #We then annotaed our graphs axis, legends and set minimum and maximum ranges for them

    plt.ylabel('Concentration (uM)', **asfont)
    plt.legend(v_arrayLabels, loc='center left', bbox_to_anchor=(1, 0.5))
    plt.ylim(0
             )
    plt.xlabel('Time (hr)', **asfont)
    plt.xlim(0, runTime)
    #plt.title('Parameter Sampling for V$_{max}$ optimisation ',fontsize=10, y=1.08)
    plt.legend(loc=1, borderaxespad=0)
    plt.ticklabel_format(style='sci', axis='y', scilimits=(0, 0))

    plt.xlim((0, runTime))
    #plt.ylim((0, 0.0000007))
    plt.show()