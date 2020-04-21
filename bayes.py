import numpy as np
from matplotlib import pyplot as plt
from numpy import pi,sqrt
import random

def gauss(x,a):
    '''
    Takes 2 arguments, first argument is variable of the gaussian
    Second is the parameter a

    returns the gaussian distribution in arbitrary base with proper normalization
    '''
    g=(sqrt(np.log(np.abs(a))/(2*pi)))*(a**(-(x**2)/2))
    
    
    return 
    
def metropolis_hastings(a_t,x,t):
    '''
    input: first guess of a, data set for x, number of iteration

    return: distribution of a value
    '''
    a=np.zeros(t)
    
    for j in range(t):
        
        
        #Since we defined the gauss function with arbitrary base and normalization, we need a > 1
        while True:
            a_tp1=np.random.normal(a_t,1,1)
            if a_tp1>1:
                break
        
        #Initialization of probability product for indipendent multivariable distribution
        prob_t=1
        prob_tp1=1
        
        #Evaluation of probability density for indipendent multivariable distribution
        for i in range(len(x)):
            prob_t=prob_t*gauss(x[i],a_t)
        for i in range(len(x)):
            prob_tp1=prob_tp1*gauss(x[i], a_tp1)
        
        c=prob_tp1/prob_t
        #Control in case the ratio is NaN
        if np.isnan(c):
            c=0
        
        #Acceptance or rejection of the value
        A=[1,c]
        u=random.random()
        acept=min(A)
        
        if u <= acept:
            a[j]=a_tp1
            a_t=a_tp1
        else:
            a[j]=a_t
        
    return a


#Generation of data set according to gaussian distribution

x=np.random.normal(0,1,200)


#test the distribution with Metropolis Hasting algorithm 
a=metropolis_hastings(3,x,2000)
a.max()
fig=plt.figure()
plt.hist(a,50)
plt.show()