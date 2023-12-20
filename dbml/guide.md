# DBML

Link : https://dbml.dbdiagram.io/cli/#installation

## Etape 1

Installer dbml2sql :

```bash
sudo npm install -g @dbml/cli
```

## Etape 2.1 - SQL

Génération d'un fichier DBML a partir du fichier SQL

```bash
sql2dbml dump.sql --mysql -o dump.dbml
```

## Etape 2.2 - DBML

Génération d'un fichier SQL a partir du fichier DBML

```bash
dbml2sql dump.dbml -o dump.sql
```

## Etape 3

Installer DBML-renderer :

```bash
npm install -g @softwaretechnik/dbml-renderer
```

## Etape 4

Génération d'un fichier SVG a partir du fichier DBML

```bash
dbml-renderer -i dump.dbml -o dump.svg
```

## Etape 5

Installer convert-svg-to-png

```bash
npm install -g convert-svg-to-png
```

Install libnss3

```bash
sudo apt-get install libnss3
sudo apt-get install libgbm1
sudo apt-get install libasound2
```

## Etape 6

Convert our svg file into png file

```bash
convert-svg-to-png dump.svg
```

## Etape 7

![dump](C:\Users\Marc\Desktop\dump.png)