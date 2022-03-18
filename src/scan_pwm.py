from pwm import *
from utils import *
import sys

def main(args):
    if (len(args) < 4): 
        print("usage: python src/scan_pwm.py file idGenbank tailleSequencePromotrice seuilScore")
        print("     example: python src/scan_pwm.py MA0083.jaspar NM_007389 6 -20")
        exit()

    fichier = args[0]
    idGenbank = args[1]
    tailleSequencePromotrice = int(args[2])
    seuilScore = int(args[3])

    pseudo_weight = 0.1
    
    id = mrna_to_gene(idGenbank)
    handle = Entrez.esummary(db="gene", id=id)
    record = Entrez.read(handle)
    handle.close()

    accession_nb = record["DocumentSummarySet"]["DocumentSummary"][0]["GenomicInfo"][0]["ChrAccVer"]
    seq_start = int(record["DocumentSummarySet"]["DocumentSummary"][0]["GenomicInfo"][0]["ChrStart"]) - tailleSequencePromotrice
    seq_stop = int(record["DocumentSummarySet"]["DocumentSummary"][0]["GenomicInfo"][0]["ChrStart"]) - 1

    fasta_handle = Entrez.efetch(db="nucleotide", id=accession_nb, rettype="fasta", retmode="text", strand=1, seq_start=seq_start, seq_stop=seq_stop)
    seq = str(SeqIO.read(fasta_handle, "fasta").seq)

    fichier = "data/" + fichier
    scan_res = list

    with open(fichier) as handle:
        for matrix in motifs.parse(handle, "jaspar"):
            matrix_id = matrix.matrix_id
            pssm = pwm2pssm(matrix, pseudo_weight, False)
            scan_res = scan_sequence(pssm, seq, seuilScore).get_result()
            for position, score in scan_res:
                print(matrix_id + " " + str(position) + " " + str(score)) 


if __name__ == "__main__":
    main(sys.argv[1:])

