import pygame as pg
from cursor import Cursor

(width, height) = (1000, 700)
screen = pg.display.set_mode((width, height))

pg.display.set_caption("Catch The Cursor")
background_colour = (255, 255, 255)
screen.fill(background_colour)

# Draw a circle in the middle of the screen
cursor = Cursor(screen, 150, 50, 15)
cursor.display()

pg.display.flip()

running = True
while running:
  for event in pg.event.get():
    if event.type == pg.QUIT:
      running = False