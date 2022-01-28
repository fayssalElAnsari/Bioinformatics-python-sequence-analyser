from Bio import SeqIO

def find_cds(seqRecord):
    liste_positions = []
    for feature in seqRecord.features:
        if feature.type == "CDS":
            liste_positions.append((feature.location.start, feature.location.end))
    return liste_positions



