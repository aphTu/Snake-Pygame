import pygame
class Snake:
  def __init__(self, color, appearance):
    self.color = color
    self.appearance = appearance
    self.length = 1
    self.direction = None
    self.timeDelay = 180/1000
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
    self.length+=1
  def getPosition(self):
    return (self.appearance.x, self.appearance.y)
  
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
