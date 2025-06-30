# Catch the Cursor 

This repo houses a very basic game designed at implementing and exploring a novel RL engine. 

## What is the Game? 
You're tasked with "catching" the cursor, that is moving your mouse to a close enough proximity to the cursor . If you get close enough you'll earn a point which is tallied in the top left hand corner of the screen. 

## Where's the Novelty? 
Each time the game loads, the computer engine is like a new born baby. It has no idea what it's doing. It's learning movement for the very first time and isn't following any predefined movement algorithms. It is however, outfitted with a RL feedback mechanism. This mechanism gives the model a strong negative signal each time it is "caught". 

## What's the Point? 
The purpose of this project is to create a RL model which within a single session and without much time can learn to never get caught. In other words make a RL model learn to go from 0->100 in as short of a time as possible (and avoid any cheats!).