from Bio import motifs

with open("data/MA0037.2.jaspar") as handle:
        m = motifs.read(handle, "jaspar")
        print(m.consensus)