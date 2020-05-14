# -*- coding: utf-8 -*-

import math
import random

class Analyse(object) :
    def __init__(self,nb_buts):
        self.liste_inscrits = []
        self.couts_precedents = []
        self.nb_buts = nb_buts

    def subscribe(self, i):
        self.liste_inscrits.append(i)
        self.couts_precedents.append([0] * self.nb_buts)

    def is_subscribed(self, i):
        return (i in self.liste_inscrits)

    def update_results(self, i, i_final, liste_resultats) :
        for j in range(0,self.nb_buts):
            self.couts_precedents[i][j] += liste_resultats[j]
        self.couts_precedents[i][i_final] -= 1

    def best_strat(self, i):
        b_goal = []
        nb_max = math.inf
        for j in range (0, self.nb_buts):
            if self.couts_precedents[i][j] <= nb_max:
                nb_max = self.couts_precedents[i][j]
                b_goal.append(j)
                
        return random.choice(b_goal)