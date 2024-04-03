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
