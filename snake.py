class Snake:
  def __init__(self, color, appearance, ):
    self.color = color
    self.appearance = appearance
    self.speed = 1
    self.length = 1

  def updateAppearance(self, appearance):
    self.appearance = appearance

  def updateSpeed(self):
    self.speed+=1
  def updateLength(self):
    self.length+=1