from pwm import *
from utils import *
import sys

def main(args):
    if (len(args) < 4): 
        print("please add params!")
        exit()
    # fichier contenant une matrice JASPAR (dirrection dossier)
    print(args[0])
    fichier = args[0]
    # un identifiant Genbank d’un mRNA ;
    print(args[1])
    idGenbank = args[1]
    # une taille pour la séquence promotrice ;
    tailleSequencePromotrice = int(args[2])
    # un seuil de score.
    print(args[3])
    seuilScore = int(args[3])

    pseudo_weight = 0.1
    seq = find_cds(idGenbank)
    pssm = pwm2pssm(matrix, seuilScore, False)
    scan_res = scan_sequence(pssm, seq, -2)

            


if __name__ == "__main__":
    main(sys.argv[1:])

