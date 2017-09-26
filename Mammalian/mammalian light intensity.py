from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt

# k1: Rate at which PhoCl becomes cleaved
# Here we create express k1 in terms of a function of light intensity (Hill equation)

k1_rate_array = []
#The array was created to add the values of k1 at the different light intensities examined
#copy_number= 0;

def cleavage(K,L,n):

    # K:Hill constant (W/m^2)
    # n: Hill coefficient
    # L: Light intensity (W/m^2)
    k1 = K*((L)**n)/(K+L)
    k1_rate_array.append(k1)
    return k1

print (k1_rate_array)

#cn_rate_array = []
#The array was created to add the values of cn at the different promoter concentrations examined

#def copy(K1,Pr,n):

    # K1:Hill constant (umol/L)
    # n: Hill coefficient
    # Pr: Promoter concentration in the nucleus (umol/L)
    #cn = K1*((Pr)**n)/(Pr+K1)

    #cn_rate_array.append(cn)

    #return cn

#print (cn_rate_array)

def diff_eqs(y, t):
    '''This function contains the differential equations'''

    """Unpacking y"""
    TF = y[0]  # Bound transbembrane protein by PhoCl
    # TFb = y[1]  #Transcrption (microM/L)
    mRNA = y[1]  # Translation (microM/L)
    P = y[2]  # Expression of the RFP protein (microM/L)

    """Set rate constants"""  # we made these numbers up we are now looking into fixing them and adding rate equations for the k values

    k2 = 57.6  # Rate of transcription per transcript (1/hr)
    k3 = 12  # Rate of translation (1/hr)
    d1 = 60 / 13  # Degradation of transcription factors (1/hr)
    d2 = 1.68  # Degradation of mRNA (1/hr)
    d3 = 1.86  # Degradation of translated protein (1/hr)
    a = 190.8  # Rate of transport of TF from cytoplasm to the nucleus (1/hr)
    b = 3  # Rate of transport of mRNA from nucleus to cytoplasm (1/hr)

    # Rate of PhoCL being cleaved by light and transmembrane protein complex being released in the cytoplasm
    dTF_dt = (light_cleavage * LACE) - (d1 * TF) - (a * TF)

    # Rate at which TF binds to the promoter in the nucleus
    # print(copy_number)
    # dTFb_dt = (TF*copy_number*a)

    # Rate of transcription

    dmRNA_dt = (k2 * TF) - (d2 * mRNA) - (b * mRNA)

    # Rate of translation
    Pt = 9.26 * (10 ** -6)  # Maximum concentration of Protein the cells can produce (umol/L)
    n = (1 - (P / (Pt)));

    dP_dt = (n * b * k3 * mRNA) - (d3 * P)

    """Repack solution in same order as y"""
    sol = [dTF_dt, dmRNA_dt, dP_dt]

    return sol


if __name__ == "__main__":
    time_steps = 1000  # Number of timepoints to simulate
    t = np.linspace(0, 10,time_steps)  # Set the time frame (start_time, stop_time, step) time frames are equally spaced within the two limits

    '''Set initial species concentration values'''
    LACE = 1.54 * (10 ** -7)  # Initial concentra0tion of the transmembrane protein complex (units)
    TF_0 = 0  # Starting concentration of free TF in thej cytoplasm
    # TFb_0= 0 # Starting conentration of the TF bound to the promoter
    mRNA_0 = 0  # Starting mRNA concentration (microM/L)
    P_0 = 0  # Starting protein concentration (microM/L)

    '''Pack intial conditions into an array'''
    y0 = [TF_0, mRNA_0, P_0]

    L_range = [0, 108000, 216000, 324000, 432000, 540000]
    # These are the range of light intensities who's effect was evaluated on the rate of 'k1'

    for L in L_range:
        print(L)
        light_cleavage = cleavage( 7.95, L, 1)
        # print(light_intensity)
        sol = odeint(diff_eqs, y0, t)
        plt.style.use('ggplot')
        plt.plot(t, sol[:, 2])
        """plot output"""
        # We set the font we wanted for our graphs
        asfont = {'fontname': 'Arial'}

        # We then annotaed our graphs axis, legends and set minimum and maximum ranges for them
        plt.legend(['0 W/$m^2$', '108,000 W/$m^2$', '216,000 W/$m^2$', '324,000 W/$m^2$', '432,000 W/$m^2$', '540,000 W/$m^2$'], loc='center left',
                   #bbox_to_anchor=(1, 0.5))
        plt.ylabel('Concentration (uM)', **asfont)
        plt.xlabel('Time (hr)', **asfont)
        plt.legend(loc=1, borderaxespad=0)
        plt.ticklabel_format(style='sci', axis='y', scilimits=(0, 0))
    plt.show()