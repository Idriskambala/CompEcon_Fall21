#the code is taking too long to run. There are no error messages but it is just taking too long,
# and I need to work other assignments. I am sure smth it is about the many loops I have. 
#Probably I didn't write the loops correctly. In the semester break I will look at it again. 
import numpy as np
from functions  import utility
from functions  import bellmanoperator
import matplotlib.pyplot as plt
from scipy import interpolate

#parameters
beta = 0.95 #time preference
alpha = 0.5 #This measures the intensity of habit formation and also denotes the nonseparability of preferences over time
Y = 100 #exogenous income
R = 1 #interest rate

#grids
a_lb = 0.1
a_ub = 4
size_a = 200
size_c = 200
a_grid = np.linspace(a_lb, a_ub, size_a)
c_grid = np.linspace(a_lb, a_ub, size_c)

#value function iteration
VFtol = 1e-5
VFdist = 7.0 
VFmaxiter = 200 
V = np.zeros((size_a, size_c))
V_func = interpolate.interp2d(a_grid, c_grid, V, kind='cubic')
Vmat = np.zeros((size_a, size_c, size_c))
Vstore = np.zeros((size_a, size_c, VFmaxiter))
VFiter = 1 
V_params = (alpha, R, Y, beta)
while VFdist > VFtol and VFiter < VFmaxiter:
    for a in range(size_a):
        for aprime in range(size_a):
            for c in range(size_c):
                for c_1 in range(size_c):
                    Vmat[a, c_1, c] = utility(a, aprime, c_1, alpha, R, Y) + (beta * V_func(aprime, c))  
                                
    Vstore[:, VFiter] = V
    TV, opta = bellmanoperator(V, a_grid, c_grid, V_params)
    VFdist = (np.absolute(V - TV)).max()  
    print('iteration ', VFiter, ', distance = ', VFdist)
    V = TV
    VFiter += 1
   

if VFiter < VFmaxiter:
    print('coverged after:', VFiter)
else:
    print('did not converge')

VF = V 

##extract decision rule from solution

optc = Y + (1 + R)*a_grid - opta # optimal consumption 

# Plot value function 
plt.figure()
plt.plot(a_grid[1:], VF[1:])
plt.xlabel('assets/debts')
plt.ylabel('Value Function')
plt.title('Value Function - habit formation')
plt.show()

# value function at several iterations
plt.figure()
fig, ax = plt.subplots()
ax.plot(a_grid, Vstore[:,0], label='1st iter')
ax.plot(a_grid, Vstore[:,10], label='0th iter')
ax.plot(a_grid, Vstore[:,20], label='20th iter')
ax.plot(a_grid, Vstore[:,30], label='30th iter')
ax.plot(a_grid, Vstore[:,40], label='40th iter')
ax.plot(a_grid, Vstore[:,VFiter-1], 'k', label='Last iter')

# legend and some customizations.
legend = ax.legend(loc='lower right', shadow=False)
# Set the fontsize
for label in legend.get_texts():
    label.set_fontsize('large')
for label in legend.get_lines():
    label.set_linewidth(1.5)  # the legend line width
plt.xlabel('assets/debts')
plt.ylabel('Value Function')
plt.title('Value Function - Habit formation')
plt.show()

#plot of policy function
#Plot optimal consumption
plt.figure()
fig, ax = plt.subplots()
ax.plot(a_grid[1:], optc[1:], label='Consumption')
legend = ax.legend(loc='upper left', shadow=False)
# Set the fontsize
for label in legend.get_texts():
    label.set_fontsize('large')
for label in legend.get_lines():
    label.set_linewidth(1.5) 
plt.xlabel('Assets/debts')
plt.ylabel('Optimal Consumption')
plt.title('Policy Function, consumption - Habit formation')
plt.show()