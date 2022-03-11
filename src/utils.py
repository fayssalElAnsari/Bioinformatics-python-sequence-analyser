from Bio import SeqIO, Entrez
from Bio.SeqFeature import FeatureLocation
import json, os, doctest

Entrez.email = "fayssal.el.ansari@gmail.com"

# TODO: faut modifier cette fonction pour accepter
# une seqRecord avec plusieurs sequences
def find_cds(seqRecord):
    '''
    Cette fonction prend en parametre une sequence et retourne les CDNs

    Example:
    >>> genebank = SeqIO.read("../data/NM_007389.gb", "genbank")
    >>> print(find_cds(genebank))
    [(ExactPosition(51), ExactPosition(1425))]
    '''
    liste_positions = []
    for feature in seqRecord.features:
        if feature.type == "CDS":
            liste_positions.append((feature.location.start, feature.location.end))
    return liste_positions
    # liste_positions = []
    # for featureLoc in FeatureLocation(seqRecord.start, seqRecord.end):
    #     liste_positions.append(featureLoc)
    # return liste_positions

def compare_rec_seq(record1, record2):
    '''
    cette fonction prend en parametre 2 records et les compare
    elle affiche le resulat de la comparaison en terminal
    et return le resulat sous forme de boolean
    '''
    resultat = str(record1.seq) == str(record2.seq)
    if (resultat): # True
        print("  Les 2 sequences sont identiques")
    else:
        print("  Les 2 sequences NE sont PAS identiques!")
    return resultat

def mrna_to_gene(pmid):
    '''
    
    '''
    try:
        handle = Entrez.elink(dbfrom="nucleotide", db="gene", id=pmid, linkname="nucleotide_gene")
        record = Entrez.read(handle)
        assert record != []
        id = record[0]['LinkSetDb'][0]['Link'][0]['Id'] #TODO: faut changer cette partie
        return id
    except AssertionError as ve:
        return ValueError(str(pmid) + " : wrong id value passed")
        

def upstream_gene_seq(pmid, taille_seq):
    '''
    à partir d’un identifiant de gène et d’une longueur retourne un objet Biopython Bio.Seq 
    correspondant à la séquence ADN amont de ce gène de la longueur demandée 
    
     /!\ (attention au brin sur lequel se trouve le gène).
    '''
    """ renvoie le numéro d'acension"""
    handle = Entrez.esummary(db="gene", id=mrna_to_gene(pmid))
    record = Entrez.read(handle)
    handle.close()
    # print(json.dumps(record, indent=2, separators=(", ", " : ")))
    # print(record["DocumentSummarySet"]["DocumentSummary"][0]["GenomicInfo"][0]["ChrAccVer"])
    return str(record["DocumentSummarySet"]["DocumentSummary"][0]["GenomicInfo"][0]["ChrAccVer"])


def download_promotors(l_mrna, taille_seq, dir="."):
    '''
    cette fonctoin prend en parametre:
    * l_mrna: une liste d'identifiants mrna,
    * taille_seq: une taille de sequence de gene a recuperer
    * dir: le repetoire destination

    Etant donné une liste d’identifiants de mRNA, une taille de séquence promotrice, 
    un répertoire d’enregistrement (. par défaut), télécharge dans des fichiers séparés 
    les séquences promotrices de ces mRNA au format FASTA
    '''
    for mrna in l_mrna:
        nom_fichier = str(mrna) + "_" + str(taille_seq) + ".fasta"
        chemin_fichier = os.path.join(os.getcwd(), "data", nom_fichier)
        
        id = mrna_to_gene(mrna)
        print(id)
        print(upstream_gene_seq(mrna, taille_seq))

        # try:
        #     fasta_handle = Entrez.efetch(db="nucleotide", id=id, rettype="fasta", retmode="text", retmax=taille_seq)
        #     output_seq = fasta_handle.read()
        #     fasta_handle.close()
        #     print(output_seq)

        #     output_file = open(chemin_fichier, "w")
        #     output_file.write(output_seq)
        #     output_file.close()
        # except:
        #     print("couldn't fetch sequence with id " + id)

        

if __name__ == "__main__":
    list_mrna = ["NM_007389", "NM_079420", "NM_001267550", "NM_002470", "NM_003279", "NM_005159", 
    "NM_003281", "NM_002469", "NM_004997", "NM_004320", "NM_001100", "NM_006757"]
    download_promotors(list_mrna, 10, "../data")
    # doctest.testmod()
