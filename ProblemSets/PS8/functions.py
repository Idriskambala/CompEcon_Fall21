#the code is taking too long to run. There are no error messages but it is just taking too long,
# and I need to work other assignments. I am sure smth it is about the many loops I have. 
#Probably I didn't write the loops correctly. In the semester break I will look at it again. 

import numpy as np
from scipy import interpolate
from scipy.optimize import fminbound
# %%
def utility(a, aprime, c_1, alpha, R, Y):
    """
    Per period utility function
    """
    c = Y + (1 + R) * a - aprime
    try:
        c[c<=0] = 1e-10 # replace 0 and negative consumption with a tiny value - to impose non-negativity on cons
    except TypeError:
        if c <= 0:
            c = 1e-10
    if [c < c_1]:
        u = np.log(c + 1e-7)
    else:
        u = np.log(c - alpha * c_1 + 1e-7) #I add a small number 1e-7 to avoid negative logs
        
    return u
# %%
def bellmanoperator(V, a_grid, c_grid, params):
    alpha, R, Y, beta = params
    V_func = interpolate.interp2d(a_grid, c_grid, V, kind='cubic')

    TV = np.empty_like(V)
    opta = np.empty_like(TV)

    # : max_a' { u(c,c_1) + beta V(a', c)} #but c = f(a, aprime)
    #This is Equation 2 
    for i, a in enumerate(a_grid):
        def objective(aprime):
            return - utility(a, aprime, c_1, alpha, R, Y) - (beta * V_func(aprime, c))

        aprime_star = fminbound(objective, 1e-6, a - 1e-6)
        opta[i] = aprime_star
        TV[i] = - objective(aprime_star)

    return TV, opta
    # %%