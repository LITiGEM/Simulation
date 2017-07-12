#All calculated TF values
TF_conc_array = []

#TF initial concentration
TF_conc = 5

def Induction(L,k1,k2,TF):

    TF_temp = (k1-k2*TF)*L

    TF_conc_array.append(TF_temp)

    return TF_temp

for t in range (0,15):
    TF_conc = Induction(1,1,4,TF_conc)

print(LIF_conc_array)

plt.plot(TF_conc_array)
plt.ylabel('[TF]')
plt.xlabel('t')
plt.show()