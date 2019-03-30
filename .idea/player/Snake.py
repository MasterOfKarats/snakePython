import pygame
import Apple



snakeHeight = 20
snakeWidth = 20
x_pos = 250
score = 0
y_pos = 250

class Snake:
    def _init_(self, display):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.display = win
        Snake.check_Collision()
    def draw(self, display):
        pygame.draw.rect(display, (255,0,0), (self.x_pos,self.y_pos,snakeWidth,snakeHeight))
        rectangle = pygame.draw.rect(display, (255,0,0), (self.x_pos,self.y_pos,snakeWidth,snakeHeight))
        pygame.display.update()
    def moveSnake(self, changeX, changeY):
        self.x_pos += changeX
        self.y_pos += changeY
    def grow(self):
        pass
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
            score += 1
            print(score)
            app = Apple.Apple.draw(Apple,display)