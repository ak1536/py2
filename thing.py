import numpy as np
import matplotlib.pyplot as plt

def main (n=901):
    x= np.random.uniform(low=-1,high=1,size=(n,));
    x.sort()

    y=x**3 + x**2+ 0.05*np.random.uniform(low=-1,high=1,size=(n,)) ;
    unused_figure,axes=plt.subplots(nrows=1, ncols=2)
    axis=axes[0]
    axis.scatter(x,y)
    axis=axes[1]
    axis.plot(x,y)
    
#     figure=plt.figure();
#     axis=figure.add_subplot(1 ,1, 1);
    
if __name__=="__main__":
    main()
    plt.show()
    
    print np
    
    
    
