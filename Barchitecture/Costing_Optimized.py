import matplotlib.pyplot as plt

pulsing_cost_array = []
# We created a cost array to input all the costs we calculate for the different Light Intensities
# and pulsing frequencies we want to test

def CostPulsing(P1):

    # L represents the price per hour for each light intensity we tested

    L1 = 0.1 # (£/hr) hourly rate for 35 W/m^2 Light Intensity lightbulb

    cost = L1 * P1
    # Cost for operating our Light Induced Technology for 2 hours

    pulsing_cost_array.append(cost)

    return cost

light_cost_array=[]

def CostIntensity(L):

    # L represents the price per hour for each light intensity we tested

    P = 60 # (minute) duration of pulsing

    cost = L * P
    # Cost for operating our Light Induced Technology for 2 hours

    light_cost_array.append(cost)

    return cost

L_range = [ 0, 0.05, 0.1, 0.20, 0.25]
#L_range array represents the price per hour for: [ 0 W/m^2, 10 W/m^2, 20 W/m^2, 30 W/m^2, 40 W/m^2, 50 W/m^2, 60 W/m^2, 70 W/m^2]

#P_range = [ 120, 80,  60, 45, 30, 15, 0]
#P_range where the operating time is 2 hours

for L in L_range:
    intensityCost = CostIntensity(L)

P1_range = [120, 80, 60, 30, 15]
# P_range where the operating time is 2 hours

for P1 in P1_range:
    pulsingCost = CostPulsing(P1)

plt.style.use('ggplot')
fig, ax1 = plt.subplots()

ax2 = ax1.twinx()
ax1.plot(light_cost_array, L_range, 'g-')
ax2.plot(pulsing_cost_array, P1_range, 'b-')

ax1.set_xlabel('Cost for 120 minute operation (£)')
ax1.set_ylabel('Light Intensity (W/$m^2$)', color='g')
ax2.set_ylabel('Pulsing duration (minutes)', color='b')

plt.show()





