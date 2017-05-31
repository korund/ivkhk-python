import sys, pygame

pygame.init()

#setting enviroment
clock = pygame.time.Clock()
clockTick = 200
size = width, height = 640, 480
screen = pygame.display.set_mode(size)

#setting colors
black = 0, 0, 0
white = 255, 255, 255
gray = 128, 128, 128
green = 0, 240, 0
blue = 0, 0, 240
#setting fonts
lifeFont = pygame.font.SysFont("monospace", 16, True)
endFont = pygame.font.SysFont("monospace", 64, True)

#setting initial game values
levelInit = 1
lifeInit = 3

#setting ball
ballSize = 20, 20
ball = pygame.Surface(ballSize)
pygame.draw.ellipse(ball, white, ball.get_rect())
ballRectInit = pygame.Rect((width/2, height/2), ballSize)

#setting platform
padSize = padWidth, padHeight = 80, 10
paddle = pygame.Surface(padSize)
pygame.draw.rect(paddle, green, paddle.get_rect())
padRect = pygame.Rect(((width-padWidth)/2, height-padHeight-50), padSize)

#main game function. may be cycled
def main():
    #setting game variables to its initial values
    ballRect = ballRectInit
    level = levelInit
    life = lifeInit
    speed = [level, level]

    #setting "life" label
    lifeMsg = "Life left: " + str(life-1)
    lifeLabel = lifeFont.render(lifeMsg, 1, white)

    #setting array of targets
    trgRow = 5
    trgCol = 10
    trgMinX = 100
    trgRowTres = 10
    trgSize = trgWidth, trgHeight = 40, 20
    target = pygame.Surface(trgSize)
    pygame.draw.rect(target, blue, target.get_rect())
    trgRect = pygame.Rect((width/(trgCol*2), trgMinX), trgSize)
    trgRectArray = list()
    for row in range(trgRow):
        for col in range(trgCol):
            trgRectArray.append(pygame.Rect(((0.5+col)*width/trgCol-0.5*trgWidth, \
                                             trgMinX+(trgHeight+trgRowTres)*row),trgSize))
    #game cycle
    while True:
        clock.tick(clockTick)
        #catch events of mouse and quit button
        for event in pygame.event.get():
            if event.type == pygame.MOUSEMOTION: 
                if event.__dict__["pos"][0] >= padWidth/2 and event.__dict__["pos"][0] <= width-padWidth/2:
                    padRect.centerx = event.__dict__["pos"][0]
            if event.type == pygame.QUIT: sys.exit()
        
        ballRect = ballRect.move(speed)
        #ball reflect borders
        if ballRect.left < 0 or ballRect.right > width:
            speed[0] = -speed[0]
        if ballRect.top < 0:
            speed[1] = -speed[1]
        #ball reflect paddle
        if ballRect.colliderect(padRect):
            speed[1] = -speed[1]
        #delete element on collide and change direction
        for item in trgRectArray:
            if ballRect.colliderect(item):
                trgRectArray.remove(item)
                speed[1] = -speed[1]

        #win condition
        if len(trgRectArray) == 0:
            winLabel = endFont.render("YOU WON", 1, white)
            screen.blit(winLabel, (0.5*(width-winLabel.get_rect().width), \
                                   0.5*(height-winLabel.get_rect().height)))
            pygame.display.flip()
            break
        
        #loose condition
        if ballRect.bottom > height:
            life -= 1
            lifeMsg = "Life left: " + str(life-1)
            lifeLabel = lifeFont.render(lifeMsg, 1, white)
            #change life icon HERE
            if life != 0:
                ballRect = ballRectInit
            else:
                looseLabel = endFont.render("YOU LOST", 1, white)
                screen.blit(looseLabel, (0.5*(width-looseLabel.get_rect().width), \
                                         0.5*(height-looseLabel.get_rect().height)))
                pygame.display.flip()
                break
        
        #drawing
        screen.fill(black)
        for i in range(len(trgRectArray)):
            screen.blit(target, trgRectArray[i])
        screen.blit(paddle, padRect)
        screen.blit(ball, ballRect)
        screen.blit(lifeLabel, (0.97*width-lifeLabel.get_rect().width, 20))
        pygame.display.flip()

if __name__ == "__main__":
    main()
