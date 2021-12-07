{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "eeceaf6a",
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy as np\n",
    "import matplotlib.pyplot as plt\n",
    "import numpy as np\n",
    "import matplotlib.pyplot as plt\n",
    "from scipy import interpolate\n",
    "import scipy.optimize as opt\n",
    "import scipy \n",
    "from scipy.optimize import fminbound\n",
    "\n",
    "# to print plots inline\n",
    "%matplotlib inline"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "0fbc3c6d",
   "metadata": {},
   "outputs": [],
   "source": [
    "def utility(a, aprime, c_1, alpha, R, Y):\n",
    "    \"\"\"\n",
    "    Per period utility function\n",
    "    \"\"\"\n",
    "    c = Y + (1 + R) * a - aprime\n",
    "    \n",
    "    U = np.log(c - alpha * c_1) \n",
    "    \n",
    "    return U "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "a53d740e",
   "metadata": {},
   "outputs": [],
   "source": [
    "def bellmanoperator(V, a_grid, c_grid, params):\n",
    "    alpha, R, Y, beta = params\n",
    "    V_func = interpolate.interp2d(a_grid, c_grid, V, kind='cubic')\n",
    "\n",
    "    TV = np.empty_like(V)\n",
    "    opta = np.empty_like(TV)\n",
    "\n",
    "    # : max_a' { u(c,c_1) + beta V(a', c)} #but c = f(a, aprime)\n",
    "    #This is Equation 2 \n",
    "    for i, a in enumerate(a_grid):\n",
    "        for j, c in enumerate(c_grid):\n",
    "            for x, c_1 in enumerate(c_grid):\n",
    "                def objective(aprime):\n",
    "                    return - utility(a, aprime, c_1, alpha, R, Y) - (beta * V_func(aprime, c))\n",
    "                aprime_star = fminbound(objective, 1e-6, a - 1e-6)\n",
    "                opta[i] = aprime_star\n",
    "                TV[i] = - objective(aprime_star)\n",
    "\n",
    "    return TV, opta"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "1afed745",
   "metadata": {},
   "outputs": [],
   "source": [
    "#parameters\n",
    "beta = 0.95 #time preference\n",
    "alpha = 0.5 #This measures the intensity of habit formation and also denotes the nonseparability of preferences over time\n",
    "Y = 100 #exogenous income\n",
    "R = 1 #interest rate\n",
    "\n",
    "#grids\n",
    "a_lb = 0.1\n",
    "a_ub = 4\n",
    "size_a = 200\n",
    "size_c = 200\n",
    "a_grid = np.linspace(a_lb, a_ub, size_a)\n",
    "c_grid = np.linspace(a_lb, a_ub, size_c)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "4136fa6e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "iteration  1 , distance =  4.663439031577435\n"
     ]
    }
   ],
   "source": [
    "#value function iteration\n",
    "VFtol = 1e-5\n",
    "VFdist = 7.0 \n",
    "VFmaxiter = 200 \n",
    "V = np.zeros((size_a, size_c))\n",
    "Vstore = np.zeros((size_a, size_c, VFmaxiter))\n",
    "VFiter = 1 \n",
    "V_params = (alpha, R, Y, beta)\n",
    "while VFdist > VFtol and VFiter < VFmaxiter:\n",
    "    Vstore[:, VFiter] = V\n",
    "    TV, opta = bellmanoperator(V, a_grid, c_grid, V_params)\n",
    "    VFdist = (np.absolute(V - TV)).max()  \n",
    "    print('iteration ', VFiter, ', distance = ', VFdist)\n",
    "    V = TV\n",
    "    VFiter += 1\n",
    "   \n",
    "\n",
    "if VFiter < VFmaxiter:\n",
    "    print('coverged after:', VFiter)\n",
    "else:\n",
    "    print('did not converge')\n",
    "\n",
    "VF = V "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "b2eb4be4",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
