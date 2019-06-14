#!/usr/bin/python3
import numpy as np
from math import inf
from operator import itemgetter
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

def drawGrid(m,n,xybreakPoints=[]):
    if xybreakPoints==[]:
        line = '╬' * m;
        for i in range(0,n):
            print(line);
    else:
        swap = lambda pair: (pair[1], pair[0]);
        breakPoints = map(swap, xybreakPoints);
        grid = np.zeros((n,m));
        for point in breakPoints:
            grid[point] = 1;
        print(grid);
        for i in range(0,n):
            line = grid[n-1-i]; #pour afficher la ligne 0 en bas
            for element in line:
                if element:
                    print('x', end='');
                else:
                    print('╬', end='');
            print();

