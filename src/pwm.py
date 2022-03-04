from Bio import SeqIO, Entrez, motifs
from Bio.SeqFeature import FeatureLocation
from Bio.Seq import Seq
import json

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
    scan l'existance d'une sequence au dessus d'un seuil dans mune PSSM
    '''
    l = list()
    seq = Seq(seqstring)
    print("recherche de la Seq(" + seqstring + ") avec un seuil de ", seuil , " : ")
    try:
        for position, score in pssm.search(seq, seuil):
            l.append((position, score))
    except:
        pass
    return l

def scan_sequences(pssm, seq_list, seuil):
    '''
    cette fonction fait la meme chose que scan sequence mais cette fois pour 
    une liste de sequence au lieu d'une seul sequence
    '''
    liste_pos_score = []
    for seq in seq_list:
        liste_pos_score.append(scan_sequence(pssm, seq, seuil))
    return liste_pos_score

def main():
    list_seq = SeqIO.read("../data/NM_007389.fasta", "fasta")
    with open("../data/MA0037.jaspar") as handle:
        for matrix in motifs.parse(handle, "jaspar"):
            pssm = pwm2pssm(matrix, 0.01, False)
            # scan_res = scan_sequence(pssm, "AGATAAGA", 1)
            # print(scan_res)
            print(scan_sequences(pssm, list_seq, -20))

if __name__ == "__main__":
    main()