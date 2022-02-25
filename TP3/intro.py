from Bio import motifs
# 1. Combien de matrices ont été lues ?
def nombre_matrice_lu(motifs_read):
    print(len(set(str(m.consensus))))

with open("data/MA0037.2.jaspar") as handle:
        m = motifs.read(handle, "jaspar")
#         print(m.consensus)
        nombre_matrice_lu(m)
        
        