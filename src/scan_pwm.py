from pwm import *
from utils import *
import sys

def main(args):
    if (len(args) < 4): 
        print("please add params!")
        exit()
    # fichier contenant une matrice JASPAR (dirrection dossier)
    # print(args[0])
    fichier = args[0]
    # un identifiant Genbank d’un mRNA ;
    # print(args[1])
    idGenbank = args[1]
    # une taille pour la séquence promotrice ;
    tailleSequencePromotrice = int(args[2])
    # un seuil de score.
    # print(args[3])
    seuilScore = int(args[3])

    pseudo_weight = 0.1
    fasta_handle = Entrez.efetch(db="nucleotide", id=idGenbank, rettype="fasta", retmode="text")
    seq = str(SeqIO.read(fasta_handle, "fasta").seq)

    fichier = "data/" + fichier
    scan_res = list
    with open(fichier) as handle:
        for matrix in motifs.parse(handle, "jaspar"):
            pssm = pwm2pssm(matrix, pseudo_weight, False)
            scan_res = scan_sequence(pssm, seq, seuilScore)
    
    for position, score in scan_res:
        print("Ahr::Arnt " + str(position) + " " + str(score)) 


if __name__ == "__main__":
    main(sys.argv[1:])

