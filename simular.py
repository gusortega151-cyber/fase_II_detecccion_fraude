import pickle

#Cargar modelo
with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

#Simulacion de transacciones
transacciones = [
    [10,12,0], #normal
    [999,1,1],  #sospechosa
    [500,23,0] #normal

]

#Ejecutar predicciones
for i,t in enumerate(transacciones):
    pred = model.predict([t])[0]
    proba = model.predict_proba([t])[0]

    if pred == 1:
        resultado = "Fraude"
    else:
        resultado = "Legítima"

    print(f"Transacción {i+1}: {t} - Predicción: {resultado}")
    print(f"Probabilidades (legítima fraude): {proba}")