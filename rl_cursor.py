import math 
from cursor import Cursor 

class RLAgentCursor(Cursor): 
    def __init__(self, *args, model=None, **kwargs):
        super().__init__(*args, **kwargs)
        self.model = model 

    def step(self, obs):
        if self.model:
            action, _ = self.model.predict(obs, deterministic=True)
            self.apply_action(action, obs)
        else:
            self.move_cursor(obs)
    
    def apply_action(self, action, obs):
        target_x = obs[2] * self.window_width
        target_y = obs[3] * self.window_height
        dx = self.x - target_x
        dy = self.y - target_y
        base_angle = math.atan2(dy, dx)

        angle = base_angle + action[0] * 0.5
        self.x += self.cursor_speed * math.cos(angle)
        self.y += self.cursor_speed * math.sin(angle)
        self.clamp_to_window()
