import gymnasium as gym
from gymnasium import spaces
import numpy as np
import math
import random

class GameEnv(gym.Env):
    def __init__(self, width=900, height=600):
        super().__init__()
        self.width = width
        self.height = height
        self.cursor_radius = 20
        self.cursor_speed = 5

        # Action space: continuous [dx, dy], each ∈ [-1, 1]
        self.action_space = spaces.Box(low=-1, high=1, shape=(2,), dtype=np.float32)

        # Observation space: [cx, cy, px, py, dist]
        self.observation_space = spaces.Box(low=0, high=1, shape=(5,), dtype=np.float32)

        self.reset()

    def reset(self, seed=None, options=None):
        super().reset(seed=seed)
        self.cursor_x = random.uniform(self.cursor_radius, self.width - self.cursor_radius)
        self.cursor_y = random.uniform(self.cursor_radius, self.height - self.cursor_radius)
        self.player_x = random.uniform(0, self.width)
        self.player_y = random.uniform(0, self.height)
        self.steps_alive = 0
        self.done = False
        return self._get_obs(), {}

    def step(self, action):
        # Apply action (dx, dy)
        dx, dy = action
        self.cursor_x += dx * self.cursor_speed
        self.cursor_y += dy * self.cursor_speed

        self._clamp_cursor()

        # Simulate player cursor chasing the fake one (for training purposes)
        self._simulate_player_movement()

        # Check if caught
        dist = self._distance()
        self.steps_alive += 1
        reward = 1.0  # survive = +1 per frame
        terminated = False

        if dist < self.cursor_radius:
            reward = -100.0
            terminated = True

        truncated = self.steps_alive >= 1000  # End after 1000 steps
        self.done = terminated or truncated

        return self._get_obs(), reward, terminated, truncated, {}

    def render(self):
        pass  # You can implement this later for debugging

    def _clamp_cursor(self):
        self.cursor_x = max(self.cursor_radius, min(self.width - self.cursor_radius, self.cursor_x))
        self.cursor_y = max(self.cursor_radius, min(self.height - self.cursor_radius, self.cursor_y))

    def _distance(self):
        dx = self.cursor_x - self.player_x
        dy = self.cursor_y - self.player_y
        return math.hypot(dx, dy)

    def _simulate_player_movement(self):
        # Player moves toward cursor (basic chasing AI)
        dx = self.cursor_x - self.player_x
        dy = self.cursor_y - self.player_y
        angle = math.atan2(dy, dx)
        speed = 6  # player cursor speed
        self.player_x += speed * math.cos(angle)
        self.player_y += speed * math.sin(angle)

    def _get_obs(self):
        dist = self._distance()
        return np.array([
            self.cursor_x / self.width,
            self.cursor_y / self.height,
            self.player_x / self.width,
            self.player_y / self.height,
            dist / (self.width + self.height)
        ], dtype=np.float32)
