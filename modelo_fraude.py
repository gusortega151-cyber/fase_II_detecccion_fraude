import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import pickle

# Generar datos simulados
np.random.seed(42)

n_samples = 1000

monto = np.random.uniform(10, 1000, n_samples)
tiempo = np.random.uniform(0, 24, n_samples)
pais_riesgo = np.random.randint(0, 2, n_samples)  # 0: bajo riesgo, 1: alto riesgo

# Etiqueta de fraude: 1 si es fraude, 0 si no lo es
# Regla simple para generar fraude
fraude = (
    (monto > 800).astype(int) | 
    (pais_riesgo == 1).astype(int) |
    ((tiempo < 6) & (monto > 500)).astype(int)
)

# Variables de entrada (features)
x = np.column_stack((monto, tiempo, pais_riesgo))
y = fraude

#Divisió de datos
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

#Entrenamiento del modelo
model = RandomForestClassifier(n_estimators=100)
model.fit(x_train, y_train)

#Almacenamiento del moedlo
with open("model.pkl", "wb") as f:
    pickle.dump(model, f)

print("Modelo entrenado y guardado como 'model.pkl'")