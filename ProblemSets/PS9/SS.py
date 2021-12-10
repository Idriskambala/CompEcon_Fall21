import numpy as np
import scipy.optimize as opt
import matplotlib.pyplot as plt
import os
import necessary_equations as ne

def ss_solver(c1_guess, r_old, params):
    beta, sigma, t_p, l_tilde, b, upsilon, A, alpha, delta, max_iter, tol, xi = params
    dist = 7
    iter = 0
    while (dist > tol) and (iter < max_iter):
        iter += 1
        r_old = r_old * np.ones(t_p)
        w_old = ne.get_w(r_old, (A, alpha, delta)) * np.ones(t_p)

        # we calculate hh decisions such that last-period savings=0
        c1_args = (r_old, w_old, beta, sigma, l_tilde, b, upsilon, t_p, 0.0)
        result_c1 = opt.root(ne.get_lastb, c1_guess, args = (c1_args))
        if result_c1.success:
            c_1 = result_c1.x
        else:
            raise ValueError("cannot find appropraite initial consumption")

        # aggregagte capital and labour 
        vec_c = ne.get_cons(c_1, r_old, beta, sigma, t_p)
        vec_n = ne.get_n(vec_c, sigma, l_tilde, b, upsilon, w_old, t_p)
        vec_b = ne.get_b(vec_c, vec_n, r_old, w_old, t_p)
        K = ne.get_K(vec_b)
        L = ne.get_L(vec_n)
        r_prime = ne.get_r(K, L, (A, alpha, delta))

        # market clearing
        dist = ((r_prime - r_old) ** 2).max()

        # updating the guess
        r_old = xi * r_prime + (1 - xi) * r_old
        print('iteration:', iter, ' squared distance: ', dist)
    return r_old[0], w_old[0], vec_c, vec_n, vec_b, K, L

#graphs for steady state c, b, n
def ss_graphs(c_ss, b_ss, n_ss):
    cur_path = os.path.split(os.path.abspath(__file__))[0]
    output_fldr = "ps9_images"
    output_dir = os.path.join(cur_path, output_fldr)
    if not os.access(output_dir, os.F_OK):
        os.makedirs(output_dir)

    plt.plot (1 + np.arange(c_ss.shape[0]), b_ss, color = 'orange', label = 'savings')
    plt.grid(b=True, which='major', color='0.40', linestyle='-')
    plt.title('SS Savings', fontsize=8)
    plt.xlabel('age')
    plt.ylabel('savings')
    plt.legend()
    output_path1 = os.path.join(output_dir, 'savings')
    plt.savefig(output_path1)
    plt.close()

    plt.plot (1 + np.arange(c_ss.shape[0]), c_ss, color = 'blue', label = 'consumption')
    plt.grid(b=True, which='major', color='0.40', linestyle='-')
    plt.title('SS Consumption', fontsize=8)
    plt.xlabel('age')
    plt.ylabel('units of consumption')
    plt.legend()
    output_path2 = os.path.join(output_dir, 'consumption')
    plt.savefig(output_path2)
    plt.close()

    plt.plot (1 + np.arange(c_ss.shape[0]), n_ss, color = 'red', label = 'labor supply')
    plt.grid(b=True, which='major', color='0.40', linestyle='-')
    plt.title('SS Labor Supply', fontsize=8)
    plt.xlabel('age')
    plt.ylabel('labor supply')
    plt.legend()
    output_path3 = os.path.join(output_dir, 'labour supply')
    plt.savefig(output_path3)
    plt.close()