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
    time_steps = 100  # Number of timepoints to simulate
    t = np.linspace(0, 5,
                    time_steps)  # Set the time frame (start_time, stop_time, step) time frames are equally spaced within the two limits

    '''Set initial species concentration values'''
    LACE = 1.54 * (10 ** -7)  # Initial concentra0tion of the transmembrane protein complex (units)
    TF_0 = 0  # Starting concentration of free TF in thej cytoplasm
    # TFb_0= 0 # Starting conentration of the TF bound to the promoter
    mRNA_0 = 0  # Starting mRNA concentration (microM/L)
    P_0 = 0  # Starting protein concentration (microM/L)

    '''Pack intial conditions into an array'''
    y0 = [TF_0, mRNA_0, P_0]

    L_range = [0, 0.005, 0.01, 0.015, 0.02]
    # These are the range of light intensities who's effect was evaluated on the rate of 'k1'

    for L in L_range:
        print(L)
        light_cleavage = cleavage(7.95, L, 1)
        sol = odeint(diff_eqs, y0, t)

   # Pr_range= [50]
    #for Pr in Pr_range:
       # print(Pr)
       # copy_number= copy(171,Pr,1)
        #sol=odeint(diff_eqs, y0, t)

        """plot output"""
        asfont = {'fontname': 'Arial'}
        hfont = {'fontname': 'Helvetica'}

        #plt.plot(t, sol[:, 0])
        #plt.plot(t, sol[:, 1])
        plt.plot(t, sol[:, 2])
        #plt.plot(t, sol[:, 3])
        #plt.legend(['Rate of photocleavage', 'mRNA', 'Translated protein'], bbox_to_anchor=(1, 0.5))

        plt.legend(['0 W/$m^2$', '0.005 W/$m^2$', '0.01 W/$m^2$', '0.015 W/$m^2$', '0.02 W/$m^2$'], loc='lower right')
        #plt.title('Figure 1: Rate kinetics of cellular mechanisms with a light intensity of 0.02 W/$m^2$',**asfont
        plt.ylabel('Concentration (uM)',**asfont)
        plt.xlabel('Time (hr)',**asfont)
        plt.title('Figure 2: Effect light intensity has on the rate of RFP expression', fontsize=10, y=1.08)
        #plt.legend(loc=1, borderaxespad=0)
        plt.ticklabel_format(style='sci', axis='y', scilimits=(0, 0))

    plt.show()