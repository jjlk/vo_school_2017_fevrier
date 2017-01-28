# Tutoriel de haute énergie - STILTS

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
([fichier](http://www.star.bris.ac.uk/~mbt/stilts/jystilts.jar)). 
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
         .cmd_keepcols('Source_Name')
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
    print('Source name: {}, RA={}, DEC={}'.format(name, ra, dec))
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
