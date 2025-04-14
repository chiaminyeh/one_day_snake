import pygame
import random
from pygame import time as t

START_LENGTH = 3
COOLDOWN = 200

class Snake():
    def __init__(self,x,y) -> None:
        self.type = 'player'
        self.name = 'greensquare'
        self.x = x
        self.y = y
        self.point = 0

    def move(self,direction):
            if direction == "up":
                self.y -=1
            if direction == "down":
                self.y +=1
            if direction == "left":
                self.x -=1
            if direction == "right":
                self.x +=1
        

class Body():
    def __init__(self,x,y,turns) -> None:
        self.type = 'body'
        self.name = 'bluesquare'
        self.x = x
        self.y = y
        self.turns = turns

class Food():
    def __init__(self,x,y) -> None:
        self.type = "food"
        self.name = "strawberry"
        self.x = x
        self.y = y


def checks(scene):
    player = scene[0]
    found = False

    for obj in scene:
        if obj .type == 'food':
            found = True
    
    if not found:
        x = random.randint(1,14)
        y = random.randint(1,14)
        for obj in scene:
            if obj.x != x and obj.y != y:
                scene.append(Food(x,y))
                break

    for obj in scene:
        if player.x == obj.x and player.y == obj.y:
            if obj.type == 'food':
                scene.remove(obj)
                player.point+=1
            elif obj.type == 'body':

                print('crushed on body gameover')
                return False
    
    if player.x < 1 or player.x > 14 or player.y < 1 or player.y > 14:
        print('gameover')
        return False

    return True


def sceneIsDraw(scene, scale = (48,48)):
    for object in scene:
        image = pygame.image.load('Sprites/' + object.name + ".png")
        image = pygame.transform.scale(image, scale)
        screen.blit(image, (object.x*scale[0], object.y*scale[1]))


pygame.init()

SPRITE_SIZE = 96

size = (SPRITE_SIZE*8, SPRITE_SIZE*8)
screen = pygame.display.set_mode(size, 0)


def main():
    running = True  
    run = True
    scene = []

    scene.append(Snake(8,7))
    scene.append(Body(8,6,3))
    scene.append(Body(8,5,2))
    scene.append(Body(8,4,1))
    player = scene[0]
    previous1 = t.get_ticks()
    previous2 = t.get_ticks()
    direction = "down"

    # show points
    font = pygame.font.Font('freesansbold.ttf', 32)
    text = font.render(str(player.point), True,(0,255,0))
    textRect = text.get_rect()
    # set the center of the rectangular object.
    textRect.center = (20, 20)
    screen.blit(text, textRect)
    

    while(running):
        now1 = t.get_ticks()
        now2 = t.get_ticks()
        
        screen.fill(0)
        pygame.draw.rect(screen,(50,50,50),(48,48,672,672))
        text = font.render(str(player.point), True,(0,255,0))
        screen.blit(text, textRect)

        if run:
            run = checks(scene) 
            sceneIsDraw(scene)
        else:
            text2 = font.render('GAME OVER', True,(0,255,0))
            textRect2 = text2.get_rect()
            textRect2.center = (400, 400)
            screen.blit(text2, textRect2)

            text3 = font.render('press r to restart', True,(0,255,0))
            textRect3 = text3.get_rect()
            textRect3.center = (400, 500)
            screen.blit(text3, textRect3)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    running = False
                if event.key == pygame.K_w:
                    if(now2 - previous2 > COOLDOWN):
                        if direction != 'down':
                            direction = 'up'
                        previous2 = now2
                if event.key == pygame.K_s:
                    if(now2 - previous2 > COOLDOWN):
                        if direction != 'up':
                            direction = 'down'
                        previous2 = now2
                if event.key == pygame.K_a:
                    if(now2 - previous2 > COOLDOWN):
                        if direction != 'right':
                            direction = 'left'
                        previous2 = now2
                if event.key == pygame.K_d:
                    if(now2 - previous2 > COOLDOWN):
                        if direction != 'left':
                            direction = 'right'
                        previous2 = now2
                if event.key == pygame.K_r:
                    for i in range(len(scene)):
                        scene.pop()

                    scene.append(Snake(8,7))
                    scene.append(Body(8,6,3))
                    scene.append(Body(8,5,2))
                    scene.append(Body(8,4,1))
                    player = scene[0]
                    direction = 'down'
                    run = True
                    
        
        if(now1 - previous1 > COOLDOWN):
            x = player.x
            y = player.y
            player.move(direction)
            scene.append(Body(x,y,player.point+START_LENGTH))

            for obj in scene:
                if obj.type == 'body':
                    obj.turns -=1
                    if obj.turns <=0:
                        scene.remove(obj)

            previous1 = now1

        pygame.display.update()

if (__name__ == "__main__"):
    main()