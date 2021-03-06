from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt

# k1: Rate at which PhoCl becomes cleaved
# Here we create express k1 in terms of a function of light intensity (Hill equation)

k1_rate_array = []
#The array was created to add the values of k1 at the different light intensities examined
#copy_number= 0;

def cleavage(L):
    K=7.95
    n=1

    # K:Hill constant (W/m^2)
    # n: Hill coefficient
    # L: Light intensity (W/m^2)
    k1 = K*((L)**n)/(K+L)
    k1_rate_array.append(k1)

    return k1

def diff_eqs(y, t):
    '''This function contains the differential equations'''

    """Unpacking y"""
    TF = y[0]  # Bound transbembrane protein by PhoCl
    mRNA = y[1]  # Translation (microM/L)
    P = y[2]  # Expression of the RFP protein (microM/L)

    """Set rate constants"""  # we made these numbers up we are now looking into fixing them and adding rate equations for the k values

    k2 = 57.6  # Rate of transcription per transcript (1/hr)
    k3 = 12  # Rate of translation (1/hr)
    d1 = 60 / 13  # Degradation of transcription factors (1/hr)
    d2 = 1.68  # Degradation of mRNA (1/hr)
    #d3 = 0.291  # Degradation of translated protein (1/hr)
    a = 190.8  # Rate of transport of TF from cytoplasm to the nucleus (1/hr)
    b = 180  # Rate of transport of mRNA from nucleus to cytoplasm (1/hr)

    # Rate of PhoCL being cleaved by light and transmembrane protein complex being released in the cytoplasm
    dTF_dt = (light_cleavage * LACE) - (d1 * TF) - (a * TF)

    # Rate at which TF binds to the promoter in the nucleus
    # print(copy_number)
    # dTFb_dt = (TF*copy_number*a)

    # Rate of transcription

    dmRNA_dt = (k2 * TF) - (d2 * mRNA) - (b * mRNA)

    # Rate of translation
    Pt = 9.26 * (10 ** -6)  # Maximum concentration of Protein the cells can produce (umol/L)
    n = (1 - (P / (Pt)))

    dP_dt = (n * b * k3 * mRNA) - (d3 * P)

    """Repack solution in same order as y"""
    sol = [dTF_dt, dmRNA_dt, dP_dt]

    return sol

# For good programming practice we created a function to allow us to randomly obtain values of Km
# within a certain range, through using normal distributions.This saved us time and allowed us to plot multiple
# light intensities on the same graph simultaneously
def SampleParam (paramValue,sigma, paramNum):

    samples = np.random.normal(paramValue,sigma,paramNum)

    return samples.astype(int)
# We returned our Light intensities as an integer type, as the function was returning our values in the format of
# normal distribution arrays, which we could not concatenate with our other arrays

if __name__ == "__main__":
    time_steps = 10000  # Number of timepoints to simulate
    stop_time = 14
    t= np.linspace( 0, stop_time, time_steps)  # Set the time frame (start_time, stop_time, step) time frames are equally spaced within the two limits

    '''Set initial species concentration values'''

    LACE = 1.54 * (10 ** -7)  # Initial concentration of the transmembrane protein complex (units)
    TF_0 = 0  # Starting concentration of free TF in thej cytoplasm
    mRNA_0 = 0  # Starting mRNA concentration (microM/L)
    P_0 = 0  # Starting protein concentration (microM/L)

    '''Pack intial conditions into an array'''

    y0 = [TF_0, mRNA_0, P_0]

    L_range = [43]

    for L in L_range:
        light_cleavage = cleavage(L)

    d3_range = (SampleParam(51,20, 6)/100)
    # These are the range of light intensities who's effect was evaluated on the rate of 'k1'

    d3_rangeLabels = []

    for i in d3_range:
        d3 = i
        sol = odeint(diff_eqs, y0, t)

        plt.style.use('ggplot')

        plt.plot(t, sol[:, 2])

        d4= d3/3600

        d6="{0:.1E}".format(d4)

        d3_rangeLabels.append(str(d6) + ' 1/s')

    """plot output"""
    # We set the font we wanted for our graphs
    asfont = {'fontname': 'Arial'}

    # We then annotaed our graphs axis, legends and set minimum and maximum ranges for them
    #plt.legend([ '0 W/$cm^2$', '11 W/$cm^2$', '22 W/$cm^2$', '32 W/$cm^2$', '43 W/$cm^2$', '54 W/$cm^2$'], loc='center left', bbox_to_anchor=( 1, 0.5))
    plt.legend(d3_rangeLabels, loc='center left', bbox_to_anchor=(1, 0.5))
    plt.ylabel('Concentration (uM)', **asfont)
    plt.xlabel('Time (hr)', **asfont)
    plt.ticklabel_format( style='sci', axis='y', scilimits=(0, 0))
    plt.xlim((0, stop_time))
    plt.ylim((0, 0.000006))
    plt.show()