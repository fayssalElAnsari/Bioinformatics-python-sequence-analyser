import unittest

class test_utils(unittest.TestCase):

    def test_find_cds(self):
        pass

    def test_compare_rec_seq(self):
        pass

    def mrna_to_gene(self):
        pass

    def upstream_gene_seq(self):
        pass

    def download_promotors(self):
        """
        dans ce test on essaye de telecharger les matrice
        a partir d'une liste de MRNA qui se trouve dans
        le fichier constantes.py : LIST_MRNA
        on doit verifier que la taille des sequences telecherges
        correspond bien a la taille passe en parametre de
        la fonction download_promotors
        """
        generated_files = download_promotors(LIST_MRNA, 1024, "../data")
        

if __name__ == "__main__":
    unittest.main()