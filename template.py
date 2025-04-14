import pygame


pygame.init()

SPRITE_SIZE = 96

size = (SPRITE_SIZE*8, SPRITE_SIZE*8)
screen = pygame.display.set_mode(size, 0)

screen.fill(0)


def main():
    running = True  

    while(running):

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    running = False


        pygame.display.update()

if (__name__ == "__main__"):
    main()