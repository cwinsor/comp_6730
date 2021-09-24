import snap

# create a graph PNGraph
G1 = snap.TNGraph.New()
G1.AddNode(1)
G1.AddNode(2)
G1.AddNode(3)

G1.AddEdge(1,2)
G1.AddEdge(2,1)
G1.AddEdge(1,3)
G1.AddEdge(1,1)

# number of nodes...
print("number of nodes = {}".format(G1.GetNodes()))
print("number of edges = {}".format(G1.GetEdges()))

G1.AddEdge(1,3)
# number of nodes...
print("number of nodes = {}".format(G1.GetNodes()))
print("number of edges = {}".format(G1.GetEdges()))



# number of edges...
self_edge_list = []
directed_edge_list = []
for EI in G1.Edges():
    if (EI.GetSrcNId() == EI.GetDstNId()):
        self_edge_list.append(EI)
    else:
        directed_edge_list.append(EI) 

print("number of nodes with a self-edge = {}".format(len(self_edge_list)))
print("number of nodes with a directed-edge = {}".format(len(directed_edge_list)))


# (5) undirected edged a.k.a. unique unordered pairs
# (a,b) or (b,a) where a!=b and order does not matter
#
# this can also be described as:
# undirected edges, excluding self-edges

# first approach:
# list = []
# for each Node n:
#   for each Edge (a,b):
#     if (a != b) and (b,a) not already in list:
#       add (a,b) to list

# second approach:
# list = []
# for each Edge (a,b):
#   if (a != b):
#     add (a,b) to list   i.e. make an undirected graph
# eliminate duplicates i.e. [(a,b),(b,a)] -> [(a,b)]

# third approach:
# convert graph to undirected graph
# count the number of edges, excluding self-edges
G2 = G1.ConvertGraph(snap.TUNGraph)
# number of non-self-edges...
non_self_edge_list = []
for EI in G2.Edges():
    if (EI.GetSrcNId() != EI.GetDstNId()):
        non_self_edge_list.append(EI)
print("number of undirected edges = {}".format(len(non_self_edge_list)))




# Recripocated pairs is a pair of edges (a->b), (b->a)  where a!=b
# algorithm:
# for each node A, a recripocated pair is where
# there is an out-edge to b, and an in-edge from b
# Since each node has in-edge and out-edge lists we will use those
#
# given a node, return the count of recripocated pair count for that node
#   neighbors_in  is a set: the neighbors in the in_edge list
#   neighbors_out is a set: the neighbors in the out_edge list
#   intersection of neighbors_in, neighbors_out is the recripocated pairs

# def recripocated_pair_count(node):
#     neighbors_out = set()
#     neighbors_in = set()
#     for edge in node.GetOutEdges():
#         neighbors_out.add(edge.GetDstNId())
#     for edge in node.getInEdges():
#         neighbors_in.add(edge.GetSrcNId())
#     # remove self-loop if it exists
#     neighbors_out.remove(node)
#     neighbors_in.remove(node)
#     # intersection of the sets are those neighbors with both in and out edges
#     intersection = neighbors_in.intersection(neighbors_out)
#     return len(intersection)


# total_recripocated_pair = 0
# for NI in G1.Nodes():
#     total_recripocated_pair += recripocated_pair_count(NI)
# print("total_recripocated_pair = {}".format(total_recripocated_pair))


