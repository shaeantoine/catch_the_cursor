from gameenv import GameEnv
from stable_baselines3 import PPO

env = GameEnv()
model = PPO("MlpPolicy", env, verbose=1)
model.learn(total_timesteps=10_000_000)

model.save("trained_model")
