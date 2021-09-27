import snap
import numpy as np
import scipy as cp

toy = False
if (toy):
    # create a graph PNGraph
    G5 = snap.TNGraph.New()
    G5.AddNode(11)
    G5.AddNode(12)
    G5.AddNode(13)
    G5.AddNode(14)
    G5.AddNode(15)
    G5.AddNode(16)
    G5.AddNode(17)
    G5.AddNode(18)
    G5.AddNode(19)

    G5.AddEdge(11,13)
    G5.AddEdge(12,13)
    G5.AddEdge(13,14)
    G5.AddEdge(13,15)
    G5.AddEdge(16,17)
    G5.AddEdge(17,18)
    G5.AddEdge(17,19)

else:
    # load from text file
    G5 = snap.LoadEdgeList(snap.TNGraph, "datasets\stackoverflow-Java.txt", 0, 1)

print("Problem 3: Java Experts Graph")
print("Nodes %d, Edges %d" % (G5.GetNodes(), G5.GetEdges()))

components = G5.GetWccs()

component_count = 0
for component in components:
    component_count += 1
print("\nQ1: The number of weakly connected components = {}".format(component_count))

# component_dist = G5.GetWccSzCnt()
# print(type(component_dist))
# for item in component_dist:
#    print("number of nodes in connected component %d: number of occurrences %d" % (item.GetVal1(), item.GetVal2()))

print("\nQ2: The number of nodes and edges in max weakly connected component")
G7 = G5.GetMxWcc()
print("Nodes %d, Edges %d" % (G7.GetNodes(), G7.GetEdges()))


print("\nQ3: The top 3 most central nodes in the network by page rank")
page_ranks = G5.GetPageRank()
# for item in page_ranks:
#     print(item, page_ranks[item])

sorted_pr = dict(sorted(page_ranks.items(), key=lambda item: item[1], reverse=True))
n = 1
for key, value in sorted_pr.items():
    print("The number {} ranked page is node {} with ranking {}".format(n, key, value))
    if n==3:
        break
    n+=1


print("\nQ4a: The top 3 hubs in the network by HITS score ")
hubs, authorities = G5.GetHits()
# for item in hubs:
#     print(item, hubs[item])

sorted_hubs = dict(sorted(hubs.items(), key=lambda item: item[1], reverse=True))
n = 1
for key, value in sorted_hubs.items():
    print("The number {} hub is node {} with value {}".format(n, key, value))
    if n==3:
        break
    n+=1

print("\nQ4b: The top 3 authorities in the network by HITS score ")
# for item in authorities:
#     print(item, authorities[item])

sorted_authorities = dict(sorted(authorities.items(), key=lambda item: item[1], reverse=True))
n = 1
for key, value in sorted_authorities.items():
    print("The number {} authority is node {} with value {}".format(n, key, value))
    if n==3:
        break
    n+=1


