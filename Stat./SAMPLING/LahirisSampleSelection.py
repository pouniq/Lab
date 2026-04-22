import random

x_i = [100,110,150,130,210,70,500,540,700,80]
M= max(x_i)
N = len(x_i)
k = 6

MAX_ATEMPTS = 1000
sample = []       
while len(sample) < k:
    i = random.choice(range(1,N))
    j = random.choice(range(1,M))

    if x_i[i] < j:
        sample.append([i,j])

