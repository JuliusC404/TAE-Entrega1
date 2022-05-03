import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.neighbors import KNeighborsClassifier
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import MinMaxScaler

import warnings
from sklearn.exceptions import DataConversionWarning
warnings.filterwarnings(action='ignore', category=DataConversionWarning)

def prediccionsatisfaccion(dic):
    lista = pd.DataFrame(data=dic)
    # REMOTO
    direccion='proyect/bd/data_60_try.csv'
    # LOCAL
    # direccion='proyect/proyect/bd/data_60_try.csv'
    basededatosmayores = pd.read_csv(direccion, index_col=0)
    basededatosmayores = basededatosmayores.drop(columns=['P767', 'P6081', 'P6083'])
    basededatosmayores = basededatosmayores[basededatosmayores['P1896'].le(10)]

    X = basededatosmayores.copy().drop(columns=['P1895','P6051','P5502'])
    y = basededatosmayores.copy().filter(items=['P1895'])
    test_size = 0.2
    random_state = 10
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=random_state)


    preprocessor = ColumnTransformer(
        [('age_', MinMaxScaler(),  ['P6040']),
        ('satisfaction_', MinMaxScaler(),  ['P1896', 'P1897', 'P1898', 'P1899', 'P3175', 'P1901', 'P1903', 'P1904', 'P1905', 'P1927'])
        ])
    preprocessor.fit(basededatosmayores)

    pipe = Pipeline([
        ('preprocessor', preprocessor),
        ('model', KNeighborsClassifier(
            n_neighbors=25,
            algorithm='auto',
            metric='manhattan',
            weights='distance'))
        ])

    pipe.fit(X_train, y_train)
    return pipe.predict(lista)[0]
