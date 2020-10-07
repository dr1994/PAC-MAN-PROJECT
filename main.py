#Pacman Ghost Algorithm - www.101computing.net/pacman-ghost-algorithm/
from math import atan, cos, sin
from processing import *

WIDTH=500
HEIGHT=500
pacman_X = 30
pacman_Y = 30
delay = 5 

ghost_X = 100
ghost_Y = 100

def setup():
    strokeWeight(3)
    frameRate(100)
    size(500,500)

def moveGhost():    
  global ghost_X,ghost_Y,pacman_X,pacman_Y
  fill(255,255,255)
  stroke(0,0,0)
  
  #Find out the direction (angle) the Ghost needs to move towards
  #Using SOH-CAH-TOA trignometic rations
  opposite=pacman_Y-ghost_Y
  adjacent=pacman_X-ghost_X
  angle = atan(opposite/adjacent)
  if ghost_X>pacman_X:
    angle=angle+500
  
  #Use this angle to calculate the velocity vector of the Ghost
  #Once again using SOH-CAH-TOA trignometic rations
  velocity=3 #pixels per frame
  
  vx = velocity * cos(angle)
  vy = velocity * sin(angle)
  
  #Apply velocity vector to the Ghost coordinates to move/translate the ghost
  ghost_X = ghost_X + vx
  ghost_Y = ghost_Y + vy
  
  #Draw Ghost  
  ellipse( ghost_X,ghost_Y,8,8)
    
def movePacman():
    global pacman_X, pacman_Y

    fill(0,0,0)
    stroke(255,255,255)
    fc = environment.frameCount

    #Pacman follows the mouse cursor
    pacman_X += (mouse.x-pacman_X)/delay;
    pacman_Y += (mouse.y-pacman_Y)/delay;
    
    #Draw Pacman
    ellipse(pacman_X,pacman_Y,40,40)

def playGame():
  background(255,255,255)
  movePacman()
  moveGhost()

draw = playGame
run()
