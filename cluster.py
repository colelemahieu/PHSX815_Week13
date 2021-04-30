# HW 14

# import packages
import sys
import numpy as np
import matplotlib.pyplot as plt
from math import *
from Random import Random

# instantiate Random class
random = Random()

# number of samples
samples = 1000

# flip coin to choose which distribution to sample
# and save the samples to plot
data_x = []
data_y = []
for i in range(0,samples):
    flip = random.Bernoulli()

    if flip==1:
        norm1_x = random.box_muller(6,1)
        norm1_y = random.box_muller(6,1)
        data_x.append(norm1_x)
        data_y.append(norm1_y)
    if flip==0:
        norm2_x = random.box_muller(9,1)
        norm2_y = random.box_muller(9,1)
        data_x.append(norm2_x)
        data_y.append(norm2_y)

# k means clustering

# inital guesses
c1_x=9
c1_y=6
c2_x=6
c2_y=8

# print the guess
print("The real centers are at (9,9) and (6,6)")

iterations = 4
for k in range(0,iterations):
    cluster1_x = []
    cluster1_y = []
    cluster2_x = []
    cluster2_y = []
    x1_total = 0
    y1_total = 0
    x2_total = 0
    y2_total = 0
    for i in range(0, samples):
        d1 = sqrt((data_x[i]-c1_x)**2 + (data_y[i]-c1_y)**2)
        d2 = sqrt((data_x[i]-c2_x)**2 + (data_y[i]-c2_y)**2)
        if (d1<d2):
            cluster1_x.append(data_x[i])
            cluster1_y.append(data_y[i])
        if (d2<d1):
            cluster2_x.append(data_x[i])
            cluster2_y.append(data_y[i])
    for j in range(0, len(cluster1_x)):
        x1_total = x1_total + cluster1_x[j]
        y1_total = y1_total + cluster1_y[j]
    for j in range(0, len(cluster2_x)):
        x2_total = x2_total + cluster2_x[j]
        y2_total = y2_total + cluster2_y[j]
    c1_x = float(x1_total) / len(cluster1_x)
    c1_y = float(y1_total) / len(cluster1_y)
    c2_x = float(x2_total) / len(cluster2_x)
    c2_y = float(y2_total) / len(cluster2_y)

# print calculated values
print("The calculated centers are at (%f, %f) and (%f, %f)" %(c1_x, c1_y, c2_x, c2_y))
    

# plotting
plt.figure()
plt.scatter(cluster1_x, cluster1_y, label="cluster 1")
plt.scatter(cluster2_x, cluster2_y, label="cluster 2")
plt.scatter(c1_x, c1_y, color="red",label="cluster center")
plt.scatter(c2_x, c2_y, color="red")
plt.title("K Means Clusters")
plt.xlabel("X Value")
plt.ylabel("Y Value")
plt.legend()
plt.show()
        


