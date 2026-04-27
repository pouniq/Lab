# PPS in sampling.

# import library
import random
import numpy as np
import pandas as pd


# make x_i
x_i = [100, 110, 150, 130, 210, 70, 500, 540, 700, 80]
# how many samples
k = 4
sum(x_i)

# choose k number of x_i
select = random.choices(x_i, k=4)
np.mean(select)

# make the t_i
t_i = np.cumsum(x_i)

df = pd.DataFrame()
df["x_i"] = x_i
df["t_i"] = t_i
df["prob"] = x_i / t_i[-1]

sampleChoose = list(range(1, t_i[-1] + 1))
sampleChoosen = random.choices(sampleChoose, k=k)
samples = []
for i in sampleChoosen:
    for j in t_i:
        if i < j:
            print(j)
            samples.append(j)
        if len(samples) == k:
            break

t_i = t_i.tolist()

theSamplesWeChoose = []
for i in samples:
    f = t_i.index(i)
    theSamplesWeChoose.append(f)
