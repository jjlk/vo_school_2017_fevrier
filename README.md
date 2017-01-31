# Tutoriel de haute énergie - STILTS

Pour télécharger les scripts et les catalogues, exécuter dans le répertoire de travail : 

```git clone  https://github.com/jjlk/vo_school_2017_fevrier```

## Objectifs
Se familiariser avec la manipulation des catalogues avec la librairie
[STILTS](http://www.star.bris.ac.uk/~mbt/stilts/). Celle-ci permet 
d'utiliser l'intégralité des fonctionalités de 
[TOPCAT](http://www.star.bris.ac.uk/~mbt/topcat/) à partir de scripts
(en bash ou en [Jython](http://www.jython.org/)).
La librairie STILTS devient indispensable lorsqu'un nombre important
de manipulations doivent être réalisées sur des catalogues.

## Installation de la librairie JyStilts
Les instructions sont indiquées [ici](http://www.star.bris.ac.uk/~mbt/stilts/#install).
Nous utiliserons le paquet qui contient STILTS et l'interpréteur Jython
([fichier](http://www.star.bris.ac.uk/~mbt/stilts/jystilts.jar)), qui correspond 
à la version de Python 2.5. 
Cette manière d'utiliser la librairie STILTS permet d'utiliser les fonctionalités
d'un language de programmation tel que Python (ici Jython, développé en java en lieu 
et place du C) comme les boucles, variables, fonctions, classes, etc.
On ne peut néanmoins pas utiliser tous les modules qui font la renommée
de Python (comme numpy, scipy, matplotlib, etc.).

On pourra vérifier le bon fonctionnement du paquet de la manière suivante : 
```
$ java -jar jystilts.jar 
>>> import stilts
>>> help(stilts)
```
## Pour commencer
Documentation de JyStilts ici : http://www.star.bris.ac.uk/~mbt/stilts/sun256/jystilts.html.
On pourra commencer par se familiariser avec les exemples suivants :
 - [lecture et écriture des tables](http://www.star.bris.ac.uk/~mbt/stilts/sun256/sec4.2.html)
 - [manipulation des tables](http://www.star.bris.ac.uk/~mbt/stilts/sun256/jytable.html)
 - [filtrer les tables](http://www.star.bris.ac.uk/~mbt/stilts/sun256/jyfilter.html)

L'exemple suivant montre comment ouvrir le catalogue 3FGL et afficher le nom 
des dix premières sources :
```
import stilts

# Load catalogue
filename = './catalogues/gll_psc_v16.fit'
table_3fgl = stilts.tread(filename)

# Selection of first ten BL Lacs (labelled as bll)
table = (table_3fgl.cmd_select('equals(CLASS1,"bll")')
         .cmd_keepcols('Source_Name')
         .cmd_head(10))
table.write()
```
On peut faire la même chose en accédant aux attributs de chacune des sources, ce qui
est parfois nécessaire, mais l'exécution du script sera plus longue :
```
import stilts

# Load catalogue
filename = './catalogues/gll_psc_v16.fit'
table_3fgl = stilts.tread(filename)

# Selection of first ten BL Lacs (labelled as bll)
table = (table_3fgl.cmd_select('equals(CLASS1,"bll")')
         .cmd_head(10))

# Loop on sources
table = table.cmd_random()  # magic command to be able to iterate
nevts = table.rowCount # number of entries
for ievt in range(nevts):
    index = ievt + 1
    row_src = table.cmd_rowrange(index, index)
    row = row_src[0]
    name = row['Source_Name']
    ra = row['RAJ2000']
    dec = row['DEJ2000']
    print('Source name: %s, RA=%f, DEC=%f' % (name, ra, dec))
```
Ces deux exemples peuvent être exécutés directement dans l'interpréteur en exécutant chacune des lignes
ou en utilisant un script qui peut être appelé avec :
```
java -jar jystilts.jar 
>>> execfile('script.py')
```
Pour obtenir des informations sur une commande de STILTS :
```
>>> import stilts
>>> help(stilts.tmatch2)  # stilts.tmatch2 permet de croiser deux tables sur différents critères
```
On peut aussi consulter la documentation pour obtenir des informations sur :
 - [les commandes de filtres](http://www.star.bris.ac.uk/~mbt/stilts/sun256/filterSteps.html)
 - [les fonctions (chaîne de caractères, coordonnées, calculs, etc.)](http://www.star.bris.ac.uk/~mbt/stilts/sun256/staticMethods.html)
 - [les différents moyens pour croiser des catalogues](http://www.star.bris.ac.uk/~mbt/stilts/sun256/match.html)
 - [les fonctions d'affichage de données (histogramme, 2D, 3D, dans le ciel, etc.)](http://www.star.bris.ac.uk/~mbt/stilts/sun256/plot2.html)
 
## S'exercer avec les blazars: différences spectrales entre les BL Lacs et les FSRQs
Dans cette partie nous allons utiliser les catalogues 3FGL (LAT 4-year Point Source Catalog) 
et 3LAC (The Third LAT AGN Catalog) fournis par la collaboration fermi/LAT.
Le catalogue 3FGL contient l'ensemble des sources détectées en 4 ans au-delà de 100 MeV par le télescope LAT 
embarqué à bord du satellite Fermi. Le catalogue 3LAC (même temps d'intégration des photons que pour le 2FGL) 
est exclusivement dédié aux noyaux actifs de galaxie (AGN) et notamment aux blazars (>95% des AGN).
 
L'objectif est de charactériser les différences spectrales entre les blazars de type BL Lac et Flat
Spectrum Radio Quasar (FSRQ) détectés par le LAT. Les catalogues sont disponibles dans le répertoire
`catalogues`.
 
### 1) Caractéristiques spectrales
Représenter sur un même graphe l'indice spectral et l'énergie pivot (qui est l'énergie à laquelle 
l'erreur sur le flux différentiel est la plus faible) des BL Lacs et des FSRQs.

Indices : 
 - sélectionner les différentes classes (CLASS1) de sources (bll, BLL, fsrq, FSRQs) avec la commande `cmd_select`
 - utilisation de la méthode `stilts.plot2d`
  
### 2) Caractéristiques spectrales - Hardness ratios
Le catalogue 3FGL fournit cinq valeurs de flux mesurées dans cinq bandes en énergie, 100-300 GeV, 300-1000 GeV, 
1000-3000 GeV, 3000-10000 GeV et 10000-100000 GeV.
En astrophysique, on utilise généralement des quantités appelées les « hardness ratios » (HR) qui permettent
d'estimer un indice spectral local avec des valeurs de flux mesurées dans deux bandes en énergie consécutives :

HR_ij = (EnergyFlux_j - EnergyFlux_i) / (EnergyFlux_i + EnergyFlux_j)

Ici on utilisera les valeurs du logarithme du flux en énergie (valeur du flux multiplié par l'énergie moyenne de l'intervalle
considéré) afin de mieux contraindre les HR.

Représenter sur un même graphe les « hardness ratios » HR_23 et HR_34.

Indices : 
 - Quelle valeur utiliser pour l'énergie moyenne de l'intervalle en énergie pour déterminer le 
 flux en énergie de la source dans une bande en énergie (la source suit une certaine loi spectrale) ?
 - calculer les hardness ratios avec plusieus étapes, énergie moyenne de l'intervalle, flux en énergie dans la bande et HR
 - utilisation de la commande `cmd_addcol` pour ajouter une colonne dans une table

### 3) Redshift
Représenter la distribution des redshifts des BL Lacs et des FSRQs sur un même graphe. Le catalogue 3LAC 
contient les redshifts des blazars lorsque celui-ci a été déterminé.

Indices : 
 - croiser les catalogues 3FGL et 3LAC avec `stilts.tmatch2`
 - exclure les sources qui n'ont pas de mesure de redshift
 - utilisation de la méthode `stilts.plothist`
