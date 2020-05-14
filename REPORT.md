# Projet Kolkata 


## Introduction

Ce projet a été réalisé par Erwan Navarro et Thibault Roche. Voici un rappel de l'énoncé:


> Plusieurs joueurs (_n_), qui habitent dans le même quartier, souhaitent se rendre dans un des  _k_  restaurants du quartier. Une fois que leur choix est effectué, les joueurs se rendent dans le restaurant choisi. La règle est alors la suivante :
>-   si un joueur est seul dans un restaurant, un plat lui est servi (gain = 1)
>-   si plusieurs joueurs se trouvent dans un même restaurant, un joueur est choisi au hasard (de manière uniforme parmi tous les joueurs présents dans ce restaurant), et est servi (gain = 1). Les autres joueurs ne sont pas servis (gain = 0). Le jeu se déroule sur plusieurs itérations (_m_, fixé à l'avance).

## Stratégies

Nous avons implémenter 3 stratégies:

 1. La stratégie **têtue** qui fait en sorte qu'un individu se concentre toujours sur le même restaurant à tous les tours.
 2. La stratégie **aléatoire** qui fait en sorte qu'un individu se déplace vers un restaurant aléatoire à chaque tour.
 3. La stratégie **"au plus proche"** qui fait en sorte qu'un individu se déplace toujours vers le restaurant le plus proche.

Ces stratégies se situent dans le fichier `strategies.py`. Ces différentes stratégies servent à augmenter le gain des différents individus. Les individus voient ses différentes stratégies leur être attribuées aléatoirement.

## Déplacement
Afin de rendre les stratégies ci-dessus efficaces, il faut s'assurer que les individus parcourent le plus court chemin. Cette contrainte est respectée par l'implémentation de l'algorithme A*, présent dans le fichier `astar.py`, qui lui même utilise des fonctions de recherche de chemins élémentaires situées dans le fichier `pathfinding.py`.

## Analyse et lancement
Pour savoir quelle stratégie est la plus optimale, il faut d'abord analyser le problème. L'analyse est effectuée par le fichier principal `kalkota_restaurants.py`, après qu'il est appelé les fonctions d'analyses présentent dans `analysis.py`.

## Exemple d'exécution (pour 5 itérations avec 10 joueurs, 6 restaurants et des murs en compartiments)

    pygame 1.9.6
Hello from the pygame community. https://www.pygame.org/contribute.html
Iterations:
5
lignes 20
colonnes 20
Init states: [(5, 0), (6, 0), (7, 0), (8, 0), (9, 0), (10, 0), (11, 0), (12, 0), (13, 0), (14, 0)]
Goal states: [(8, 7), (8, 10), (8, 13), (11, 6), (11, 9), (11, 12)]
Wall states: [(4, 5), (4, 8), (4, 11), (4, 14), (5, 5), (5, 8), (5, 11), (5, 14), (6, 5), (6, 8), (6, 11), (6, 14), (7, 5), (7, 8), (7, 11), (7, 14), (8, 5), (8, 8), (8, 11), (8, 14), (9, 5), (9, 6), (9, 7), (9, 8), (9, 9), (9, 10), (9, 11), (9, 12), (9, 13), (9, 14), (10, 5), (10, 6), (10, 7), (10, 8), (10, 9), (10, 10), (10, 11), (10, 12), (10, 13), (10, 14), (11, 5), (11, 8), (11, 11), (11, 14), (12, 5), (12, 8), (12, 11), (12, 14), (13, 5), (13, 8), (13, 11), (13, 14), (14, 5), (14, 8), (14, 11), (14, 14), (15, 5), (15, 8), (15, 11), (15, 14)]
Analyse pour le joueur 0 4
Analyse pour le joueur 1 1
Analyse pour le joueur 2 3
Analyse pour le joueur 3 3
.
.
.
Fin du tour : distribution des gains.
Gains Actuels:
[3, 0, 2, 1, 1, 3, 3, 2, 3, 4]
