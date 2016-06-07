'''
Created on Jun 7, 2016

@author: andrewkennedy
'''
from scipy.integrate import odeint
import matplotlib.pyplot as plt
import numpy as np


def main():
    def rhs(X,t,a=-2,b=1):
        R = X[0]
        J = X[1]
        rdot=a*R + b*J
        jdot=b*R + a*J
        return [rdot, jdot]
    figure,axes=plt.subplots(nrows=1,ncols=2)
    ics=[
         (-1,5),
         (5,-1),
         (5,5),
         ]
    for i in range(len(ics)):
        ic=ics[i]
        Tvals = np.linspace(-10, 10, 100)
        Xvals=odeint(rhs,ic,Tvals)
        print Xvals
        if i ==0:
            
            axes[0].plot(Tvals, Xvals[:,0],label="R", color="red")
            axes[0].plot(Tvals, Xvals[:,1],label="J", color="blue")
        else :
            
            axes[0].plot(Tvals, Xvals[:,0], color="red")
            axes[0].plot(Tvals, Xvals[:,1], color="blue")
        axes[0].legend()
        axes[0].set_xlabel("Time") 
        axes[0].set_yscale('log')
        
        axes[1].plot(Xvals[:,0],Xvals[:,1])
        axes[1].set_xlabel("R")
        axes[1].set_ylabel("J")
    
if __name__ == '__main__':
    main()
    plt.show()
    
