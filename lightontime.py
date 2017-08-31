import matplotlib.pyplot as plt

light_pulsing=0

k1_pulsing_array =[]
k1=458.4
k1_pulse = k1

def pulsing(k1,t):

        if t>43200 and t<0:
            k1_pulse = 0
        else:
            k1_pulse=k1
            k1_pulsing_array.append(k1_pulse)

        return k1_pulse


for t in range (0,86400):
    light_pulsing = pulsing( 458.4, t)

print(k1_pulsing_array)

plt.plot(k1_pulsing_array)
plt.ylabel('k$_1$')
plt.xlabel('Time')
plt.show()

