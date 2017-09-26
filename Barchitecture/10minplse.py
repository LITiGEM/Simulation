from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt
import math

k1_pulsing_array =[]

light_pulsing=0
k1=458.4
k1_pulse =0

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

def diff_eqs(y, t):
    '''This function contains the differential equations'''

    """Unpacking y"""
    B = y[0] # Bound EL222 to the promoter (microM/L)
    mRNA = y[1] # Transcrption (microM/L)
    P = y[2] # Translation (microM/L)
    S = y[3] # Expression on surface (microM/L)

    """Set rate constants"""  # we made these numbers up we are now looking into fixing them and adding rate equations for the k values
    k2 = (108/25) #103.7 #(108/25) # Rate of transcription per transcript (1/hr)
    k3 = (3600/660) #130.9 #(3600/660) # Rate of translation (1/hr)
    d1 = 60/300 #4.8 #60/300 # Degradation of transcript (1/hr)
    d2 = 60/20 #72 #60/20 # Degradation of protein (Half-life of E.coli) (1/hr)
    d3= (60/20) #72 #60/20 #half-life of intimin (1/hr)
    light_pulsing = pulsing(t)
    # Rate of EL222 being activated by light and binding to the promoter
    dB_dt = (light_pulsing* (T) ** 2) - (k2 * B)

    # Rate of transcription
    dmRNA_dt = (k2 * B) - (d1 * mRNA) - (k3 * mRNA)

    # Rate at which the protein is transferred to the surface of the cell
    Km = 5  # (microM/L)
    v = 11520  #276480 #11520  # Based on the rate at which mRNA is transferred from within the nucleus of a mammalian cell to its cytoplasm (1/hr)
    n = 1 - (S / (6.48 * 10 ** -6))  # Representing the space available for more proteins on the surface of the cell in the form of a ratio (Dimensionless)
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
    t = np.linspace(0, 25, 100)  # Set the time frame (start_time, stop_time, step) time frames are equally spaced within the two limits

    '''Set initial species concentration values'''
    T = 2.37 * (10 ** -4)  # Initial concentration of EL222 (microM/L)
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

    t2_range = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

    for t2 in t2_range:
        # print(t)
        light_pulsing=pulsing(t2)
        #  print(light_pulsing)
        sol = odeint(diff_eqs, y0, t)
        plt.style.use('ggplot')
        #plt.plot(t, sol[:, 0])
        #plt.plot(t, sol[:, 1])
        #plt.plot(t, sol[:, 2])
        plt.plot(t, sol[:, 3])

    # These are the range of light intensities who's effect was evaluated on the rate of 'k1'
    #for light_pulsing in light_pulsing_range:
        # print(L)
        # light_intensities = light(1545, L, 2, 6.554)
        #print(light_pulsing)
        #sol = odeint(diff_eqs, y0, t)

    """plot output"""
    asfont = {'fontname': 'Arial'}
    hfont = {'fontname': 'Helvetica'}

    plt.ticklabel_format(style='sci', axis='y', scilimits=(0, 0))
    plt.ticklabel_format(style='sci', axis='x', scilimits=(0, 24))

    #plt.title('Effect pulsing light in 4 hour intervals has on intimin surface expression', fontsize=10, y=1.08)
    #plt.legend(['Transport to the cell surface'], loc='center left', bbox_to_anchor=(1, 0.5))
    plt.ylabel('Concentration (uM)',**asfont)
    plt.xlabel('Time (hr)',**asfont)
    plt.xlim((0,25))
plt.show()