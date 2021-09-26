import snap
import numpy as np
import scipy as cp




# load from text file
G5 = snap.LoadEdgeList(snap.TUNGraph, "datasets\stackoverflow-Java.txt", 0, 1)
print("Problem 3: Java Experts Graph")
#print("Nodes %d, Edges %d" % (G5.GetNodes(), G5.GetEdges()))

components = G5.GetWccs()

component_count = 0
for component in components:
    component_count += 1
print("Q1: number of weakly connected components = {}".format(component_count))

# component_dist = G5.GetWccSzCnt()
# print(type(component_dist))
# for item in component_dist:
#    print("number of nodes in connected component %d: number of occurrences %d" % (item.GetVal1(), item.GetVal2()))

print("Q2: edges and nodes in max weakly connected component")
G7 = G5.GetMxWcc()
print(type(G7))
print("Edges %d, Nodes %d" % (G7.GetNodes(), G7.GetEdges()))


print("\nQ3: Top 3 most central nodes by page rank")
page_ranks = G7.GetPageRank()
# x = 0
# for item in page_ranks:
#     print(item, page_ranks[item])
#     x+=1
#     if x==3:
#         break
sorted_page_ranks = dict(sorted(page_ranks.items(), key=lambda item: item[1]))
sprl = list(sorted_page_ranks.items())

print("Top    ranked page is node {} with ranking {}".format(sprl[-1][0], sprl[-1][1]))
print("Second ranked page is node {} with ranking {}".format(sprl[-2][0], sprl[-2][1]))
print("Third  ranked page is node {} with ranking {}".format(sprl[-3][0], sprl[-3][1]))


print("\nQ4: top 3 hubs and top 3 authorities in the network by HITS score ")
hubs, authorities = G5.GetHits()

hubs_sorted_dict = dict(sorted(hubs.items(), key=lambda item: item[1]))
hsl = list(hubs_sorted_dict)
print("Top    hub is {} with ranking {}".format(hsl[-1][0], hsl[-1][1]))
print("Second hub is {} with ranking {}".format(hsl[-2][0], hsl[-2][1]))
print("Third  hub is {} with ranking {}".format(hsl[-3][0], hsl[-3][1]))

auth_sorted_dict = dict(sorted(authorities.items(), key=lambda item: item[1]))
asl = list(auth_sorted_dict)
print("Top    authority is {} with ranking {}".format(asl[-1][0], asl[-1][1]))
print("Second authority is {} with ranking {}".format(asl[-2][0], asl[-2][1]))
print("Third  authority is {} with ranking {}".format(asl[-3][0], asl[-3][1]))



# authorities_sorted = dict(sorted(authorities.items(), key=lambda item: item[1]))


# sprl = list(sorted_page_ranks.items())


# NIdHubH, NIdAuthH = Graph.GetHits()
# for item in NIdHubH:
#     print(item, NIdHubH[item])
# for item in NIdAuthH:
#     print(item, NIdAuthH[item])




# sorted_page_ranks = dict(sorted(page_ranks.items(), key=lambda item: item[1]))
# sprl = list(sorted_page_ranks.items())



# print("Top page rank:  node {}".format(sprl[-1]))
# print("Top page rank:  node {}".format(sprl[-1]))

# print(sprl[-2])
# print(sprl[-3])


# dict_items = a_dictionary.items()

# first_two = list(dict_items)[:2]
# print(first_two)
# OUTPUT




# print(type(foo))


# for NI in UGraph.Nodes():
#     DegCentr = UGraph.GetDegreeCentr(NI.GetId())
#     print("node: %d centrality: %f" % (NI.GetId(), DegCentr))

#     PRankH = Graph.GetPageRank()




#print("Size of component: %d" % CnCom.Len())
#num_weakly_connected_components = G5.GetWccs()

