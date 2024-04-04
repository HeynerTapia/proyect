# Proyecto de Visión Artificial

- **Nombre:** Daniel Tapia Morales
- **Universidad:** Universidad Privada Domingo Savio
- **Carrera:** Ingeniería de Sistemas
- **Facebook:** [danielheyner.tapiamorales](https://www.facebook.com/danielheyner.tapiamorales/)

## Introducción

Este proyecto tiene como objetivo desarrollar un sistema de visión artificial que utilice la biblioteca OpenCV para realizar operaciones de procesamiento de imágenes, como la detección de bordes.

## Objetivo

Crear un sistema de visión artificial capaz de procesar imágenes y realizar tareas específicas, como la detección de bordes, utilizando la biblioteca OpenCV.

## Marco Teórico

Se emplea la biblioteca OpenCV para el procesamiento de imágenes y la realización de tareas de visión artificial, como la detección de bordes.

### OpenCV

OpenCV es una biblioteca de código abierto que se utiliza principalmente para el procesamiento de imágenes y visión artificial. Proporciona diversas funciones y algoritmos para realizar tareas como la detección de bordes.

## Código Fuente y Procedimientos de Instalación

```bash
pip install opencv-python-headless
import cv2

# Función para aplicar detección de bordes a una imagen
def detectar_bordes(imagen):
    # Convertir la imagen a escala de grises
    imagen_gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
    
    # Aplicar el algoritmo Canny para detección de bordes
    bordes = cv2.Canny(imagen_gris, 100, 200)
    
    return bordes

# Lista de nombres de archivos de imagen
nombres_archivos = ["imagen1.jpg", "imagen2.jpg", "imagen3.jpg"]

# Iterar sobre cada nombre de archivo
for nombre_archivo in nombres_archivos:
    # Cargar la imagen desde el archivo
    imagen = cv2.imread(nombre_archivo)

    # Verificar si la imagen se cargó correctamente
    if imagen is None:
        print(f"No se pudo cargar la imagen {nombre_archivo}. Verifica la ruta y el nombre del archivo.")
    else:
        # Aplicar detección de bordes a la imagen
        bordes = detectar_bordes(imagen)

        # Mostrar la imagen original y los bordes detectados en una ventana
        cv2.imshow("Imagen Original", imagen)
        cv2.imshow("Bordes Detectados", bordes)

        # Esperar hasta que se presione una tecla y luego cerrar la ventana
        cv2.waitKey(0)
        cv2.destroyAllWindows()

```
## 🖥️ Modelado o Sistematización
El sistema se basa en la biblioteca OpenCV para realizar operaciones de procesamiento de imágenes. En este proyecto, se implementa la detección de bordes como ejemplo de funcionalidad de visión artificial.

## 📊 Conclusiones
El sistema de visión artificial desarrollado utilizando la biblioteca OpenCV es capaz de procesar imágenes y realizar tareas específicas, como la detección de bordes. Esto demuestra el potencial de la visión artificial para diversas aplicaciones en campos como la robótica, la seguridad, el reconocimiento de objetos, entre otros.

## 📚 Bibliografía
OpenCV. (2024). OpenCV Documentation. Recuperado de https://opencv.org/
## 📁 Anexos
Código Fuente: GitHub
Documentación de OpenAI: OpenAI Docs