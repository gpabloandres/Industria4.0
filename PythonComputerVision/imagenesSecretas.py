import cv2
import numpy as np
import random

# Crear una imagen en blanco
height, width = 400, 800
img = np.ones((height, width, 3), np.uint8) * 255

# Escribir el mensaje oculto en azul
mensaje = "Secreto!"
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img, mensaje, (50, 200), font, 3, (250, 255, 250), 10, cv2.LINE_AA)

# Añadir ruido en los canales rojo y verde
for i in range(height):
    for j in range(width):
        img[i, j, 1] += random.randint(0, 255)  # Canal verde
        img[i, j, 0] += random.randint(0, 255)  # Canal rojo

# Guardar la imagen
cv2.imwrite('imagen_oculta_con_ruido.png', img)