from Bio import SeqIO, Entrez, motifs
from Bio.SeqFeature import FeatureLocation
from Bio.Seq import Seq
import json

Entrez.email = "fayssal.el.ansari@gmail.com"

def jaspar2pwm():
    with open("data/MA0037.2.jaspar") as handle:
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
    l = list()
    seq = Seq(seqstring)
    print("recherche de la Seq('AGATAAGA') avec un seuil de ", seuil , " : ")
    for position, score in pssm.search(seq, seuil):
        l.append((position, score))
    return l


def main():
    # jaspar2pwm()
    with open("data/MA0037.2.jaspar") as handle:
        for matrix in motifs.parse(handle, "jaspar"):
            pssm = pwm2pssm(matrix, 0.01, False)
            scan_res = scan_sequence(pssm, "AGATAAGA", 1)
            print(scan_res)


if __name__ == "__main__":
    main()