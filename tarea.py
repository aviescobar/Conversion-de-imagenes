from PIL import Image #Importacion de la imaen
import numpy as np   #Importacion de la libreria 
import os

# Verificar el directorio actual y los archivos en él
print("Directorio actual:", os.getcwd())
print("Archivos en el directorio actual:", os.listdir('.'))

# Nombre del archivo de imagen
nombre_archivo = 'FORD150.jpeg'

try:
    # Cargar la imagen
    imagen = Image.open(nombre_archivo)

    # Convertir la imagen en una matriz NumPy
    matriz = np.array(imagen)

    # Mostrar la matriz
    print(matriz)

except FileNotFoundError:
    print(f"Error: El archivo '{nombre_archivo}' no se encuentra en la carpeta actual.")