import pygame
class Snake:
  def __init__(self, color, appearance):
    self.color = color
    self.appearance = appearance
    self.length = 1
    self.direction = None
  def updateAppearance(self, appearance):
    self.appearance = appearance

  def updateDirection(self, key):
    match key:
      case pygame.K_w:
        self.direction = 'u'
      case pygame.K_UP:
        self.direction = 'u'

      case pygame.K_s:
        self.direction  ='d'
      case pygame.K_DOWN:
        self.direction = 'd'

      case pygame.K_LEFT:
        self.direction = 'l'
      case pygame.K_a:
        self.direction = 'l'

      case pygame.K_RIGHT:
        self.direction = 'r'
      case pygame.K_d:
        self.direction = 'r'
  def updateLength(self):
    self.length+=1
  def getPosition(self):
    return (self.appearance.x, self.appearance.y)

