from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt
import math

#The rate of photocleavage is dependant on the light intensity of the light. We optimised the light intensity we will
#be using in our optogenetic technology, therefore the rate of photoactivation can be calculated from the equation below:
#k1 = (K*((L)**n)/(K+L))
#where: K= 7.95 W/cm^2 ; L= 27 W/cm^2 ; n= 1

k1_pulsing_array =[]
light_pulsing=0
k1_pulse=0
k1= 6.14

def pulsing(t2):

    ON=22/24

    if t2<0:
        k1_pulse =0

    else:
        k1_pulse = k1 * (math.sin(((t2/24 - math.floor(t2/24))) * math.pi / (1 - ON)))

    if k1_pulse<0:
        k1_pulse =0
    #k1_pulsing_array.append(k1_pulse)

    return k1_pulse

k1_rate_array = []


def diff_eqs(y, t):
    '''This function contains the differential equations'''

    light_pulsing = pulsing(t)
    """Unpacking y"""
    TF = y[0]  # Bound transbembrane protein by PhoCl
    #TFb = y[1]  #Transcrption (microM/L)
    mRNA = y[1]  # Translation (microM/L)
    P = y[2]  # Expression of the RFP protein (microM/L)

    """Set rate constants"""  # we made these numbers up we are now looking into fixing them and adding rate equations for the k values

    k2 =  57.6 # Rate of transcription per transcript (1/hr)
    k3 = 12 # Rate of translation (1/hr)
    d1= 60/13 # Degradation of transcription factors (1/hr)
    d2 = 1.68 # Degradation of mRNA (1/hr)
    d3 = 1.86 # Degradation of translated protein (1/hr)
    a = 190.8 # Rate of transport of TF from cytoplasm to the nucleus (1/hr)
    b = 180 # Rate of transport of mRNA from nucleus to cytoplasm (1/hr)

    #Rate of PhoCL being cleaved by light and transmembrane protein complex being released in the cytoplasm
    dTF_dt = (light_pulsing*LACE)-(d1*TF)-(a*TF)

    #Rate at which TF binds to the promoter in the nucleus
    #print(copy_number)
    #dTFb_dt = (TF*copy_number*a)

    #Rate of transcription

    dmRNA_dt = (k2*TF)-(d2*mRNA)-(b*mRNA)

    #Rate of translation
    Pt = 9.26 * (10 ** -6)  #Maximum concentration of Protein the cells can produce (umol/L)
    n = (1 - (P / (Pt)))

    dP_dt = (n*b*k3*mRNA)-(d3*P)

    """Repack solution in same order as y"""
    sol = [dTF_dt, dmRNA_dt, dP_dt]

    return sol

if __name__ == "__main__":
    time_steps = 100000 # Number o timepoints to simulate
    stop_time = 25
    t = np.linspace(0, stop_time, time_steps)  # Set the time frame (start_time, stop_time, step) time frames are equally spaced within the two limits

    '''Set initial species concentration values'''
    LACE = 1.54*(10**-7)  # Initial concentration of the transmembrane protein complex (units)
    TF_0 = 0  # Starting concentration of free TF in thej cytoplasm
    #TFb_0= 0 # Starting conentration of the TF bound to the promoter
    mRNA_0 = 0  # Starting mRNA concentration (microM/L)
    P_0 = 0  # Starting protein concentration (microM/L)

    '''Pack intial conditions into an array'''
    y0 = [TF_0, mRNA_0, P_0]

    L_range = [27]
    #These are the range of light intensities who's effect was evaluated on the rate of 'k1'

    for L in L_range:
        print(L)

    t2_range = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8])

    for t2 in t2_range:
        # print(t)
        light_pulsing = pulsing(t2)
        #  print(light_pulsing)
        sol = odeint(diff_eqs, y0, t)

    """plot output"""
    asfont = {'fontname': 'Arial'}
    hfont = {'fontname': 'Helvetica'}

    plt.style.use('ggplot')
    plt.ticklabel_format(style='sci', axis='y', scilimits=(0, 0))
    plt.ticklabel_format(style='sci', axis='x')
    plt.plot(t, sol[:, 0])
    plt.plot(t, sol[:, 1])
    plt.plot(t, sol[:, 2])

    plt.legend(['Free $TF_C$', '$mRNA_N$', 'RFP Protein'], bbox_to_anchor=(1, 0.5))
    #plt.legend(['Free $TF_C$'], bbox_to_anchor=(1, 0.5))
    #plt.legend(['0 W/$m^2$', '0.005 W/$m^2$', '0.01 W/$m^2$', '0.015 W/$m^2$', '0.02 W/$m^2$'], loc='lower right')
    #plt.title('Rate kinetics of mammalian cellular mechanisms with a light intensity of 0.02 W/$m^2$', fontsize=10, y=1.08)
    plt.ylabel('Concentration (uM)',**asfont)
    plt.xlabel('Time (hr)',**asfont)
    plt.xlim((0,stop_time))
    plt.ylim((0,0.0000014))
    plt.ticklabel_format(style='sci', axis='y', scilimits=(0, 0))

plt.show()
    #plt.title('Figure 2: Effect light intensity has on the rate of RFP expression', fontsize=10, y=1.08)

