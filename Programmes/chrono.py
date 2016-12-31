def chronometre(n):
    import time
    import matplotlib.pyplot as plt
    import numpy as np
    temps=time.time()
    while 1:
        y=time.time()-temps
        if int(y) == n:
            plt.ylim([0,y+2])
            plt.xlim([0,y+2])
            plt.plot([0.0, y*0.5], [y, y],'k-',lw=2)
            plt.plot([y*0.5, y*0.5], [0, y],'k-',lw=2)
            plt.text(y*0.5,y,'TEMPS')              
            plt.show()
            break
            
def chronometre():
    global y
    temps=time.time()
    y=time.time()-temps  
    while 1:
        y=time.time()-temps       
    
    return y        
        
def affichage_chrono(chrono):
    global y
    if chrono == 1:
        plt.ylim([0,y+2])
        plt.xlim([0,y+2])
        plt.plot([0.0, y*0.5], [y, y],'k-',lw=2)
        plt.plot([y*0.5, y*0.5], [0, y],'k-',lw=2)
        plt.text(y*0.5,y,'TEMPS')              
        plt.show()
       
   
         