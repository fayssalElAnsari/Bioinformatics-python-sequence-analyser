from Bio import SeqIO, Entrez, motifs
from Bio.SeqFeature import FeatureLocation
from Bio.Seq import Seq
from utils import *
from pprint import *
import json
from SequenceResult import *
from MatrixResult import *


Entrez.email = "fayssal.el.ansari@gmail.com"


def jaspar2pwm():
    ''' 
    cette fonction est la reponse a la premiere partie du TP3
    on genere une matrice de frequence on la normalise pour
    obtenir la PWM, a partir de cette matrice on genere la PSSM
    et finalement on cherche la presence d'une Seq (on a choisis
    une sequence qu'on sait qu'elle existe dans la matric) au dessus
    d'un seuil calculer a partir du min et max de la PSSM
    '''
    with open("../data/MA0037.jaspar") as handle:
        count = 0
        for m in motifs.parse(handle, "jaspar"):
            print(m)
            print("normalizing...")
            print("PWM with pseudo wieght of 50:")
            pwm = m.counts.normalize(50)
            print(pwm) # 50 by trial to get a 0.0x difference
            pwm2 = m.counts.normalize(0.01)
            print("PSSM")
            pssm = pwm2.log_odds()
            print(pssm)
            print("PWM score for 'ACGTACGT': ")
            calculate_res = pssm.calculate(pssm.consensus)
            print(calculate_res)
            max_score = pssm.max
            min_score = pssm.min
            abs_score_threshold = (max_score - min_score) * 0.8 + min_score
            print("recherche de la Seq('AGATAAGA') avec un seuil de ", abs_score_threshold , " : ")
            for position, score in pssm.search(Seq("AGATAAGA"), threshold = abs_score_threshold):
                print("Position %d: score = %5.3f" % (position, score))
            # motifs.calculate(m)
            count = count + 1

    # print("Le nombre des matrices lus: " + str(count))


def pwm2pssm(matrix, pseudo_weight, v = False):
    '''
    cette fonction converti une PWM en une PSSM
    '''
    if v:
        print(matrix)
        print("normalizing...")
        print("PWM with pseudo wieght of: ", pseudo_weight)
    pwm2 = matrix.counts.normalize(pseudo_weight)
    if v:
        print("PSSM")
    pssm = pwm2.log_odds()
    if v:
        print(pssm)
    return pssm


def scan_sequence(pssm, seqstring, seuil):
    '''
    scan l'existance d'une sequence au dessus d'un seuil dans une PSSM
    renvoie une liste de (position, score) pour la 'pssm' dans 'seqstring'
    returns: the result as an instance of the class SequenceResult
    '''
    seq = Seq(seqstring)

    scan = SequenceResult()
    scan.set_name(seqstring) # maybe change it later to something simpler
    scan.set_seq(seq)
    scan.set_matrix(pssm)
    scan.set_threshhold(seuil)
    # print("recherche de la Seq(" + seqstring + ") avec un seuil de ", seuil , " : ")
    try:
        for position, score in pssm.search(seq, seuil):
            scan.append_pos_score((position, score))
    except:
        pass
    return scan


def scan_all_sequences(pssm, seq_list, seuil):
    '''
    applique la fonction `scan_sequence()` deja definie sur une liste de sequences
    et retourne le resultat sous forme de liste de liste
    pour chaque pmid la liste de (pos, score) qui lui correspond
    returns: the result as an instance of the class MatrixResult
    '''
    scan = MatrixResult()
    scan.set_name(pssm.consensus)
    scan.set_matrix(pssm)
    scan.set_seq_list(seq_list)
    scan.set_threshhold(seuil)

    for seq in seq_list:
        scan.append_scan_result(scan_sequence(pssm, seq, seuil))
    return scan


def score_window(res_scan, coord_start, coord_stop):
    '''
    étant donné un résultat de scan_all_sequences et des coordonnées
    début/fin dans les séquences, retourne le score de la fenêtre.
    '''
    for matrix in res_scan:
        for sequences in matrix:
            for seq in sequences:
                for (pos, score) in seq:
                    if (pos < coord_start or pos > coord_start): #need to be edited
                        res_scan[matrix][seq].remove((pos, score))
    return res_scan


def main():
    # generated_files = download_promotors(LIST_MRNA, 1024, "../data") #comment to use local files
    list_seq = []
    generated_files = []
    for mrna in LIST_MRNA:
        generated_files.append("./data/" + mrna + "_1024.fasta")

    for file_path in generated_files:
        list_seq.append(SeqIO.read(file_path, "fasta").seq)

    matrices = list()

    with open("./data/MA0037.jaspar") as handle: # one matrix for starters
        for matrix in motifs.parse(handle, "jaspar"):
            pssm = pwm2pssm(matrix, 0.01, False)
            matrices.append(scan_all_sequences(pssm, list_seq, -20))
        for matrix in matrices:
            print(matrix)


if __name__ == "__main__":
    main()

