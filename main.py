#!/usr/bin/python3

import Draw as d;
import Valuation as v;
#import Dijkstra as dij;
#import Genetic as gen;
import Itinerary as it;
import numpy as np;
import networkx as nx;

#Script de démo

#ENTREE
debug = False;

if not debug:
    
    inputData = True;
    while inputData:
        print("Entrez les dimensions de la grille:");
        m = int(input("lignes: "));
        n = int(input("colonnes : "));
        if n>0 and m>0:
            inputData = False;
        else:
            print("Veuillez entrer des dimensions entières strictement positives.");
    
    
    print("Soit " + str(n*m) + " intersections entre couloirs");
    d.drawGrid(n,m);
    
    corridorWidth = 0;
    while corridorWidth <= 0:
       corridorWidth = float(input("Largeur de couloir en mètres:"));
    
    print("Entrez les coordonnées des points par lesquels le chariot doit passer. (0,0) représente l'intersection en bas à gauche, (0," + str(n-1) + ") représente l'intersection en bas à droite.");
    print("Le premier point saisi sera le point de départ.");
    
    inputData = True;
    breakPoints = [];
    
    while inputData:
        x = int(input("Abscisse: "));
        y = int(input("Ordonnée: "));
        if x < n and y < m:
            breakPoints.append((x,y));
        else:
            print("Ce point dépasse la capacité de la grille.");
        inputData = int(input("Entrer un nouveau point d'arrêt imposé? (0/1)"));
else:
    n = 5;
    m = 5;
    breakPoints = [(0,0),(1,1),(0,1),(2,3),(4,4)];
    corridorWidth = 0.2;
d.drawGrid(n,m,breakPoints);




#TRAITEMENT

#calcul des chemins optimaux dans les sous-grilles locales (et de leur coût), on obtient un graphe simplifié qui fait abstraction du modèle de la grille
Gsimp = v.valuate(n,m,breakPoints,corridorWidth);
#affichage du graphe simplifié
d.drawNxGraph(Gsimp);

#dij.itinerary(Gsimp,breakPoints[0],breakPoints[-1]);
#calcul du meilleur itinéraire avec un algo génétique (problème de voyageur de commerce)
#gen.genetic(adjMat);

#adjMat = np.asarray(nx.to_numpy_matrix(Gsimp));
#d.drawAdjMat(adjMat);

nodeList = list(Gsimp.nodes());
print(it.itinerary(Gsimp,nodeList[0]));
