#!/usr/bin/python3

import Draw as d;

#Script de démo
print("Entrez les dimensions de la grille:");
m = int(input("lignes: "));
n = int(input("colonnes : "));

print("Soit " + str(n*m) + " intersections entre couloirs");
d.drawGrid(n,m);

print("Entrez les coordonnées des points par lesquels le chariot doit passer. (0,0) représente l'intersection en bas à gauche, (0," + str(n) + "représente l'intersection en bas à droite.");

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

d.drawGrid(n,m,breakPoints);
