TP3 - Recherche d’occurrences de matrices PFM
=============================================

Département informatique – Université de Lille

*   [Rendu intermédiaire](#rendu-intermédiaire)
*   [Calcul de score à partir de matrices de fréquences (repris du TP2)](#calcul-de-score-à-partir-de-matrices-de-fréquences-repris-du-tp2)
*   [Mise en place de fonctions utiles pour manipuler les PWM](#mise-en-place-de-fonctions-utiles-pour-manipuler-les-pwm)
*   [Script pour le rendu intermédiaire](#script-pour-le-rendu-intermédiaire)
*   [Recherche pour un ensemble de séquences](#recherche-pour-un-ensemble-de-séquences)
*   [Le module de gestion des arguments `argparse` de Python](#le-module-de-gestion-des-arguments-argparse-de-python)

L’objectif de ce TP est :

*   de faire ou finaliser la partie du TP2 pour la recherche d’occurrences d’une PFM
*   recherche des occurrences et stockage d’une PWM pour une séquence
*   rendu intermédiaire
*   calcul de score d’une fenêtre glissante

Rendu intermédiaire
-------------------

À la fin de la séance (i.e. avant 17h00), vous devez avoir réalisé un script python, qui s’exécute en ligne de commande, prend en argument :

*   un fichier contenant une matrice JASPAR ;
*   un identifiant Genbank d’un mRNA ;
*   une taille pour la séquence promotrice ;
*   un seuil de score.

et produit sur la sortie standard une liste d’occurrences dont le score est supérieur au seuil. Typiquement :

    Ahr::Arnt 71 6.198700428009033
    Ahr::Arnt -745 5.744134426116943
    Ahr::Arnt 444 6.198700428009033
    Ahr::Arnt 446 6.198700428009033
    Ahr::Arnt -388 10.591017723083496
    Ahr::Arnt 920 6.198700428009033

(voir la section dédiée plus bas)

Calcul de score à partir de matrices de fréquences (repris du TP2)
------------------------------------------------------------------

Nous allons maintenant utiliser Biopython pour trouver les endroits correspondant à des sites de fixation du facteur de transcription.

Nous allons travailler à partir du fichier que vous avez [téléchargé la semaine dernière sur JASPAR](https://www.fil.univ-lille.fr/~salson/portail/bioinfo-s6/TP1.html#sites-de-fixation-des-facteurs-de-transcription), à mettre dans votre répertoire `data/`. Le module `motifs` de Biopython est celui qui nous intéressera pour rechercher les occurrences de PSSM. Chargez-le.

Le chargement de ce type fichier (matrices de fréquences) se fait avec la méthode `read` du module `motifs` ([documentation](https://biopython.org/docs/1.75/api/Bio.motifs.html#Bio.motifs.read)), en lui précisant que le format est `jaspar`.

- [x] 1.  Combien de matrices ont été lues ? ***=> On a lu 1 matrices***

Pour chaque entrée, la matrice est accessible via l’attribut `counts`, de type `FrequencyPositionMatrix` ([documentation](https://biopython.org/docs/1.75/api/Bio.motifs.matrix.html?highlight=frequencypositionmatrix#Bio.motifs.matrix.FrequencyPositionMatrix)).

- [x] 2.  De quelle manière allez-vous pouvoir obtenir une matrice poids-position (_position-weight matrix_, PWM) ? Quelle valeur mettez-vous pour les pseudo-poids (_pseudocounts_) ? (souvenez-vous du cours…) ***=> 0.01***

Le résultat que vous obtenez doit dont être une PWM, de type `PositionWeightMatrix` ([documentation](https://biopython.org/docs/1.75/api/Bio.motifs.matrix.html?highlight=frequencypositionmatrix#Bio.motifs.matrix.PositionWeightMatrix)).

- [x] 3.  Comment obtenir une PSSM à partir de cette PWM ?

La PSSM obtenue est de type `PositionSpecificScoringMatrix` ([documentation](https://biopython.org/docs/1.75/api/Bio.motifs.matrix.html?highlight=frequencypositionmatrix#Bio.motifs.matrix.PositionSpecificScoringMatrix)).

- [x] 4.  Comment rechercher les occurrences d’une PSSM dans une séquence ?

Mise en place de fonctions utiles pour manipuler les PWM
--------------------------------------------------------

Toutes les fonctions seront positionnées dans un fichier `pwm.py`.

- [x] 1.  Réalisez une fonction `pwm2pssm` qui, à partir d’une matrice de fréquence JASPAR (un objet `FrequencyPositionMatrix`) et d’un pseudo-poids passés en paramètre, retourne la PSSM correspondante (un objet `PositionSpecificScoringMatrix`).

- [x] 2.  Réalisez une fonction `scan_sequence` qui, à partir d’une PSSM (un objet `PositionSpecificScoringMatrix`), d’une séquence (un objet Biopython `Bio.Seq`), et d’un seuil de score passés en paramètre, retourne une liste de couples position, score d’occurrence.


Script pour le rendu intermédiaire
----------------------------------

Il est temps maintenant de consolider ce qui a été fait la semaine dernière et cette semaine.

- [x] 1.  Réalisez le script `scan_pwm.py` pour le rendu intermédiaire (le pseudo-poids sera figé à la valeur 0.1). Bien sûr ce script importera les modules `pwm.py` et `utils.py`.

- [x] 2.  Pour tester votre script vous pourrez faire des recherches les matrices `MA0083, MA0114, MA0056` sur `NM_007389` avec un seuil de score positionné à -2.0.
  ```shell
  ~/TP3$ python scan_pwm.py MA0083.jaspar NM_007389 6 -2
  ```
- [x] 3.  Que signifie une position d’occurrence négative ? ***Cela signifie que la séquence est plus loin de la distance moyenne moyenne***

- [ ] 4.  En lien avec la question précédente, posez-vous la question de l’endroit où se trouve, vis-à-vis du début du gène, la position d’occurrence d’une matrice fournie par votre script.















TP2 - Manipulation de séquences biologiques avec Python
=======================================================

Département informatique – Université de Lille

*   [Utilisation de Biopython](#utilisation-de-biopython)
    *   [Lecture de fichiers](#lecture-de-fichiers)
    *   [API du NCBI avec Biopython](#api-du-ncbi-avec-biopython)
        *   [efetch](#efetch)
        *   [elink](#elink)
        *   [Récupération de la portion amont d’un gène](#récupération-de-la-portion-amont-dun-gène)
*   [Calcul de score à partir de matrices de fréquences](#calcul-de-score-à-partir-de-matrices-de-fréquences)

L’objectif de ce TP est :

*   d’automatiser avec Python ce qui a été fait la semaine dernière
*   d’avoir du code permettant de récupérer les séquences en amont d’un gène
*   de commencer à effectuer le calcul de score pour une PWM

Utilisation de Biopython
------------------------

Biopython est module Python qui offre des facilités pour faire des analyses bioinformatiques. Ici nous n’allons utiliser qu’une partie de Biopython :

*   la lecture dans un fichier au format FASTA ou Genbank
*   la représentation des séquences
*   l’utilisation de l’API du NCBI

La [documentation de Biopython](https://biopython.org/docs/1.75/api/Bio.html) ainsi que le [tutorial and cookbook](http://biopython.org/DIST/docs/tutorial/Tutorial.html) pourront vous aider dans ce TP et la suite du travail à effectuer.

### Lecture de fichiers

- [x] Pour commencer, récupérez [depuis la banque _Nucleotide_ du NCBI](https://www.ncbi.nlm.nih.gov/nuccore) l’enregistrement aux formats FASTA et Genbank correspondant à la séquence ARN étudiée la semaine dernière, dont le numéro d’accession est `NM_007389`.

- [x] Enregistrez ces fichiers FASTA et Genbank dans un répertoire `data/` sur votre dépôt.

- [x] Vous allez commencer par faire des essais dans un intepréteur Python afin de manipuler ces fichiers. La lecture et l’écriture de fichier se fait avec le module `SeqIO` de Biopython. Chargez ce module, puis chargez le fichier FASTA et le fichier Genbank, chacun dans une variable différente (`fasta` et `genbank`) grâce à la méthode `SeqIO.read` ([voir sa documentation](https://biopython.org/docs/1.75/api/Bio.SeqIO.html#Bio.SeqIO.read)).

Le type renvoyé par `SeqIO.read` est un `SeqRecord` ([documentation](https://biopython.org/docs/1.75/api/Bio.SeqRecord.html)).    
- [x] Déterminez comment obtenir les résultats suivants et mettez vos réponses dans un fichier `TP2.md` à la racine de votre dépôt.

1.  - [x] En consultant la documentation, identifiez comment récupérez la séquence depuis ces entrées.
2.  - [x] Comment obtenir la séquence sous forme d’une `string` Python (de type `str`) ? Vérifiez que les séquences sont bien identiques entre l’entrée Genbank et l’entrée FASTA.
3.  - [x] Comment obtenir la séquence complémentaire inverse (_reverse complement_ en anglais) ?
4.  - [x] Des attributs existent pour récupérer les annotations ou les _features_ des entrées. Quels sont ces attributs ? Existent-ils aussi bien pour l’entrée FASTA que pour l’entrée Genbank ? Pourquoi ?
5.  - [x] Intéressez-vous à la première _feature_. Comment peut-on accéder à ses positions de début et de fin ?

- [x] Vous allez maintenant réaliser certaines fonctions, qui s’appuient sur votre compréhension des `SeqRecord` qui pourront vous être utiles pour la suite.

- [x] Créez un répertoire `src/` à la racine de votre dépôt et dans un fichier `utils.py` ajoutez la fonction suivante :
  * [x] `find_cds`, qui prend en paramètre un `SeqRecord` et qui renvoie une liste des couples de positions de début et de fin des CDS contenues dans cette séquence (pour récupérer les positions de début et fin, [voir la documentation de `FeatureLocation`](https://biopython.org/docs/1.75/api/Bio.SeqFeature.html#Bio.SeqFeature.FeatureLocation)). La liste sera vide si le `SeqRecord` n’a pas de CDS.

Nous nous sommes ici intéressés à la méthode `SeqIO.read` qui lit **une** entrée. Si le fichier contient plusieurs entrées, il faudra utiliser la méthode `SeqIO.parse` qui permet d’itérer sur tous les `SeqRecord` contenus dans le fichier.

### API du NCBI avec Biopython

La [semaine dernière vous avez utilisé l’API du NCBI](TP1.html#utiliser-lapi). Plus précisément vous avez eu recours à `esearch`, `efetch` et `elink` en accédant directement à certaines URL. Nous allons faire la même chose, mais en utilisant le module Biopython, ce qui permet de récupérer des résultats sous forme d’objets Biopython qui peuvent être aisément manipulés.

Dans Biopython, c’est le module `Entrez`, que vous devrez importer qui permet d’interroger l’API du NCBI ([documentation](https://biopython.org/docs/1.75/api/Bio.Entrez.html)). Un préalable est de renseigner votre adresse email afin de pouvoir utiliser l’API :

    Entrez.email = "email@example.org"

Comme vous pouvez le voir dans la documentation, le module `Entrez` possède des méthodes `esearch`, `efetch`, `elink`

#### efetch

1.  - [x] Utilisez la méthode `efetch` pour récupérer l’entrée `NM_007389` au format Genbank puis au format FASTA. Cette méthode retourne un _handle_ qui peut ensuite être passé à la méthode `SeqIO.read` (à la place du nom de fichier).
2.  - [x] Vérifiez que les séquences des entrées obtenues sont bien identiques
3.  - [x] En utilisant votre méthode `find_cds` sur le résultat au format Genbank, vérifiez que la CDS est bien identique à celle identifiée dans la première partie, avec le fichier Genbank.

#### elink

Comme la semaine dernière, nous allons utilisez `elink` pour connaître l’identifiant du gène correspondant à l’ARNm qu’on étudie. Cette fois nous utiliserons la méthode `elink` du module `Entrez`.

1.  - [x] Utilisez la méthode `elink` pour récupérer le gène correspondant à l’entrée `NM_007389`. Ici le résultat n’est pas exploitable par `SeqIO.read`. Regardez dans la documentation de la méthode `elink` pour savoir comment obtenir un objet exploitable à partir du résultat de la méthode `elink`.
2.  - [x] Dans le résultat obtenu, identifiez comment trouver l’identifiant du gène.
3.  - [x] Dans le fichier `utils.py` réalisez une méthode `mrna_to_gene` qui prenne un numéro d’accession d’un ARNm et qui renvoie l’identifiant du gène correspondant (ou qui lève une exception `ValueError` en cas de problème).

#### Récupération de la portion amont d’un gène

1.  - [x] À partir de l’identifiant du gène obtenu, utilisez la méthode `esummary` ([documentation](https://biopython.org/docs/1.75/api/Bio.Entrez.html#Bio.Entrez.esummary)) pour pouvoir déterminer le numéro d’accession du chromosome (commençant par `NC_`) et les positions chromosomiques du gène.
2.  - [x] À partir de l’identifiant de ce chromosome, déterminez comment obtenir la séquence en amont du gène. **Attention** ne téléchargez pas tout le chromosome, mais uniquement la portion d’intérêt (comme la semaine dernière en utilisant `seq_start` et `seq_stop`).
3.  - [ ] Dans le fichier `utils.py` réalisez une fonction `upstream_gene_seq` qui, à partir d’un identifiant de gène et d’une longueur retourne un objet Biopython `Bio.Seq` correspondant à la séquence ADN amont de ce gène de la longueur demandée (attention au brin sur lequel se trouve le gène).

- [ ] Pour vérifier le bon fonctionnement de votre fonction, recherchez la séquence obtenue sur le site Ensembl, [avec l’outil Blat](http://www.ensembl.org/Multi/Tools/Blast?db=core) (pensez à sélectionner le bon organisme).


Calcul de score à partir de matrices de fréquences
--------------------------------------------------

Nous allons maintenant utiliser Biopython pour trouver les endroits correspondant à des sites de fixation du facteur de transcription.

- [ ] Nous allons travailler à partir du fichier que vous avez [téléchargé la semaine dernière sur JASPAR](TP1.html#sites-de-fixation-des-facteurs-de-transcription), à mettre dans votre répertoire `data/`.   
- [ ] Le module `motifs` de Biopython est celui qui nous intéressera pour rechercher les occurrences de PSSM. Chargez-le.

Le chargement de ce type fichier (matrices de fréquences) se fait avec la méthode `read` du module `motifs` ([documentation](https://biopython.org/docs/1.75/api/Bio.motifs.html#Bio.motifs.read)), en lui précisant que le format est `jaspar`.

1.  - [ ] Combien de matrices ont été lues ?

Pour chaque entrée, la matrice est accessible via l’attribut `counts`, de type `FrequencyPositionMatrix` ([documentation](https://biopython.org/docs/1.75/api/Bio.motifs.matrix.html?highlight=frequencypositionmatrix#Bio.motifs.matrix.FrequencyPositionMatrix)).

2.  - [ ] De quelle manière allez-vous pouvoir obtenir une matrice poids-position (_position-weight matrix_, PWM) ? Quelle valeur mettez-vous pour les pseudo-poids (_pseudocounts_) ? (souvenez-vous du cours…)

Le résultat que vous obtenez doit dont être une PWM, de type `PositionWeightMatrix` ([documentation](https://biopython.org/docs/1.75/api/Bio.motifs.matrix.html?highlight=frequencypositionmatrix#Bio.motifs.matrix.PositionWeightMatrix)).

3.  - [ ] Comment obtenir une PSSM à partir de cette PWM ?

La PSSM obtenue est de type `PositionSpecificScoringMatrix` ([documentation](https://biopython.org/docs/1.75/api/Bio.motifs.matrix.html?highlight=frequencypositionmatrix#Bio.motifs.matrix.PositionSpecificScoringMatrix)).

4.  - [ ] Réalisez une fonction qui, à partir d’une matrice de fréquence et de pseudo-poids, renvoie la PSSM correspondante.

5.  - [ ] Comment rechercher les occurrences d’une PSSM dans une séquence ?














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

1.  - [x] Parmi les organismes disponibles, sélectionner la souris (_Mus musculus_), sur la droite de la page, dans _Top organisms_, cliquez sur _More…_ pour voir plus d’organismes (s'il n'apparaît pas cliquez sur *All other taxa*). Constatez que cela modifie votre champ de recherche pour y ajouter cette contrainte.

2.  - [x] Nous voulons nous intéresser ici à un ARN messager (ARNm, ou _mRNA_ en anglais) du gène CHRNA1. Ne conservez que les ARNm en choisissant l’entrée correspondante (à gauche de la page).

3.  - [x] Enfin, ne conservez que les résultats provenant de RefSeq (à gauche de la page), qui ne contient que des données vérifiées sans doublon.


- [x] Il ne reste plus qu’un seul résultat, c’est celui qui nous intéresse. ***=> [Ici](https://www.ncbi.nlm.nih.gov/nuccore/NM_007389.5)***

Nous n’arrivons pas toujours à un seul résultat avec cette démarche, il peut par exemple y avoir plusieurs ARNm pour un même gène, ou alors le nom du gène peut être présent sans que la molécule vienne de ce gène, dans ce cas il aurait fallu raffiner la recherche en précisant que `CHRNA1` était le nom du gène, en notant `CHRNA1[gene name]`.

### Comprendre une entrée

Une entrée possède de nombreuses informations la décrivant mais également détaillant comment la séquence a été identifiée. Le format utilisé pour cette description est un format texte appelé _GenBank_ ([documentation](https://www.ncbi.nlm.nih.gov/genbank/samplerecord/)).

Sur la première ligne, commençant par `LOCUS` on a notamment:
  - [x] l’identifiant de cet ARN messager (commençant par `NM_`)  ***=> NM_007389***,
  - [x] sa taille en nucléotides  ***=> 4320***,
  - [x] le type de molécule ***=> mRNA***.

Un peu plus bas, la ligne commençant par `ORGANISM` confirme qu’il s’agit bien d’une séquence identifiée chez des souris. Ensuite de nombreuses lignes correspondent aux références des articles scientifiques ayant participé à la mise en évidence de cet ARN messager et de ses caractéristiques.

Descendez jusqu’à la ligne qui commence par `FEATURES`. Un certain nombre d’informations sont visibles. Identifiez :

1. -  [x] Le chromosome où le gène codant cet ARNm est présent  ***=>  /chromosome="2"***

2.  - [x] Un autre nom pour le gène CHRNA1  ***=> /gene_synonym="Achr-1; Acra; AI385656; AI608266"***

3.  - [x] L’identifiant numérique de ce gène  ***=>  /db_xref="GeneID:11435"***

4.  - [x] Le nombre d’exons ***=> 9: (1..94; 95..240; 241..285; 286..395; 396..591; 592..829; 830..1053; 1054..1293; 1294..4320)***


Enfin la séquence ADN de l’ARNm est présente à la fin du fichier. La séquence est écrite sous forme de blocs de 10 nucléotides séparées par une espace, mais ce format n’est pas le plus simple pour la manipulation des séquences.

### Formats de données

Nous allons visualiser cette entrée sous un autre format.   
- [x] Revenez tout en haut de la page.    
- [x] Cliquez à l’endroit où se trouve un lien _GenBank_ (au dessus du nom de l’ARNm) et choisissez le format _Fasta (text)_.  ***=> [Ici](https://www.ncbi.nlm.nih.gov/nuccore/NM_007389.5?report=fasta), et pour le télécharger [ici](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch/efectch.fcgi?db=nucleotide&id=425905338&rettype=fasta)***  
- [x] À quelle position commence et se termine la séquence de la protéine (sur fond rouge, dont le nom commence par `NP_`) ?  ***=> 52..1,425 (elle va coder la proteine)***   
- [x] Pourquoi la protéine ne recouvre pas tout le gène ? ***=> Le gène debuté sa séquence et la termine en 1..4,320 .***  


### Au-delà du transcrit

Pour que ce gène soit exprimé, ce qui nous intéresse c’est le promoteur du gène qui est en amont de celui-ci. Or pour identifier cette région amont, il faut s’intéresser à la position de ce gène sur le chromosome sur lequel il se trouve.

Dans l’entrée GenBank nous avons identifié le chromosome sur lequel ce gène se trouve. Pour autant nous ne connaissons pas sa position sur le chromosome.

- [x] Pour cela nous allons utiliser les liens que fait le NCBI entre ces différentes banques de données. Nous sommes actuellement sur la banque de données nucléotides, sur une entrée d’un ARNm, et nous allons nous rendre sur l’entrée qui correspond à ce gène dans la banque _Gene_.

- [x] Pour cela cliquer sur _Gene_ dans _Related information_ dans le bandeau de droite.  ***=> [Ici](https://www.ncbi.nlm.nih.gov/gene?LinkName=nuccore_gene&from_uid=425905338)***

- [x] Sur cette page, trouvez l’identifiant du gène, qui doit être le même que celui relevé précédemment dans les informations de l’entrée GenBank.

Ensuite vous trouverez:
  + - [x] le nom du chromosome  ***=> Chromosome 2***,
  + - [x] son numéro d’accession (commençant par `NC_`) ***=> NC_000068.8***,
  + - [x] et les positions sur celui-ci. ***=>  (73393625..73410682, complement)***

- [x] Si nous voulons étudier les positions en amont du gène, quelles positions devons-nous étudier ? (attention au brin sur lequel le gène se trouve) ***=>  à partir de la position 73410683***

- [x] Trouvez comment extraire la région se situant 1000 bases en amont du début du mRNA (la séquence promotrice). ***=>  (73410683...73411682)***
- [x] La sauvegarder au format Fasta.***=> [Ici](https://www.ncbi.nlm.nih.gov/nuccore/NC_000068.8?report=fasta&from=73393625&to=73410682&strand=true)***

Utiliser l’API
--------------

Nous avons fait tout cela manuellement, mais il est nécessaire d’automatiser cela afin de pouvoir traiter les données automatiquement.

Pour cela le NCBI offre [une API](https://www.ncbi.nlm.nih.gov/books/NBK25501/).

Cette API peut être utilisée en accédant directement à certaines URL ou, via des packages dans certains langages de programmation.

*   [esearch](https://www.ncbi.nlm.nih.gov/books/NBK25500/#chapter1.Searching_a_Database) : permet de chercher certains termes dans une base de données (p. ex. https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch/esearch.fcgi?db=MY\_DB&term=MY\_TERM)

*   [efetch](https://www.ncbi.nlm.nih.gov/books/NBK25500/#chapter1.Downloading_Full_Records) : permet de récupérer une entrée précise dans une base de données (p. ex. https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch/efectch.fcgi?db=MY\_DB&id=MY\_ACCESSION&rettype=MY\_TYPE&retmode=text)

*   [elink](https://www.ncbi.nlm.nih.gov/books/NBK25500/#chapter1.Finding_Related_Data_Through_En) : fait un lien entre une entrée dans une base de données et l’entrée correspondante dans une autre base de données (p.ex. https://eutils.ncbi.nlm.nih.gov/entrez/eutils/elink/elink.fcgi?dbfrom=MY\_DB\_FROM&db=MY\_DB&id=MY\_ACCESSION)


Renouvelez ce que nous avons fait précédemment mais en utilisant cette API :

- [x] Effectuez la recherche avec `esearch` (sans les filtres), sur la base de données `nucleotide` (attention à bien remplacer `MY_DB` et `MY_TERM` dans l’URL donnée en exemple). ***=>  En executant [esearch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch/esearch.fcgi?db=nucleotide&term=Chrna1)***

- [x] Quel est le format obtenu ?  ***=>  XML***  
- [x] Combien de résultats y a-t-il au total (pas seulement ceux affichés) ?  ***=> 2560***

- [x] Afin d’appliquer les mêmes filtres que précédemment il faudra indiquer comme terme de recherche `Chrna1 AND biomol_mrna[PROP] AND refseq[filter] AND "Mus musculus"[Organism]`. ***=> [Ici](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch/esearch.fcgi?db=nucleotide&term=Chrna1%20AND%20biomol_mrna[PROP]%20AND%20refseq[filter]%20AND%20%22Mus%20musculus%22[Organism])***  
- [x] Quel est l’identifiant du résultat obtenu ? ***=> 425905338***

Utilisez maintenant `efetch` pour récupérer l’entrée correspondante dans cette banque de données:
  - [x] Récupérez l’entrée au format GenBank (`gb`) ***=> [Ici pour gb](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch/efectch.fcgi?db=nucleotide&id=425905338&rettype=gb);***
  - [x] puis FASTA (`fasta`) (ce qui remplace `MY_TYPE`, qui est le type de format de données). ***=> [Ici pour fasta](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch/efectch.fcgi?db=nucleotide&id=425905338&rettype=fasta)***

Réessayez en remplaçant l’identifiant par le numéro d’accession de la molécule (commençant par `NM_`):
  - [x] Obtenez-vous la même chose ?  ***En executant: [AVEC NM_007389](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch/efectch.fcgi?db=nucleotide&id=NM_007389&rettype=fasta) on obtient la meme chose.***

Enfin utilisez `elink` afin de passer de la banque de données `nucleotide` à la banque de données `gene`, comme précédemment sur le site web:
  - [x] Cela nous permettra de connaître l’identifiant du gène. ***=> En executant [elink entre nucleotide et gene et NM_007389](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/elink/elink.fcgi?dbfrom=nucleotide&FROM&db=gene&id=NM_007389), nous obtiendrons:***
  ```xml
  <eLinkResult>
      <LinkSet>
      <DbFrom>nuccore</DbFrom>
          <IdList>
           <Id>425905338</Id>
          </IdList>
      <LinkSetDb>
              <DbTo>gene</DbTo>
              <LinkName>nuccore_gene</LinkName>
              <Link>
              <Id>11435</Id>
          </Link>
      </LinkSetDb>
      </LinkSet>
  </eLinkResult>
  ```
***donc le gene id est: `11435`***

Avec `efetch` récupérez les informations, au format GenBank, pour ce gène-là (banque de données `gene`).   
Cela nous (re)donne:
  - [x] le numéro d’accession du chromosome ***=> Annotation: Chromosome 2 NC_000068.8***
  - [x] et les positions du gène sur le chromosome. ***=> (73393625..73410682, complement)***

***=> Nous allons executer: `https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch/efectch.fcgi?db=gene&id=11435&rettype=gb&retmode=text***

- [x] Utilisez à nouveau `efetch` pour récupérer la séquence en amont de ce gène (pour préciser les positions, il faut utiliser `seq_start` et `seq_stop`, `seq_start` étant supérieur à `seq_stop` lorsqu’on est sur le brin anti-sens). ***=> En executant [efectch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch/efectch.fcgi?db=nucleotide&id=NC_000068.8&seq_start=73410682&seq_end=73393625&strand=2&rettype=gb&retmode=text)***

Sites de fixation des facteurs de transcription
-----------------------------------------------

Comme expliqué en cours, pour que la transcription s’initie il faut que des protéines, les facteurs de transcription, viennent “s’accrocher” en amont du gène, dans la partie promotrice.

Ces protéines reconnaissent des sites spécifiques : les sites de fixation de facteurs de transcription (en anglais _Transcription Factor Binding Sites_, TFBS). Les motifs de TFBS sont modélisés par des matrices de comptage ou de fréquence. À partir de données récoltées pour un site de fixation (un certain nombre de séquences ADN pour lesquelles on sait qu’elles correspondent à ce site) on a établi un décompte du nombre de lettres à chaque position du site. Une telle modélisation est plus expressive qu’une simple expression régulière qui ne permet pas d’associer une probabilité d’occurrences lorsqu’il y a plusieurs possibilités pour une position. Ces matrices sont nommées PFM (_Position Frequency Matrix_), PWM (_Position Weight Matrix_) ou PSSM (_Position Specific Scoring Matrix_) suivant la donnée qu’elles contiennent. Nous reviendrons sur cette modélisation la semaine prochaine.

Il existe deux ressources principales regroupant des TFBS modélisés par des matrices : [Transfac](https://genexplain.com/transfac/) et [Jaspar](http://jaspar.genereg.net/). Nous utiliserons Jaspar car l’accès à Transfac est payant.

Suivez le ‘_Jaspar Interactive Tour_ ’ proposé sur la page d’accueil et répondez aux questions suivantes (nous ne traiterons pas l’étape 10 sur les TFFMs) :

- [x] combien de matrices modélisent le site de fixation `GATA3` ?  ***=>  4***

- [x] quelles sont les longueurs des sites `GATA` d’après le modèle ?  ***=>  55***

- [ ] d’après-vous, pourquoi ce site est nommé GATA ?  ***=>  .***

- [x] sur combien de séquences la matrice `MA0037.2` a-t-elle été construite ?  ***=> AGATAA_GA_GAC***

- [ ] d’après-vous, que signifie la hauteur des lettres du schéma coloré affiché ?  ***=> .***

- [ ] Recherchez les matrices modélisant le site `HNF4A`. Choisissez la version qui vous semble la plus appropriée : en correspondance avec l’organisme choisi.

- [ ] Grâce à la fonction _Scan_ proposée sur le site et à la séquence promotrice récupérée précédemment, trouvez des occurrences de **HNF4** dans le promoteur de `Chrna1` (utilisez la séquence que vous avez téléchargée précédemment).

- [ ] Terminez cette partie en téléchargeant l’ensemble des matrices PFM pour les vertébrés contenue dans CORE JASPAR (voir le menu Download).
