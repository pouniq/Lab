import random
import numpy as np
import pandas as pd

class Pps:
    def __init__(self,x_i):
        self.x_i = np.array(x_i)
        self.t_i = np.cumsum(x_i)
        self.prob = x_i / self.t_i
        self.df = pd.DataFrame({
            'x_i': x_i,
            't_i': self.t_i,
            'probability': x_i/self.t_i
        })

    
    
l = [100, 110, 150, 130, 210, 70, 500, 540, 700, 80] 
MyList = Pps(l)