## Comprendre une entrée
1. Le chromosome où le gène codant cet ARNm est présent: `2` ( a partir de la ligne: `/chromosome="2"`)
2. Un autre nom pour le gène CHRNA1: `Achr-1; Acra; AI385656; AI608266` ( a partir de la ligne: `/gene_synonym="Achr-1; Acra; AI385656; AI608266"`)
3. L’identifiant numérique de ce gène: `GeneID:11435` ( a partir de la ligne: `/db_xref="GeneID:11435"`)
4. Le nombre d’exons: `9`

## Formats de données
* Graphics. Est-ce que cela confirme bien le nombre d’exons précédemment identifié ?
  * Dans le format `Graphics` on peut voir: 9 exons donc `oui`
* À quelle position commence et se termine la séquence de la protéine (sur fond rouge, dont le nom commence par NP_) ? Pourquoi la protéine ne recouvre pas tout le gène ?
  * ca commence par `1` et se termine par `1374`
  * le proteine ne couvre pas tout le gene par ce que 

## Au-delà du transcrit
*   Maintenant on passe au Banque `Gene` 
    *   on peut voir le meme ID que pour celui dans la banque des nucleotides: `11435` en haut de la page.
    *   nom du chromosome: `Chromosome 2`
    *   numero d'assecion:   `NC_000068.8`
    *   les positions sur celui ci: 

*   Si nous voulons étudier les positions en amont du gène, quelles positions devons-nous étudier ? (attention au brin sur lequel le gène se trouve)
    *   ..
  
*   Trouvez comment extraire la région se situant 1000 bases en amont du début du mRNA (la séquence promotrice). La sauvegarder au format Fasta.
    *   ...
    *   sous format `FASTA`:
```FASTA

```


# Utiliser l’API
*   `esearch` : permet de chercher certains termes dans une base de données (p. ex. https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch/esearch.fcgi?db=MY_DB&term=MY_TERM)
    *   on essaye d'executer par exemple:  `https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch/esearch.fcgi?db=gene&term=CHRNA1[gene name] Mus musculus[organism]`

*   `efetch` : permet de récupérer une entrée précise dans une base de données (p. ex. https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch/efectch.fcgi?db=MY_DB&id=MY_ACCESSION&rettype=MY_TYPE&retmode=text)
    *   par exemple:    `https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch/efectch.fcgi?db=gene&id=11435&rettype=MY_TYPE&retmode=text`
  
*   `elink` : fait un lien entre une entrée dans une base de données et l’entrée correspondante dans une autre base de données (p.ex. https://eutils.ncbi.nlm.nih.gov/entrez/eutils/elink/elink.fcgi?dbfrom=MY_DB_FROM&db=MY_DB&id=MY_ACCESSION)
    *   par exemple:    `https://eutils.ncbi.nlm.nih.gov/entrez/eutils/elink/elink.fcgi?dbfrom=nucleotide&db=gene&id=11435`
  
* Maintenant on refait ce qu'on a fait dans la premiere partie mais on utilisant l'API:
1.  Effectuez la recherche avec esearch (sans les filtres), sur la base de données nucleotide
    *   