################################################################################
# # Starter code for Problem 1
# Author: praty@stanford.edu
# Last Updated: Sep 28, 2017
################################################################################

import snap
import numpy as np
import matplotlib.pyplot as plt

# Setup
erdosRenyi = None
smallWorld = None
collabNet = None


# Problem 1.1
def genErdosRenyi(N=5242, E=14484):
    """
    :param - N: number of nodes
    :param - E: number of edges

    return type: snap.PUNGraph
    return: Erdos-Renyi graph with N nodes and E edges
    """
    ############################################################################
    # TODO: Your code here!
    Graph = snap.TUNGraph.New()

    import random

    for n in range(0,N):
        Graph.AddNode(n)

    while Graph.GetEdges() < E:
        src = random.randrange(N)
        dst = random.randrange(N)
        if src != dst:
            Graph.AddEdge(src, dst)

    # print("number of nodes = {}".format(Graph.GetNodes()))
    # print("number of edges = {}".format(Graph.GetEdges()))
    # assert Graph.GetNodes()==N, "number of nodes should be N"
    # assert Graph.GetEdges()==E, "number of edges should be E"
    ############################################################################
    return Graph


def genCircle(N=5242):
    """
    :param - N: number of nodes

    return type: snap.PUNGraph
    return: Circle graph with N nodes and N edges. Imagine the nodes form a
        circle and each node is connected to its two direct neighbors.
    """
    ############################################################################
    # TODO: Your code here!
    Graph = snap.TUNGraph.New()

    # create nodes
    for n in range(0,N):
        Graph.AddNode(n)

    # create a circle each node visited once (a Hamilton path)
    for n in range(0,N):
        Graph.AddEdge(n, (n+1)%N)

    # print("number of nodes = {}".format(Graph.GetNodes()))
    # print("number of edges = {}".format(Graph.GetEdges()))
    # assert Graph.GetNodes()==N, "number of nodes should be N"
    # assert Graph.GetEdges()==N, "number of edges should be same as number of nodes"
    ############################################################################
    return Graph


def connectNbrOfNbr(Graph, N=5242):
    """
    :param - Graph: snap.PUNGraph object representing a circle graph on N nodes
    :param - N: number of nodes

    return type: snap.PUNGraph
    return: Graph object with additional N edges added by connecting each node
        to the neighbors of its neighbors
    """
    ############################################################################
    # TODO: Your code here!

    # connect each node in the path to its neighbor's neighbors
    for n in range(0,N):
        Graph.AddEdge(n, (n+2)%N)

    # print("number of nodes = {}".format(Graph.GetNodes()))
    # print("number of edges = {}".format(Graph.GetEdges()))
    # assert Graph.GetNodes()==N, "number of nodes should be N"
    # assert Graph.GetEdges()==2*Graph.GetNodes(), "number of edges should be 2 * nodes"
    ############################################################################
    return Graph


def connectRandomNodes(Graph, M=4000):
    """
    :param - Graph: snap.PUNGraph object representing an undirected graph
    :param - M: number of edges to be added

    return type: snap.PUNGraph
    return: Graph object with additional M edges added by connecting M randomly
        selected pairs of nodes not already connected.
    """
    ############################################################################
    # TODO: Your code here!

    import random

    # add additional random edges
    # there are already 2N edges from Hamilton path and second order links
    desired_total_edges =  2*Graph.GetNodes() + M
    num_nodes = Graph.GetNodes()
    while Graph.GetEdges() < desired_total_edges:
        src = random.randrange(num_nodes)
        dst = random.randrange(num_nodes)
        if src != dst:
            Graph.AddEdge(src, dst)

    # print("number of nodes = {}".format(Graph.GetNodes()))
    # print("number of edges = {}".format(Graph.GetEdges()))
    # assert Graph.GetNodes()==num_nodes, "number of nodes should be N"
    # assert Graph.GetEdges()==desired_total_edges, "number of edges should be 2N + M"
    ############################################################################
    return Graph


def genSmallWorld(N=5242, E=14484):
    """
    :param - N: number of nodes
    :param - E: number of edges

    return type: snap.PUNGraph
    return: Small-World graph with N nodes and E edges
    """
    Graph = genCircle(N)
    Graph = connectNbrOfNbr(Graph, N)
    Graph = connectRandomNodes(Graph, 4000)
    return Graph


def loadCollabNet(path):
    """
    :param - path: path to edge list file

    return type: snap.PUNGraph
    return: Graph loaded from edge list at `path and self edges removed

    Do not forget to remove the self edges!
    """
    ############################################################################
    # TODO: Your code here!
    Graph = snap.LoadEdgeList(snap.TUNGraph, path)

    # remove self-edges
    for edge in Graph.Edges():
        src = edge.GetSrcNId() 
        dst = edge.GetDstNId()
        if src == dst:
            Graph.DelEdge(src, dst)
    # print("number of nodes = {}".format(Graph.GetNodes()))
    # print("number of edges = {}".format(Graph.GetEdges()))
    ############################################################################
    return Graph


