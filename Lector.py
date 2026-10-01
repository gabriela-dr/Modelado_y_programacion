import cv2

def cargar_imagen(ruta_imagen):
    imagen = cv2.imread(ruta_imagen, 1)
    if imagen is None:
        raise FileNotFoundError(f"Error: No se pudo cargar la imagen '{ruta_imagen}'. Verifica la ruta y que sea .bmp")
    return imagen

def convertir_a_grises(imagen_color):
    return cv2.cvtColor(imagen_color, cv2.COLOR_BGR2GRAY)

def rgb_a_hexadecimal(red, green, blue):
    # Se añade .upper() para que el formato hexadecimal se vea más limpio (ej. #FF0000)
    return "#{:02x}{:02x}{:02x}".format(red, green, blue).upper()
