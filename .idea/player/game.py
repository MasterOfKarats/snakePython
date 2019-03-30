import pygame
import sys
pygame.init()

screenWidth = 500
screenHeight = 500
player = 0

win = pygame.display.set_mode((screenHeight, screenWidth))
pygame.display.set_caption("Snake Game")

class Game:
    def __init__(self):
        self.rectangle = Player.snake(win,20,20)
        run = True
        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run =False
            self.moveR(self.rectangle)
        pygame.quit()
    def moveR(obj):
        for event in pygame.event.get():
            key = pygame.key.get_pressed()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    obj.move(-1,0)
                if event.key == pygame.K_RIGHT:
                    obj.move(1,0)
                if event.key == pygame.K_UP:
                    obj.move(0,1)
                if event.key == pygame.K_DOWN:
                    obj.move(0,-1)

class Player:
    def snake(back,x,y):
        rectangle = pygame.draw.rect(back, (255,0,0), (x,y,20,20))
        pygame.display.update()


Game.__init__(Game)