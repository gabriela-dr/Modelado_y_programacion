import cv2
from Clasificacion import clasificacion_de_figuras
from Lector import rgb_a_hexadecimal

def analizar_arreglo_figuras(contornos, imagen):
    if not contornos:
        print("No se detectaron figuras en la imagen.")
        return

    print(f"Se encontraron {len(contornos)} figura(s). Analizando...")
    print("-" * 30)

    for i, contorno in enumerate(contornos):
        perimetro = cv2.arcLength(contorno, True)
        aproximacion = cv2.approxPolyDP(contorno, 0.04 * perimetro, True)
        puntas = len(aproximacion)

        if puntas > 6:
            puntas = 0

        categoria = clasificacion_de_figuras(puntas)

        M = cv2.moments(contorno)
        if M["m00"] != 0:
            cX = int(M["m10"] / M["m00"])
            cY = int(M["m01"] / M["m00"])
        else:
            cX, cY = contorno[0][0]

        color_bgr = imagen[cY, cX]
        blue, green, red = color_bgr[0], color_bgr[1], color_bgr[2]

        hex_color = rgb_a_hexadecimal(red, green, blue)

        print(f"Figura {i+1}:")
        print(f"  - Categoría: {categoria}")
        print(f"  - Color (Hex): {hex_color}")
        print("-" * 30)
