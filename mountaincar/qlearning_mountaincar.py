import gym
import numpy as np
import matplotlib.pyplot as plt
import yaml
import os
import warnings

# Ignorar warnings molestos
warnings.filterwarnings("ignore", category=DeprecationWarning)
warnings.filterwarnings("ignore", category=UserWarning)

# 1. Cargar configuración
with open("config.yaml", "r") as f:
    config = yaml.safe_load(f)

# 2. Inicializar entorno
env = gym.make("MountainCar-v0")

# 3. Discretización del espacio de estados
DISCRETE_OS_SIZE = [config["discrete_size"]] * len(env.observation_space.high)
discrete_os_win_size = (env.observation_space.high - env.observation_space.low) / DISCRETE_OS_SIZE

def get_discrete_state(state):
    return tuple(((state - env.observation_space.low) / discrete_os_win_size).astype(int))

# 4. Inicializar Q-table
q_table = np.random.uniform(
    low=config["qtable_init_low"],
    high=config["qtable_init_high"],
    size=(DISCRETE_OS_SIZE + [env.action_space.n])
)

# 5. Epsilon-greedy
epsilon = config["epsilon_start"]
epsilon_decay_value = epsilon / (config["end_epsilon_decay"] - config["start_epsilon_decay"])

# 6. Métricas
ep_rewards = []
aggr_ep_rewards = {'ep': [], 'avg': [], 'max': [], 'min': []}

# 7. Entrenamiento
os.makedirs("qtables", exist_ok=True)
os.makedirs("plots", exist_ok=True)

for episode in range(config["episodes"]):
    state = env.reset()
    discrete_state = get_discrete_state(state)
    done = False
    episode_reward = 0
    
    while not done:
        if episode % config["show_every"] == 0:
            env.render()
        
        if np.random.random() > epsilon:
            action = np.argmax(q_table[discrete_state])
        else:
            action = np.random.randint(0, env.action_space.n)
        
        new_state, reward, done, _ = env.step(action)
        new_discrete_state = get_discrete_state(new_state)
        
        if done and new_state[0] >= env.unwrapped.goal_position:
            reward = 0
        else:
            reward = -1
        
        if not done:
            max_future_q = np.max(q_table[new_discrete_state])
            current_q = q_table[discrete_state + (action,)]
            new_q = (1 - config["learning_rate"]) * current_q + \
                    config["learning_rate"] * (reward + config["discount"] * max_future_q)
            q_table[discrete_state + (action,)] = new_q
        
        discrete_state = new_discrete_state
        episode_reward += reward

    # Guardar tabla cada 1000 episodios
    if episode % 100 == 0:
        ruta = f"qtables/{episode}-qtable.npy"
        np.save(ruta, q_table)
    
    # Decaimiento de epsilon
    if config["end_epsilon_decay"] >= episode >= config["start_epsilon_decay"]:
        epsilon = max(0.01, epsilon - epsilon_decay_value)

    # Métricas
    ep_rewards.append(episode_reward)
    if episode % config["stats_every"] == 0:
        avg_reward = np.mean(ep_rewards[-config["stats_every"]:])
        aggr_ep_rewards['ep'].append(episode)
        aggr_ep_rewards['avg'].append(avg_reward)
        aggr_ep_rewards['max'].append(np.max(ep_rewards[-config["stats_every"]:]))
        aggr_ep_rewards['min'].append(np.min(ep_rewards[-config["stats_every"]:]))
        print(f"Episodio: {episode:5d} | Recompensa: {avg_reward:7.2f} | Epsilon: {epsilon:.2f}")

# 8. Guardar tabla final
np.save("qtables/qtable_final.npy", q_table)

# 9. Gráfica de entrenamiento
plt.figure(figsize=(10, 5))
plt.plot(aggr_ep_rewards['ep'], aggr_ep_rewards['avg'], label="Promedio")
plt.plot(aggr_ep_rewards['ep'], aggr_ep_rewards['max'], label="Máximo")
plt.plot(aggr_ep_rewards['ep'], aggr_ep_rewards['min'], label="Mínimo")
plt.title("Progreso de Entrenamiento")
plt.xlabel("Episodios")
plt.ylabel("Recompensa")
plt.legend()
plt.savefig("plots/rewards.png")
plt.show()

env.close()
