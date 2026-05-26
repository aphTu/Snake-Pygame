import pygame
import random
class Apple():
  def __init__(self, position_x, position_y, apple_scale):
    self.position_x = position_x
    self.position_y = position_y
    self.color = (255, 0, 0)
    self.eaten = False
    self.radius = 50
    self.scale = apple_scale

  def updatePositionX(self, position):
    self.position_x = position

  def updatePositionY(self, position):
    self.position_y = position

  def getPositionX(self):
    return self.position_x
  
  def getPositionY(self):
    return self.position_y
  
  def drawApple(self, screen):
    pygame.draw.circle(screen, self.color, (self.position_x, self.position_y), 50)

  
  def updateEaten(self):
    if self.eaten:
      self.eaten = False
    else:
     self.eaten = True

  # this generate the new position
  def newPosition(self, board_length, board_width, snake_position, snake_size):
    if not self.eaten:
      return
    chosenPosition = (random.randint(0,board_length)*snake_size[0] + self.scale[0], random.randint(0, board_width) *snake_size[1] +self.scale[1])
    while not self.isValidPosition(snake_position, chosenPosition, snake_size):
      chosenPosition = (random.randint(0,board_length)*snake_size[0] + self.scale[0], random.randint(0, board_width) *snake_size[1] +self.scale[1])
    self.updatePositionX(chosenPosition[0])
    self.updatePositionY(chosenPosition[1])

    
  # this check if the new position is an invalid position
  def isValidPosition(self, snake_position, chosenPosition, snake_size):
    invalid_position = set(snake_position.copy())
    invalid_position.add((self.position_x, self.position_y))

    head = snake_position[len(snake_position) - 1]
    up, down, right, left = set(), set(), set(), set()
    for i in range(1,4):
      up.add((head[0], head[1] - i* snake_size[1] + self.scale[1]))
      down.add((head[0], head[1] + i * snake_size[1] + self.scale[1]))
      right.add((head[0] + i * snake_size[0]+ self.scale[0],head[1]))
      left.add((head[0] - i *snake_size[0] + self.scale[0], head[1]))

    invalid_position.update(up)
    invalid_position.update(down)
    invalid_position.update(left)
    invalid_position.update(right)

    # ul is up left, ur is up right, dl is down left, dr is down right
    ul, ur, dl, dr = set(), set(), set(), set()

    for i  in range(1, 3):
      ul.add((head[0] - i * snake_size[0] +  self.scale[0], head[1] - i * snake_size[1] +self.scale[1]))
      ur.add((head[0]  + i * snake_size[0] + self.scale[0], head[1] - i * snake_size[1] + self.scale[1]))
      dl.add((head[0] - i * snake_size[0] + self.scale[0], head[1] + i* snake_size[1] +self.scale[1]))
      dr.add((head[0] + i * snake_size[0] + self.scale[0], head[1] + i* snake_size[1] + self.scale[1]))

    invalid_position.update(ul)
    invalid_position.update(ur)
    invalid_position.update(dl)
    invalid_position.update(dr)
    if chosenPosition in invalid_position:
      return False
    return True

    
    

    