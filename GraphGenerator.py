import networkx as nx
from random import randint as rand
import numpy as np
import matplotlib.pyplot as plt


def generateBase(numberOfCliques):
    G=nx.Graph()
    distibutionArray=[0.1 for i in range(1)]+[0.5 for i in range(3)]+[0.25 for i in range(2)]+[0.15 for i in range(1)]
    for i in range(numberOfCliques):
        size=len(G)
        n=np.random.choice(range(1,7), 1, distibutionArray)[0]
        m={i:size+i for i in range(n)}
        G.add_weighted_edges_from((u, v, 1) for u,v in nx.relabel_nodes(nx.complete_graph(n),m).edges())
    return G


def generateBridges(G, numberOfBridges):
    assert len(G)*len(G)>=numberOfBridges, 'numberOfBridges cannot exceed the maximum number of node pair combinations'
    b=np.random.choice((list(G.nodes())), size=(numberOfBridges,2))
    for i in b:
        w=1
        com=set(G.neighbors(i[0])) & set(G.neighbors(i[1]))
        for j in com:
            w+=1
            G[i[0]][j]['weight']+=1
            G[i[1]][j]['weight']+=1
        G.add_weighted_edges_from([(i[0],i[1],w)])


G=generateBase(100)
generateBridges(G, 30)
nx.draw(G)
plt.draw()


