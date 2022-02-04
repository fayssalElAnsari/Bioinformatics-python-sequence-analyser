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
from src.utils import *
from Bio import Entrez

# API du NCBI avec Biopython-------------------------------------------------

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

# efetch
    # 1. récupérer l’entrée NM_007389 au format Genbank puis au format FASTA.
        # On se connecte
Entrez.email = "angeldaniel.pastorrojas.etu@univ-lille.fr"
        # On recupere
gb_handle = Entrez.efetch(db="nucleotide", id="NM_007389", rettype="gb", retmode="text")
fasta_handle = Entrez.efetch(db="nucleotide", id="NM_007389", rettype="fasta", retmode="text")
        # On stock
gb_record = SeqIO.read(gb_handle, "gb")
fasta_record = SeqIO.read(fasta_handle, "fasta")
        # On ferme
fasta_handle.close()
gb_handle.close()
    # 2. Vérifiez que les séquences des entrées obtenues sont bien identiques
        # On compare
# compare_rec_seq(gb_record, fasta_record)
    # 3. En utilisant votre méthode find_cds sur le résultat au format Genbank, vérifiez que la CDS est bien identique à celle identifiée dans la première partie, avec le fichier Genbank.
# for i in record_genbank.features:
#     if i.type=="CDS":
#         print(i.location.start,i.location.end)
#         print(find_cds(gb_record))
#         print([i.location.start,i.location.end]==find_cds(gb_record))
# elink
    # 1. récupérer le gène correspondant à l’entrée `NM_007389`
gb_handle_elink = Entrez.elink(dbfrom="nucleotide",db="gene", id="NM_007389")
gb_record_elink = Entrez.read(gb_handle_elink)
gb_handle_elink.close()
# print(gb_record_elink)
    # 2. Identifiez comment trouver l’identifiant du gène.
# mrna_to_gene("NM_007389")
# ou
linked = [link["Id"] for link in gb_record_elink[0]["LinkSetDb"][0]["Link"]]
# print(linked[0])
# ou
# print(gb_record_elink[0]["LinkSetDb"][0]["Link"][0]["Id"])

    # 3. Dans le fichier `utils.py` réalisez une méthode `mrna_to_gene` qui prenne un numéro d’accession d’un ARNm et qui renvoie l’identifiant du gène correspondant (ou qui lève une exception `ValueError` en cas de problème).
# print(mrna_to_gene("12")) # renvoie ValueError
# print(mrna_to_gene("NM_007389")) # renvoie Id 

# Récupération de la portion amont d'un gène
    # 1. À partir de l’identifiant du gène obtenu, utilisez la méthode esummary pour pouvoir déterminer le numéro d’accession du chromosome (commençant par NC_) et les positions chromosomiques du gène.
gb_handle_esummary = Entrez.esummary(db="gene", id=mrna_to_gene("NM_007389"))
gb_record_esummary = Entrez.read(gb_handle_esummary)
gb_handle_esummary.close()

# print(type(gb_record_esummary))
# print(gb_record_esummary.keys())
# print(type(gb_record_esummary["DocumentSummarySet"]))
# print(gb_record_esummary["DocumentSummarySet"].keys())

    # numéro d’accession du chromosome :
# print(gb_record_esummary["DocumentSummarySet"]["DocumentSummary"][0]["GenomicInfo"][0]["ChrAccVer"])
    # les positions chromosomiques du gène début
# print(gb_record_esummary["DocumentSummarySet"]["DocumentSummary"][0]["GenomicInfo"][0]["ChrStop"])
    # les positions chromosomiques du gène fin
# print(gb_record_esummary["DocumentSummarySet"]["DocumentSummary"][0]["GenomicInfo"][0]["ChrStop"])

# Calcul de score à partir de matrices de fréquences --------------------------
