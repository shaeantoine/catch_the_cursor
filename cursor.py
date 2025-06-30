import pygame as pg

class Cursor: 
    def __init__(self, screen, x, y, size): 
        self.screen = screen
        self.x = x
        self.y = y
        self.size = size 
        self.colour = (0,0,255)
        self.thickness = 2

    def display(self): 
        pg.draw.circle(self.screen, self.colour, (self.x, self.y), self.size, self.thickness)