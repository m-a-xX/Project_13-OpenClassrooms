# Générateur de citations

Ce programme a pour but de générer des citations en donnant la possibilité à l'utilisateur de consulter une citation au hasard ou de choisir une catégorie pour consulter une citation ayant pour thème celle-là.

## Dépendances et installation

Vous devez avoir MySQL et Virtualenv installé sur votre ordinateur.
Premièrement, créez un environnement Python3 avec la commande Unix :
$ virtualenv env -p python3
Ensuite, après avoir clone le repo, passez dans l'environnement et installez les dépendances :
$ . env/bin/activate
(env) $ pip install -r requirements.txt
Puis initialisez la base de données de citations utilisée par le programme avec la commande :
(env) $ python create_db.py

## Utilisation

Une fois la préparation effectuée, vous pouvez utiliser le programme en lançant la commande :
(env) $ python main.py
