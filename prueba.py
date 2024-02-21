# Carga de datos
###########################

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
