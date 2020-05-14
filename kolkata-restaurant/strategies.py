# -*- coding: utf-8 -*-

import random
import math

def stubborn_strategy(index,nb_restaurants):
    """Stratégie consistant à se concentrer sur un seul restaurant à chaque tour."""
    return index % nb_restaurants

def random_strategy(nb_restaurants):
    """Stratégie consistant en des deplacements aléatoires."""
    return random.randint(0,nb_restaurants - 1)
    
def nearest_strategy(liste_buts,coord_de_depart):
    """Stratégie consistant en des déplacements jugeant par le restaurant le plus proche."""
    (x0,y0) = coord_de_depart
    but_optimal = None
    dist_optimale = math.inf
    
    for e in range(len(liste_buts)):
        (x,y) = liste_buts[e]
        dist_courrante = abs(x0 - x) + abs(y0 - y)
        if dist_optimale > dist_courrante:
            but_optimal = e
            dist_optimale = dist_courrante
    return but_optimal