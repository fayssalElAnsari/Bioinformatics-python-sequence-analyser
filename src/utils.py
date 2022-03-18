from Bio import Entrez, SeqIO
from constants import LIST_MRNA
import os
import doctest
# import json

Entrez.email = "fayssal.el.ansari@gmail.com"


# TODO: faut modifier cette fonction pour accepter
# une seqRecord avec plusieurs sequences
def find_cds(seqRecord):
    '''
    Cette fonction prend en parametre une sequence et retourne les CDNs

    Example:
    >>> genebank = SeqIO.read("./data/NM_007389.gb", "genbank")
    >>> print(find_cds(genebank))
    [(ExactPosition(51), ExactPosition(1425))]
    '''
    liste_positions = []
    for feature in seqRecord.features:
        if feature.type == "CDS":
            liste_positions.append((feature.location.start,
                                    feature.location.end))
    return liste_positions

def compare_rec_seq(record1, record2):
    '''
    cette fonction prend en parametre 2 records et les compare
    elle affiche le resulat de la comparaison en terminal
    et return le resulat sous forme de boolean
    '''
    resultat = str(record1.seq) == str(record2.seq)
    if (resultat):  # True
        print("  Les 2 sequences sont identiques")
    else:
        print("  Les 2 sequences NE sont PAS identiques!")
    return resultat


def mrna_to_gene(pmid):
    '''
    '''
    try:
        handle = Entrez.elink(dbfrom="nucleotide", db="gene",
                              id=pmid, linkname="nucleotide_gene")
        record = Entrez.read(handle)
        assert record != []
        # TODO: faut changer cette partie
        id = record[0]['LinkSetDb'][0]['Link'][0]['Id']
        return id
    except AssertionError as ae:
        return ValueError(str(ae) + str(pmid) + " : wrong id value passed")
        

def upstream_gene_seq(pmid, taille_seq):
    '''
    à partir d’un identifiant de gène et d’une longueur retourne un objet Biopython Bio.Seq 
    correspondant à la séquence ADN amont de ce gène de la longueur demandée 
    
     /!\ (attention au brin sur lequel se trouve le gène).
    '''
    """ renvoie le numéro d'accession"""
    id = mrna_to_gene(pmid)
    handle = Entrez.esummary(db="gene", id=id)
    record = Entrez.read(handle)
    handle.close()
    # print(json.dumps(record, indent=2, separators=(", ", " : ")))
    accession_nb = record["DocumentSummarySet"]["DocumentSummary"][0]["GenomicInfo"][0]["ChrAccVer"]
    seq_start = int(record["DocumentSummarySet"]["DocumentSummary"][0]["GenomicInfo"][0]["ChrStart"]) - taille_seq
    seq_stop = int(record["DocumentSummarySet"]["DocumentSummary"][0]["GenomicInfo"][0]["ChrStart"]) - 1
    fasta_handle = Entrez.efetch(db="nucleotide", id=accession_nb, rettype="fasta", retmode="text", strand=1, seq_start=seq_start, seq_stop=seq_stop)
    return fasta_handle.read()


def download_promotors(l_mrna, taille_seq, dir="."):
    '''
    cette fonctoin prend en parametre:
    * l_mrna: une liste d'identifiants mrna,
    * taille_seq: une taille de sequence de gene a recuperer
    * dir: le repetoire destination

    Etant donné une liste d’identifiants de mRNA, une taille de séquence promotrice, 
    un répertoire d’enregistrement (. par défaut), télécharge dans des fichiers séparés 
    les séquences promotrices de ces mRNA au format FASTA

    et renvoie la liste des fichiers generer 
    '''
    list_files = []
    for mrna in l_mrna:
        nom_fichier = str(mrna) + "_" + str(taille_seq) + ".fasta"
        chemin_fichier = os.path.join(os.getcwd(), "data", nom_fichier)
        
        id = mrna_to_gene(mrna)
        output_seq = upstream_gene_seq(mrna, taille_seq)

        output_file = open(chemin_fichier, "w")
        output_file.write(output_seq)
        output_file.close()
        print("Wrote to file: " + nom_fichier)
        list_files.append(chemin_fichier)
    return list_files
        

if __name__ == "__main__":
    # download_promotors(LIST_MRNA, 1024, "../data")
    doctest.testmod()

