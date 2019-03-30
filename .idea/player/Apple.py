import pygame
import random

apple_Height = 20
apple_Width = 20
x_pos = 0
y_pos = 0

class Apple:
    def _init_(self):
        self.x_pos = x_pos
        self.y_pos = x_pos
        self.display = display
        self.randomize()
    def randomize(self):
        GameWidth = 480
        GameHeight = 480
        self.x_pos =random.randint(20,GameHeight)
        self.y_pos = random.randint(20, GameWidth)
    def getX(self):
        return self.x_pos
    def getY(self):
        return self.y_pos

    def draw(self, display):
        apple = pygame.draw.rect(display, (0, 100, 0), (self.x_pos,self.y_pos,apple_Width,apple_Height))
        pygame.display.update()
        return apple
