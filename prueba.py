## Libreria scikit-survival
!pip install scikit-survival
## Librerias de tratamiento de datos y entorno gráfico
import os
import numpy as np      # importamos numpy como np
import pandas as pd     # importamos pandas como pd
import math             # importamos módulo para cáculos matemáticos
import random

# Configuración de entorno gráfico
######################################
%matplotlib inline
import matplotlib.pyplot as plt # importamos matplotlib como plt
import seaborn as sns # importamos seaborn como sns
sns.set_style("ticks")
%config InlineBackend.figure_format = 'retina'

# Módulos scikit-survival
###########################
from sksurv.linear_model import CoxPHSurvivalAnalysis, CoxnetSurvivalAnalysis
from sksurv.ensemble import RandomSurvivalForest
from sksurv.metrics import (
    concordance_index_censored,concordance_index_ipcw,cumulative_dynamic_auc
)
