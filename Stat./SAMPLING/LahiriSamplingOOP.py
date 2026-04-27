import random

arr = [100, 110, 150, 130, 210, 70, 500, 540, 700, 80]
class Lahiri:
    def __init__(self, x_i,k):
        self.x_i = x_i
        self.M = max(x_i)
        self.N = len(x_i)
        self.k = k
    def get_sample(self):
        
        sample = []
        while len(sample) < self.k:
            i = random.choice(range(1,self.N))
            j = random.choice(range(self.N))
            
            if self.x_i[i] > j:
                sample.append([i,j])
        return sample
                
MyList = Lahiri(arr,3)
MyList.get_sample()