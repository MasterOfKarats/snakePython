import pygame
import Snake, Apple
import sys
pygame.font.init()
pygame.init()

pos = []
score = 0
speed = 10
snakeHeight = 20
snakeWidth = 20
changeX = 0
changeY = 0
x_pos = 20
y_pos = 20
screenWidth = 500
screenHeight = 500
player = 0

win = pygame.display.set_mode((screenHeight, screenWidth))
pygame.display.set_caption("Snake Game")
clock = pygame.time.Clock()
pygame.font.init()
font = pygame.font.SysFont("comicsansms", 30)
title = font.render("Snake Game", True, (74, 88, 112))




class Game:
    def _init_(self, display):
        self.display = win
    def loop(self):
        global changeX, changeY, score
        run = True
        #game loop
        while run:
            #runs the game
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run =False
                #moves the snake which is the red squarw
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        changeX -= speed
                        changeY = 0
                    elif event.key == pygame.K_RIGHT:
                        changeX += speed
                        changeY = 0
                    elif event.key == pygame.K_UP:
                        changeX = 0
                        changeY -= speed
                    elif event.key == pygame.K_DOWN:
                        changeX = 0
                        changeY += speed
                #Moves snake and checks for collision
                Snake.Snake.moveSnake(Snake, changeX, changeY)
                Snake.Snake.check_Collision(Snake, x_pos , y_pos)
                #draws apple and snake
                snake_rect = Snake.Snake.draw(Snake, win)
                apple_rect = Apple.Apple.draw(Apple, win)
                win.fill((182, 175, 183))
                #Snake eats apple
                if apple_rect.colliderect(snake_rect):
                    Apple.Apple.randomize(Apple)
                    Snake.score += 1
                    score = Snake.score
                    print(score)
                text = font.render("Score "+str(score), True, (74, 88, 112))
                win.blit(text, (20 , 450 ))
                win.blit(title, (150,5))

        pygame.display.update()
        pygame.quit()
        clock.tick(30)


Game.loop(Game)