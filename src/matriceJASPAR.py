#!/usr/bin/python
import urllib.request
import sys

def matriceJaspar(matrice):
    """Creer dans le fichier jaspar dans le repertoire "../data", la matrice passer en paramètre 
    matrice(str)
    """
    link = "https://jaspar.genereg.net/api/v1/matrix/"+matrice+".jaspar"
    req_url = urllib.request.urlopen(link)
    src=req_url.read()
    fichier=open("../data/"+matrice+".jaspar","wb")
    fichier.write(src)
    fichier.close()

def matricesJaspar(list_matrice):
    """Creer dans le fichier jaspar dans le repertoire "../data", la matrice passer en paramètre 
    list_matrice(list) : tous ses élément de type str
    """
    for e in list_matrice:
        matriceJaspar(e)

if __name__ == "__main__":
    #sur le shell
    # Exemple:
    # ~/bioinfo-tps-el_ansari-pastor_rojas/src$python3 matriceJASPAR.py MA0037.3 MA0001
    matricesJaspar(sys.argv[1:len(sys.argv)])