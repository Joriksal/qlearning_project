import numpy as np
from PIL import Image
import cv2
import matplotlib.pyplot as plt
import pickle
import time
from matplotlib import style
import os

style.use("ggplot")

TAMANO = 10
EPISODIOS = 25000
PENALIZACION_MOVIMIENTO = 1
PENALIZACION_ENEMIGO = 300
RECOMPENSA_COMIDA = 25

epsilon = 0.9
DECAY_EPSILON = 0.9998
MOSTRAR_CADA = 1000

TASA_APRENDIZAJE = 0.1
DESCUENTO = 0.95

JUGADOR_N = 1
COMIDA_N = 2
ENEMIGO_N = 3

COLORES = {
    JUGADOR_N: (255, 175, 0),   # Naranja
    COMIDA_N: (0, 255, 0),      # Verde
    ENEMIGO_N: (0, 0, 255),     # Rojo
}

class Blob:
    def __init__(self):
        self.x = np.random.randint(0, TAMANO)
        self.y = np.random.randint(0, TAMANO)

    def __sub__(self, otro):
        return (self.x - otro.x, self.y - otro.y)

    def accion(self, opcion):
        if opcion == 0:
            self.mover(x=1, y=1)
        elif opcion == 1:
            self.mover(x=-1, y=-1)
        elif opcion == 2:
            self.mover(x=-1, y=1)
        elif opcion == 3:
            self.mover(x=1, y=-1)

    def mover(self, x=False, y=False):
        if not x:
            self.x += np.random.randint(-1, 2)
        else:
            self.x += x
        if not y:
            self.y += np.random.randint(-1, 2)
        else:
            self.y += y

        self.x = max(0, min(self.x, TAMANO - 1))
        self.y = max(0, min(self.y, TAMANO - 1))

if __name__ == "__main__":
    tabla_q = {}
    for x1 in range(-TAMANO+1, TAMANO):
        for y1 in range(-TAMANO+1, TAMANO):
            for x2 in range(-TAMANO+1, TAMANO):
                for y2 in range(-TAMANO+1, TAMANO):
                    tabla_q[((x1, y1), (x2, y2))] = [np.random.uniform(-5, 0) for _ in range(4)]

    recompensas_episodio = []

    for episodio in range(EPISODIOS):
        jugador = Blob()
        comida = Blob()
        enemigo = Blob()

        if episodio % MOSTRAR_CADA == 0:
            print(f"Episodio {episodio}, epsilon: {epsilon:.3f}, recompensa media: {np.mean(recompensas_episodio[-MOSTRAR_CADA:]) if episodio >= MOSTRAR_CADA else 0}")
            mostrar = True
        else:
            mostrar = False

        recompensa_episodio = 0

        for _ in range(200):
            observacion = (jugador - comida, jugador - enemigo)

            if np.random.random() > epsilon:
                accion = np.argmax(tabla_q[observacion])
            else:
                accion = np.random.randint(0, 4)

            jugador.accion(accion)

            if jugador.x == enemigo.x and jugador.y == enemigo.y:
                recompensa = -PENALIZACION_ENEMIGO
            elif jugador.x == comida.x and jugador.y == comida.y:
                recompensa = RECOMPENSA_COMIDA
            else:
                recompensa = -PENALIZACION_MOVIMIENTO

            nueva_obs = (jugador - comida, jugador - enemigo)

            max_q_futuro = np.max(tabla_q[nueva_obs])
            q_actual = tabla_q[observacion][accion]

            if recompensa == RECOMPENSA_COMIDA:
                nuevo_q = RECOMPENSA_COMIDA
            else:
                nuevo_q = (1 - TASA_APRENDIZAJE) * q_actual + TASA_APRENDIZAJE * (recompensa + DESCUENTO * max_q_futuro)

            tabla_q[observacion][accion] = nuevo_q

            if mostrar:
                entorno = np.zeros((TAMANO, TAMANO, 3), dtype=np.uint8)
                entorno[comida.x][comida.y] = COLORES[COMIDA_N]
                entorno[jugador.x][jugador.y] = COLORES[JUGADOR_N]
                entorno[enemigo.x][enemigo.y] = COLORES[ENEMIGO_N]

                imagen = Image.fromarray(entorno, 'RGB')
                imagen = imagen.resize((300, 300))
                cv2.imshow("Juego Blob", np.array(imagen))

                if recompensa in [RECOMPENSA_COMIDA, -PENALIZACION_ENEMIGO]:
                    if cv2.waitKey(500) & 0xFF == ord('q'):
                        break
                else:
                    if cv2.waitKey(1) & 0xFF == ord('q'):
                        break

            recompensa_episodio += recompensa
            if recompensa in [RECOMPENSA_COMIDA, -PENALIZACION_ENEMIGO]:
                break

        recompensas_episodio.append(recompensa_episodio)
        epsilon *= DECAY_EPSILON

    promedio_mov = np.convolve(recompensas_episodio, np.ones((MOSTRAR_CADA,)) / MOSTRAR_CADA, mode='valid')

    plt.plot(promedio_mov)
    plt.ylabel(f"Recompensa promedio {MOSTRAR_CADA}")
    plt.xlabel("Episodio #")
    plt.show()

    os.makedirs("qtable_backups", exist_ok=True)
    with open(f"qtable_backups/qtable-{int(time.time())}.pickle", "wb") as f:
        pickle.dump(tabla_q, f)