import pygame

pygame.init()
screen = pygame.display.set_mode((400, 300))
pygame.draw.rect(screen , (0 , 128 , 255), pygame.Rect(30, 30 , 60 , 60))
done = False
is_blue = True
clock = pygame.time.Clock()

while not done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True
                if is_blue: color = (0 ,128, 255)
                else: color = (255, 100, 0)
                pygame.draw.rect(screen , color , pygame.Rect(30 ,30, 60, 60))
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                        is_blue =is_blue
        clock.tick(60)
        pygame.display.flip()

"""
import pygame - this is of course needed to access the PyGame framework.
pygame.init() - This kicks things off. It initializes all the modules required for PyGame.
pygame.display.set_mode((width, height)) - This will launch a window of the desired size. The return value is a Surface object which is the object you will perform graphical operations on. This will be discussed later. 
pygame.event.get() - this empties the event queue. If you do not call this, the windows messages will start to pile up and your game will become unresponsive in the opinion of the operating system. 
pygame.QUIT - This is the event type that is fired when you click on the close button in the corner of the window.
pygame.display.flip() - PyGame is double-buffered. This swaps the buffers. All you need to know is that this call is required in order for any updates that you make to the game screen to become visible."""

