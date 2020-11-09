# Rechargez votre voiture électrique

## Contexte

La voiture électrique est plus écologique

Est-il facile de recharger sa voiture électrique en France ?
Quels sont les principaux opérateurs en France ?
Peut on trouver des bornes de recharges électriques sur l'ensemble du territoire français ?
De plus, les bornes possèdent elles assez de prises pour pouvoir réagir à une forte demande ?

## Rapport d'analyse

<img src="https://github.com/Fabinours/PYB/blob/master/images/map.png" width="400" height="300">  

Bla bla **bla** bla

<img src="https://github.com/Fabinours/PYB/blob/master/images/histo.png" width="400" height="300">

Bla bla **bla** bla

<img src="https://github.com/Fabinours/PYB/blob/master/images/pie.png" width="400" height="300">

Bla bla **bla** bla

## User Guide

Pour exécuter l'application, il faut avoir installé le langage python. Si cela n'est pas fait, veuillez consultez le lien suivant : https://www.python.org/downloads/.

De plus, il faut installer les librairies suivantes :
- dash : ``` pip install dash ```
- pandas : ``` pip install pandas ```
- plotly : ``` pip install plotly ```
- requests : ``` pip install requests ```

Une fois installées, vous pouvez éxécuter le programme en lançant la commande :```python main.py```

Pour ouvrir l'application, ouvrer un navigateur web et saisissez l'URL suivante : http://127.0.0.1:8050/

## Developper Guide

Le projet est décomposé en 3 parties : 
- Le téléchargement des données, qui s'effectue lors de l'appel de fonction ```downloadCsv()```.
- Le traitement des données téléchargées, qui s'effectue lors de l'appel de fonction ```modifyCsv()```.
- L'affichage des données traitées, qui s'effectue dans la partie ```main```.

Nous utilisons le package ```requests``` pour télécharger les données et modifions par la suite en brut les données. 
Dans la partie ```main```, nous utilisons les packages ```pandas``` et ```plotly``` pour créer les différents éléments graphiques, et ```dash``` pour gérer leur disposition.

### Crédits

Développeurs : 
- Ewen Bouquet (@iFairPlay22);
- Loic Fournier (@Azukiro);

Source des données utilisées : 
- API des bornes électrique : https://www.data.gouv.fr/fr/datasets/r/50625621-18bd-43cb-8fde-6b8c24bdabb3<br>
- API de géolocalisation : https://api-adresse.data.gouv.fr/search/

Projet réalisé dans le cadre de l'unité Python de l'école ESIEE Paris, en 1ère année de cycle ingénieur E3FI.
