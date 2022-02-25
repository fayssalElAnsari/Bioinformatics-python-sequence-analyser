#!/usr/bin/python
import sys

def main(args):
    # fichier contenant une matrice JASPAR (dirrection dossier)
    print(args[0])
    fichier=args[0]
    # un identifiant Genbank d’un mRNA ;
    print(args[1])
    idGenbank=args[1]
    # une taille pour la séquence promotrice ;
    tailleSequencePromotrice=args[2]
    # un seuil de score.
    print(args[3])
    seuilScore=args[3]
    
if __name__ == "__main__":
   main(sys.argv[1:])
              