def getDataPointsToPlot(Graph):
    """
    :param - Graph: snap.PUNGraph object representing an undirected graph
    
    return values:
    X: list of degrees
    Y: list of frequencies: Y[i] = fraction of nodes with degree X[i]
    """
    ############################################################################
    # TODO: Your code here!
    x_count_x = {} # dictionary: key is out-degree, value is count of instances
    number_of_nodes = Graph.GetNodes()

    for NI in Graph.Nodes():
        this_out_degree = NI.GetOutDeg()
        if this_out_degree in x_count_x:
            x_count_x[this_out_degree] += 1
        else:
            x_count_x[this_out_degree] = 1

    sorted_dict = dict(sorted(x_count_x.items()))

    X = list(sorted_dict) # out degree
    Y = list(map(lambda x: x / number_of_nodes, sorted_dict.values())) # fraction of nodes
    ############################################################################
    return X, Y




# Problem 1.2   



# Erdos Renyi
def calcQk(Graph, maxDeg):
    """
    :param Graph - snap.PUNGraph object representing an undirected graph
    :param maxDeg - maximum degree(+1) for which q_k needs to be calculated
    
    return type: np.array
    return: array q_k of dimension maxDeg representing the excess degree
        distribution  
    """
    ############################################################################
    # TODO: Your code here!
    q_k_count = np.zeros(maxDeg) # index is k, value is count

    for node in Graph.Nodes():
        node_degree = node.GetDeg()
        if node_degree > 0:
            k = node_degree - 1
            q_k_count[k] += node_degree

    q_k = q_k_count / np.sum(q_k_count) # scale

    ############################################################################
    return q_k


def calcExpectedDegree(Graph):
    """
    :param Graph - snap.PUNGraph object representing an undirected graph

    return type: float
    return: expected degree of Graph
    """
    ############################################################################
    # TODO: Your code here!

    sum_of_node_degrees = 0
    for node in Graph.Nodes():
        sum_of_node_degrees += node.GetDeg()

    ed = sum_of_node_degrees / Graph.GetNodes()
    ############################################################################
    return ed


def calcExpectedExcessDegree(Graph, qk):
    """
    :param Graph - snap.PUNGraph object representing an undirected graph
    :param qk - np.array of dimension maxdeg representing excess degree
        distribution of `Graph

    return type: float
    return: expected excess degree of `Graph
    """
    ############################################################################
    # TODO: Your code here!

    k_qk_sum = 0.0
 
    for node in Graph.Nodes():
        node_degree = node.GetDeg()
        if node_degree > 0:
            k = node_degree - 1
            k_qk_sum += k * node_degree

    eed = k_qk_sum / Graph.GetEdges()
    # print("eed calc 1 = {}".format(eed))
    ############################################################################
    return eed





# Problem 1.3 - Clustering Coefficient

def calcClusteringCoefficient(Graph):
    """
    :param - Graph: snap.PUNGraph object representing an undirected graph

    return type: float
    returns: clustering coeffient of `Graph 
    """    
    ############################################################################
    # TODO: Your code here!

    def neighbors_of_node(node):
        neighbor_set = set({})
        for n in range(node.GetDeg()):
            neighbor_set.add(node.GetNbrNId(n))
        return neighbor_set

    def count_of_edges_between_neighbors(Graph, neighbor_set):
        count = 0
        for node1_id in neighbor_set:
            for node2_id in neighbor_set:
                if Graph.GetNI(node2_id).IsNbrNId(node1_id):
                    count +=1
        return count // 2

    from math import factorial
    def comb(n, k):
        try:
            return factorial(n) // factorial(k) // factorial(n - k)
        except ValueError:
            return 0

    def clustering_coefficient(Graph, neighbor_set):

        n = len(neighbor_set)
        if n < 2:
            return 0
        else:
            actual_edge_count = count_of_edges_between_neighbors(Graph, neighbor_set)
            n_choose_2 = comb(n,2)

            return actual_edge_count / n_choose_2

    # using above functions - do the actual work...
    sum_clustering_coefficients = 0.0
    for node in Graph.Nodes():
        neighbor_set = neighbors_of_node(node)
        # print("\nnode: {}, degree {} len(neighbors) {} neighbors {}".format(node.GetId(), node.GetDeg(), len(neighbor_set), neighbor_set))
        clustering_coefficient_this_node = clustering_coefficient(Graph, neighbor_set)
        # print("clustering coefficient = {}".format(clustering_coefficient_this_node))
        sum_clustering_coefficients += clustering_coefficient_this_node
    C = sum_clustering_coefficients / Graph.GetNodes()

    ############################################################################
    return C



