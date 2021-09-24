import snap

# create a random directed graph
G = snap.GenRndGnm(snap.PNGraph, 10000, 5000)

# test if the graph is connected or weakly connected
print("IsConnected(G) =", G.IsConnected())
print("IsWeaklyConnected(G) =", G.IsWeaklyConn())

# get the weakly connected component counts
WccSzCnt = G.GetWccSzCnt()
for i in range (0, len(WccSzCnt)):
    print("WccSzCnt[%d] = (%d, %d)" % (
                i, WccSzCnt[i].GetVal1(), WccSzCnt[i].GetVal2()))

# return nodes in the same weakly connected component as node 1
CnCom = G.GetNodeWcc(1)
print("CnCom size = %d" % (len(CnCom)))

# get nodes in weakly connected components
WCnComV = G.GetWccs()
for i in range(0, len(WCnComV)):
    print("WCnComV[%d] size = %d" % (i, len(WCnComV[i])))
    for j in range (0, len(WCnComV[i])):
        print("WCnComV[%d][%d] = %d" % (i, j, WCnComV[i][j]))

# get the size of the maximum weakly connected component
MxWccSz = G.GetMxWccSz();
print("MxWccSz = %.5f" % (MxWccSz))

# get the graph with the largest weakly connected component
GMx = G.GetMxWcc();
print("GMx: GetNodes() = %d, GetEdges() = %d" % (
    GMx.GetNodes(), GMx.GetEdges()))

# get strongly connected components
SCnComV = G.GetSccs()
for i in range(0, len(SCnComV)):
    print("SCnComV[%d] size = %d" % (i, len(SCnComV[i])))

# get the graph representing the largest bi-connected component
GMxBi = G.GetMxBiCon()
print("GMxBi: GetNodes() = %d, GetEdges() = %d" % (
    GMxBi.GetNodes(), GMxBi.GetEdges()))
