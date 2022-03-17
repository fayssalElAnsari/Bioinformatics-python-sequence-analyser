from Bio import SeqIO, Entrez
from Bio.SeqFeature import FeatureLocation
import json, os, doctest

Entrez.email = "fayssal.el.ansari@gmail.com"

# TODO: faut modifier cette fonction pour accepter
# une seqRecord avec plusieurs sequences
def find_cds(seqRecord): #marche
    '''Renvoie une liste des couples de positions de début et de fin des CDS contenues dans la séquence seqRecord

    Example:
    >>> genebank = SeqIO.read("../data/NM_007389.gb", "genbank")
    >>> find_cds(genebank)
    [(ExactPosition(51), ExactPosition(1425))]
    '''
    liste_positions = []
    for feature in seqRecord.features:
        if feature.type == "CDS":
            liste_positions.append((feature.location.start, feature.location.end))
    return liste_positions

def geneID(NM):
    """
    renvoie la liste des Identifiants numerique geneID:
    >>> geneID("NM_007389")
    ['11435']
    """
    handle_elink = Entrez.elink(dbfrom="nucleotide",db="gene", id=NM)
    record_elink = Entrez.read(handle_elink)
    handle_elink.close()
    l=[]
    print(record_elink)
    for link in record_elink[0]["LinkSetDb"][0]["Link"]:
        l.append(link["Id"])
    return l

def mrna_to_gene(gene_NM_):
    '''
    renvoie l’identifiant du gène (gene_ID) (de type <class 'Bio.Entrez.Parser.StringElement'> )
    >>> mrna_to_gene("NM_007389")
    ['11435']
    '''
    try:
        handle_elink = Entrez.elink(dbfrom="nucleotide",db="gene", id=gene_NM_)
        record_elink = Entrez.read(handle_elink)
        handle_elink.close()
        assert record_elink != []
        l=[]
        assert record_elink[0]["LinkSetDb"] != [] #mrna_to_gene("19304878") il est correct mais ...
        for link in record_elink[0]["LinkSetDb"][0]["Link"]:
            l.append(link["Id"])
        return l
    except AssertionError as ve:
        return ValueError(str(gene_NM_) + " : wrong id value passed")

def numero_accession(gene_ID):
    """
    renvoie le numéro d’accession du chromosome (commençant par NC_) :
    >>> numero_accession(mrna_to_gene("NM_007389"))
    'NC_000068.8'
    """
    try:
        handle_esummary = Entrez.esummary(dbfrom="nucleotide", db="gene", id=gene_ID)
        record_esummary = Entrez.read(handle_esummary)
        handle_esummary.close()
        return record_esummary["DocumentSummarySet"]["DocumentSummary"][0]["GenomicInfo"][0]["ChrAccVer"]
    except AssertionError as ve:
        return ValueError(str(gene_ID) + " : wrong id value passed")

def postion_chromosomique_gene_debut(gene_ID):
    """
    renvoie la postion_chromosomique_gene_debut du chromosome :
    >>> postion_chromosomique_gene_debut(mrna_to_gene("NM_007389"))
    '73410681'
    """
    try:
        handle_esummary = Entrez.esummary(dbfrom="nucleotide", db="gene", id=gene_ID)
        record_esummary = Entrez.read(handle_esummary)
        handle_esummary.close()
        return record_esummary["DocumentSummarySet"]["DocumentSummary"][0]["GenomicInfo"][0]["ChrStart"]
    except AssertionError as ve:
        return ValueError(str(gene_ID) + " : wrong id value passed")

def postion_chromosomique_gene_fin(gene_ID):
    """
    renvoie la postion_chromosomique_gene_fin du chromosome :
    >>> postion_chromosomique_gene_fin(mrna_to_gene("NM_007389"))
    '73393624'
    """
    try:
        handle_esummary = Entrez.esummary(dbfrom="nucleotide", db="gene", id=gene_ID)
        record_esummary = Entrez.read(handle_esummary)
        handle_esummary.close()
        return record_esummary["DocumentSummarySet"]["DocumentSummary"][0]["GenomicInfo"][0]["ChrStop"]
    except AssertionError as ve:
        return ValueError(str(gene_ID) + " : wrong id value passed")

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

def upstream_gene_seq(pmid):
    '''
    à partir d’un identifiant de gène et d’une longueur retourne un objet Biopython Bio.Seq
    correspondant à la séquence ADN amont de ce gène de la longueur demandée
     /!\ (attention au brin sur lequel se trouve le gène).
    '''
    """ renvoie le numéro d'acension"""
    handle = Entrez.esummary(db="gene", id=mrna_to_gene(pmid))
    record = Entrez.read(handle)
    handle.close()
    print(json.dumps(record, indent=2, separators=(", ", " : ")))
    # print(record["DocumentSummarySet"]["DocumentSummary"][0]["GenomicInfo"][0]["ChrAccVer"])
    return record["DocumentSummarySet"]["DocumentSummary"][0]["GenomicInfo"][0]["ChrAccVer"]



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
        # id = Entrez.read(Entrez.esearch(db="genbank", term=mrna))
        id = mrna_to_gene(mrna)
        print(id)
        fast_handle = Entrez.efetch(db="nucleotide", id=id, rettype="fasta", retmode="text")
        fast_record = fast_handle.read()
        print(fast_record)
        # sequence = Entrez.read(gb_handle)
        # print(sequence)
        fast_handle.close()

if __name__ == "__main__":
    list_mrna = ["NM_007389", "NM_079420", "NM_001267550", "NM_002470", "NM_003279", "NM_005159", "NM_003281", "NM_002469", "NM_004997", "NM_004320", "NM_001100", "NM_006757"]
#     download_promotors(list_mrna, 1024, "../data")
    # doctest.testmod()
