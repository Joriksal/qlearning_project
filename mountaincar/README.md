# MountainCar Q-learning

Proyecto de entrenamiento con Q-learning en el entorno MountainCar-v0 de Gym. Incluye entrenamiento, guardado de tablas Q, visualización de resultados y generación de video.

## Requisitos

- Python 3.8+
- Gym
- Numpy
- Matplotlib
- OpenCV (cv2)
- PyYAML

## 1. Crear y activar entorno virtual
```bash
# Entrar a la caprte mountaincar
cd mountaincar

# Crear entorno virtual llamado 'venv_mountaincar'
py -3.10 -m venv venv_mountaincar 

# Activar entorno en Windows
venv_mountaincar\Scripts\activate

# Activar entorno en Linux/MacOS
source venv_mountaincar/bin/activate
```

## 2. Instalar dependencias
```bash
pip install -r requirements.txt
```

## 3. Entrenar con Q-Learning
Asegúrate de tener un archivo de configuración llamado config.yaml en la raíz del proyecto con parámetros como:

```yaml
learning_rate: 0.1
discount: 0.95
episodes: 20000
discrete_size: 40
epsilon_start: 1.0
start_epsilon_decay: 0
end_epsilon_decay: 5000
qtable_init_low: -3
qtable_init_high: 0
stats_every: 1000
show_every: 1000
```

Luego ejecuta el script de entrenamiento:

```bash
python qlearning_mountaincar.py
```

Esto generará:

 - Carpeta qtables/ con la tabla Q final.

 - Carpeta plots/ con un gráfico del progreso del entrenamiento.

## 4. Visualizar comportamiento con la Q-table entrenada
Una vez entrenado el agente y guardada la tabla qtable_final.npy, ejecuta el script de visualización para generar imágenes del comportamiento del agente y luego un video:

```bash
python visualizations.py
```

Esto crea:

- Carpeta qtable_charts/ con imágenes por cada frame.

- Carpeta videos/ con un archivo .mp4 mostrando la evolución del agente.

## 5. Explicación del algoritmo Q-learning y Reinforcement Learning
¿Qué es Reinforcement Learning (Aprendizaje por Refuerzo)?
Es un paradigma de aprendizaje automático donde un agente aprende a tomar decisiones secuenciales en un entorno con el objetivo de maximizar una señal de recompensa acumulada a lo largo del tiempo.

El agente:

- Observa un estado del entorno.

- Elige una acción basada en su política actual.

- Recibe una recompensa y observa un nuevo estado.

- Actualiza su conocimiento para mejorar la política.

### ¿Qué es Q-learning?
Q-learning es un algoritmo de aprendizaje por refuerzo basado en valores. El agente aprende una función Q que estima la utilidad de realizar una acción en un estado dado.

La actualización de la tabla Q se realiza con la fórmula:

    *𝑄(𝑠,𝑎)←𝑄(𝑠,𝑎)+𝛼(𝑟+𝛾max⁡𝑎′𝑄(𝑠′,𝑎′)−𝑄(𝑠,𝑎))*

Donde:

    𝑠: estado actual

    𝑎: acción tomada

    𝑟: recompensa recibida

    𝑠′: nuevo estado

    𝛼: tasa de aprendizaje

    𝛾: factor de descuento para recompensas futuras

### Aplicación en MountainCar
MountainCar es un entorno clásico donde un auto debe aprender a subir una colina. El estado es continuo (posición y velocidad). Se discretiza el espacio para aplicar Q-learning.

El agente aprende a elegir acciones (acelerar izquierda, derecha o sin acción) para alcanzar la cima lo antes posible y maximizar la recompensa acumulada.

## 7. Cómo interpretar los resultados
- El gráfico en plots/rewards.png muestra la recompensa promedio, máxima y mínima por bloques de episodios, indicando progreso del aprendizaje.

- Las imágenes en qtable_charts/ visualizan los valores Q para cada acción y estado discretizado.

- El video en videos/ muestra la evolución del agente aprendiendo a resolver MountainCar.

## 8. Posibles mejoras y extensiones
- Ajustar parámetros en config.yaml para optimizar resultados.

- Implementar Deep Q-Network (DQN) para evitar discretización.

- Añadir visualizaciones interactivas o exportar resultados para web.

- Incorporar métricas adicionales para analizar estabilidad y convergencia.

## 9. Créditos
Desarrollado por Jose Ricardo Salas Castañon
Estudiante de Ingeniería en Mecatrónica en especialidad en robotica en el Centro de Enseñanza Tecnica Industrial en Guadalajara, Jalisco