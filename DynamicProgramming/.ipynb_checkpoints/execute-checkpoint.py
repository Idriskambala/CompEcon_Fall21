{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "ab5b3720",
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy as np\n",
    "import matplotlib.pyplot as plt\n",
    "import numpy as np\n",
    "import matplotlib.pyplot as plt\n",
    "from scipy import interpolate\n",
    "import scipy \n",
    "import functions"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "ae8e58cb",
   "metadata": {},
   "source": [
    "# grid for a and c"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "6e2f3e9e",
   "metadata": {},
   "outputs": [],
   "source": [
    "#create a grid for the cake size\n",
    "a_lb = 0.1\n",
    "a_ub = 4\n",
    "size_a = 300\n",
    "size_c = 300\n",
    "a_grid = np.linspace(a_lb, a_ub, size_a)\n",
    "c_grid = np.linspace(a_lb, a_ub, size_c)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "16b06538",
   "metadata": {},
   "source": [
    "# parameters"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "87b831ad",
   "metadata": {},
   "source": [
    "Paramters \\\n",
    "$\\beta = 0.95 $  time preference \\\n",
    "$\\alpha = 0.50 $  This measures the intensity of habit formation and also denotes the nonseparability of preferences over time \\\n",
    "R = 1  interest rate \\\n",
    "y = 100 exogenous income "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "5ff59eeb",
   "metadata": {},
   "outputs": [],
   "source": [
    "beta = 0.95\n",
    "alpha = 0.5\n",
    "R = 1\n",
    "Y = 100\n",
    "params = [alpha, Y, R, beta]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "8ab4e931",
   "metadata": {},
   "outputs": [],
   "source": [
    "#initial guesses\n",
    "u = np.zeros((size_a,size_c))\n",
    "c = np.zeros((size_a,size_c))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "70c43205",
   "metadata": {},
   "outputs": [
    {
     "ename": "NameError",
     "evalue": "name 'functions' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-5-3475a8119c18>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[0;32m      1\u001b[0m \u001b[1;31m#the v function\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      2\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m----> 3\u001b[1;33m \u001b[0mfunction\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mfunctions\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mvalue_fi\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mparams\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0ma_grid\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mc_grid\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mu\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mc\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[1;31mNameError\u001b[0m: name 'functions' is not defined"
     ]
    }
   ],
   "source": [
    "#the v function \n",
    "\n",
    "function = functions.value_fi(params, a_grid, c_grid, u, c)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "04d968ef",
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