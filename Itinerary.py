#!/usr/bin/env python3
#Algo partant du principe que tous les chemins entre deux points sont minimaux: il suffit de prendre le plus proche non visité, puis le plus proche non visité, etc.

import networkx as nx;

def itinerary(G, source):
    path = [source];
    while len(path) < G.number_of_nodes():
        path.append(min(compl(path,G.neighbors(path[-1])), key = lambda node : getWeight(node,path,G)));
    return path;

def compl(a,b):
    out = [];
    for element in b:
        if element not in a:
            out.append(element);
    return out;

def getWeight(node,path,G):
    return G[path[-1]][node]['weight'];
