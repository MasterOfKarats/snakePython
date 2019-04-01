import pygame
import random

apple_Height = 20
apple_Width = 20
x_pos = 0
x_pos2 = 0
apples = []
y_pos = 0
y_pos2 = 0

class Apple:
    def _init_(self):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.display = display
        self.randomize()
    #randomizes the location of the apple
    def randomize(self):
        GameWidth = 480
        GameHeight = 480
        self.x_pos =random.randint(50,450)
        self.y_pos = random.randint(50, 450)


    #returns the X location
    def getX(self):
        return self.x_pos
    #returns Y location
    def getY(self):
        return self.y_pos
    #draws apple and returns the rectangle object of the apple
    def draw(self, display):
        apple = pygame.draw.rect(display, (148, 195, 134), (self.x_pos,self.y_pos,apple_Width,apple_Height))
        pygame.display.update()
        return apple
