# Tutoriel de haute énergie - STILTS

## Objectifs
Se familiariser avec la manipulation des catalogues avec la librairie
[STILTS](http://www.star.bris.ac.uk/~mbt/stilts/). Celle-ci permet de 
d'utiliser l'intégralité des fonctionalités de 
[TOPCAT](http://www.star.bris.ac.uk/~mbt/topcat/) à partir de scripts
(en bash ou en [Jython](http://www.jython.org/)).
La librairie STILTS devient indispensable lorsqu'un nombre important
de manipulations doivent être réalisées sur des catalogues.

## Installation de la librairie
Les instructions sont indiquées [ici](http://www.star.bris.ac.uk/~mbt/stilts/#install).
Nous utiliserons le paquet qui contient STILTS et l'interpréteur Jython
(fichier [ici](http://www.star.bris.ac.uk/~mbt/stilts/jystilts.jar)). 
On pourra vérifier le bon fonctionnement du paquet de la manière suivante : 
```
$ java -jar jystilts.jar 
>>> import stilts
>>> help(stilts)
```
