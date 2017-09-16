import scipy.integrate as scipy
import numpy as np
import matplotlib.pyplot as plt

# k1: Rate at which EL222 becomes activated with light to bind to the promoter
# Here we express k1 in terms of a function of light intensity

k1_rate_array = []
# The array was created to add the values of k1 as different light intensities are examined

def light(k, L, n, K1):
    a = 444.6  # Basal expression level of the promoter (microM)

    # k: Maximum expression due to induction (a.u.)
    # K1:Hill constant (W/m^2)
    # n: Hill coefficient (dimensionless)
    # a: Basal expression level of the promoter (microM)
    # L: Light intensity (W)

    k1 = a + ((k * ((L)) ^ n) / ((k) ^ n + ((L)) ^ n))

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

    # Rate of EL222 being activated by light, dimerizing and binding to the promoter
    dEL222dimer_dt = (light_intensity * (T) ** 2) - (k2 * EL222dimer)

    # Rate of transcription
    dmRNA_dt = (k2 * EL222dimer) - (d1 * mRNA) - (k3 * mRNA)

    # Rate at which the protein is transferred to the surface of the cell
    Km = 5  # (microM/L)
    v = 115200/ 10  # Based on the rate at which mRNA is transferred from within the nucleus of a mammalian cell to
    # its cytoplasm (1/hr)
    n = 1 - (Intiminsurface / (6.48 * 10 ** -6))  # Representing the space available for more proteins on the surface
    # of the cell in the form of a ratio (Dimensionless)
    b = (Intiminintracellular / (Intiminintracellular + Km)) * n * v  # Rate at which the protein is transferred to the surface of the cell (1/s)

    # Rate of translation
    dIntiminintracellular_dt = (k3 * mRNA) - (d2 * Intiminintracellular) - (b * Intiminintracellular)

    # Rate of expression of the protein on the surface of the cell
    dIntiminsurface_dt = (b * Intiminintracellular)

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
    runTime = 200 #hours
    time_steps = 1000  # Number of timepoints to simulate
    t = np.linspace(0, runTime, time_steps)  # Set the time frame (start_time, stop_time, step) time frames are equally
    # spaced within the two limits

    '''Set initial species concentration values'''
    T = 2.37 * (10 ** -4)  # Initial concentration of inactive EL222 monomers (microM/L)
    EL222dimer_0 = 0  # Starting concentration of dimerised EL222 bound to the promoter (microM/L)
    mRNA_0 = 0  # Starting mRNA concentration (microM/L)
    Intiminintracellular_0 = 0  # Starting intimin concentration in the cells (microM/L)
    Intiminsurface_0 = 0  # Starting concentration of intimin expressed on the surface of the cell (microM/L)

    '''Pack intial conditions into an array'''
    y0 = [EL222dimer_0, mRNA_0, Intiminintracellular_0, Intiminsurface_0]

    # We then called the function we created to randomly select light intensities with normal distribution
    L_range = SampleParam(150, 50, 10)

    print(L_range)

    L_rangeLabels = []

    plt.style.use("ggplot")

    # Once we selected our range of light intensities we inputted them into our initial function to calculate the value
    # of k1 and then inputted the values of k1 into our differential equations

    for L in L_range:

        light_intensity = light(1545, L, 2, 6.554)

        sol = scipy.odeint(diff_eqs, y0, t)

        plt.plot(t, sol[:,3])

        L_rangeLabels.append(str(L) + 'W/$m^2$')

    """plot output"""
    #We set the fonts we wanted for our graphs
    asfont = {'fontname': 'Arial'}
    hfont = {'fontname': 'Helvetica'}

    #We then annotaed our graphs axis, legends and set minimum and maximum ranges for them
    plt.ylabel('Concentration (uM)', **asfont)
    plt.ylim(0)
    plt.xlabel('Time (hr)', **asfont)
    plt.xlim(0, runTime)
    plt.title('Figure 2: Effect light intensity has on the rate of intimin expression on the cell surface ',fontsize=10, y=1.08)
    plt.legend(loc=1, borderaxespad=0)
    plt.ticklabel_format(style='sci', axis='y', scilimits=(0, 0))
    plt.legend(L_rangeLabels, loc='lower right')
    plt.show()