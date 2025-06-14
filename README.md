# Q-Learning Project

Este repositorio contiene implementaciones de algoritmos de **Q-learning** aplicados a dos entornos distintos:  
- **MountainCar** (de OpenAI Gym)  
- **Blob Game** (entorno personalizado tipo grid-world)

El objetivo es demostrar el aprendizaje por refuerzo en problemas de control y toma de decisiones.

---

## Estructura del Proyecto

```
qlearning_project/
│
├── blob_game/
│   ├── qlearning_blob.py
│   ├── requirements.txt
│   ├── README.md
│   ├── qtable_backups/
│   └── venv_blobgame/
│
├── mountaincar/
│   ├── qlearning_mountaincar.py
│   ├── visualizations.py
│   ├── config.yaml
│   ├── requirements.txt
│   ├── README.md
│   ├── plots/
│   ├── qtables/
│   ├── qtable_charts/
│   └── videos/
│
├── .gitignore
└── README.md
```

---

## Descripción General

| Entorno      | Descripción                                                                 | Script Principal                                      |
|--------------|-----------------------------------------------------------------------------|-------------------------------------------------------|
| **MountainCar** | Agente aprende a subir una colina usando Q-learning y discretización.        | [`mountaincar/qlearning_mountaincar.py`](mountaincar/qlearning_mountaincar.py) |
| **Blob Game**   | Agente tipo "blob" navega una cuadrícula para buscar comida y evitar enemigos. | [`blob_game/qlearning_blob.py`](blob_game/qlearning_blob.py)                   |

---

## Instalación y Uso

### 1. Clonar el repositorio

```bash
git clone https://github.com/tu_usuario/qlearning_project.git
cd qlearning_project
```

### 2. Crear y activar entornos virtuales

#### MountainCar

```bash
# Entrar a la carpeta
cd mountaincar

# Crear entorno virtual 
py -3.10 -m venv venv_mountaincar 

# Activar entorno en Windows
venv_mountaincar\Scripts\activate

# Activar entorno en Linux/MacOS
source venv_mountaincar/bin/activate
```

#### Blob Game

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

### 3. Ejecutar los scripts de entrenamiento

| Entorno      | Comando de Ejecución                        |
|--------------|---------------------------------------------|
| MountainCar  | `python qlearning_mountaincar.py`           |
| Blob Game    | `python qlearning_blob.py`                  |

---

## Salidas del Proyecto

- **Tablas Q:** Guardadas periódicamente en carpetas específicas para cada entorno.
- **Gráficas de recompensas:** Visualizan el progreso del aprendizaje.
- **Visualizaciones y videos:** Permiten observar la evolución de la política aprendida.

---

## Créditos

Desarrollado por **Jose Ricardo Salas Castañon**  
Estudiante de Ingeniería en Mecatrónica, especialidad en Robótica  
Centro de Enseñanza Técnica Industrial, Guadalajara, México

---

## Licencia

Este proyecto es de uso educativo y libre
