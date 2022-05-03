import math
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.neighbors import KNeighborsClassifier
import warnings
from sklearn.exceptions import DataConversionWarning
warnings.filterwarnings(action='ignore', category=DataConversionWarning)

def prediccionsatisfaccionMen(lista):
  # REMOTO
  direccion='proyect/bd/menores.csv'
  # LOCAL
  # direccion='proyect/proyect/bd/menores.csv'
  menores = pd.read_csv(direccion, index_col=0)

  valores = menores.drop(columns=['cuidador', 'valor'])
  pesos = [0.6,0.7,0.85,0.35,1,0.2]

  for i in range(20119):
    suma=0
    for x in range(6):
      if valores.iloc[i][x] != 0:
        valor=(valores.iloc[i][x]/valores.iloc[i][x])*(1/valores.iloc[i][x])*pesos[x]
      else:
        valor=0
      suma=suma+valor
    menores['valor'].iloc[i]=suma

  for i in range(20119):
    suma=0
    if menores['cuidador'].iloc[i] == 1:
      suma=3
    elif menores['cuidador'].iloc[i] == 2:
      suma=8
    elif menores['cuidador'].iloc[i] == 3:
      suma=7
    elif menores['cuidador'].iloc[i] == 4:
      suma=6
    elif menores['cuidador'].iloc[i] == 5:
      suma=4
    elif menores['cuidador'].iloc[i] == 6:
      suma=5
    elif menores['cuidador'].iloc[i] == 7:
      suma=1
    elif menores['cuidador'].iloc[i] == 8:
      suma=2    
    menores['valor'].iloc[i]=math.floor(menores['valor'].iloc[i]+suma-1)

  X = menores.copy().drop(columns=['valor'])
  y = menores.copy().filter(items=['valor'])
  test_size = 0.3
  random_state = 8
  X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=random_state)

  pipe = Pipeline([
      ('model', KNeighborsClassifier(
          n_neighbors=11,
          algorithm='auto',
          metric='manhattan',
          weights='distance'))
      ])

  pipe.fit(X_train, y_train)
  return pipe.predict(lista)[0]