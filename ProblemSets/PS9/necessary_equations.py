import numpy as np
import scipy.optimize as opt

def get_w(r, params): # wage
    '''
    function to compute wage
    r = interest rate
    '''
    A, alpha, delta = params
    w = (1 - alpha) * A * (((alpha * A) / (r + delta)) ** (alpha / (1 - alpha)))
    return w

def get_r(K, L, params): # interest rate
    '''
    function to compute interest rate
    '''
    A, alpha, delta = params
    r = alpha * A * ((L / K) ** (1 - alpha)) - delta
    return r

def get_L(vec_n): # labour
    ''''
    function to compute aggregate labour supply
    vec_n = vector of lifetime labour supply
    '''
    L = vec_n.sum()
    return L

def get_K(vec_b): # capital
    ''''
    function to compute aggreggate capital supply
    vec_b = vector of lifetime savings 
    '''
    K = vec_b.sum()
    return K

def get_cons(c_1, r, beta, sigma, t_p): # consumption
    '''
    function to compute consumption
    vec_c = vector of lifetime consumption
    cs = current consumption
    c1 = initial consumption
    t_p = numer of time periods remaining
    '''
    vec_c = np.zeros(t_p)
    vec_c[0] = c_1
    cs = c_1
    s = 0
    while s < t_p - 1:
        vec_c[s + 1] = cs * (beta * (1 + r[s + 1])) ** (1 / sigma) #transition eqution for cons (from the FOCs/euler eqn)
        cs = vec_c[s + 1]
        s += 1
    return vec_c

def muc_func(vec_c, sigma): #marginal utility of consumption
    '''
    function to compute MU of cons
    vec_c = vector of lifetime consumption
    mu_c = mu of consumption
    '''
    mu_c = vec_c ** (-sigma)

    return mu_c

def mun_func(vec_n, params): #marginal (dis)utility of labour supply
    ''''
    function to compute marginal (dis)utility of labour supply
    mu_n = marginal (dis)utility of labour supply
    vec_n = vector of lifetime labour supply
    '''
    l_tilde, b, upsilon = params

    mu_n = ((b / l_tilde) * ((vec_n / l_tilde) ** (upsilon - 1)) * (1 - ((vec_n / l_tilde) ** upsilon)) **\
           ((1 - upsilon) / upsilon))

    return mu_n

def get_b(vec_c, vec_n, r, w, t_p, bs = 0.0): # savings
    ''''
    function to compute lifetime savings
    vec_b = vector of lifetime savings
    bs = initial savings/bonds = 0.0
    t_p = number of time periods remaining
    s = current period
    w = wage per period
    vec_n = vector of lifetime labour supply
    vec_c = vector of lifetime consumption
    '''
    vec_b = np.zeros(t_p)
    s = 0
    vec_b[0] = bs
    while s < t_p - 1:
        vec_b[s + 1] = (1 + r[s]) * bs + w[s] * vec_n[s] - vec_c[s] #transiton equation for savings from the BC
        bs = vec_b[s + 1]
        s += 1
    return vec_b

def get_n_errors(vec_n, *args): # euler errors
    ''''
    function to compute euler errors of labour supply
    n_errors = euler errors of labour supply
    '''
    vec_c, sigma, l_tilde, b, upsilon, w = args
    mu_c = muc_func(vec_c, sigma)
    mu_n = mun_func(vec_n, (l_tilde, b, upsilon))
    n_errors = w * mu_c - mu_n
    return n_errors

def get_n(vec_c, sigma, l_tilde, b, upsilon, w, t_p): #  labor supply
    '''
    function to compute labour supply
    n_guess = initial guess of labour supply
    '''
    n_args = (vec_c, sigma, l_tilde, b, upsilon, w)
    n_guess = 0.5 * l_tilde * np.ones(t_p)
    result = opt.root(get_n_errors, n_guess, args = (n_args), method = 'lm')
    if result.success:
        vec_n = result.x
    else:
        raise ValueError("cannot find appropriate labor decision")
    return vec_n

def get_lastb(c_1, *args): # last-period savings
    ''''
    function to compute last period savings
    for optimilaity, the individual does not save at s = S
    lastb = last period savings
    '''
    r, w, beta, sigma, l_tilde, b, upsilon, t_p, bs = args
    vec_c = get_cons(c_1, r, beta, sigma, t_p)
    vec_n = get_n(vec_c, sigma, l_tilde, b, upsilon, w, t_p)
    vec_b = get_b(vec_c, vec_n, r, w, t_p, bs)
    lastb = (1 + r[-1]) * vec_b[-1] + w[-1] * vec_n[-1] - vec_c[-1]
    return lastb