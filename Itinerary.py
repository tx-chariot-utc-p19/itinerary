#!/usr/bin/env python3
#Algo partant du principe que tous les chemins entre deux points sont minimaux: il suffit de prendre le plus proche non visité, puis le plus proche non visité, etc.

import networkx as nx;
import Valuation as v;

def itinerary(G, source,rc):
    path = [source];
    bendCost = v.bendTime(rc);
    while len(path) < G.number_of_nodes():
        cost = {};
        for node in compl(path,G.neighbors(path[-1])):
            cost[node] = getWeight(node,path,G);
            if node[0] != path[-1][0] and node[1] != path[-1][1]:
                cost[node] = cost[node] + bendCost;

        path.append(min(compl(path,G.neighbors(path[-1])), key = lambda node : cost[node]));
    return path;

def compl(a,b):
    out = [];
    for element in b:
        if element not in a:
            out.append(element);
    return out;

def getWeight(node,path,G):
    return G[path[-1]][node]['weight'];
