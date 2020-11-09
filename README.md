# Rechargez votre voiture électrique

## Contexte

La voiture électrique est plus écologique

Est-il facile de recharger sa voiture électrique en France ?
Quels sont les principaux opérateurs en France ?
Peut on trouver des bornes de recharges électriques sur l'ensemble du territoire français ?
De plus, les bornes possèdent elles assez de prises pour pouvoir réagir à une forte demande ?

## Rapport d'analyse

<img src="https://github.com/Azukiro/DataVizPython/edit/master/assets/readme/map.png" width="400" height="300">  

Bla bla **bla** bla

<img src="https://github.com/Azukiro/DataVizPython/blob/master/assets/readme/histo.png" width="400" height="300">

Bla bla **bla** bla

<img src="https://github.com/Azukiro/DataVizPython/edit/master/assets/readme/pie.png" width="400" height="300">

Bla bla **bla** bla

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

Le projet est découpé en plusieurs composantes :
- console : affichage sur la console ;
- fetch : récupération des données via internet ;
- view : affichage de la page web ;
- viewHistogram : gestion de l'histogramme ;
- viewMap : gestion de la carte ;
- viewPieChart : gestion du pie chart ;

### Déroulé du programme

Le programme suit les étapes suivantes :
- Télécharge la dernière version du CSV via une requête web (fetch) ;
- Manipule les données afin de préparer l'affichage des graphiques et de la carte (viewHistogram, viewMap, viewPieChart) <br/>
  Ex : On récupère les coordonnées géographiques des bornes électriques mal renseignées ;
- Génère la structure HTML et ajoute une feuille de CSS (view) ;
- Lance le serveur web (view) ;

### Crédits

Source des données utilisées : 
- Bornes électrique : https://www.data.gouv.fr/fr/datasets/r/50625621-18bd-43cb-8fde-6b8c24bdabb3 ;
- Géolocalisation : https://api-adresse.data.gouv.fr/search ;

Développeurs : 
- Ewen Bouquet (@iFairPlay22) ;
- Loic Fournier (@Azukiro) ;

Le projet a été réalisé dans le cadre de l'unité Python, en 1ère année de cycle ingénieur E3FI à l'ESIEE Paris.
