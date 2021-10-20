################################################################################
# Homework 2 problem 2 (Bowtie Structure)
# Author: cwinsor
# Last Updated: Oct 11, 2021
################################################################################

import snap
import numpy as np
import matplotlib.pyplot as plt


# Problem 2 - Bowtie structure

# Read the graphs
def read_graphs(toy=False):
    if (toy):
        # create a toy directed graph
        Graph = snap.TNGraph.New()
        Graph.AddNode(100)
        Graph.AddNode(101)
        Graph.AddNode(102)
        Graph.AddNode(103)
        Graph.AddNode(104)
        Graph.AddNode(105)
        Graph.AddNode(106)
        Graph.AddNode(107)
        Graph.AddNode(108)
        Graph.AddNode(109)
        Graph.AddNode(110)
        Graph.AddEdge(101, 102 )
        Graph.AddEdge(102, 104 )
        Graph.AddEdge(103, 105 )
        Graph.AddEdge(104, 105 )
        Graph.AddEdge(105, 106 )
        Graph.AddEdge(106, 107 )
        Graph.AddEdge(107, 104 )
        Graph.AddEdge(107, 108 )
        Graph.AddEdge(107, 109 )
        Graph.AddEdge(109, 110 )
        return [Graph, Graph]
    else:
        # load from text file
        g_epinions = snap.LoadEdgeList(snap.TNGraph, ".\datasets\soc-Epinions1.txt", 0, 1)
        g_email = snap.LoadEdgeList(snap.TNGraph, ".\datasets\Email-EuAll.txt", 0, 1)
        return [g_epinions, g_email]

 # get inbound 
def get_set_of_nodes_from_n(Graph, start_node):
    # traverse using FollowOut
    # return set of node IDs
    node_set = set({start_node})
    BfsTree = Graph.GetBfsTree(start_node, True, False)
    for EI in BfsTree.Edges():
        node_set.add(EI.GetDstNId())
    return node_set

def get_set_of_nodes_to_n(Graph, finish_node):
    # traverse using FollowOut
    # return set of node IDs
    node_set = set({finish_node})
    BfsTree = Graph.GetBfsTree(finish_node, False, True)
    for EI in BfsTree.Edges():
        node_set.add(EI.GetDstNId())
    return node_set

def consider_node(name, Graph, node):
    to_nodes = get_set_of_nodes_from_n(Graph, node)
    from_nodes = get_set_of_nodes_to_n(Graph, node)
    component = to_nodes.intersection(from_nodes)
    return [name, node, to_nodes, from_nodes, component]

def chart_reachability(gname, technique, values_list):
    import numpy as np

    x = np.linspace(0,1,len(values_list))
    values_list.sort()

    fig, ax1 = plt.subplots()
    ax1.set_title("Whatever!")
    ax1.set_yscale('log')

    plt.scatter(x, values_list)
    plt.xlabel('Fraction of Starting Nodes')
    plt.ylabel('Number of Nodes Reached')
    plt.title('Reachability of {} using {}'.format(gname, technique))
    # plt.legend()
    plt.show()


def compute_size_of_bowtie_regions_and_print(name, graph, list_out, list_in):
    scc_e = graph.GetSccs()
    wcc_e = graph.GetWccs()

    graph_size = graph.GetNodes()
    scc_size = scc_e[0].Len()
    wcc_size = wcc_e[0].Len()

    print("{}:".format(name))
    print("Number of nodes is {}".format(graph_size))
    print("Number of nodes in the large SCC is {}".format(scc_size))
    print("Number of nodes in the large WCC is {}".format(wcc_size))
    print("thus...")
    print("The SCC constitutes {:2.0%} of the nodes in the graph".format(scc_size/graph_size))
    print("")
    print("From our random sampling and BFS...")
    scc_and_out = list_out[0]
    scc_and_in = list_in[0]
    print("bfs-forward (SCC+OUT) gives {} nodes".format(scc_and_out))
    print("bfs-backward (IN+SCC) gives {} nodes".format(scc_and_in))

    # we solve using linear equations
    #  (0)IN + (1)SCC + (1)OUT = BFS_FORWARD
    #  (1)IN + (1)SCC + (0)OUT = BFS_BACKWARD
    #  (0)IN + (1)SCC + (0)OUT = SCC_NODES
    a = np.array([[0,1,1], [1,1,0], [0,1,0]])
    b = np.array([scc_and_out, scc_and_in, scc_size])
    computed_in, computed_scc, computed_out = np.linalg.solve(a, b)
    print("thus we calculate [IN, SCC, OUT] as {} {} {}".format(computed_in, computed_scc, computed_out))
    print()
    tendrals = wcc_size - computed_in - computed_scc - computed_out
    print("Tendrals = (WCC - IN - SCC - OUT) = {}".format(tendrals))
    