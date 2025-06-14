from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
from matplotlib import style
import numpy as np
import cv2
import os

style.use('ggplot')

# Asigna un color verde a la mejor acción, rojo a las demás
def obtener_color_q(valor, valores):
    if valor == max(valores):
        return "green", 1.0
    else:
        return "red", 0.3

# Genera imágenes para visualizar la tabla Q a lo largo del entrenamiento
def generar_imagenes_desde_qtables(inicio, fin, paso):
    os.makedirs("qtable_charts", exist_ok=True)
    for episodio in range(inicio, fin, paso):
        print(f"Generando imagen para qtable {episodio}")
        figura = plt.figure(figsize=(12, 9))
        ax0 = figura.add_subplot(311)
        ax1 = figura.add_subplot(312)
        ax2 = figura.add_subplot(313)

        qtable = np.load(f"qtables/{episodio}-qtable.npy")

        for x, fila in enumerate(qtable):
            for y, valores_acciones in enumerate(fila):
                ax0.scatter(x, y, c=obtener_color_q(valores_acciones[0], valores_acciones)[0],
                            marker="o", alpha=obtener_color_q(valores_acciones[0], valores_acciones)[1])
                ax1.scatter(x, y, c=obtener_color_q(valores_acciones[1], valores_acciones)[0],
                            marker="o", alpha=obtener_color_q(valores_acciones[1], valores_acciones)[1])
                ax2.scatter(x, y, c=obtener_color_q(valores_acciones[2], valores_acciones)[0],
                            marker="o", alpha=obtener_color_q(valores_acciones[2], valores_acciones)[1])

        ax0.set_ylabel("Acción 0")
        ax1.set_ylabel("Acción 1")
        ax2.set_ylabel("Acción 2")

        plt.savefig(f"qtable_charts/{episodio}.png")
        plt.clf()

# Crea un video a partir de las imágenes generadas
def crear_video_desde_imagenes():
    os.makedirs("videos", exist_ok=True)
    codificador = cv2.VideoWriter_fourcc(*'XVID')
    salida = cv2.VideoWriter('videos/qlearn.avi', codificador, 60.0, (1200, 900))

    for episodio in range(0, 25000, 10):
        ruta_imagen = f"qtable_charts/{episodio}.png"
        if not os.path.exists(ruta_imagen):
            print(f"Imagen no encontrada: {ruta_imagen}")
            continue
        cuadro = cv2.imread(ruta_imagen)
        salida.write(cuadro)

    salida.release()
    print("Video creado: videos/qlearn.avi")

if __name__ == "__main__":
    generar_imagenes_desde_qtables(0, 20000, 100)
    crear_video_desde_imagenes()
