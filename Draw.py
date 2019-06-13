#!/usr/bin/python3
import numpy as np
from math import inf
import networkx as nx
import matplotlib.pyplot as plt

def drawAdjMat(graph2):
    graph=graph2;
    [m,n] = np.shape(graph);
    for i in range(0,n):
        for j in range(0,m):
            if np.isinf(graph[i,j]):
                graph[i,j]=0;


    
    G = nx.from_numpy_matrix(graph);

    pos=nx.spring_layout(G);
    nx.draw_networkx(G,pos)
    labels = nx.get_edge_attributes(G,'weight')
    nx.draw_networkx_edge_labels(G,pos,edge_labels=labels)


    plt.draw();  # pyplot draw()
    plt.show();

def drawNxGraph(G):
    pos=nx.spring_layout(G);
    nx.draw_networkx(G,pos);
    labels = nx.get_edge_attributes(G,'weight');
    nx.draw_networkx_edge_labels(G,pos,edge_labels=labels);
    plt.draw();
    plt.show();
