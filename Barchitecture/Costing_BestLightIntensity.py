import matplotlib.pyplot as plt

costArray = []
# We created a cost array to input all the costs we calculate for the different Light Intensities
# and pulsing frequencies we want to test

def Cost(L):

    # L represents the price per hour for each light intensity we tested

    P=120
    cost = L * P
    # Cost for operating our Light Induced Technology for 2 hours

    costArray.append(cost)

    return cost

L_range = [ 0, 0.05, 0.1, 0.20, 0.25]
#L_range array represents the price per hour for: [ 0 W/m^2, 10 W/m^2, 20 W/m^2, 30 W/m^2, 40 W/m^2, 50 W/m^2, 60 W/m^2, 70 W/m^2]

#P_range = [ 120, 80,  60, 45, 30, 15, 0]
#P_range where the operating time is 2 hours

for L in L_range:
    finalCost = Cost(L)

print(costArray)

plt.style.use('ggplot')
plt.plot(L_range, costArray)
plt.title('Light Intensity effect on costing')
x=L_range
my_xticks = ['0', '18', '35', '53', '70']
plt.xticks(x, my_xticks)
plt.ylabel('Cost for 120 minute operation (£)')
plt.xlabel('Light Intensity (W/$m^2$)')
plt.show()