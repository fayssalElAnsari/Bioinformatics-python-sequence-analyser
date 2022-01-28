from Bio import SeqIO

# 1.lecture des sequence a partir des fichiers
fasta = SeqIO.read("data/NM_007389.fasta", "fasta")
genebank = SeqIO.read("data/NM_007389.gb", "genbank")


# 2.comparaison entre les 2 sequence lus
if (str(fasta.seq) == str(genebank.seq)): # True
    print("les 2 sequences sont identiques")

# 3.passage au complement inverse des sequences
fasta.reverse_complement(id = fasta.id + "_rc")
genebank.reverse_complement(id = genebank.id + "_rc")

# 4.
