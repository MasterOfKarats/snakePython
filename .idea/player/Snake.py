import pygame
import Apple
import random



snakeHeight = 20
snakeWidth = 20
x_pos = 250
score = 0
y_pos = 250
pos = []

class Snake:
    def _init_(self, display):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.snakeWidth = snakeWidth
        self.snakeHeight = snakeHeight
        self.display = display
        self.pos = []
        Snake.check_Collision()
    def draw(self, display):
        rectangle = pygame.draw.rect(display, (189, 139, 196), (self.x_pos,self.y_pos,self.snakeWidth,self.snakeHeight))
        return rectangle

    def moveSnake(self, changeX, changeY):
        self.pos.append((self.x_pos,self.y_pos))
        self.x_pos += changeX
        self.y_pos += changeY

    def drawBody(self,display):
        for x in self.pos:
            rectangle = pygame.draw.rect(display, (189, 139, 196), (x[0],x[1],self.snakeWidth,self.snakeHeight))
            pygame.display.update()

    def grow(self, score):
        if len(self.pos) > score:
            self.pos.remove(self.pos[0])
        else:
            self.pos.append((self.x_pos,self.y_pos))
    def headPos(self):
        return self.pos[0]
    def tailPos(self):
        pass

    def getX(self):
        return self.x_pos
    def getY(self):
        return self.y_pos

    def check_Collision(self, startX, startY):
        GameWidth = 500
        collision = False
        GameHeight = 500
        if(self.x_pos < 0 or self.y_pos < 0 or self.x_pos > GameWidth or self.y_pos > GameHeight):
            self.y_pos = startX
            self.x_pos = startY
            return True
