import numpy as np
import SS as ss

# Parameters
sigma = 1.5
l_tilde = 1.0
b = 0.501
upsilon = 1.554
alpha = 0.30
A = 1.0
yrs_lived = 90 #individual lived for 90 years
S = 100 #total total period
beta_annual = .96
beta = beta_annual ** (yrs_lived / S)
delta_yr = 0.05
delta = 1.0 - ((1.0 - delta_yr) ** (yrs_lived / S))
ss_solve = True
max_iter = 400
tol = 1e-9
xi = 0.1
chi_n_vec = 1.0 * np.ones(S)

if ss_solve:
    c1_guess = 1
    r_old = 0.1
    params = (beta, sigma, S, l_tilde, b, upsilon, A, alpha, delta, max_iter, tol, xi)
    r_ss, w_ss, c_ss, n_ss, b_ss, K_ss, L_ss = ss.ss_solver(c1_guess, r_old, params)
    ss.ss_graphs(c_ss, b_ss, n_ss)