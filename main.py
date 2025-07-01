import pygame as pg
from gamestate import GameState

model = None
try: 
    from stable_baselines3 import PPO 
    model = PPO.load("trained_model") 
    print("RL model found. Prepare for Games")
except: 
    print("No RL Model Found. Prepare for Default Games")

def run(): 
    pg.init() 
    width, height = 900, 600 
    screen = pg.display.set_mode((width, height))
    pg.display.set_caption("Catch the Cursor")
    clock = pg.time.Clock()

    # Initialize game state
    gameState = GameState(width, height, model=model)
    running = True

    while running:
        screen.fill((30,30,30))

        # Stop game look if user has quit
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            
        # Update game state
        gameState.update()
        
        # Draw current game state
        gameState.draw(screen)

        pg.display.flip()
        clock.tick(60)

    pg.quit()

if __name__=="__main__":
    run()