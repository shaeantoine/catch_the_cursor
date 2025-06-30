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
    