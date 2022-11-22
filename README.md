# Code Studio Test

This project contains the solution proposed by Alexandre to the code studio test code. 

The goal of this project is to create a data pipeline (python script) to prepare this [dataframe](https://opendata.paris.fr/explore/dataset/tous-les-documents-des-bibliotheques-de-pret/table/?disjunctive.langue&disjunctive.editeur&disjunctive.auteur_nom&disjunctive.auteur_secondaire_nom&disjunctive.libelle_v_smart_et_webopac&disjunctive.categorie_statistique_1&disjunctive.categorie_statistique_2&disjunctive.auteur&disjunctive.collectivite_auteur&disjunctive.collectivite_auteur_secondaire_&disjunctive.collectivite_co_auteur_)

The output of the data pipeline is a normalised dataframe called final_data.pkl in the root folder.

## Prerequisites

1. Use a machine with at least 16 Go of RAM
2. Use python 3.9
3. install requirements with ```pip install -r requirements```

## Quickstart

How to launch the projet ?

Simply run the main.py file:

```
python main.py
```

