import math

import pandas as pd

class PrepareParisDataLibray:
    paris_library_df = None
    def run(self):
        self.check_requirements()
        self.load_data()
        self.check_format()
        self.normalize()
        self.persist()
        print("Final dataframe:")
        print(self.paris_library_df.head())

    def load_data(self):
        print("Loading data")
        self.paris_library_df = pd.read_csv('data.csv',sep=';',low_memory=False)



    def check_requirements(self):
        print("Checking requirements")
        from os.path import exists

        file_exists = exists("data.csv")
        if not file_exists:
            print("Requirements are not met: please download the 'Paris Data Library' dataframe with that command:")
            print(" curl --location --request GET 'https://opendata.paris.fr/explore/dataset/tous-les-documents-des-bibliotheques-de-pret/download/?format=csv&timezone=Europe/Berlin&lang=fr&use_labels_for_header=true&csv_separator=%3B' > data.csv")


    def check_format(self):
        print("Checking format")
        import pandera as pa


        paris_library_df = self.paris_library_df




        schema = pa.DataFrameSchema({
            'N° de notice': pa.Column(int, nullable=True),
            'ISBN': pa.Column(str, nullable=True),
            'ISSN': pa.Column(str, nullable=True),
            'EAN': pa.Column(str, nullable=True),
            'Langue': pa.Column(str, nullable=True),
            'Titre': pa.Column(str, nullable=True),
            'Edition': pa.Column(str, nullable=True),
            'Editeur': pa.Column(str, nullable=True),
            'Date': pa.Column(str, nullable=True),
            'Format': pa.Column(str, nullable=True),
            'Collection': pa.Column(str, nullable=True),
            'Titre de série': pa.Column(str, nullable=True),
            'N°': pa.Column(str, nullable=True),
            'Auteur Nom': pa.Column(str, nullable=True),
            'Auteur Prénom': pa.Column(str, nullable=True),
            'Auteur Dates': pa.Column(str, nullable=True),
            'Co-auteur Nom': pa.Column(str, nullable=True),
            'Co-auteur Prénom': pa.Column(str, nullable=True),
            'Dates': pa.Column(str, nullable=True),
            'Auteur secondaire Nom': pa.Column(str, nullable=True),
            'Auteur secondaire Prénom': pa.Column(str, nullable=True),
            'Auteur secondaire Dates': pa.Column(str, nullable=True),
            'Auteur collectivité': pa.Column(str, nullable=True),
            'Subdivision auteur collectivité': pa.Column(str, nullable=True),
            'Co-auteur collectivité': pa.Column(str, nullable=True),
            'Subdivision co-auteur collectivité': pa.Column(str, nullable=True),
            'Auteur secondaire collectivité': pa.Column(str, nullable=True),
            'Subdivision auteur secondaire collectivité': pa.Column(str, nullable=True),
            'Indice': pa.Column(str, nullable=True),
            'Cote majoritaire': pa.Column(str, nullable=True),
            'Type de document': pa.Column(str, nullable=True),
            'Nombre de localisations': pa.Column(float, nullable=True, coerce=True),
            'Nombre de prêt total': pa.Column(float, nullable=True, coerce=True),
            'Nombre de prêts 2017': pa.Column(float, nullable=True, coerce=True),
            'Nombre de prêt année 2018 au 26 juillet 2018': pa.Column(float, nullable=True, coerce=True),
            "Nombre d'exemplaires": pa.Column(float, nullable=True, coerce=True),
            'Catégorie statistique 1': pa.Column(str, nullable=True),
            'Catégorie statistique 2': pa.Column(str, nullable=True),
            'Aimé Césaire': pa.Column(float, nullable=True,coerce=True),
            'Amélie': pa.Column(float, nullable=True, coerce=True),
            'André Malraux': pa.Column(float, nullable=True, coerce=True),
            'Andrée Chedid': pa.Column(float, nullable=True, coerce=True),
            'Arthur Rimbaud': pa.Column(float, nullable=True, coerce=True),
            'Assia Djebar': pa.Column(float, nullable=True, coerce=True),
            'Batignolles': pa.Column(float, nullable=True, coerce=True),
            'Benjamin Rabier': pa.Column(float, nullable=True, coerce=True),
            'Buffon': pa.Column(float, nullable=True, coerce=True),
            'Canopée - la fontaine': pa.Column(float, nullable=True, coerce=True),
            'Chaptal': pa.Column(float, nullable=True, coerce=True),
            'Charlotte Delbo': pa.Column(float, nullable=True, coerce=True),
            'Claude Lévi-Strauss': pa.Column(float, nullable=True, coerce=True),
            'Colette Vivier': pa.Column(float, nullable=True, coerce=True),
            'Courcelles': pa.Column(float, nullable=True, coerce=True),
            'Couronnes - Naguib Mahfouz': pa.Column(float, nullable=True, coerce=True),
            'Crimée': pa.Column(float, nullable=True, coerce=True),
            'Diderot': pa.Column(float, nullable=True, coerce=True),
            'Drouot': pa.Column(float, nullable=True, coerce=True),
            'Edmond Rostand': pa.Column(float, nullable=True, coerce=True),
            'Europe': pa.Column(float, nullable=True, coerce=True),
            'Faidherbe': pa.Column(float, nullable=True, coerce=True),
            'Fessart': pa.Column(float, nullable=True, coerce=True),
            'François Villon': pa.Column(float, nullable=True, coerce=True),
            'Françoise Sagan': pa.Column(float, nullable=True, coerce=True),
            'Georges Brassens': pa.Column(float, nullable=True, coerce=True),
            'Germaine Tillion': pa.Column(float, nullable=True, coerce=True),
            'Glacière': pa.Column(float, nullable=True, coerce=True),
            "Goutte d'Or": pa.Column(float, nullable=True, coerce=True),
            'Gutenberg': pa.Column(float, nullable=True, coerce=True),
            'Hélène Berr': pa.Column(float, nullable=True, coerce=True),
            'Hergé': pa.Column(float, nullable=True, coerce=True),
            'Heure Joyeuse': pa.Column(float, nullable=True, coerce=True),
            'Italie': pa.Column(float, nullable=True, coerce=True),
            'Jacqueline de Romilly': pa.Column(float, nullable=True),
            'Jean-Pierre Melville': pa.Column(float, nullable=True, coerce=True),
            'Lancry': pa.Column(float, nullable=True, coerce=True),
            'Louise Michel': pa.Column(float, nullable=True, coerce=True),
            'Marguerite Audoux': pa.Column(float, nullable=True, coerce=True),
            'Marguerite Duras': pa.Column(float, nullable=True, coerce=True),
            'Marguerite Yourcenar': pa.Column(float, nullable=True, coerce=True),
            'Maurice Genevoix': pa.Column(float, nullable=True, coerce=True),
            'MMP': pa.Column(float, nullable=True, coerce=True),
            'Mohammed Arkoun': pa.Column(float, nullable=True, coerce=True),
            'Mortier': pa.Column(float, nullable=True, coerce=True),
            'Musset': pa.Column(float, nullable=True, coerce=True),
            'Oscar Wilde': pa.Column(float, nullable=True, coerce=True),
            'Parmentier': pa.Column(float, nullable=True, coerce=True),
            'Place des Fêtes': pa.Column(float, nullable=True, coerce=True),
            'Rainer Maria Rilke': pa.Column(float, nullable=True, coerce=True),
            'Réserve Centrale': pa.Column(float, nullable=True, coerce=True),
            'Robert Sabatier': pa.Column(float, nullable=True, coerce=True),
            'Sorbier': pa.Column(float, nullable=True, coerce=True),
            'Vaclav Havel': pa.Column(float, nullable=True, coerce=True),
            'Jacqueline de Romilly': pa.Column(float, nullable=True, coerce=True),
            'Valeyre': pa.Column(float, nullable=True, coerce=True),
            'Vandamme': pa.Column(float, nullable=True, coerce=True),
            'Vaugirard': pa.Column(float, nullable=True, coerce=True),
            'Auteur': pa.Column(str, nullable=True, coerce=True),
            'Co-auteur': pa.Column(str, nullable=True, coerce=True),
            'Auteur secondaire': pa.Column(str, nullable=True, coerce=True),
            'Collectivité auteur': pa.Column(str, nullable=True, coerce=True),
            'Collectivité auteur secondaire ': pa.Column(str, nullable=True, coerce=True),
            'Collectivité co-auteur ': pa.Column(str, nullable=True)


        })

        validated_df = schema(paris_library_df)

        self.paris_library_df=validated_df

        return

    def normalize(self):
        print("Normalizing data")

        libraries = ['Aimé Césaire',
                     'Amélie',
                     'André Malraux',
                     'Andrée Chedid',
                     'Arthur Rimbaud',
                     'Assia Djebar',
                     'Batignolles',
                     'Benjamin Rabier',
                     'Buffon',
                     'Canopée - la fontaine',
                     'Chaptal',
                     'Charlotte Delbo',
                     'Claude Lévi-Strauss',
                     'Colette Vivier',
                     'Courcelles',
                     'Couronnes - Naguib Mahfouz',
                     'Crimée',
                     'Diderot',
                     'Drouot',
                     'Edmond Rostand',
                     'Europe',
                     'Faidherbe',
                     'Fessart',
                     'François Villon',
                     'Françoise Sagan',
                     'Georges Brassens',
                     'Germaine Tillion',
                     'Glacière',
                     "Goutte d'Or",
                     'Gutenberg',
                     'Hélène Berr',
                     'Hergé',
                     'Heure Joyeuse',
                     'Italie',
                     'Jacqueline de Romilly',
                     'Jean-Pierre Melville',
                     'Lancry',
                     'Louise Michel',
                     'Marguerite Audoux',
                     'Marguerite Duras',
                     'Marguerite Yourcenar',
                     'Maurice Genevoix',
                     'MMP',
                     'Mohammed Arkoun',
                     'Mortier',
                     'Musset',
                     'Oscar Wilde',
                     'Parmentier',
                     'Place des Fêtes',
                     'Rainer Maria Rilke',
                     'Réserve Centrale',
                     'Robert Sabatier',
                     'Sorbier',
                     'Vaclav Havel',
                     'Jacqueline de Romilly',
                     'Valeyre',
                     'Vandamme',
                     'Vaugirard']

        paris_library_df = self.paris_library_df


        library = paris_library_df[libraries]


        library=library.fillna("")
        library[library != ""] = True

        library=library.apply(lambda x: x.replace(True,x.name))

        library = library.apply(lambda x: '|'.join(filter(len,x.tolist())),axis=1)


        library = paris_library_df.assign(libray=library)

        paris_library_df.drop(libraries, axis=1)

        paris_library_df = pd.concat([paris_library_df,library], axis=1)

        self.paris_library_df=paris_library_df


        return

    def persist(self):
        print("Persisting data")
        paris_library_df=self.paris_library_df
        paris_library_df.to_pickle('final_data.pkl')
        return

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    job = PrepareParisDataLibray()
    job.run()
