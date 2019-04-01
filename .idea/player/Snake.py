import pygame
import Apple
import random



snakeHeight = 20
snakeWidth = 20
x_pos = 250
score = 0
y_pos = 250
pos = []
count = 0

class Snake:
    def _init_(self, display):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.count = count
        self.snakeWidth = snakeWidth
        self.snakeHeight = snakeHeight
        self.display = display
        self.pos = pos
        Snake.check_Collision()
    def draw(self, display):
        rectangle = pygame.draw.rect(display, (189, 139, 196), (self.x_pos,self.y_pos,self.snakeWidth,self.snakeHeight))
        return rectangle

    def moveSnake(self, changeX, changeY):
        self.pos.append((self.x_pos,self.y_pos))
        count = len(self.pos)
        self.x_pos += changeX
        self.y_pos += changeY
        pygame.display.update()
    def counting(self):
        return self.count
    def drawBody(self,display,score):
        for x in self.pos:
            rectangle = pygame.draw.rect(display, (189, 139, 196), (x[0],x[1],self.snakeWidth,self.snakeHeight))
        max = score * snakeWidth
        if len(self.pos) > max:
            self.pos.remove(self.pos[0])
        else:
            self.pos.append((self.x_pos,self.y_pos))
        pygame.display.update()


    def getX(self):
        return self.x_pos
    def getY(self):
        return self.y_pos
    def returnPos(self):
        return self.pos

    def collisionWithSelf(self,startX, startY):
        if(len(self.pos) >= 1):
            snake_head = self.pos[0]
            if snake_head[0] in self.pos[1:][0] and snake_head[1] in self.pos[1:][1]:
                return True
            else:
                return False

    def check_Collision(self, startX, startY):
        GameWidth = 500
        collision = False
        GameHeight = 500
        if(self.x_pos < 0 or self.y_pos < 0 or self.x_pos > GameWidth- 20 or self.y_pos > GameHeight - 20):
            self.y_pos = startX
            self.x_pos = startY
            del self.pos[:]
            return True
