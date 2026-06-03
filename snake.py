import pygame
from apple import Apple
class Snake:
  def __init__(self, color, snake_size):
    self.color = color
    self.snake_size = snake_size
    self.position = [(snake_size[0] * 1, snake_size[1] * 3),(snake_size[0] * 2, snake_size[1] * 3),(snake_size[0] * 3, snake_size[1] * 3)]
    self.length = 3
    self.direction = None
    self.timeDelay = 167/1000


  def updateAppearance(self, appearance):
    self.appearance = appearance

  def updateDirection(self, key):
    if(self.direction is None):
      self.direction = self.whatDirection(key)
      return 1
    if self.isDirectionPerpendicular(key):
      self.direction = self.whatDirection(key)
    else:
      pass
      #direction should stay same if it not perpendicular
  def updateLength(self):
    tail = self.getPosition()[self.length-1]
    bottom_two = self.getPosition()[-2:]
    change_x = bottom_two[0][0] - bottom_two[1][0]
    change_y = bottom_two[0][1] - bottom_two[1][1] 
    if change_x < 0:
      self.position.insert(0, (tail[0] + self.snake_size[0], tail[1]))
    elif change_x > 0:
      self.position.insert(0, (tail[0] - self.snake_size[0], tail[1]))
    elif change_y > 0:
      self.position.insert(0, (tail[0], tail[1] - self.snake_size[1]))
    else:
      self.position.insert(0,(tail[0], tail[1] + self.snake_size[1]))

    self.length+=1
    
  def getPosition(self):
    return self.position
  
  def isDirectionPerpendicular(self, key):
    if (self.direction == 'u' or self.direction == 'd') and (self.whatDirection(key) != 'l' and self.whatDirection(key) != 'r'):
      return False

    if (self.direction == 'l' or self.direction=="r") and (self.whatDirection(key) != 'u' and self.whatDirection(key) != 'd'):
      return False

    return True 
  
  def whatDirection(self, key):
    match key:
      case pygame.K_w:
        return 'u'
      case pygame.K_UP:
        return 'u'

      case pygame.K_s:
        return 'd'
      case pygame.K_DOWN:
        return 'd'

      case pygame.K_LEFT:
        return 'l'
      case pygame.K_a:
        return 'l'

      case pygame.K_RIGHT:
        return 'r'
      case pygame.K_d:
        return 'r'
      
  def drawSnake(self, screen):
    for coord in self.position:
      x, y = coord[0], coord[1]
      rect = pygame.Rect( x, y, self.snake_size[0], self.snake_size[1])
      # print(f"width : {rect.width}")
      # print(f"height: {rect.height}")
      pygame.draw.rect(screen, self.color, rect)

  def updatePositionHead(self, Coord, outOfBound):
    if not isinstance(Coord, tuple):
      raise Exception("Please input a tuple")
    # print(self.getPositionHead())
    current_head_x = None
    current_head_y = None
    if not outOfBound:
      current_head_x = self.position[self.length-1][0] + Coord[0]
      current_head_y = self.position[self.length-1][1] + Coord[1]
    else:
      current_head_x = Coord[0]
      current_head_y = Coord[1]
    self.position.append((current_head_x, current_head_y))
    self.position.pop(0)

  def getPositionHead(self):
    return self.position[self.length-1]
  
  def outOfBound(self, boundaryList):
    head  = self.getPositionHead()
    leftMost = boundaryList[0][0]
    topMost = boundaryList[0][1]
    rightMost = boundaryList[1][0]
    botMost = boundaryList[1][1]
    if head[0] < leftMost:
      self.updatePositionHead((rightMost,head[1]), True)
    elif head[0] > rightMost:
      print(self.getPositionHead())
      self.updatePositionHead((leftMost, head[1]), True)
    elif head[1] < topMost:
      self.updatePositionHead((head[0], botMost), True)
    else:
      self.updatePositionHead((head[0], topMost), True)
  
  def hitBody(self):
    copy = self.position[:-1]
    if self.getPositionHead() in copy:
      return True
    return False
  
  def hitApple(self, apple):
    if not isinstance(apple, Apple):
      raise Exception("Argument has to be an Apple object")
    if apple.eaten:
      return
    app_pos = (apple.position_x, apple.position_y)

    # print(app_pos)
    # print(self.getPositionHead())
    left = self.getPositionHead()[0]
    top = self.getPositionHead()[1]
    right = left + self.snake_size[0]
    bottom = top + self.snake_size[1]
    # print(f"left: {left}, right: {right}, top: {top}, bottom: {bottom}")
    if app_pos[0] > left and app_pos[0] < right and app_pos[1] > top and app_pos[1] < bottom :
      self.updateLength()
      apple.updateEaten()
    