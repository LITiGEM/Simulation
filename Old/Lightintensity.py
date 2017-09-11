
def light(k, L, n, K1):
    a = 444.6  # Basal expression level of the promoter (microM)

    # k: Maximum expression due to induction (a.u.)
    # K1:Hill constant (W/m^2)
    # n: Hill coefficient
    # a: Basal expression level of the promoter (microM)
    # L: Light intensity (W)

    k1 = a + ((k * (L) ^ n) / ((k) ^ n + (L) ^ n))

    k1_induction_array.append(k1)

    return k1

light_pulsing=0

def pulsing(k1,t):
    k1_pulsing_array = []
    DFracON = 2 / 24
    k1_pulse = 0
    for t in range(86400) :
        if (t >7200):# ) > (t/ 86400) + DFracON:
            k1_pulse= 0
        else:
            k1_pulse= (k1*(math.sin((((t/ 86400 -(t/ 86400)))*math.pi)//(1 - DFracON))));
        k1_pulsing_array.append(k1_pulse)

    return k1_pulse