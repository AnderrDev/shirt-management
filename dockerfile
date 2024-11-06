# Usar una imagen base de Python
FROM python:3.9

# Configurar el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiar los archivos del proyecto
COPY . .

# Instalar las dependencias del proyecto
RUN pip install --no-cache-dir -r requirements.txt.txt

# Exponer el puerto de Flask
EXPOSE 5000

# Comando para iniciar Flask en modo producción
CMD ["python", "run.py"]
