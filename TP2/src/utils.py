from Bio import SeqIO

# faut modifier cette fonction pour accepter 
# une seqRecord avec plusieurs sequences
def find_cds(seqRecord):
    '''
    Cette fonction prend en parametre une sequence et retourne les CDNs
    
    Example:
    >>> genebank = SeqIO.read("data/NM_007389.gb", "genbank")
    >>> print(find_cds(genebank))
    [(ExactPosition(51), ExactPosition(1425))]

    '''
    liste_positions = []
    for feature in seqRecord.features:
        if feature.type == "CDS":
            liste_positions.append((feature.location.start, feature.location.end))
    return liste_positions

if __name__ == "__main__":
    import doctest
    doctest.testmod()

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