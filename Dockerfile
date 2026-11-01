# 1. Imagen base: Elegimos una versión ligera de Python como nuestro sistema operativo base.
FROM python:3.10-slim

# 2. Variables de entorno: Le decimos a Python que no genere archivos basura y muestre los errores directo en pantalla.
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# 3. Directorio de trabajo: Creamos una carpeta llamada /app DENTRO de la burbuja (contenedor) y nos movemos allí.
WORKDIR /app

# 4. Copiar dependencias: Copiamos tu archivo requirements.txt desde tu PC hacia el contenedor.
COPY requirements.txt .

# 5. Instalar dependencias: Le decimos al contenedor que instale las librerías que listaste.
RUN pip install --no-cache-dir -r requirements.txt

# 6. Copiar el proyecto: Copiamos tu código de la API y el modelo entrenado hacia el contenedor.
COPY main.py .
COPY model.pkl .

# 7. Exponer puerto: Le decimos al contenedor que vamos a comunicarnos con él a través de la puerta (puerto) 8000.
EXPOSE 8000

# 8. Comando de ejecución: Esta es la instrucción que el contenedor ejecutará automáticamente al encenderse (arrancar tu API).
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]