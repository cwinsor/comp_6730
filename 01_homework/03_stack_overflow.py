import snap
import numpy as np
import scipy as cp




# load from text file
G5 = snap.LoadEdgeList(snap.TNGraph, "datasets\stackoverflow-Java.txt", 0, 1)
print("G5: Nodes %d, Edges %d" % (G5.GetNodes(), G5.GetEdges()))
