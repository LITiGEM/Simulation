light_pulsing=0

k1_pulsing_array =[]
k1=458.4
k1_pulse = k1

def pulsing(k1,t):

        for t in range (86400):

            if t>43200 and t<0:
                k1_pulse = 0
            else:
                k1_pulse=k1
                k1_pulsing_array.append(k1_pulse)

        return k1_pulse

print(k1_pulsing_array)

