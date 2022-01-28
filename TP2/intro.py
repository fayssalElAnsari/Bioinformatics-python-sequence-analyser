#protéine s'accroche à des facteurs de fixation
#facteur de transcription (une protéine) reconnais un petit bout d'adn pas exactement mais à peu près
#2 facteur de transcription n'ont pas la même accroche
#en amon du début du gène une flèche blue
#matrice des comptage
#calculer pssm, pwm
#par défaut 0.1 des pseudo pounts
#jaspar il faut télécharger les matrices à la main

#DOCTEST À FAIRE

# TP2
from Bio import SeqIO

    # 1. En consultant la documentation, identifiez comment récupérez la séquence depuis ces entrées
record_genbank = SeqIO.read("data/NM_007389.gb", "genbank")
sequance_gb=record_genbank.seq
# print(sequance_gb)
record_fasta = SeqIO.read("data/NM_007389.fasta", "fasta")
sequance_fasta=record_fasta.seq
# print(sequance_fasta)

    # 2. Comment obtenir la séquence sous forme d’une string Python (de type str) ? Vérifiez que les séquences sont bien identiques entre l’entrée Genbank et l’entrée FASTA.
sequance_fasta_str = str(sequance_fasta)
sequance_gb_str = str(sequance_gb)
# print(sequance_fasta_str,"\n",sequance_gb_str)

    # 3. Comment obtenir la séquence complémentaire inverse (reverse complement en anglais) ?
sequance_fasta_reverse = sequance_fasta.reverse_complement()
sequance_gb_reverse = sequance_gb.reverse_complement()
# print(sequance_fasta,"\n",sequance_gb)

    # 4. Des attributs existent pour récupérer les annotations ou les features des entrées. Quels sont ces attributs ? Existent-ils aussi bien pour l’entrée FASTA que pour l’entrée Genbank ? Pourquoi ?
# print(record_fasta,"\n"*8,record_genbank) # pour fasta, on a 0 freatures tandis que pour genbank on en a 19
record_fasta_features_len = len(record_fasta.features)     # nombre de features dans record fasta
record_genbank_features_len = len(record_genbank.features) # nombre de features dans record ganbank

def affiche(features):
    for i in features:
        print(i)    
# affiche(record_fasta.features)
# affiche(record_genbank.features)

    # 5. Intéressez-vous à la première feature. Comment peut-on accéder à ses positions de début et de fin ?
def premier_fin_features(features):
    debut=0
    if len(features)==0 :
        print("pas de features")
    elif len(features)==1 :
        print("début et fin de features : \n", features[debut])
    else:
        fin=len(features)-1
        print("début features : \n",features[0],"\n","fin features: \n",features[fin])
# premier_fin_features(record_fasta.features)
# premier_fin_features(record_genbank.features)