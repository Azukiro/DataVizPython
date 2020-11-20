# Rechargez votre voiture électrique

## Contexte

Ces dernières années, on entend beaucoup parler de la voiture électrique. Cette dernière est effet plus écologique que la voiture à essence, mais aussi plus rentable sur la durée, et moins bruyante. Cependant, la voiture électrique à une autonomie réduite : entre 200 et 300km selon les modèles. Pour pouvoir l'utiliser, il faut donc facilement pouvoir la recharger. Il est donc primordial d'avoir accès à des bonnes de recharge électrique.

Notre analyse, centrée sur le territoire Français, permettra de répondre à ces questions cruciales :
- Est-il facile de recharger sa voiture électrique en France ?
- Peut on trouver des bornes de recharges électriques sur l'ensemble du territoire français ?
- De plus, les bornes possèdent elles assez de prises pour pouvoir réagir à une forte demande ?
- Quels sont les principaux opérateurs ?

## Rapport d'analyse

<img src="https://github.com/Azukiro/DataVizPython/blob/master/assets/readme/map.png" width="325" height="300">  

En décembre 2020, la France recense près de 14760 bornes électriques sur son sol d'après son API sur data.gouv.fr. La carte réalisée nous montre que celles-ci sont **réparties sur l'ensemble du territoire Français**. La puissance maximale délivée est en général comprise entre **18 et 22 kwa**, ce qui parfaitement adapté. Il est donc possible de voyager partout en France en voiture électrique.

<img src="https://github.com/Azukiro/DataVizPython/blob/master/assets/readme/histo.png" width="500" height="300">

D'après ce graphique, environ 68% des bornes électriques donnent un accès à 2 prises. Il est donc possible de recharger deux voitures électriques en même temps.  De plus, environ 90% des bornes fournissent plus de 2 prises (majoritairement entre 2 et 6). Sachant que le temps de recharge est approximativement de 35 minutes sur une borne rapide, il c'est donc relativement rapide.

<img src="https://github.com/Azukiro/DataVizPython/blob/master/assets/readme/pie.png" width="500" height="300">

Maintenant, nous allons nous focaliser sur le marché des fournisseurs électriques. On constate via ce graphique que les principaux fournisseurs des bornes électriques françaises sont Bouygues Energie & Services (30%), Izivia (13%) et la Mairie de Paris (8%). On voit aussi que le secteur est très ouvert à la concurrence. En effet, un tiers des bornes électriques sont approvisionnées par 96% des fournisseurs. Ceux-ci ne sont foclisés que sur quelques dixaines voir quelques centaines de bornes. 

## User Guide

Pour exécuter l'application, il faut avoir installé le langage python. Si cela n'est pas fait, veuillez consultez le lien suivant : https://www.python.org/downloads/.

De plus, il faut installer les librairies suivantes :
- dash : ``` pip install dash ``` ;
- pandas : ``` pip install pandas ``` ;
- plotly : ``` pip install plotly ``` ;
- requests : ``` pip install requests ``` ;

Une fois installées, vous pouvez éxécuter le programme en lançant la commande : ```python main.py```.

Pour ouvrir l'application, ouvrer un navigateur web et saisissez l'URL suivante : http://127.0.0.1:8050/

## Developper Guide

### Organisation en fichiers

Le projet est découpé en plusieurs composants :
- console : affichage sur la console ;
- fetch : récupération des données via internet ;
- view : affichage de la page web ;
- viewHistogram : gestion de l'histogramme ;
- viewMap : gestion de la carte ;
- viewPieChart : gestion du pie chart ;

Dans chacun d'entre eux, on retrouvera les paramètres d'éxécution qui leurs sont propres. On y stipule par exemple les chemins d'accès des fichiers externes utilisés, les URLs des APIs, etc.

### Déroulé du programme

Le programme suit les étapes suivantes :
- Télécharge la dernière version du CSV via une requête web (fetch) ;
- Manipule les données afin de préparer l'affichage des graphiques et de la carte (viewHistogram, viewMap, viewPieChart) <br/>
  Ex : On récupère les coordonnées géographiques des bornes électriques mal renseignées ;
- Génère la structure HTML et ajoute une feuille de CSS (view) ;
- Lance le serveur web (view) ;

### APIs utilisées

Source de données utilisées : 
- Bornes électrique : https://www.data.gouv.fr/fr/datasets/r/50625621-18bd-43cb-8fde-6b8c24bdabb3 ;
- Géolocalisation : https://api-adresse.data.gouv.fr/search ;

## Crédits

Développeurs : 
- Ewen Bouquet (@iFairPlay22) ;
- Lucas Billard (@Azukiro) ;

Le projet a été réalisé dans le cadre de l'unité Python, en 1ère année de cycle ingénieur E3FI à l'ESIEE Paris.
