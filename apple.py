import pygame
class Apple():
  def __init__(self, position_x, position_y):
    self.position_x = position_x
    self.position_y = position_y
    self.color = (255, 0, 0)
    self.eaten = False

  def updatePositionX(self, position):
    self.position_x = position

  def updatePoitionY(self, position):
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
    self.eaten = True