import pygame
import Apple
import random



snakeHeight = 20
snakeWidth = 20
x_pos = 250
score = 0
y_pos = 250

class Snake:
    def _init_(self):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.snakeWidth = snakeWidth
        self.snakeHeight = snakeHeight
        self.display = win
        Snake.check_Collision()
    def draw(self, display):
        #197, 164, 232
        rectangle = pygame.draw.rect(display, (150, 131, 170), (self.x_pos,self.y_pos,self.snakeWidth,self.snakeHeight))
        pygame.display.update()
        return rectangle
    def moveSnake(self, changeX, changeY):
        self.x_pos += changeX
        self.y_pos += changeY
    def grow(self):
        self.snakeWidth += 10

    def getX(self):
        return self.x_pos
    def getY(self):
        return self.y_pos
    def check_Collision(self, startX, startY):
        GameWidth = 500
        GameHeight = 500
        if(self.x_pos < 0 or self.y_pos < 0 or self.x_pos > GameWidth or self.y_pos > GameHeight):
            self.y_pos = startX
            self.x_pos = startY
    def eatApple(self, apple, display):
        global score
        if self.x_pos == apple.x_pos or self.y_pos == apple.y_pos:
            Apple.Apple.randomize(Apple)
            Apple.Apple.draw(Apple, display)
            score += 1
            print(score)