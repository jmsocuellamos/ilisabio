# Carga de datos
###########################

import os
import numpy as np      # importamos numpy como np
import pandas as pd     # importamos pandas como pd
import math             # importamos módulo para cáculos matemáticos
import random

# Inputs originales
url = 'https://raw.githubusercontent.com/jmsocuellamos/ilisabio/main/inputs_ori.csv'
X = pd.read_csv(url)
# Inputs preprocesados
url = 'https://raw.githubusercontent.com/jmsocuellamos/ilisabio/main/inputs_pp.csv'
X_pp = pd.read_csv(url)
# Survival data
url = 'https://raw.githubusercontent.com/jmsocuellamos/ilisabio/main/survival.csv'
survival = pd.read_csv(url)
# Creamos Structured arrays necesario para los modelos de supervivencia
y = np.zeros(X_pp.shape[0], dtype={'names':('Status', 'Survival'),
                          'formats':('?', 'f8')})
y['Status'] = survival['ICCenseguimiento']
y['Survival'] = survival['meses_hasta_ICC']

print("")
print("")
print("\033[1m" + "Datos cargados con éxito" + "\033[0m")
print("")
print("")


# Modelo de RF
###########################
# Selección de variables
nombres_m1 = ['ckd_epi', 'IC_eningreso', 'FEVI', 'Hbing', 
              'sum_charlson', 'FA_antec']
nombres_pp_m1 = ['ckd_epi', 'IC_eningreso_Yes', 'FEVI', 'Hbing', 
                 'sum_charlson', 'FA_antec_Yes']
inputs_m1 = X_pp[nombres_pp_m1].copy()

rsf_m1 = sksurv.ensemble.RandomSurvivalForest(
    n_estimators=1000, min_samples_split=10, min_samples_leaf=15, 
    n_jobs=-1, random_state=20
)
rsf_m1.fit(inputs_m1, y)

# Evaluación
print("")
print("")
print("\033[1m" + "The value of the corcondance index of the model is " + "\033[0m", np.round(rsf_m1.score(inputs_m1, y),3))
print("")
print("")
