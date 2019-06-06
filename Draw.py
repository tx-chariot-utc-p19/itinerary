#!/usr/bin/python3
import numpy as np
from math import inf
import networkx as nx
import matplotlib.pyplot as plt

def draw(graph2):
    graph=graph2;
    [m,n] = np.shape(graph);
    for i in range(0,n):
        for j in range(0,m):
            if np.isinf(graph[i,j]):
                graph[i,j]=0;

    nxgraph = nx.from_numpy_matrix(graph);
    nx.draw(nxgraph);
    plt.draw();  # pyplot draw()
    plt.show();
