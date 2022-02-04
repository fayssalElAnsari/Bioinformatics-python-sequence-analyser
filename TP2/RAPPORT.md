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

1.  - [ ] Utilisez la méthode `efetch` pour récupérer l’entrée `NM_007389` au format Genbank puis au format FASTA. Cette méthode retourne un _handle_ qui peut ensuite être passé à la méthode `SeqIO.read` (à la place du nom de fichier).
2.  - [ ] Vérifiez que les séquences des entrées obtenues sont bien identiques
3.  - [ ] En utilisant votre méthode `find_cds` sur le résultat au format Genbank, vérifiez que la CDS est bien identique à celle identifiée dans la première partie, avec le fichier Genbank.

#### elink

Comme la semaine dernière, nous allons utilisez `elink` pour connaître l’identifiant du gène correspondant à l’ARNm qu’on étudie. Cette fois nous utiliserons la méthode `elink` du module `Entrez`.

1.  - [ ] Utilisez la méthode `elink` pour récupérer le gène correspondant à l’entrée `NM_007389`. Ici le résultat n’est pas exploitable par `SeqIO.read`. Regardez dans la documentation de la méthode `elink` pour savoir comment obtenir un objet exploitable à partir du résultat de la méthode `elink`.
2.  - [ ] Dans le résultat obtenu, identifiez comment trouver l’identifiant du gène.
3.  - [ ] Dans le fichier `utils.py` réalisez une méthode `mrna_to_gene` qui prenne un numéro d’accession d’un ARNm et qui renvoie l’identifiant du gène correspondant (ou qui lève une exception `ValueError` en cas de problème).

#### Récupération de la portion amont d’un gène

1.  - [ ] À partir de l’identifiant du gène obtenu, utilisez la méthode `esummary` ([documentation](https://biopython.org/docs/1.75/api/Bio.Entrez.html#Bio.Entrez.esummary)) pour pouvoir déterminer le numéro d’accession du chromosome (commençant par `NC_`) et les positions chromosomiques du gène.
2.  - [ ] À partir de l’identifiant de ce chromosome, déterminez comment obtenir la séquence en amont du gène. **Attention** ne téléchargez pas tout le chromosome, mais uniquement la portion d’intérêt (comme la semaine dernière en utilisant `seq_start` et `seq_stop`).
3.  - [ ] Dans le fichier `utils.py` réalisez une fonction `upstream_gene_seq` qui, à partir d’un identifiant de gène et d’une longueur retourne un objet Biopython `Bio.Seq` correspondant à la séquence ADN amont de ce gène de la longueur demandée (attention au brin sur lequel se trouve le gène).

- [ ] Pour vérifier le bon fonctionnement de votre fonction, recherchez la séquence obtenue sur le site Ensembl, [avec l’outil Blat](http://www.ensembl.org/Multi/Tools/Blast?db=core) (pensez à sélectionner le bon organisme).


Calcul de score à partir de matrices de fréquences
--------------------------------------------------

Nous allons maintenant utiliser Biopython pour trouver les endroits correspondant à des sites de fixation du facteur de transcription.

Nous allons travailler à partir du fichier que vous avez [téléchargé la semaine dernière sur JASPAR](TP1.html#sites-de-fixation-des-facteurs-de-transcription), à mettre dans votre répertoire `data/`. Le module `motifs` de Biopython est celui qui nous intéressera pour rechercher les occurrences de PSSM. Chargez-le.

Le chargement de ce type fichier (matrices de fréquences) se fait avec la méthode `read` du module `motifs` ([documentation](https://biopython.org/docs/1.75/api/Bio.motifs.html#Bio.motifs.read)), en lui précisant que le format est `jaspar`.

1.  - [ ] Combien de matrices ont été lues ?

Pour chaque entrée, la matrice est accessible via l’attribut `counts`, de type `FrequencyPositionMatrix` ([documentation](https://biopython.org/docs/1.75/api/Bio.motifs.matrix.html?highlight=frequencypositionmatrix#Bio.motifs.matrix.FrequencyPositionMatrix)).

2.  - [ ] De quelle manière allez-vous pouvoir obtenir une matrice poids-position (_position-weight matrix_, PWM) ? Quelle valeur mettez-vous pour les pseudo-poids (_pseudocounts_) ? (souvenez-vous du cours…)

Le résultat que vous obtenez doit dont être une PWM, de type `PositionWeightMatrix` ([documentation](https://biopython.org/docs/1.75/api/Bio.motifs.matrix.html?highlight=frequencypositionmatrix#Bio.motifs.matrix.PositionWeightMatrix)).

3.  - [ ] Comment obtenir une PSSM à partir de cette PWM ?

La PSSM obtenue est de type `PositionSpecificScoringMatrix` ([documentation](https://biopython.org/docs/1.75/api/Bio.motifs.matrix.html?highlight=frequencypositionmatrix#Bio.motifs.matrix.PositionSpecificScoringMatrix)).

4.  - [ ] Réalisez une fonction qui, à partir d’une matrice de fréquence et de pseudo-poids, renvoie la PSSM correspondante.

5.  - [ ] Comment rechercher les occurrences d’une PSSM dans une séquence ?
