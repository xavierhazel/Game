WIDTH = 300
HIGHT = 300


def draw():
    screen.fill((15, 56, 36))
    screen.clear()
    marsh.draw()


marsh = Actor("smore")
marsh.pos = 100, 50
marsh.topright = 0, 10
WIDTH = 500
HEIGHT = marsh.hight + 20


def update():
    marsh.left += 2
    if marsh.left > WIDTH:
        marsh.right = 0


def on_mouse_down(pos):
    print("tu clique")
    if marsh.collidepoint(pos):
        sounds.eep.play()
        marsh.image = "mallo"
        time.sleep(1)
        marsh.image = "smore"
        set_marsh_hurt
    if button == mouse.LEFT and marsh.collidepoint(pos):
        print("sacra bleu")
    else:
        print("tu manque moi!!")


def set_marsh_hurt(pos):
    marsh.image = "mallo"
    sounds.eep.play()
    clock.schedule_unique(set_marsh_normal, 1.0)


def set_marsh_normal():
    marsh.image = "smore"
