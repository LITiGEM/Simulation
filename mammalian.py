from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt


# k1: Rate at which PhoCl becomes cleaved
# Here we create express k1 in terms of a function of light intensity (Hill equation)

k1_rate_array = []
#The array was created to add the values of k1 as different light intensities are examined

def light():
    a =   # Basal expression level of the promoter (microM)

    # k: Maximum expression due to induction (a.u.)
    # K1:Hill constant (W/m^2)
    # n: Hill coefficient
    # a: Basal expression level of the promoter (microM)
    # L: Light intensity (W)

    k1 = #implement the right equation

    k1_rate_array.append(k1)

    return k1


print (k1_rate_array)



def diff_eqs(y, t):
    '''This function contains the differential equations'''

    """Unpacking y"""
    TF = y[0]  #Bound transbembrane protein by PhoCl
    TFb = y[1]  #Transcrption (microM/L)
    mRNA = y[2]  #Translation (microM/L)
    P = y[3]  #expression of the RFP protein (microM/L)

    """Set rate constants"""  # we made these numbers up we are now looking into fixing them and adding rate equations for the k values

    k2 = # Rate of transcription per transcript (1/s)
    k3 =   # Rate of translation (1/hr)
    d1 =   # Degradation of transcript (1/hr)
    d2 =  # Degradation of protein (Half-life of E.coli) (1/hr)
    d3 = # Degradation of translated protein (find units)
    a = #rate of transport of TF from cytoplasm to the nucleus


    # Rate of PhoCL being cleaved by light and transmembrane protein complex being released in the cytoplasm
    dTF_dt = (k1*LACE)-(d1*TF)-(a*TF)

    # Rate at which TF binds to the promoter in the nucleus
    dTFb_dt = (a*c*TF)

    # Rate of transcription
    dmRNA_dt = (k2*TFb)-(d2*mRNA)-(b*mRNA)


    # Rate at which the protein is transferred to the surface of the cell
    Km =   # (microM/L)
    v =  # Based on the rate at which mRNA is transferred from within the nucleus of a mammalian cell to its cytoplasm (1/hr)
    n =  # Representing the space available for more proteins on the surface of the cell in the form of a ratio (Dimensionless)
    b =  # Rate of transport of mRNA from nucleus to cytoplasm

    # Rate of translation
    dP_dt = (b * k3 * mRNA) - (d3 * P)


    """Repack solution in same order as y"""
    sol = [dTF_dt, dTFb_dt, dmRNA_dt, dP_dt]

    return sol

if __name__ == "__main__":
    time_steps =  # Number of timepoints to simulate
    t = np.linspace(x, x, time_steps)  # Set the time frame (start_time, stop_time, step) time frames are equally spaced within the two limits

    '''Set initial species concentration values'''
    LACE =   # Initial concentration of the transmembrane protein complex (units)
    TF_0 = 0  # Starting concentration of free TF in the cytoplasm
    TFb_0=  # Starting conentration of the TF bound to the promoter
    mRNA_0 = 0  # Starting mRNA concentration (microM/L)
    P_0 = 0  # Starting protein concentration (microM/L)


    '''Pack intial conditions into an array'''
    y0 = [TF_0, TFb_0, mRNA_0, P_0]

    L_range = []
    # These are the range of light intensities who's effect was evaluated on the rate of 'k1'

    for L in L_range:
        print(L)
        light_intensity = light ()
        sol = odeint(diff_eqs, y0, t)

        """plot output"""
        asfont = {'fontname': 'Arial'}
        hfont = {'fontname': 'Helvetica'}

        #plt.plot(t, sol[:, 0])
        #plt.plot(t, sol[:, 1])
        #plt.plot(t, sol[:, 2])
        plt.plot(t, sol[:, 3])
        #plt.legend(['EL222 bound to promoter', 'mRNA', 'Translated protein', 'Surface-expressed protein',], bbox_to_anchor=(1, 0.5))

        plt.legend(['2 W/$m^2$', '14 W/$m^2$', '27 W/$m^2$', '40 W/$m^2$'], loc='lower right')
        #plt.title('Figure 2: Effect light intensity has on the rate of intimin expression on the cell surface',**asfont )
        plt.ylabel('Concentration (uM)',**asfont)
        plt.xlabel('Time (hr)',**asfont)
        plt.title('Figure 2: Effect light intensity has on the rate of intimin expression on the cell surface ', fontsize=10, y=1.08)
        plt.legend(loc=1, borderaxespad=0)
        plt.ticklabel_format(style='sci', axis='y', scilimits=(0, 0))

