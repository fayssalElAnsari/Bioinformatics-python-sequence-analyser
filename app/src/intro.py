from Bio import motifs

# Calcul de score à partir de matrices de fréquences
    # 1. Combien de matrices ont été lues ? => 1
with open("data/MA0037.2.jaspar") as handle:
        m = motifs.read(handle, "jaspar")
#         print(m.consensus)
        print(m) # on a 1 matrice
    # 2. De quelle manière allez-vous pouvoir obtenir une matrice poids-position (position-weight matrix, 
        print("PWM sans poids")
        print(m.counts.normalize())
            #  Quelle valeur mettez-vous pour les pseudo-poids (pseudocounts) ? => 0.01
        print("PWM avec poids de 0.01")
        print(m.counts.normalize(0.01))
    # 3. Comment obtenir une PSSM à partir de cette PWM ?
        print("PSSM de PWM avec poids de 0.01")
        pssm=m.counts.normalize(0.01).log_odds()
        print(pssm)
    # 4. Comment rechercher les occurrences d’une PSSM dans une séquence ?
        #voir pwm.py