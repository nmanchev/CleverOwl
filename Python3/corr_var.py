# -*- coding: utf-8 -*-
"""
(C) 2016 Nikolay Manchev, [CleverOwl blog](http://http://www.cleverowl.uk)

This work is licensed under the Creative Commons Attribution 4.0 International
License. To view a copy of this license, visit
http://creativecommons.org/licenses/by/4.0/.
"""

from math import pi
from math import sin

import matplotlib.pyplot as plt

import numpy as np

def corr_vars( start=-10, stop=10, step=0.5, mu=0, sigma=3, func=lambda x: x ):
    """
    Generates a data set of (x,y) pairs with an underlying regularity. y is a
    function of x in the form of
    
    y = f(x) + e
    
    Where f(x) is specified by the *func* argument and e is a random Gaussian
    noise specified by *mu* and *sigma*.
    
    Keyword arguments:

      *start* : number, optional
        Start of the x interval.  Defaults to -10.
        
      *stop* : number, optional
        End of the x interval.  Defaults to 10.

      *step* : number, optional
        Spacing between x values. Defaults to 0.5.

      *mu* : number, optional
        Mean of the distribution generating the noise. Defaults to 0.

      *sigma* : number, optional
        Standard deviation of the distribution generating the noise. 
        Defaults to 3.

      *func* : function, optional
        Function for calculating the y values using x. Defaults to y = x.
   
   Returns: 

   x,y : tuple
       
       - *x* is a Numpy array of values in [*start*, *stop*]
       - *y* is calculated as y = *func* (x) + e

    Examples::

        (x,y) = corr_vars(sigma=3, func=lambda x: 2*pi*sin(x))

    """

    # Generate x
    x = np.arange(start, stop, step)    
    
    # Generate random noise
    e = np.random.normal(mu, sigma, x.size)
    
    # Generate y values as y = func(x) + e
    y = np.zeros(x.size)
    
    for ind in range(x.size):
        y[ind] = func(x[ind]) + e[ind]
    
    return (x,y)

def main():

    np.random.seed(2)

    (x0,y0) = corr_vars(sigma=3)   
    (x1,y1) = corr_vars(sigma=3, func=lambda x: 2*pi*sin(x))   

    f, axarr = plt.subplots(2, sharex=True, figsize=(7,7))

    axarr[0].scatter(x0, y0)        
    axarr[0].plot(x0, x0, color='r')
    axarr[0].set_title('y = x + e')
    axarr[0].grid(True)

    axarr[1].scatter(x1, y1)        
    axarr[1].plot(x1, 2*pi*np.sin(x1), color='r')
    axarr[1].set_title('y = 2*π*sin(x) + e')
    axarr[1].grid(True)

    
if __name__ == "__main__":
    main()    
