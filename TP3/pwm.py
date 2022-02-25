from Bio import SeqIO, Entrez, motifs
from Bio.SeqFeature import FeatureLocation
import json

Entrez.email = "fayssal.el.ansari@gmail.com"

def jaspar2pwm():
    with open("data/MA0037.2.jaspar") as handle:
        count = 0
        for m in motifs.parse(handle, "jaspar"):
            print(m)
            print("normalizing...")
            print("PWM:")
            print(m.counts.normalize(50)) # 50 by trial to get a 0.0x difference
            print("PSSM")
            print(m.counts.normalize(0.01).log_odds())

            # motifs.calculate(m)
            count = count + 1

    print("Le nombre des matrices lus: " + str(count))

def pwm2pssm(matrix, pseudo_weight):
    pass


def main():
    jaspar2pwm()

if __name__ == "__main__":
    main()