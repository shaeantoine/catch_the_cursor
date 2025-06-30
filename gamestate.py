import math
import pygame as pg
from cursor import Cursor 
from rl_cursor import RLAgentCursor

class GameState: 
    
    # Initialize the game state
    def __init__(self, width, height, model=None):
        self.window_width = width
        self.window_height = height   
        self.font = pg.font.SysFont(None, 36)
        
        self.score = 0
        self.cursor = RLAgentCursor(window_width=width, window_height=height, model=model)

    def update(self):
        obs = self.observe()
        self.cursor.step(obs)

        # Check if caught 
        px, py = obs[2] * self.window_width, obs[3] * self.window_height
        dx = self.cursor.x - px
        dy = self.cursor.y - py
        distance = math.hypot(dx, dy)
        if distance < self.cursor.cursor_radius:
            self.score += 1
            self.cursor.respawn_randomly()

    def draw(self, screen): 
        pg.draw.circle(screen, (200,50,50), self.cursor.get_pos(), self.cursor.cursor_radius)
        pg.draw.circle(screen, (255, 255, 255), self.cursor.get_pos(), 2)

        score_text = self.font.render(f"Score: {self.score}", True, (255,255,255))
        screen.blit(score_text, (10,10))
    
    def observe(self): 
        px, py = pg.mouse.get_pos()
        cx, cy = self.cursor.x, self.cursor.y
        dx = cx - px 
        dy = cy - py
        distance = math.hypot(dx, dy)

        return [
            cx / self.window_width,
            cy / self.window_height,
            px / self.window_width,
            py / self.window_height,
            distance / (self.window_width + self.window_height)
        ] 