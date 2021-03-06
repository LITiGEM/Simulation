import matplotlib.pyplot as plt

k1_rate_array = []

def light(k,L,n,K1):

    a=444.6
    # k:  Maximum expression due to induction
    # K1: Hill constant
    # n: Hill coefficient
    # a: basal expression level of the promoter
    # L: light intensity (W/m^2)

    k1 =a+((k*(L)^n)/((k)^n+(L)^n))

    k1_rate_array.append(k1)

    return k1

L_range= [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

for L in L_range:
    light_intensity = light( 1545, L, 2, 6.554)

print(k1_rate_array)

plt.plot(k1_rate_array)
plt.ylabel('k$_1$')
plt.xlabel('Light Intensity (W/$m^{2}$)')
plt.show()