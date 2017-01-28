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

