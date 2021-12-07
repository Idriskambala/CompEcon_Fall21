{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "2c99ebb2",
   "metadata": {},
   "outputs": [
    {
     "ename": "NameError",
     "evalue": "name 'null' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-2-01a49f1064bc>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[1;32m----> 1\u001b[1;33m \u001b[1;32mimport\u001b[0m \u001b[0mfunctions\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[1;32m~\\Desktop\\Computational\\CompEcon_Fall21\\DynamicProgramming\\functions.py\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[0;32m     74\u001b[0m   {\n\u001b[0;32m     75\u001b[0m    \u001b[1;34m\"cell_type\"\u001b[0m\u001b[1;33m:\u001b[0m \u001b[1;34m\"code\"\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m---> 76\u001b[1;33m    \u001b[1;34m\"execution_count\"\u001b[0m\u001b[1;33m:\u001b[0m \u001b[0mnull\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m     77\u001b[0m    \u001b[1;34m\"id\"\u001b[0m\u001b[1;33m:\u001b[0m \u001b[1;34m\"37aff18f\"\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m     78\u001b[0m    \u001b[1;34m\"metadata\"\u001b[0m\u001b[1;33m:\u001b[0m \u001b[1;33m{\u001b[0m\u001b[1;33m}\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mNameError\u001b[0m: name 'null' is not defined"
     ]
    }
   ],
   "source": [
    "import functions"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "974ef904",
   "metadata": {},
   "source": [
    "# grid for a and c"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "efb48ee8",
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
   "id": "5df5825c",
   "metadata": {},
   "source": [
    "# parameters"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "df303b3e",
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
   "execution_count": null,
   "id": "8b4d16ad",
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
   "execution_count": null,
   "id": "ff3c0c85",
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
   "execution_count": null,
   "id": "5d825283",
   "metadata": {},
   "outputs": [],
   "source": [
    "#the v function \n",
    "\n",
    "function = functions.value_func(params, u, c, c_1, a_grid, c_grid)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "7a067e06",
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
