# -*- coding: utf-8 -*-

# Nicolas, 2020-03-20
# Erwan NAVARRO et Thibault ROCHE

from __future__ import absolute_import, print_function, unicode_literals
from gameclass import Game,check_init_game_done
from spritebuilder import SpriteBuilder
from players import Player
from sprite import MovingSprite
from ontology import Ontology
from itertools import chain
import pygame
import glo

import random 
import numpy as np
import sys

import analysis
import astar
import pathfinding
import strategies
    
# ---- ---- ---- ---- ---- ----
# ---- Main                ----
# ---- ---- ---- ---- ---- ----

game = Game()

def init(_boardname=None):
    global player,game
    # pathfindingWorld_MultiPlayer4
    name = _boardname if _boardname is not None else 'kolkata_6_10'
    game = Game('Cartes/' + name + '.json', SpriteBuilder)
    game.O = Ontology(True, 'SpriteSheet-32x32/tiny_spritesheet_ontology.csv')
    game.populate_sprite_names(game.O)
    game.fps = 60  # frames per second
    game.mainiteration()
    game.mask.allow_overlaping_players = True
    #player = game.player
    
def main():

    #for arg in sys.argv:
    iterations = 5 # default
    if len(sys.argv) == 2:
        iterations = int(sys.argv[1])
    print ("Iterations: ")
    print (iterations)

    init()
    
    #-------------------------------
    # Initialisation
    #-------------------------------
    nbLignes = game.spriteBuilder.rowsize
    nbColonnes = game.spriteBuilder.colsize
    print("lignes", nbLignes)
    print("colonnes", nbColonnes)
    
    
    players = [o for o in game.layers['joueur']]
    nbPlayers = len(players)
    
    
    # on localise tous les états initiaux (loc du joueur)
    initStates = [o.get_rowcol() for o in game.layers['joueur']]
    print ("Init states:", initStates)
    
    
    # on localise tous les objets  ramassables (les restaurants)
    goalStates = [o.get_rowcol() for o in game.layers['ramassable']]
    print ("Goal states:", goalStates)
    nbRestaus = len(goalStates)
        
    # on localise tous les murs
    wallStates = [w.get_rowcol() for w in game.layers['obstacle']]
    print ("Wall states:", wallStates)

    # on liste toutes les positions permises
    allowedStates = [(x,y) for x in range(nbLignes) for y in range(nbColonnes)\
                     if (x,y) not in wallStates or  goalStates] 

    analyse = analysis.Analyse(len(goalStates))
    
    #-------------------------------
    # Placement aleatoire des joueurs, en évitant les obstacles
    #-------------------------------

    liste_gains=[0]*nbPlayers
    
    #inscription à la stratégie d'analyse
    analyse.subscribe(0)
    analyse.subscribe(1)
    analyse.subscribe(2)
    analyse.subscribe(3)
       
    for i in range(iterations):
        est_fini=False
        ite_courrante=0

        posPlayers = initStates

        
        for j in range(nbPlayers):
            x,y = random.choice(allowedStates)
            players[j].set_rowcol(x,y)
            game.mainiteration()
            posPlayers[j]=(x,y)


            

        #-------------------------------
        # chaque joueur choisit un restaurant
        #-------------------------------

        restaurant = [0]*nbPlayers
        for j in range(nbPlayers):
            if analyse.is_subscribed(j):
                c = analyse.best_strat(j)
                print("Analyse pour le joueur",j,c)
            else :  
                c = strategies.random_strategy(nbRestaus)              
                print(c)
               
            restaurant[j]=c

        chemins=[0]*nbPlayers

        #-------------------------------
        # Boucles de déplacements 
        #-------------------------------

        for i in range(nbPlayers):
            chemins[i] = astar.astar(posPlayers[i],goalStates[restaurant[i]],wallStates)

        for i in range(iterations):
            est_fini = False
            ite_courrante = 0

        while(not(est_fini)):
            cpt_fin = 0
        
            for j in range(nbPlayers): # on fait bouger chaque joueur séquentiellement
                if len(chemins[j]) > ite_courrante :
                    (prochaine_ligne,prochaine_colonne) = chemins[j][ite_courrante]
                    players[j].set_rowcol(prochaine_ligne,prochaine_colonne)
                    print ("pos :", j, prochaine_ligne,prochaine_colonne)
                    game.mainiteration()
                    posPlayers[j] = (prochaine_ligne,prochaine_colonne)
                else :
                    print(("Le joueur ", j, " a fini."))
                    cpt_fin += 1
                    game.mainiteration()
                    
            ite_courrante += 1
            
            if cpt_fin == 10 :
                est_fini = True
                print('Fin du tour : distribution des gains.')
                
                for g in range(len(goalStates)):
                    gagnants = []
                    
                    for h in range(nbPlayers):
                        if posPlayers[h] == goalStates[g] :
                            gagnants.append(h)
                            
                    if len(gagnants) != 0 :
                        gagnant=random.choice(gagnants)
                        liste_gains[gagnant] += 1
                        
                    tab_fin = [0] * len(goalStates)
                    
                for k in range(len(tab_fin)):
                
                    for l in range(nbPlayers):
                        if posPlayers[l] == goalStates[k] :
                            tab_fin[k] += 1
                            
                for m in range(nbPlayers):
                    if analyse.is_subscribed(m) :
                        cpt_fin =- 1
                        
                        for n in range(len(goalStates)) :
                            if posPlayers[m] == goalStates[n]:
                                cpt_fin = n
                                
                        analyse.update_results(m, n, tab_fin)

                print('Gains Actuels:')
                print(liste_gains)
    
    pygame.quit()
      

if __name__ == '__main__':
    main()

