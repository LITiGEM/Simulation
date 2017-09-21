import matplotlib.pyplot as plt

costArray = []
# We created a cost array to input all the costs we calculate for the different Light Intensities
# and pulsing frequencies we want to test

def Cost(L,P):

    # L represents the price per hour for each light intensity we tested

    cost = L * P
    # Cost for operating our Light Induced Technology for 2 hours

    costArray.append(cost)

    return cost

#L_range = [ 0.05, 0.15, 0.20, 0.25, 0.30, 0.35, 0.40]
#L_range array represents the price per hour for: [ 0 W/m^2, 10 W/m^2, 20 W/m^2, 30 W/m^2, 40 W/m^2, 50 W/m^2, 60 W/m^2, 70 W/m^2]

P_range = [ 120, 80, 60, 30, 15]
#P_range where the operating time is 2 hours

for P in P_range:
    finalCost = Cost(0.05,P)

print(costArray)

plt.style.use('ggplot')
plt.plot(P_range,costArray)
x=P_range
my_xticks = ['120', '80', '60', '30', '15']
plt.xticks(x, my_xticks)
plt.title('Pulsing frequency effect on costing')
plt.ylabel('Cost for 120 minute operation (£)')
plt.xlabel('Pulse duration (minutes)')
plt.show()