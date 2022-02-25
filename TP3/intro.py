from Bio import motifs

# Calcul de score à partir de matrices de fréquences
    # 1. Combien de matrices ont été lues ? => 1
with open("data/MA0037.2.jaspar") as handle:
        m = motifs.read(handle, "jaspar")
        print(m.consensus)
        print(m)
    # 2. De quelle manière allez-vous pouvoir obtenir une matrice poids-position (position-weight matrix, 
        print(m.counts.normalize())
            #  Quelle valeur mettez-vous pour les pseudo-poids (pseudocounts) ?
        