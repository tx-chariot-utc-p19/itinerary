#!/usr/bin/python3
#Prend en entrée une grille-hangar et une liste de points imposés. Pour chaque couple de points imposés, calcule un chemin ayant un nombre minimum de virages (1); calcule le coût en temps de ce chemin; puis trouve un chemin passant par tous les points imposés.

import numpy as np;
from math import sqrt, pi;
import networkx as nx;
from itertools import combinations;
import Draw as d;


#constantes
#universelles
g = 9.80665; #m*s^-2*g
#intrinsèques au chariot
mu = 0.35; #coefficient de frottement statique carton/fer déterminé pour notre prototype
r = 0.02; #m, rayon des roues
e = 0.07; #m, hauteur du centre de gravité (colis)
l = 0.03; #m, écartement des roues


def localPath(a,b,rc):
    #prend en entrée deux points de la grille, retourne le meilleur chemin et son coût
    #la convention est de toujours prendre le chemin dont le premier segment est horizontal
    #le chemin est encodé au format sommet
    path = [];
    path.append(a);
    path.append((a[0],b[1]));
    path.append(b);
    return [path,straightLineTime(abs(b[0]-a[0])) + straightLineTime(abs(b[1] - a[1])) + bendTime(rc)];

def straightLineTime(d):
    #temps minimal pour parcourir une belle ligne droite de longueur d
    return 2*sqrt(d/(mu*g));

def bendTime(rc):
    #temps minimal pour parcourir un virage de rayon de courbure rc
    return pi*sqrt(rc*(r+e)/(2*l*g));

def breakDownGrid(grid,breakPoints,rc):
    #retourne un graphe fortement connexe dont les sommets sont les points d'arrêt pour chaque couple de points imposés, chaque arête a pour poids le coût du chemin optimal local, le tracé dans la grille du chemin optimal local est stocké dans l'attribut localPath
    G = nx.Graph();
    G.add_nodes_from(breakPoints);
    pairs = list(combinations(breakPoints,2)); #very bad code
    for pair in pairs:
        path = localPath(pair[0],pair[1],rc);
        G.add_edge(pair[0],pair[1],weight=path[1],localPath=path[0]); #localPath est un attribut non-standard de networkx (il n'a pas d'effet de bord, son nom est défini arbitrairement)
    return G;




def valuate(n,m,breakPoints,corridorWidth):
    grid = np.array([n,m]);
    return breakDownGrid(grid, breakPoints, rc(corridorWidth));

def rc(corridorWidth):
    return corridorWidth/2;
