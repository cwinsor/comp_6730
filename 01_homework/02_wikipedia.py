import snap
import numpy as np
import scipy as cp


# load from text file
G5 = snap.LoadEdgeList(snap.TNGraph, ".\datasets\Wiki-Vote.txt", 0, 1)
print("G5: Nodes %d, Edges %d" % (G5.GetNodes(), G5.GetEdges()))


import matplotlib.pyplot as plt
plt.plot([1, 2, 3, 4])
plt.ylabel('some numbers')
plt.show()


