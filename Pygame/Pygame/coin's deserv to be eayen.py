from random inport randint
WIDTH = 400
HEIGHT = 400
score = 0
game_over = False

Fox=Actor("Samual-mander")
fox.pos = 100,100

coin = actor("New Piskel")
coin.pos = 200, 200



def draw():
    screen.fill("gray")
    fox.draw()
    coin.draw()
    screen.draw.text("score:"+str(score, color="black", topleft=(10, 10

    if game_over:
        screen.fill("pink")
        screen.daw.text("Final Score: " + str(score), topleft(10,10), fontsize =60)



def place_coin():
    coin.x = randint(20, (WIDTH - 20))
    coin.y = randint(20, (HIGHT -20))


def time_up():
    global game_over
    game_over = true


def update():
    global score

    if keyboard.left:
        fox.x=fox.x-4
    elif keyboard.right:
        fox.x = fox.x + 4
    elif keyboard.up:
        fox.y= fox.y - 4
    elif keyboard.down:
        fox.y = fox.y + 4

    coin_collected = fox. colliderect(coin)

    if coin_collected:
        score= score +10
        place_coin()

clock.schedule(time_up, 15.0)
place_coin



