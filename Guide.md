# SAE51 - Interaction et mise en place d'une database

Dans cette Situation d'Apprentissage Professionnel, il nous est demandé de mettre en place une base de donné, y injecter des tables, des données et interagir avec celle-ci sous la forme de 12 requêtes personnalisées.

## Guide de démarrage

**DISCLAIMER**

docker : 20.10.24

docker-compose : 1.29.2

### Etape 1

Il est nécessaire de démarrer le stack docker :

```bash
docker-compose up -d
```

Il est normalement non nécessaire de démarrer le stack dans notre cas, il est déjà démarrer sur mon serveur distant, si néanmoins vous souhaitez faire les tests vous même, je vous recommande de supprimer la partie network et VPN du docker-compose.

Le stack contient :

- Container mysql 8.2
- Container wgEasy latest

### Etape 2

On peut vérifier le bon démarrage du/des container(s) avec "mysql Workbench 8.0", un schéma et des tables sont normalement déjà créées.

- *Mot de passe et identifiant dans le docker-compose et le .env*

### Etape 3

Nous devons maintenant injecter les données dans le schéma.

Pour ceci nous lançons :

1. **sql_data/generator.py**
2. **sql_injector/sql_injector.py**

Dans cette ordre précis, le premier créer la donnée et le second l'injecte dans le schéma.

### Etape 4

Si l'étape 3 est fonctionnelle dans ce cas, il ne reste plus que a utiliser **main.py** modifier l'IP dans le dossier sql_interact, fichier main.py.

Vous aurez donc accès une fois lancée a une interface pour interagir avec la database.