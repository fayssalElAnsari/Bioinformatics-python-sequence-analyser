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


def pwm2pssm(fpm, pseudo_weight, v = False):
    '''
    This function converts a PWM into a PSSM

    Args:
        fpm: Frequency Position Matrix in JASPAR format
        psuedo_weight: to be passed into the normalize function
        v: is set to true adds verbosity

    Returns:
        A Position Specific Scoring Matrix

    Raises:

    '''
    if v:
        print(fpm)
        print("Normalizing...")
        print("PWM with pseudo wieght of: ", pseudo_weight)
    pwm2 = fpm.counts.normalize(pseudo_weight)
    if v:
        print("PSSM")
    pssm = pwm2.log_odds()
    if v:
        print(pssm)
    return pssm


def scan_sequence(pssm, seqstring, threshold):
    '''
    Scan l'existance d'une sequence au dessus d'un threshold dans une PSSM
    renvoie une liste de (position, score) pour la 'pssm' dans 'seqstring'
    returns: the result as an instance of the class SequenceResult

    Args:
        pssm: A Position Specific Scoring Matrix
        seqstring: The sequence to be scanned
        threshold: the threshold to be taken in account in the scan

    Returns:
        A SequenceResult object containing the list of (pos, score)
        for the given sequence scan

    Raises:
        
    '''
    seq = Seq(seqstring)

    scan = SequenceResult()
    scan.set_name(seqstring) # maybe change it later to something simpler
    scan.set_seq(seq)
    scan.set_matrix(pssm)
    scan.set_threshold(threshold)
    # print("recherche de la Seq(" + seqstring + ") avec un threshold de ", threshold , " : ")
    try:
        for position, score in pssm.search(seq, threshold):
            scan.append_pos_score((position, score))
    except:
        pass
    return scan


def scan_all_sequences(pssm, seq_list, threshold):
    '''
    Applique la fonction `scan_sequence()` deja definie sur une liste de sequences
    et retourne le resultat sous forme de liste de liste
    pour chaque pmid la liste de (pos, score) qui lui correspond
    returns: the result as an instance of the class MatrixResult
    
    Args:
        pssm: A Position Specific Scoring Matrix
        seq_list: The list of sequences to be scanned
        threshold: the threshold to be taken in account in the scan

    Returns:
        A MatrixResult object containing the result of the scan 
        for one matrix (pssm)

    Raises:


    '''
    scan = MatrixResult()
    scan.set_name(pssm.consensus)
    scan.set_matrix(pssm)
    scan.set_seq_list(seq_list)
    scan.set_threshhold(threshold)

    for seq in seq_list:
        scan.append_scan_result(scan_sequence(pssm, seq, threshold))
    return scan


def score_window(res_scan:MatrixResult, coord_start, coord_stop):
    '''
    étant donné un résultat de scan_all_sequences et des coordonnées
    début/fin dans les séquences, retourne le score de la fenêtre.
    '''
    before = list()
    result = list()
    for matrix in res_scan.get_result():
        print(len(matrix.get_result()))
        for (pos, score) in matrix.get_result():
            if (abs(pos) > coord_start and abs(pos) < coord_stop): #needs to be edited
                result.append((pos, score))
        break
    print(len(result))
    return len(result)
    

def generatedFiles():
    """Renvoie une liste de type str contenant
    les chemins dans ""../data",
    des fichiers issue de la list LIST_MRNA (se trouvant dans src/constant.py)
    et finissant par "_1024.fasta"
    """
    generated_files = []
    for mrna in LIST_MRNA:
        generated_files.append("./data/" + mrna + "_1024.fasta")
    return generated_files


def listSeq(generated_files):
    """Renvoie une List<class 'Bio.Seq.Seq'>, une liste des séquences de chaque chemin issue de la liste passé en paramètre
    Prend un parametre de type List<str>, une liste contenant les chemins des fichier .fasta contenant des séquences
    """
    list_seq = []
    for file_path in generated_files:
        list_seq.append(SeqIO.read(file_path, "fasta").seq)
    return list_seq


def main():
    # generated_files = download_promotors(LIST_MRNA, 1024, "../data") #comment to use local files
    generated_files=[]
    list_seq=[]
    generated_files = generatedFiles()
    list_seq = listSeq(generated_files)
    l=["./data/MA0037.jaspar","./data/MA0083.jaspar"]
    matrices = list()
    for e in l:
        with open(e) as handle: # one matrix for starters
            for matrix in motifs.parse(handle, "jaspar"):
                pssm = pwm2pssm(matrix, 0.01, False)
                matrices.append(scan_all_sequences(pssm, list_seq, -20))
    matrices.append(scan_all_sequences(pssm, list_seq, -20))
    for matrix in matrices:
        # print(matrix)
        score_window(matrix, 0, 100)
        break


if __name__ == "__main__":
    main()

