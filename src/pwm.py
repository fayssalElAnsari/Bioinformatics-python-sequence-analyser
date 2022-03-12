from Bio import SeqIO, Entrez, motifs
from Bio.SeqFeature import FeatureLocation
from Bio.Seq import Seq
from utils import *
import json
from pprint import *

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
            calculate_res = pssm.calculate(Seq("ACGTACGT"))
            print(calculate_res)
            max_score = pssm.max
            min_score = pssm.min
            abs_score_threshold = (max_score - min_score) * 0.8 + min_score
            print("recherche de la Seq('AGATAAGA') avec un seuil de ", abs_score_threshold , " : ")
            for position, score in pssm.search(Seq("AGATAAGA"), threshold=abs_score_threshold):
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
    '''
    pos_score_list = list()
    seq = Seq(seqstring)
    # print("recherche de la Seq(" + seqstring + ") avec un seuil de ", seuil , " : ")
    try:
        for position, score in pssm.search(seq, seuil):
            pos_score_list.append((position, score))
    except:
        pass
    return pos_score_list

def scan_all_sequences(pssm, seq_list, seuil):
    '''
    applique la fonction `scan_sequence()` deja definie sur une liste de sequences
    et retourne le resultat sous forme de liste de liste
    pour chaque pmid la liste de (pos, score) qui lui correspond
    '''
    seq_pos_score = list()
    for seq in seq_list:
        seq_pos_score.append(scan_sequence(pssm, seq, seuil))
    return seq_pos_score

def main():
    # generated_files = download_promotors(LIST_MRNA, 1024, "../data") #comment to use local files

    list_seq = []
    generated_files = []
    for mrna in LIST_MRNA:
        generated_files.append("./data/" + mrna + "_1024.fasta")

    for file_path in generated_files:
        list_seq.append(SeqIO.read(file_path, "fasta").seq)
    '''
    generated dictionary format:
        dictionary : {
            'pssm1' :
                {'pmid_1': [(pos1,score1), (pos2, score2),..., (pos_n, score_n)]},
                {'pmid_2': [(pos1,score1), (pos2, score2),..., (pos_n, score_n)]},
                ...
                ..
                .
                {'pmid_n': [(pos1,score1), (pos2, score2),..., (pos_n, score_n)]},
            'pssm2' :
                {'pmid_1': [(pos1,score1), (pos2, score2),..., (pos_n, score_n)]},
                {'pmid_2': [(pos1,score1), (pos2, score2),..., (pos_n, score_n)]},
                ...
                ..
                .
                {'pmid_n': [(pos1,score1), (pos2, score2),..., (pos_n, score_n)]},
            ...
            ..
            .
            'pssm_n' :
                {'pmid_1': [(pos1,score1), (pos2, score2),..., (pos_n, score_n)]},
                {'pmid_2': [(pos1,score1), (pos2, score2),..., (pos_n, score_n)]},
                ...
                ..
                .
                {'pmid_n': [(pos1,score1), (pos2, score2),..., (pos_n, score_n)]},
        }
    '''
    matrix_entry = {}
    mrna_entry = {}
    pos_score_list = []
    with open("./data/MA0037.jaspar") as handle: #one matrix for starters
        for matrix in motifs.parse(handle, "jaspar"):
            pssm = pwm2pssm(matrix, 0.01, False)
            pos_score_list.append(scan_all_sequences(pssm, list_seq, -20))
            for file_name, pos_score in zip(generated_files, pos_score_list[0]):
                mrna_entry[file_name] = pos_score
            matrix_entry[matrix] = mrna_entry
        pprint(matrix_entry)



if __name__ == "__main__":
    main()
