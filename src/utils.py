from Bio import SeqIO, Entrez
from Bio.SeqFeature import FeatureLocation
import json

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
    cette fonction prend en parametre 2 records et les comparer
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
    try:
        handle = Entrez.elink(dbfrom="nucleotide", db="gene", id=pmid, linkname="nucleotide_gene")
        record = Entrez.read(handle)
        assert record != []
        id = record[0]['LinkSetDb'][0]['Link'][0]['Id'] #TODO: faut changer cette partie
        return id
    except AssertionError as ve:
        return ValueError(str(pmid) + " : wrong id value passed")
        

def upstream_gene_seq(pmid):
    """ renvoie le numéro d'acension"""
    handle = Entrez.esummary(db="gene", id=mrna_to_gene(pmid))
    record = Entrez.read(handle)
    handle.close()
    print(json.dumps(record, indent=2, separators=(", ", " : ")))
    # print(record["DocumentSummarySet"]["DocumentSummary"][0]["GenomicInfo"][0]["ChrAccVer"])
    return record["DocumentSummarySet"]["DocumentSummary"][0]["GenomicInfo"][0]["ChrAccVer"]

if __name__ == "__main__":
    import doctest
    doctest.testmod()
