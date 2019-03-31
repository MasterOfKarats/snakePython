def moveSnake(changeX, changeY):
    x_pos = 0
    y_pos = 0
    x_pos += changeX
    y_pos += changeY

def grow():
    snakeWidth=0
    snakeWidth += 10

def getX():
    x=0
    return x

def getY():
    y=0
    return y

def check_Collision(startX, startY):
    GameWidth = 500
    GameHeight = 500
    x_pos=0
    y_pos=0
    if(x_pos < 0 or y_pos < 0 or x_pos > GameWidth or y_pos > GameHeight):
        y_pos = startX
        x_pos = startY