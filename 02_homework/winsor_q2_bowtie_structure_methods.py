################################################################################
# Homework 2 problem 2 (Bowtie Structure)
# Author: cwinsor
# Last Updated: Oct 11, 2021
################################################################################

import snap
import numpy as np
import matplotlib.pyplot as plt


# Problem 2.1 Node Position

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

