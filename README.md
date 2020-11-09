# ParkYourBike

De nos jours, nos **modes de déplacement** doivent **évoluer** à cause de la **surpopulation** et la **surconsommation** des véhicules à moteur.<br>
Néanmoins, pour **changer le mode de vie** de nombreuses personnes, il est nécessaire de leur montrer les **alternatives éventuelles** à celui-ci.<br><br>
C'est pourquoi notre outil est composé d'un **histogramme** et d'**une carte**, illustrants tout deux la **densité des emplacements de stationnement pour vélo en Île-de-France, en fonction de leur capacité d'accueil**.

## Rapport d'analyse
<img src="https://github.com/Fabinours/PYB/blob/master/PYB/Images/histo.png" width="400" height="200">  <img src="https://github.com/Fabinours/PYB/blob/master/PYB/Images/carte1.png" width="300" height="200">

**La première figure** est **l'histogramme** illustrant **le nombre d'emplacements** de stationnements en fonction de **leur capacité d'accueil**. Pour des raisons de présentation et de lisibilité, nous avons ici limité notre histogramme à **150 de capacité**. Néanmoins, il est quand même important de souligner que **le plus grand emplacement** se situe à Rueil-Malmaison et peut accueillir jusqu'à **448 vélos**.<br>

Hormis certaines valeurs isolées comme celle-ci, nous pouvons remarquer sur l'histogramme que **la majorité des emplacements** peuvent à peine accueillir **50 vélos**. En effet, **la valeur moyenne** de capacité d'accueil est **seulement de 10 vélos** par emplacement. De plus, seulement **8,7% des emplacements sont couverts** et seulement **0,3% des emplacements sont surveillés**.

Tous ces résultats montrent que même si **de plus en plus d'emplacements de stationnements sont crées, très peu sont réellement utilisables du au nombre de places disponibles, mais surtout du au manque de protection.**

## User Guide

Pour exécuter l'application, Python doit être installé ainsi que les packages suivants :
- plotly
- dash
- pandas
- requests

Commande d'installation : ```pip install plotly & pip install dash & pip install pandas & pip install requests```

Commande d'exécution : ```python main.py```

Pour ouvrir l'application, ouvrer un navigateur web et rentrer l'URL ci-dessous.

URL : http://127.0.0.1:8050/

## Developper Guide

Le projet est décomposé en 3 parties : 
- Le téléchargement des données, qui s'effectue lors de l'appel de fonction ```downloadCsv()```.
- Le traitement des données téléchargées, qui s'effectue lors de l'appel de fonction ```modifyCsv()```.
- L'affichage des données traitées, qui s'effectue dans la partie ```main```.

Nous utilisons le package ```requests``` pour télécharger les données et modifions par la suite en brut les données. 
Dans la partie ```main```, nous utilisons les packages ```pandas``` et ```plotly``` pour créer les différents éléments graphiques, et ```dash``` pour gérer leur disposition.

### Crédits

Développeurs : Fabien Courtois (@Fabinours) & Loic Fournier (@Hereal)<br>

Source des données utilisées : https://www.data.gouv.fr/fr/datasets/stationnement-velo-en-ile-de-france/<br>

Projet réalisé dans le cadre de l'unité Python de l'école ESIEE Paris, en 1ère année de cycle ingénieur E3FI.
