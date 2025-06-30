import pygame as pg

(width, height) = (1000, 700)
screen = pg.display.set_mode((width, height))

pg.display.set_caption("Catch The Cursor")
background_colour = (255, 255, 255)
screen.fill(background_colour)

# Draw a circle in the middle of the screen
class Particle: 
    def __init__(self, x, y, size): 
        self.x = x
        self.y = y
        self.size = size 
        self.colour = (0,0,255)
        self.thickness = 2

    def display(self): 
        pg.draw.circle(screen, self.colour, (self.x, self.y), self.size, self.thickness)

particle = Particle(150,50,15)
particle.display()

pg.display.flip()

running = True
while running:
  for event in pg.event.get():
    if event.type == pg.QUIT:
      running = False