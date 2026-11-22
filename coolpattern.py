import pgzrun
import random
WIDTH=500
HEIGHT=500

def draw():
    w=500
    h=167
   

    screen.fill("#000000")
    for i in range(35):
        r=random.randint(0,255)
        g=random.randint(0,255)
        b=random.randint(0,255)
        a=Rect((250,250),(w,h))
        a.center=(250,250)
        screen.draw.rect(a,(r,g,b))
        w=w-10
        h=h+10
    
pgzrun.go()