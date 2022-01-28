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


