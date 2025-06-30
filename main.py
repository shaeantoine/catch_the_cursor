import pygame as pg

(width, height) = (1000, 700)
screen = pg.display.set_mode((width, height))
pg.display.set_caption("Catch The Cursor")
pg.display.flip()

running = True
while running:
  for event in pg.event.get():
    if event.type == pg.QUIT:
      running = False