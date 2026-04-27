import random
import numpy as np
import pandas as pd

class Pps:
    def __init__(self,x_i,k):
        self.x_i = np.array(x_i)
        self.t_i = np.cumsum(x_i)
        self.prob = x_i / self.t_i
        self.TotalSize = self.t_i[-1]
        self.k = k
        self.sample_idx = self.get_sample
        self.df = pd.DataFrame({
            'x_i': x_i,
            't_i': self.t_i,
            'probability': x_i/self.t_i
        })
        
    def get_sample(self):
        # we choose k number of sample from 1 to end of the cumulative summation
        idx = np.random.choice(range(1,self.TotalSize+1) , size = self.k)
        samples = []
        for i in idx:
            for j in self.t_i:
                if i < j :
                    samples.append(j)
                if len(samples) == self.k:
                    break
        
        
        samples_idx = []    
        t_List = self.t_i.tolist()
        for z in samples:
            f = t_List.index(z)
            samples_idx.append(f)
        return samples_idx
    

    
arr = [100, 110, 150, 130, 210, 70, 500, 540, 700, 80]

Mylist = Pps(arr,6) 
Mylist.df
Mylist.get_sample()

                   
        


    
    



