import snap
import numpy as np
import matplotlib.pyplot as plt

toy = False
if (toy):
    # create a graph PNGraph
    G1 = snap.TNGraph.New()
    G1.AddNode(1)
    G1.AddNode(2)
    G1.AddNode(3)

    G1.AddEdge(1,2)
    G1.AddEdge(2,1)
    G1.AddEdge(1,3)
    G1.AddEdge(1,1)
else:
    # load from text file
    G1 = snap.LoadEdgeList(snap.TNGraph, ".\datasets\Wiki-Vote.txt", 0, 1)

# number of nodes...
print("number of nodes = {}".format(G1.GetNodes()))
print("number of edges = {}".format(G1.GetEdges()))

def out_degree(node):
    out_edges = set()
    for id in node.GetOutEdges():
        out_edges.add(id)

    # in-degree, out-degree
    out_degree = len(out_edges)
    return out_degree

out_degree_list = []
for NI in G1.Nodes():
    this_out_degree = out_degree(NI)
    if this_out_degree > 0:
        out_degree_list.append(this_out_degree)

min_bin = min(out_degree_list)
max_bin = max(out_degree_list)
bins=np.logspace(np.log10(min_bin),np.log10(max_bin), 20)


plt.hist(
    x=out_degree_list,
    bins=bins,
    range=None,
    density=False,
    weights=None,
    cumulative=False,
    bottom=None,
    histtype='bar',
    align='mid',
    orientation='vertical',
    rwidth=None,
    log=True,
    color=None,
    # label="",
    stacked=False,
    data=None)

#plt.plot(out_degree_list)
plt.xlabel('Out-Degree')
plt.ylabel('Count')
plt.title("Out Degree (log-log) of the Wikipedia Voters Network")
plt.show()

