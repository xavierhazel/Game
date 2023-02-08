
marsh=Actor('mallo')
marsh.pos= 10,50

WIDTH = 300
HEIGHT= 300

def draw():
    screen.fill((128,0,0))
    marsh.draw()


def update():
    marsh.left +=2
    if marsh.left > WIDTH:
       marsh.right=0

marsh.topright= 0,10

    def on_mouse_down(pos):
        if marsh.collidepoint(pos):
        else:
            pring("tu manque moi!")
    def on_mouse_down():
        print("tu clique")

