# ue19-lab-05

Petite application Python qui interroge une API publique ([JokeAPI](https://jokeapi.dev/)) avec la librairie "requests" et affiche une blague de programmation dans la console.

## Contenu

- "app.py" : le programme qui interroge l'API
- "requirements.txt" : les dépendances Python
- "Dockerfile" : permet de créer l'image du conteneur, qui exécute "app.py"

## Installation et lancement en local

"bash
pip install -r requirements.txt
python app.py
"

## Avec Docker

"bash
docker build -t ue19-lab-05 .
docker run --rm ue19-lab-05
"

## Fonctionnement

Le programme envoie une requête GET à l'API JokeAPI, récupère la réponse JSON et affiche la blague.
