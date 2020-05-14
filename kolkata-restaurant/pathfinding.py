# -*- coding: utf-8 -*-

def manhattan_distance(a, b):
    """Calcule la distance de Manhattan."""
    (x1,y1) = a
    (x2,y2) = b
    return abs(x1 - x2) + abs(y1 - y2)
    
def neighbors(murs,courrant):
    """Renvoie la liste des voisins"""
    liste_voisins = []
    (ligne,colonne) = courrant
    
    for direction in [(0,1),(0,-1),(1,0),(-1,0)]:
        prochaine_ligne = ligne + direction[0]
        prochaine_colonne = colonne + direction[1]
        prochain = (prochaine_ligne,prochaine_colonne)
        if ((prochain not in murs) and prochaine_ligne >= 0 and prochaine_colonne >= 0 and prochaine_ligne <= 19 and prochaine_colonne <= 19):
            liste_voisins.append(prochain)
            
    return liste_voisins