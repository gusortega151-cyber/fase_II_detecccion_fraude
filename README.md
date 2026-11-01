# API de Detección de Fraude 💳🔍

## 📋 Descripción del Proyecto
Este proyecto implementa una solución técnica completa y desplegable basada en un modelo de Machine Learning para la detección de fraude en transacciones financieras. El objetivo principal es encapsular el modelo entrenado dentro de una API utilizando FastAPI y contenerizar la aplicación con Docker para garantizar su portabilidad y consistencia en cualquier entorno de ejecución, preparándolo para un eventual despliegue en la nube (PaaS).

## 🗂️ Estructura del Repositorio
El proyecto sigue una estructura modular para separar la lógica de inferencia, la configuración del entorno y las dependencias:

\`\`\`text
Actividad_Fase_II/
│
├── main.py              # Código fuente de la API REST (FastAPI)
├── model.pkl            # Modelo de Machine Learning preentrenado serializado
├── requirements.txt     # Lista de dependencias y librerías necesarias de Python
├── Dockerfile           # Instrucciones para la construcción de la imagen del contenedor Docker
└── README.md            # Documentación principal del proyecto
\`\`\`

## 🛠️ Tecnologías Utilizadas
- **Lenguaje:** Python 3.10
- **Framework Web (API):** FastAPI, Uvicorn
- **Machine Learning:** Scikit-Learn, Pandas, Numpy
- **Contenedores:** Docker

## 🚀 Guía de Instalación y Ejecución Local

Para ejecutar este proyecto de forma local utilizando Docker, sigue estos pasos:

### 1. Clonar el repositorio
Abre tu terminal y ejecuta el siguiente comando para clonar el proyecto en tu máquina local:
\`\`\`bash
git clone https://github.com/TU_USUARIO/api-deteccion-fraude.git
cd api-deteccion-fraude
\`\`\`

### 2. Construir la imagen de Docker
Asegúrate de tener Docker Desktop en ejecución. Luego, construye la imagen del contenedor ejecutando:
\`\`\`bash
docker build -t modelo_fraude .
\`\`\`

### 3. Ejecutar el contenedor
Una vez construida la imagen, levanta el contenedor mapeando el puerto 8000:
\`\`\`bash
docker run -p 8000:8000 modelo_fraude
\`\`\`

### 4. Validar el funcionamiento (Swagger UI)
Abre tu navegador web y dirígete a la siguiente dirección para interactuar con la API a través de la interfaz visual generada automáticamente por FastAPI:
\`http://localhost:8000/docs\`

## 💡 Uso de la API (Endpoint de Predicción)

El endpoint principal para realizar predicciones es \`POST /predict\`. El modelo espera recibir una lista de transacciones en formato JSON.

**Ejemplo de cuerpo de la solicitud (Request Body):**
\`\`\`json
[
  {
    "monto": 850.50,
    "tiempo": 3.5,
    "pais_riesgo": 1
  },
  {
    "monto": 150.0,
    "tiempo": 14.0,
    "pais_riesgo": 0
  }
]
\`\`\`

**Ejemplo de respuesta (Response):**
La API devolverá una lista indicando `1` para transacciones fraudulentas y `0` para transacciones legítimas.
\`\`\`json
{
  "predicciones": [1, 0]
}
\`\`\`