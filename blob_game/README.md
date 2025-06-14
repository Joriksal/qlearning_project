# Blob Game Q-Learning

Proyecto de entrenamiento con **Q-learning** para un juego simple llamado **Blob Game**, donde un agente inteligente aprende a navegar en una cuadrícula para encontrar comida y evitar enemigos.

---

## Descripción General

**Blob Game** es un entorno tipo *grid world* con tres entidades principales:

-  **Agente (Blob):** Aprende a moverse por la cuadrícula.
-  **Comida:** Objetivo a alcanzar para obtener recompensa positiva.
-  **Enemigo:** Obstáculo que debe evitar para no recibir penalizaciones.

El agente puede desplazarse en las 4 direcciones diagonales y su objetivo es maximizar la recompensa acumulada encontrando la comida y evitando al enemigo. El aprendizaje se realiza usando un algoritmo simple de Q-learning con una tabla Q.

---

## Funcionamiento

- **Tamaño de cuadrícula:** 10x10
- **Inicio de episodio:** Posiciones aleatorias para agente, comida y enemigo.
- **Acciones:** El agente elige entre 4 movimientos diagonales.
- **Recompensas:**
  -  **+25** por encontrar la comida.
  -  **-300** por chocar con el enemigo.
  -  **-1** por cada movimiento sin recompensa.
- **Fin de episodio:** Al encontrar comida, chocar con enemigo o alcanzar el límite de pasos.
- **Visualización:** Cada cierto número de episodios se muestra una ventana gráfica con los blobs en la cuadrícula.

---

##  Cómo usar

### 1. Preparar entorno virtual

```bash
```bash
# Entrar a la carpeta
cd blob_game

# Crear entorno virtual 
py -3.10 -m venv venv_blob

# Activar entorno en Windows
venv_blob\Scripts\activate

# Activar entorno en Linux/MacOS
source venv_blob/bin/activate
```

### 2. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 3. Ejecutar entrenamiento

```bash
python qlearning_blob.py
```

---

##  Salidas del proyecto

- **Tabla Q:** Se guarda automáticamente en `qtable_backups/` con timestamp.
- **Gráfica de recompensas:** Curva de recompensa promedio móvil al finalizar el entrenamiento.
- **Visualización en tiempo real:** Ventana gráfica mostrando el progreso del agente.

---

##  Estructura interna

- **Clase `Blob`:** Maneja posición y movimiento de los objetos en la cuadrícula.
- **Entrenamiento:** Controla episodios, actualización de la tabla Q y visualización.
- **Recompensas y penalizaciones:** Guían el aprendizaje hacia la estrategia óptima.

---

##  Posibles mejoras futuras

- Implementar redes neuronales para aproximar la tabla Q (*Deep Q-Learning*).
- Aumentar tamaño y complejidad del entorno.
- Añadir múltiples enemigos y tipos de comida con diferentes recompensas.
- Optimizar la visualización para mejorar rendimiento.
- Guardar y cargar modelos entrenados para evaluación.

---

##  Créditos

Desarrollado por **Jose Ricardo Salas Castañon**  
Estudiante de Ingeniería en Mecatrónica, especialidad en Robótica  
Centro de Enseñanza Técnica Industrial, Guadalajara, México

---