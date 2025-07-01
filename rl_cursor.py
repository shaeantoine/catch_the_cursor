import math 
from cursor import Cursor 

class RLAgentCursor(Cursor): 
    def __init__(self, *args, model=None, **kwargs):
        super().__init__(*args, **kwargs)
        self.model = model 

    def step(self, obs):
        if self.model:
            action, _ = self.mode.predict(obs, deterministic=True)
            self.apply_action(action)
        else:
            self.move_cursor(obs)
    
    def apply_action(self, action):
        angle = action * 2 * math.pi 
        self.x = self.cursor_speed * math.cos(angle)
        self.x = self.cursor_speed * math.sin(angle)
        self.clamp_to_window()
