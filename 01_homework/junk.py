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


# traverse the edges by nodes
for NI in G1.Nodes():
    print('--- {}  {}'.format(type(G1), type(NI)))
    for Id in NI.GetInEdges():
        print("------ type {} value {}".format(type(Id), Id))
        print("------ edge (%d %d)" % (NI.GetId(), Id))

           