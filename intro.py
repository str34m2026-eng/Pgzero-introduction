import pgzrun

WIDTH=800
HEIGHT=530

def draw():
    screen.fill("#B0DCE8")
    r=Rect((400,265),(50,50))
    r.center=(400,265)
    screen.draw.rect(r,"#4F2317")
    b=Rect((750,50),(30,100))

    screen.draw.filled_rect(b,"#000000")
pgzrun.go()