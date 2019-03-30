import pygame
import Snake, Apple
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

class Game:
    def __init__(self, display):
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
                win.fill((0, 0, 0))
                #draws apple and snake
                snake_rect = Snake.Snake.draw(Snake, win)
                apple_rect = Apple.Apple.draw(Apple, win)
                #Snake eats apple
                if Snake.Snake.getX(Snake) ==Apple.Apple.getX(Apple) or Snake.Snake.getY(Snake) == Apple.Apple.getY(Apple):
                    Apple.Apple.randomize(Apple)
                    score += 1
                    print(score)
                    app = Apple.Apple.draw(Apple,win)

        pygame.quit()
        clock.tick(30)


Game.loop(Game)