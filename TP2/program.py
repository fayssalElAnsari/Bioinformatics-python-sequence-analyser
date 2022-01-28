from Bio import SeqIO
from src.utils import *
from Bio import Entrez

# 1.lecture des sequence a partir des fichiers
fasta = SeqIO.read("data/NM_007389.fasta", "fasta")
genebank = SeqIO.read("data/NM_007389.gb", "genbank")

# 2.comparaison entre les 2 sequence lus
if (str(fasta.seq) == str(genebank.seq)): # True
    print("2. les 2 sequences sont identiques")

# 3.passage au complement inverse des sequences
fasta.reverse_complement(id = fasta.id + "_rc")
genebank.reverse_complement(id = genebank.id + "_rc")

# 4.
print("4.a la longeur du format fasta est: " + str(len(fasta.features)))
print("    la longeur du format genebank est: " + str(len(genebank.features)))
# le format fasta n'a pas de features (la longeur de sa liste features est 0)
print("4.b les features du format genebank sont: ")
for feature in genebank.features:
    print("  " +feature.type)

# 5. position de debut et de fin de la premiere feature
print("debut: " + str(genebank.features[0].location.start))
print("fin: " + str(genebank.features[0].location.end))

# 6. utilisation fn find_cds de utils.py
print(find_cds(genebank))


################################
## API du NCBI avec Biopython ##
################################
## efetch
# 1. Entrez
Entrez.email = "fayssal.el.ansari@gmail.com" # why ? XD
gb_handle = Entrez.efetch(db="nucleotide", id="NM_007389", rettype="gb", retmode="text")
fasta_handle = Entrez.efetch(db="nucleotide", id="NM_007389", rettype="fasta", retmode="text")

# 2. comparaison sequences
gb_record = SeqIO.read(gb_handle, "gb")
fasta_record = SeqIO.read(fasta_handle, "fasta")

compare_rec_seq(gb_record, fasta_record)

# 3. comparaison CDS
print(find_cds(gb_record)) # donc c'est le meme posittion des CDS

## elink


