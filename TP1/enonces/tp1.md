TP1 - Appréhender des séquences biologiques
===========================================

Département informatique – Université de Lille

*   [Étudier une séquence ARN](#étudier-une-séquence-arn)
    *   [Filtrer les résultats](#filtrer-les-résultats)
    *   [Comprendre une entrée](#comprendre-une-entrée)
    *   [Formats de données](#formats-de-données)
    *   [Au-delà du transcrit](#au-delà-du-transcrit)
*   [Utiliser l’API](#utiliser-lapi)
*   [Sites de fixation des facteurs de transcription](#sites-de-fixation-des-facteurs-de-transcription)

Plusieurs banques de données internationales centralisent les séquences biologiques obtenues par des scientifiques autour du monde.

Nous allons ici nous concentrer sur le [NCBI](https://www.ncbi.nlm.nih.gov/) (National Center for Biology Information), le centre de bioinformatique des États-Unis d’Amérique. Ce centre pointe vers de nombreuses ressources : des séquences ADN ou ARN, des séquences protéiques, des articles scientifiques, des livres…

Ici nous allons aller sur [le site qui correspond aux séquences nucléotidiques](https://www.ncbi.nlm.nih.gov/nuccore) (ADN ou ARN).

Étudier une séquence ARN
------------------------

Dans le champ de recherche, entrez `CHRNA1`. CHRNA1, est [le nom d’un gène](https://en.wikipedia.org/wiki/CHRNA1) qui code une protéine réceptrice de l’acétylcholine (un neurotransmetteur).

Une fois la recherche validée, vous devez obtenir quelques milliers de résultats. Ce qui est beaucoup. Nous allons les filtrer pour obtenir ce qui nous intéresse.

### Filtrer les résultats

1.  Parmi les organismes disponibles, sélectionner la souris (_Mus musculus_), sur la droite de la page, dans _Top organisms_, cliquez sur _More…_ pour voir plus d’organismes (s'il n'apparaît pas cliquez sur *All other taxa*). Constatez que cela modifie votre champ de recherche pour y ajouter cette contrainte.

2.  Nous voulons nous intéresser ici à un ARN messager (ARNm, ou _mRNA_ en anglais) du gène CHRNA1. Ne conservez que les ARNm en choisissant l’entrée correspondante (à gauche de la page).

3.  Enfin, ne conservez que les résultats provenant de RefSeq (à gauche de la page), qui ne contient que des données vérifiées sans doublon.


Il ne reste plus qu’un seul résultat, c’est celui qui nous intéresse.***[Ici](https://www.ncbi.nlm.nih.gov/nuccore/NM_007389.5)***

Nous n’arrivons pas toujours à un seul résultat avec cette démarche, il peut par exemple y avoir plusieurs ARNm pour un même gène, ou alors le nom du gène peut être présent sans que la molécule vienne de ce gène, dans ce cas il aurait fallu raffiner la recherche en précisant que `CHRNA1` était le nom du gène, en notant `CHRNA1[gene name]`.

### Comprendre une entrée

Une entrée possède de nombreuses informations la décrivant mais également détaillant comment la séquence a été identifiée. Le format utilisé pour cette description est un format texte appelé _GenBank_ ([documentation](https://www.ncbi.nlm.nih.gov/genbank/samplerecord/)).

Sur la première ligne, commençant par `LOCUS` on a notamment l’identifiant de cet ARN messager (commençant par `NM_`) ***NM_007389***, sa taille en nucléotides ***4320***, le type de molécule ***mRNA***.

Un peu plus bas, la ligne commençant par `ORGANISM` confirme qu’il s’agit bien d’une séquence identifiée chez des souris. Ensuite de nombreuses lignes correspondent aux références des articles scientifiques ayant participé à la mise en évidence de cet ARN messager et de ses caractéristiques.

Descendez jusqu’à la ligne qui commence par `FEATURES`. Un certain nombre d’informations sont visibles. Identifiez :

1.  Le chromosome où le gène codant cet ARNm est présent ***/chromosome="2"***

2.  Un autre nom pour le gène CHRNA1 ***/gene_synonym="Achr-1; Acra; AI385656; AI608266"***

3.  L’identifiant numérique de ce gène ***/db_xref="GeneID:11435"***

4.  Le nombre d’exons ***sont 9 : (1..94; 95..240; 241..285; 286..395; 396..591; 592..829; 830..1053; 1054..1293; 1294..4320)**


Enfin la séquence ADN de l’ARNm est présente à la fin du fichier. La séquence est écrite sous forme de blocs de 10 nucléotides séparées par une espace, mais ce format n’est pas le plus simple pour la manipulation des séquences.

### Formats de données

Nous allons visualiser cette entrée sous un autre format. Revenez tout en haut de la page. Cliquez à l’endroit où se trouve un lien _GenBank_ (au dessus du nom de l’ARNm) et choisissez le format _Fasta (text)_.***[Ici](https://www.ncbi.nlm.nih.gov/nuccore/NM_007389.5?report=fasta)***

S’affiche alors la séquence de l’ARNm au format FASTA, un format texte simple dans lequel les lignes commençant par `>` décrivent la séquence écrite sur les lignes suivantes (les sauts de ligne dans la séquence n’ont pas de signification particulière). Ce format est très utilisé en bioinformatique pour travailler sur les séquences.

Revenez en arrière et sélectionnez un autre format, plus visuel : _Graphics_.***[Ici](https://www.ncbi.nlm.nih.gov/nuccore/NM_007389.5?report=graph&log$=seqview)***  
Est-ce que cela confirme bien le nombre d’exons précédemment identifié ? ***Oui***

À quelle position commence et se termine la séquence de la protéine (sur fond rouge, dont le nom commence par `NP_`) ?***52..1,425***   (elle va coder la proteine)
Pourquoi la protéine ne recouvre pas tout le gène ?
***Le gène debuté sa séquence et la termine en 1..4,320***  


### Au-delà du transcrit

Pour que ce gène soit exprimé, ce qui nous intéresse c’est le promoteur du gène qui est en amont de celui-ci. Or pour identifier cette région amont, il faut s’intéresser à la position de ce gène sur le chromosome sur lequel il se trouve.

Dans l’entrée GenBank nous avons identifié le chromosome sur lequel ce gène se trouve. Pour autant nous ne connaissons pas sa position sur le chromosome.

Pour cela nous allons utiliser les liens que fait le NCBI entre ces différentes banques de données. Nous sommes actuellement sur la banque de données nucléotides, sur une entrée d’un ARNm, et nous allons nous rendre sur l’entrée qui correspond à ce gène dans la banque _Gene_.

Pour cela cliquer sur _Gene_ dans _Related information_ dans le bandeau de droite.***https://www.ncbi.nlm.nih.gov/gene?LinkName=nuccore_gene&from_uid=425905338***

Sur cette page, trouvez l’identifiant du gène, qui doit être le même que celui relevé précédemment dans les informations de l’entrée GenBank.

Ensuite vous trouverez le nom du chromosome, son numéro d’accession (commençant par `NC_`) et les positions sur celui-ci. ***NC_000068.8 (73393625..73410682, complement)***

Si nous voulons étudier les positions en amont du gène, quelles positions devons-nous étudier ? (attention au brin sur lequel le gène se trouve) ***73393625..73410682***

Trouvez comment extraire la région se situant 1000 bases en amont du début du mRNA (la séquence promotrice). La sauvegarder au format Fasta.***[Ici](https://www.ncbi.nlm.nih.gov/nuccore/NC_000068.8?report=fasta&from=73393625&to=73410682&strand=true)***

Utiliser l’API
--------------

Nous avons fait tout cela manuellement, mais il est nécessaire d’automatiser cela afin de pouvoir traiter les données automatiquement.

Pour cela le NCBI offre [une API](https://www.ncbi.nlm.nih.gov/books/NBK25501/).

Cette API peut être utilisée en accédant directement à certaines URL ou, via des packages dans certains langages de programmation.

*   [esearch](https://www.ncbi.nlm.nih.gov/books/NBK25500/#chapter1.Searching_a_Database) : permet de chercher certains termes dans une base de données (p. ex. https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch/esearch.fcgi?db=MY\_DB&term=MY\_TERM)

*   [efetch](https://www.ncbi.nlm.nih.gov/books/NBK25500/#chapter1.Downloading_Full_Records) : permet de récupérer une entrée précise dans une base de données (p. ex. https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch/efectch.fcgi?db=MY\_DB&id=MY\_ACCESSION&rettype=MY\_TYPE&retmode=text)

*   [elink](https://www.ncbi.nlm.nih.gov/books/NBK25500/#chapter1.Finding_Related_Data_Through_En) : fait un lien entre une entrée dans une base de données et l’entrée correspondante dans une autre base de données (p.ex. https://eutils.ncbi.nlm.nih.gov/entrez/eutils/elink/elink.fcgi?dbfrom=MY\_DB\_FROM&db=MY\_DB&id=MY\_ACCESSION)


Renouvelez ce que nous avons fait précédemment mais en utilisant cette API :

Effectuez la recherche avec `esearch` (sans les filtres), sur la base de données `nucleotide` (attention à bien remplacer `MY_DB` et `MY_TERM` dans l’URL donnée en exemple).

Quel est le format obtenu ? Combien de résultats y a-t-il au total (pas seulement ceux affichés) ?  
```

```

Afin d’appliquer les mêmes filtres que précédemment il faudra indiquer comme terme de recherche `Chrna1 AND biomol_mrna[PROP] AND refseq[filter] AND "Mus musculus"[Organism]`. Quel est l’identifiant du résultat obtenu ?

Utilisez maintenant `efetch` pour récupérer l’entrée correspondante dans cette banque de données. Récupérez l’entrée au format GenBank (`gb`) puis FASTA (`fasta`) (ce qui remplace `MY_TYPE`, qui est le type de format de données).

Réessayez en remplaçant l’identifiant par le numéro d’accession de la molécule (commençant par `NM_`). Obtenez-vous la même chose ?  
```

```

Enfin utilisez `elink` afin de passer de la banque de données `nucleotide` à la banque de données `gene`, comme précédemment sur le site web. Cela nous permettra de connaître l’identifiant du gène.

Avec `efetch` récupérez les informations, au format GenBank, pour ce gène-là (banque de données `gene`). Cela nous (re)donne le numéro d’accession du chromosome et les positions du gène sur le chromosome.

Utilisez à nouveau `efetch` pour récupérer la séquence en amont de ce gène (pour préciser les positions, il faut utiliser `seq_start` et `seq_stop`, `seq_start` étant supérieur à `seq_stop` lorsqu’on est sur le brin anti-sens).

Sites de fixation des facteurs de transcription
-----------------------------------------------

Comme expliqué en cours, pour que la transcription s’initie il faut que des protéines, les facteurs de transcription, viennent “s’accrocher” en amont du gène, dans la partie promotrice.

Ces protéines reconnaissent des sites spécifiques : les sites de fixation de facteurs de transcription (en anglais _Transcription Factor Binding Sites_, TFBS). Les motifs de TFBS sont modélisés par des matrices de comptage ou de fréquence. À partir de données récoltées pour un site de fixation (un certain nombre de séquences ADN pour lesquelles on sait qu’elles correspondent à ce site) on a établi un décompte du nombre de lettres à chaque position du site. Une telle modélisation est plus expressive qu’une simple expression régulière qui ne permet pas d’associer une probabilité d’occurrences lorsqu’il y a plusieurs possibilités pour une position. Ces matrices sont nommées PFM (_Position Frequency Matrix_), PWM (_Position Weight Matrix_) ou PSSM (_Position Specific Scoring Matrix_) suivant la donnée qu’elles contiennent. Nous reviendrons sur cette modélisation la semaine prochaine.

Il existe deux ressources principales regroupant des TFBS modélisés par des matrices : [Transfac](https://genexplain.com/transfac/) et [Jaspar](http://jaspar.genereg.net/). Nous utiliserons Jaspar car l’accès à Transfac est payant.

Suivez le ‘_Jaspar Interactive Tour_’ proposé sur la page d’accueil et répondez aux questions suivantes (nous ne traiterons pas l’étape 10 sur les TFFMs) :

*   combien de matrices modélisent le site de fixation `GATA3` ?  
```

```
*   quelles sont les longueurs des sites `GATA` d’après le modèle ?  
```

```
*   d’après-vous, pourquoi ce site est nommé GATA ?  
```

```
*   sur combien de séquences la matrice `MA0037.2` a-t-elle été construite ?  
```

```
*   d’après-vous, que signifie la hauteur des lettres du schéma coloré affiché ?  
```

```  

Recherchez les matrices modélisant le site `HNF4A`. Choisissez la version qui vous semble la plus appropriée : en correspondance avec l’organisme choisi.

Grâce à la fonction _Scan_ proposée sur le site et à la séquence promotrice récupérée précédemment, trouvez des occurrences de **HNF4** dans le promoteur de `Chrna1` (utilisez la séquence que vous avez téléchargée précédemment).

Terminez cette partie en téléchargeant l’ensemble des matrices PFM pour les vertébrés contenue dans CORE JASPAR (voir le menu Download).
