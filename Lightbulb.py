import matplotlib.pyplot as plt


class Employee:
    'Common base class for all employees'
    empCount = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1

    def displayCount(self):
        print "Total Employee %d" % Employee.empCount

    def displayEmployee(self):
        print "Name : ", self.name, ", Salary: ", self.salary


Employee1 = Employee("brian",4)

Employee1.displayCount()

#All calculated LIF values
LIF_conc_array = []

#LIF concentration
LIF_conc = 5

def lalala(k1,k2,LIF):

    LIF_temp = k1*LIF-k2*LIF

    LIF_conc_array.append(LIF_temp)

    return LIF_temp

for t in range (0,15):
    LIF_conc = lalala(1,4,LIF_conc)

print(LIF_conc_array)

plt.plot(LIF_conc_array)
plt.ylabel('[LIF]')
plt.xlabel('t')
plt.show()