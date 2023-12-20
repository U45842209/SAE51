# SAE51

Groupe : E04

## Objectif

— soutenance orale de présentation du travail, en binôme, durée 10mn + 5mn questions (créneau à
définir)

— livrable : vous produirez un seul fichier zip contenant tout le nécessaire pour réaliser une démonstration fonctionnelle de votre travail ;

— le Dockerfile du SGBD (MySql ou MariaDB) avec un script bash réalisant le build et le lancement
du conteneur ;

— un script de chargement de la BDD, ainsi que les n fichiers CSV de données (virtuelles) associés ;

— un unique script reprenant les requêtes décrites ci-dessus, avec éventuellement des fichiers annexes contenant les requêtes SQL si elles sont trop complexes pour être mises directement dans
le script.

## Procédure

Dans un premier temps nous avons élaboré un plan SQL, qui a déterminé l’emplacement de chaque clef.
Nous sommes arrivés à un fichier SQL pour notre BDD.

Échantillon de notre fichier SQL.


Nous avons généré à l’aide de python et du module Faker, des fichier CSV à injecter dans notre BDD.
L’injection des données est gérée en python via le module MySql connector.

Les requêtes sont aussi gérées en python via MySql connector à l’instar des injections. Et pour une simplicité d’utilisation, les requêtes peuvent être visualisées via un serveur Flask.

Voir la documention [ici](Guide.md)


