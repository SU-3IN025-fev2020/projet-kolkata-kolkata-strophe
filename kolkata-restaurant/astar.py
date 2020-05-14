# -*- coding: utf-8 -*-

import queue

import pathfinding

def astar(depart,arrivee,murs):
    if depart == arrivee:
        return []
        
    frontiere = queue.PriorityQueue()
    frontiere.put((0, depart))
    
    precedent = {}
    precedent[depart] = None
    
    cout_courrant = {}
    cout_courrant[depart] = 0

    while not frontiere.empty():
        (optimal,courrant) = frontiere.get()

        if courrant == arrivee:
            break
       
        for suivant in pathfinding.neighbors(murs,courrant):
            cout = cout_courrant[courrant] + 1
            if suivant not in cout_courrant or cout < cout_courrant[suivant]:
                cout_courrant[suivant] = cout
                optimal = cout + pathfinding.manhattan_distance(arrivee, suivant)
                frontiere.put((optimal,suivant))
                precedent[suivant] = courrant 
                
    courrant = arrivee
    chemin = []

    while courrant != depart:
        chemin.append(courrant)
        courrant = precedent[courrant]       
    chemin.reverse()
    
    return chemin