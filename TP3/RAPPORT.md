TP3 - Recherche d’occurrences de matrices PFM
=============================================

Département informatique – Université de Lille

*   [Rendu intermédiaire](#rendu-intermédiaire)
*   [Calcul de score à partir de matrices de fréquences (repris du TP2)](#calcul-de-score-à-partir-de-matrices-de-fréquences-repris-du-tp2)
*   [Mise en place de fonctions utiles pour manipuler les PWM](#mise-en-place-de-fonctions-utiles-pour-manipuler-les-pwm)
*   [Script pour le rendu intermédiaire](#script-pour-le-rendu-intermédiaire)
*   [Recherche pour un ensemble de séquences](#recherche-pour-un-ensemble-de-séquences)
*   [Le module de gestion des arguments `argparse` de Python](#le-module-de-gestion-des-arguments-argparse-de-python)

L’objectif de ce TP est :

*   de faire ou finaliser la partie du TP2 pour la recherche d’occurrences d’une PFM
*   recherche des occurrences et stockage d’une PWM pour une séquence
*   rendu intermédiaire
*   calcul de score d’une fenêtre glissante

Rendu intermédiaire
-------------------

À la fin de la séance (i.e. avant 17h00), vous devez avoir réalisé un script python, qui s’exécute en ligne de commande, prend en argument :

*   un fichier contenant une matrice JASPAR ;
*   un identifiant Genbank d’un mRNA ;
*   une taille pour la séquence promotrice ;
*   un seuil de score.

et produit sur la sortie standard une liste d’occurrences dont le score est supérieur au seuil. Typiquement :

    Ahr::Arnt 71 6.198700428009033
    Ahr::Arnt -745 5.744134426116943
    Ahr::Arnt 444 6.198700428009033
    Ahr::Arnt 446 6.198700428009033
    Ahr::Arnt -388 10.591017723083496
    Ahr::Arnt 920 6.198700428009033

(voir la section dédiée plus bas)

Calcul de score à partir de matrices de fréquences (repris du TP2)
------------------------------------------------------------------

Nous allons maintenant utiliser Biopython pour trouver les endroits correspondant à des sites de fixation du facteur de transcription.

Nous allons travailler à partir du fichier que vous avez [téléchargé la semaine dernière sur JASPAR](https://www.fil.univ-lille.fr/~salson/portail/bioinfo-s6/TP1.html#sites-de-fixation-des-facteurs-de-transcription), à mettre dans votre répertoire `data/`. Le module `motifs` de Biopython est celui qui nous intéressera pour rechercher les occurrences de PSSM. Chargez-le.

Le chargement de ce type fichier (matrices de fréquences) se fait avec la méthode `read` du module `motifs` ([documentation](https://biopython.org/docs/1.75/api/Bio.motifs.html#Bio.motifs.read)), en lui précisant que le format est `jaspar`.

- [x] 1.  Combien de matrices ont été lues ? ***=> On a lu 4 matrices***

Pour chaque entrée, la matrice est accessible via l’attribut `counts`, de type `FrequencyPositionMatrix` ([documentation](https://biopython.org/docs/1.75/api/Bio.motifs.matrix.html?highlight=frequencypositionmatrix#Bio.motifs.matrix.FrequencyPositionMatrix)).

- [ ] 2.  De quelle manière allez-vous pouvoir obtenir une matrice poids-position (_position-weight matrix_, PWM) ? Quelle valeur mettez-vous pour les pseudo-poids (_pseudocounts_) ? (souvenez-vous du cours…)

Le résultat que vous obtenez doit dont être une PWM, de type `PositionWeightMatrix` ([documentation](https://biopython.org/docs/1.75/api/Bio.motifs.matrix.html?highlight=frequencypositionmatrix#Bio.motifs.matrix.PositionWeightMatrix)).

- [ ] 3.  Comment obtenir une PSSM à partir de cette PWM ?

La PSSM obtenue est de type `PositionSpecificScoringMatrix` ([documentation](https://biopython.org/docs/1.75/api/Bio.motifs.matrix.html?highlight=frequencypositionmatrix#Bio.motifs.matrix.PositionSpecificScoringMatrix)).

- [ ] 4.  Comment rechercher les occurrences d’une PSSM dans une séquence ?

Mise en place de fonctions utiles pour manipuler les PWM
--------------------------------------------------------

Toutes les fonctions seront positionnées dans un fichier `pwm.py`.

1.  Réalisez une fonction `pwm2pssm` qui, à partir d’une matrice de fréquence JASPAR (un objet `FrequencyPositionMatrix`) et d’un pseudo-poids passés en paramètre, retourne la PSSM correspondante (un objet `PositionSpecificScoringMatrix`).

2.  Réalisez une fonction `scan_sequence` qui, à partir d’une PSSM (un objet `PositionSpecificScoringMatrix`), d’une séquence (un objet Biopython `Bio.Seq`), et d’un seuil de score passés en paramètre, retourne une liste de couples position, score d’occurrence.


Script pour le rendu intermédiaire
----------------------------------

Il est temps maintenant de consolider ce qui a été fait la semaine dernière et cette semaine.

1.  Réalisez le script `scan_pwm.py` pour le rendu intermédiaire (le pseudo-poids sera figé à la valeur 0.1). Bien sûr ce script importera les modules `pwm.py` et `utils.py`.

2.  Pour tester votre script vous pourrez faire des recherches les matrices `MA0083, MA0057, MA0114, MA0056` sur `NM_007389` avec un seuil de score positionné à -2.0.

3.  Que signifie une position d’occurrence négative ?

4.  En lien avec la question précédente, posez-vous la question de l’endroit où se trouve, vis-à-vis du début du gène, la position d’occurrence d’une matrice fournie par votre script.


Recherche pour un ensemble de séquences
---------------------------------------

Dans la suite du projet nous allons rechercher les occurrences de matrices dans un ensemble de séquences.

1.  Ajouter à `utils.py` une fonction `download_promotors` qui, étant donné une liste d’identifiants de mRNA, une taille de séquence promotrice, un répertoire d’enregistrement (`.` par défaut), télécharge dans des fichiers séparés les séquences promotrices de ces mRNA au format FASTA. Les noms des fichiers seront les nom des identifiants mRNA suivi de la longueur du promoteur (par exemple, le promoteur de taille 100 de `NM_007389` sera stocké dans le fichier `NM_007389_100.fa`).

La construction d’un chemin valide se fait grâce à `os.path.join` (voir [documentation de `os.path`](https://docs.python.org/3.8/library/os.path.html))

Cette fonction sera utile dans les tests des fonctions suivantes car elle évitera de réaliser des requêtes trop fréquentes au NCBI (le NCBI pourrait réduire votre accès si il estime qu’il y a trop de requêtes).

2.  Mettez en œuvre la fonction `download_promotors` en téléchargeant les promoteurs des mRNA suivants : `NM_007389, NM_079420, NM_001267550, NM_002470, NM_003279, NM_005159, NM_003281, NM_002469, NM_004997, NM_004320, NM_001100, NM_006757` dans le répertoire `data`.

3.  Réalisez dans le module `pwm.py` une fonction `scan_all_sequences` qui, à partir d’une PSSM (un objet \``PositionSpecificScoringMatrix`), d’une liste de séquences (des objets Biopython `Bio.Seq`), retourne les couples position/score d’occurrence pour l’ensemble des séquences. Réfléchissez à la façon de structurer ces données pour pouvoir les exploiter ensuite.

4.  Réalisez dans le module `pwm.py` une fonction `score_window` qui, étant donné un résultat de `scan_all_sequences` et des coordonnées début/fin dans les séquences, retourne le score de la fenêtre.

5.  Réalisez dans le module `pwm.py` une fonction `best_window` qui, étant donné un résultat de `scan_all_sequences` et une taille de fenêtre, retourne les coordonnées de la fenêtre de meilleur score.

6.  Testez en cherchant la meilleure fenêtre pour la liste des mRNA donnée ci-dessus pour la matrice `MA_0114`.


Le module de gestion des arguments `argparse` de Python
-------------------------------------------------------

Dans l’objectif de livrer à la fin de l’UE un programme Python de bonne qualité, nous vous proposons d’explorer le module [argparse](https://docs.python.org/fr/3.8/library/argparse.html#module-argparse) de Python permettant de traiter très simplement les paramètres de la ligne de commande

En vous inspirant de ce [tutoriel](https://docs.python.org/fr/3/howto/argparse.html) mettez en place un script Python `test_args.py` qui prenne en option :

*   `-t` pour le seuil de score (option longue `--threshold`, pas de valeur par défaut) ;
*   `-l` pour la longueur du promoteur (option longue `--promotor-length`, par défaut 1000) ;
*   `-w` pour la longueur de la fenêtre glissante (option longue `--window-size`, par défaut 40).

Les identifiants des mRNA seront donnés en argument (et pas en option). Le script affichera simplement les valeurs des options et la liste des arguments.

Ce script préfigure le script de rendu final.
