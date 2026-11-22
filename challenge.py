import pgzrun
import random

WIDTH=500
HEIGHT=500


def draw():
    radius=250
    for i in range(100):
      r=random.randint(0,255)
      g=random.randint(0,255)
      b=random.randint(0,255)
      screen.draw.filled_circle((250,250),radius,(r,g,b))
      radius=radius-5

pgzrun.go()