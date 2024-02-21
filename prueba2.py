# Modelo de RF
###########################
# Selección de variables
nombres_m1 = ['ckd_epi', 'IC_eningreso', 'FEVI', 'Hbing', 
              'sum_charlson', 'FA_antec']
nombres_pp_m1 = ['ckd_epi', 'IC_eningreso_Yes', 'FEVI', 'Hbing', 
                 'sum_charlson', 'FA_antec_Yes']
inputs_m1 = X_pp[nombres_pp_m1].copy()

rsf_m1 = RandomSurvivalForest(
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
