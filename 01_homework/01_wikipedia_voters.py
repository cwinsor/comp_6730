import snap

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

print("Problem 1: Wikipedia Voters Network")
# number of nodes...
print("Q1:")
print("number of nodes = {}".format(G1.GetNodes()))
print("number of edges = {}".format(G1.GetEdges()))


#(2) number of self-edges
#(3) number of directed edges
self_edge_list = []
directed_edge_list = []
for EI in G1.Edges():
    if (EI.GetSrcNId() == EI.GetDstNId()):
        self_edge_list.append(EI)
    else:
        directed_edge_list.append(EI) 

print("\nQ2: Number of nodes with a self-edge = {}".format(len(self_edge_list)))
print("\nQ3: Number of directed edges in the network = {}".format(len(directed_edge_list)))


# (4) undirected edged a.k.a. unique unordered pairs
#   (a,b) or (b,a) where a!=b and order does not matter
# approach:
#   convert graph to undirected graph
#   count the number of edges, excluding self-edges
G2 = G1.ConvertGraph(snap.TUNGraph)
# number of non-self-edges...
non_self_edge_list = []
for EI in G2.Edges():
    if (EI.GetSrcNId() != EI.GetDstNId()):
        non_self_edge_list.append(EI)
print("\nQ4: Number of undirected edges in the network = {}".format(len(non_self_edge_list)))

# (5) Recripocated pairs is a pair of edges (a->b), (b->a)  where a!=b
# algorithm:
#   for each node A, a recripocated pair is
#   where there exists an out-edge to b, and an in-edge from b
#
# method:
#   given a node, return the count of recripocated pairs for that node
#   neighbors_in  is a set: the neighbors in the in_edge list
#   neighbors_out is a set: the neighbors in the out_edge list
#   intersection of neighbors_in, neighbors_out is the recripocated pairs
def recripocated_pair_count(node):
    out_edges = set()
    in_edges = set()
    for id in node.GetOutEdges():
        out_edges.add(id)
    for id in node.GetInEdges():
        in_edges.add(id)

    # in-degree, out-degree
    out_degree = len(out_edges)
    in_degree = len(in_edges)

    # for recriprocal pair - remove self-loop if it exists
    try: 
        out_edges.remove(node.GetId())
        in_edges.remove(node.GetId())
    except KeyError:
        x = 0 # do nothing
    # intersection of the sets are those neighbors with both in and out edges
    out_intersect_in = in_edges.intersection(out_edges)

    return [len(out_intersect_in), out_degree, in_degree]

total_recripocated_pair = 0
total_out_degree_eq_zero = 0
total_out_degree_gt_10 = 0
total_in_degree_eq_zero = 0
total_in_degree_lt_10 = 0
for NI in G1.Nodes():
    recripocated_pair_ct, out_deg, in_deg = recripocated_pair_count(NI)
    total_recripocated_pair += recripocated_pair_ct
    if out_deg == 0:
        total_out_degree_eq_zero += 1 
    if in_deg == 0:
        total_in_degree_eq_zero += 1
    if out_deg > 10:
        total_out_degree_gt_10 += 1
    if in_deg < 10:
        total_in_degree_lt_10 += 1

print("\nQ5: Total recripocated_pair = {}".format(total_recripocated_pair//2))
print("\nQ6: Total nodes with out-degree zero is {}".format(total_out_degree_eq_zero))
print("\nQ7: Total nodes with in-degree zero is {}".format(total_in_degree_eq_zero))
print("\nQ8: Total nodes with out-degree > 10 is {}".format(total_out_degree_gt_10))
print("\nQ9: Total nodes with in-degree < 10 is {}".format(total_in_degree_lt_10))

