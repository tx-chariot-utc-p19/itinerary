#!/usr/bin/python3
import numpy as np
from math import inf #représentation de l'infini (nAn)
import Draw as d
#données de test
graph = np.array([
        [0, 4, 2, inf, inf, inf],
        [4, 0, 1, 5, inf, inf],
        [2, 1, 0, 8, 10, inf],
        [inf, 5, 8, 0, 2, 6],
        [inf, inf, 10, 2, 0, 3],
        [inf, inf, inf, 6, 3, 0]
        ]); #représentation en matrice d'adjacence valuée de ce graphe: https://www.codewithc.com/wp-content/uploads/2014/07/dijkstra-algorithm-weighted-graph.png

source = 1; #indice du sommet de départ
destination=5; #indice du sommet d'arrivée

d.draw(graph);

def dijkstra(a, source, destination):
    if len(a.shape) != 2 or max(a.shape) != min(a.shape):
        raise ValueError('Pas une matrice carrée.')
    previous = {};
    [n,n] = a.shape; #nombre de sommets
    distances = inf * np.array(np.ones(n)); #la distance de source à tous les sommets est l'infini
    distances[source] = 0; #la distance de la source à elle-même est 0;
    unvisited = np.ones(n, bool); #tous les sommets n'ont pas encore été visités
    currentNode = source; #on s'intéresse au sommet de départ

    while unvisited[destination]: #tant qu'on est pas arrivé à destination:
        print(unvisited);
        #si le sommet courant a déjà été visité, il faut en changer on doit sélectionner un sommet à visiter
        if not unvisited[currentNode]: #il faut changer de sommet
            unvisitedDistances = unvisited * distances;
            for i in range(0,n-1):
                if np.isnan(unvisitedDistances[i]) or unvisitedDistances[i] == 0:
                    unvisitedDistances[i] = np.inf; #permet d'éliminer les sommets visités à distance finie (false*n=0) et les sommets visités à distance infinie (false*inf=nan) du calcul de min
            if min(unvisitedDistances) == np.inf:
                raise ValueError('Il n\'existe pas de chemin entre la source et la destination.');
            currentNode = np.argmin(unvisitedDistances); #prend l'index du plus petit sommet


        #on s'intéresse à tous les successeurs non visités du noeud sur lequel on est
        unvisitedSuccessors = a[currentNode, :] * unvisited; #on sélectionne une ligne=prédécesseur (le sommet en cours) et toutes les colonnes=successeur. On multiplie par les non visitées, ce qui annule celles qui ont déjà été visitées. (dans le cas 0*inf on a une forme indéterminée).
        #on calcule les distances de source à chaque noeud. C'est la distance de source au noeud actuel plus la distance du noeud actuel à chaque successeur non visité.
        #si une distance a déjà été calculée, on garde la plus petite des deux.
        i = 0; #on a besoin de conserver les indices
        for node in unvisitedSuccessors:
            if np.isfinite(node) and node!=0: #si il vaut 0, l'infini ou nan, ce n'est pas un successeur non visité
                if distances[currentNode] + node < distances[i]:
                    distances[i] = distances[currentNode] + node;
                    previous[i] = currentNode;
            i+=1;
        unvisited[currentNode] = False; #on a fini d'explorer les successeurs de ce sommet


    #à ce stade, previous contient une liste d'arcs optimaux, y compris des arcs qui n'interviennent pas dans le chemin souhaité. Il suffit donc de parcourir le trajet de la destination à l'arrivée, en n'empruntant que des arcs optimaux, pour trouver le chemin optimal.
    return previous;


print("dijkstra 0 3");
print(dijkstra(graph,0,3));
