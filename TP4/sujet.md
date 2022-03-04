TP4 - Recherche d’occurrences de matrices PFM dans un ensemble de séquences
===========================================================================

Département informatique – Université de Lille

*   [Recherche pour un ensemble de séquences](#recherche-pour-un-ensemble-de-séquences)
*   [Le module de gestion des arguments `argparse` de Python](#le-module-de-gestion-des-arguments-argparse-de-python)

L’objectif de ce TP est :

*   d’étendre le travail du TP3 pour la recherche d’occurrences d’une PFM pour un esnemble de séquences et non plus une seule séquence

Recherche pour un ensemble de séquences
---------------------------------------

Dans la suite du projet nous allons rechercher les occurrences de matrices dans un ensemble de séquences.

- [ ] 1.  Ajouter à `utils.py` une fonction `download_promotors` qui, étant donné une liste d’identifiants de mRNA, une taille de séquence promotrice, un répertoire d’enregistrement (`.` par défaut), télécharge dans des fichiers séparés les séquences promotrices de ces mRNA au format FASTA. Les noms des fichiers seront les nom des identifiants mRNA suivi de la longueur du promoteur (par exemple, le promoteur de taille 100 de `NM_007389` sera stocké dans le fichier `NM_007389_100.fa`).

La construction d’un chemin valide se fait grâce à `os.path.join` (voir [documentation de `os.path`](https://docs.python.org/3.8/library/os.path.html))

Cette fonction sera utile dans les tests des fonctions suivantes car elle évitera de réaliser des requêtes trop fréquentes au NCBI (le NCBI pourrait réduire votre accès si il estime qu’il y a trop de requêtes).

- [ ] 2.  Mettez en œuvre la fonction `download_promotors` en téléchargeant les promoteurs des mRNA suivants : `NM_007389, NM_079420, NM_001267550, NM_002470, NM_003279, NM_005159, NM_003281, NM_002469, NM_004997, NM_004320, NM_001100, NM_006757` dans le répertoire `data`.

- [ ] 3.  Réalisez dans le module `pwm.py` une fonction `scan_all_sequences` qui, à partir d’une PSSM (un objet \``PositionSpecificScoringMatrix`), d’une liste de séquences (des objets Biopython `Bio.Seq`), retourne les couples position/score d’occurrence pour l’ensemble des séquences. Réfléchissez à la façon de structurer ces données pour pouvoir les exploiter ensuite.

- [ ] 4.  Réalisez dans le module `pwm.py` une fonction `score_window` qui, étant donné un résultat de `scan_all_sequences` et des coordonnées début/fin dans les séquences, retourne le score de la fenêtre.

- [ ] 5.  Réalisez dans le module `pwm.py` une fonction `best_window` qui, étant donné un résultat de `scan_all_sequences` et une taille de fenêtre, retourne les coordonnées de la fenêtre de meilleur score.

- [ ] 6.  Testez en cherchant la meilleure fenêtre pour la liste des mRNA donnée ci-dessus pour la matrice `MA_0114`.


Le module de gestion des arguments `argparse` de Python
-------------------------------------------------------

Dans l’objectif de livrer à la fin de l’UE un programme Python de bonne qualité, nous vous proposons d’explorer le module [argparse](https://docs.python.org/fr/3.8/library/argparse.html#module-argparse) de Python permettant de traiter très simplement les paramètres de la ligne de commande

En vous inspirant de ce [tutoriel](https://docs.python.org/fr/3/howto/argparse.html) mettez en place un script Python `test_args.py` qui prenne en option :

*   `-t` pour le seuil de score (option longue `--threshold`, pas de valeur par défaut) ;
*   `-l` pour la longueur du promoteur (option longue `--promotor-length`, par défaut 1000) ;
*   `-w` pour la longueur de la fenêtre glissante (option longue `--window-size`, par défaut 40).

Les identifiants des mRNA seront donnés en argument (et pas en option). Le script affichera simplement les valeurs des options et la liste des arguments.

Ce script préfigure le script de rendu final.
