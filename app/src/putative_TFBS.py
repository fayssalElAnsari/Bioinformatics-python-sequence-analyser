import argparse
from pwm import main as pwm_main
from pwm import *

'''
-m pour le fichier contenant la matrice (option longue --pfm, pas de valeur par défaut) ;
-t pour le seuil de score de matrice (option longue --threshold, pas de valeur par défaut) ;
-l pour la longueur du promoteur (option longue --promotor-length, par défaut 1000) ;
-w pour la longueur de la fenêtre glissante (option longue --window-size, par défaut 40) ;
-s pour le seuil de score de fenêtre (option longue --window-threshold, pas de valeur par défaut) ;
-p pour la valeur du pseudo-poids (option longue --pseudocount, valeur par défaut 0.1).
'''
def main(args):
    parser = argparse.ArgumentParser()
    parser.parse_args()
    

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-m", "--pfm", help="le fichier contenant la matrice")
    parser.add_argument("-t", "--threshold", help="The threshold of the results", type=int)
    parser.add_argument("-l", "--promotor-length", help="The lengh of the promotor", type=int, default=1000)
    parser.add_argument("-w", "--window-size", help="the size of the sliding window", type=int, default=40)
    parser.add_argument("-s", "--window-threshold", type=int)
    parser.add_argument("-p", "--pseudocount", help="le seuil de poids", type=int, default=0.1)

    parser.add_argument("-v", "--verbosity", help="increases the verbosity", action="store_true")
    args = parser.parse_args()
    if (args.verbosity):
        print("verbosity turned on")
    
    nb_occurences = scan_sequence()
    score_de_fenetre = score_window()

    pwm_main()

    
