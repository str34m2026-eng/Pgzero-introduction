import pgzrun
import random

WIDTH=500
HEIGHT=500

def draw():
    while True:
    
            R=random.randint(0,255)
            G=random.randint(0,255)
            B=random.randint(0,255)
            R1=random.randint(0,255)
            G1=random.randint(0,255)
            B1=random.randint(0,255)
            R2=random.randint(0,255)
            G2=random.randint(0,255)
            B2=random.randint(0,255)
            
            A1=(R,G,B)
            A2=(R1,G1,B1)
            A3=(R2,G2,B2)
            
            screen.draw.filled_circle((250,250),250,A1)
            
            screen.draw.filled_circle((166,150),40,A3)
            screen.draw.filled_circle((332,150),40,A3)
            screen.draw.filled_circle((166,150),20,A2)
            screen.draw.filled_circle((332,150),20,A2)
            screen.draw.filled_circle((250,360),130,A2)
            screen.draw.filled_circle((250,300),130,A1)
            screen.draw.text("HELPME",center=(250,250),color="#EC2E2E",fontsize=50)
            screen.draw.text("EMPLEH",center=(250,280),color="#EC2E2E",fontsize=50)
    



    
    
    

pgzrun.go()
    
    
