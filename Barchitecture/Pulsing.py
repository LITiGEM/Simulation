from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt
import math

k1_pulsing_array =[]

light_pulsing=0
#The rate of photocleavage is dependant on the light intensity of the light. We optimised the light intensity we will
#be using in our optogenetic technology, therefore the rate of photoactivation can be calculated from the equation below:
#k1 = ((k * (L) ^ n) / ((k) ^ n + (L) ^ n))
#where: k= 1,545 W/cm^2 ; L= 60 W/cm^2 ; n= 2; K1= 6.55

k1=27
k1_pulse=0

def pulsing(t2):
    ON=43200/86400

    if t2>12:
            k1_pulse=0

    elif t2<0:
            k1_pulse=0

    else:
            k1_pulse=k1*(math.sin(((t2/24-math.floor(t2/24)))*math.pi/(1-ON)))

    #k1_pulsing_array.append(k1_pulse)

    return k1_pulse

def diff_eqs(y, t):
    '''This function contains the differential equations'''

    """Unpacking y"""
    B = y[0] # Bound EL222 to the promoter (microM/L)
    mRNA = y[1] # Transcrption (microM/L)
    P = y[2] # Translation (microM/L)
    S = y[3] # Expression on surface (microM/L)

    """Set rate constants"""  # we made these numbers up we are now looking into fixing them and adding rate equations for the k values
    k2 = (108/25) # Rate of transcription per transcript (1/hr)
    k3 = (3600/660) # Rate of translation (1/hr)
    d1 = 60/300 # Degradation of transcript (1/hr)
    d2 = 60/20 # Degradation of protein (Half-life of E.coli) (1/hr)
    d3= 60/20 #half-life of intimin (1/hr)
    a = ((20 / 100) * (3.5 * (10 ** -1))) # Basal promoter expression
    light_pulsing = pulsing(t)

    # Rate of EL222 being activated by light and binding to the promoter
    dB_dt = a+(light_pulsing* (T) ** 2) - (k2 * B)

    # Rate of transcription
    dmRNA_dt = (k2 * B) - (d1 * mRNA) - (k3 * mRNA)

    # Rate at which the protein is transferred to the surface of the cell
    Km = 5  # (microM/L)
    v = 115200/ 10  # Based on the rate at which mRNA is transferred from within the nucleus of a mammalian cell to its cytoplasm (1/hr)
    n = 1 - (S / (1.24))  # Representing the space available for more proteins on the surface of the cell in the form of a ratio (Dimensionless)
    b = (P / (P + Km)) * n * v  # Rate at which the protein is transferred to the surface of the cell (1/s)

    # Rate of translation
    dP_dt = (k3 * mRNA) - (d2 * P) - (b * P)

    # Rate of expression of the protein
    dS_dt = (b * P)-(d3*S)

    """Repack solution in same order as y"""

    sol= [dB_dt, dmRNA_dt, dP_dt, dS_dt]

    return sol

if __name__ == "__main__":
    #time_steps = 1000  # Number of timepoints to simulate
    t = np.linspace(0, 15, 10000)  # Set the time frame (start_time, stop_time, step) time frames are equally spaced within the two limits

    '''Set initial species concentration values'''
    T = 0.032  # Initial concentration of EL222 (microM/L)
    B_0 = 0  # Starting concentration of EL222 bound to the promoter (microM/L)
    mRNA_0 = 0  # Starting mRNA concentration (microM/L)
    P_0 = 0  # Starting protein concentration (microM/L)
    S_0 = 0  # Starting concentration of protein expressed on the surface of the cell (microM/L)

    '''Pack intial conditions into an array'''
    y0 = [B_0, mRNA_0, P_0, S_0]

    #L_range = [14]
    # These are the range of light intensities who's effect was evaluated on the rate of 'k1'
    #for L in L_range:
        #print(L)
        #light_intensities = light(1545, L, 2, 6.554)
        #sol = odeint(diff_eqs, y0, t)

    t2_range = np.array([0, 10000, 20000, 30000, 40000, 50000, 60000, 70000, 80000])

    for t2 in t2_range:
        # print(t)
        light_pulsing=pulsing(t2)
        #  print(light_pulsing)
        sol = odeint(diff_eqs, y0, t)

    # These are the range of light intensities who's effect was evaluated on the rate of 'k1'
    #for light_pulsing in light_pulsing_range:
        # print(L)
        # light_intensities = light(1545, L, 2, 6.554)
        #print(light_pulsing)
        #sol = odeint(diff_eqs, y0, t)

    """plot output"""
    asfont = {'fontname': 'Arial'}
    hfont = {'fontname': 'Helvetica'}

    plt.style.use('ggplot')
    plt.ticklabel_format(style='sci', axis='y', scilimits=(0, 0))
    plt.ticklabel_format(style='sci', axis='x')
    plt.plot(t, sol[:, 0])
    plt.plot(t, sol[:, 1])
    plt.plot(t, sol[:, 2])
    plt.plot(t, sol[:, 3])
    #plt.title('Visualising the effect 1 pulse has on rate kinetics', fontsize=10, y=1.08)
    plt.legend(['EL222 Dimer', 'mRNA', 'Translated Intimin', 'Surface expressed Intimin'],loc='center left', bbox_to_anchor=(1, 0.5))
        #plt.title('Figure 2: Effect light intensity has on the rate of intimin expression on the cell surface',**asfont )
    plt.ylabel('Concentration (uM)',**asfont)
    plt.xlabel('Time (hr)',**asfont)
    plt.xlim((0, 15))
    #plt.ylim((0, 0.0000005))
        #plt.ticklabel_format(style='sci', axis='y', scilimits=(0, 0))
    plt.show()