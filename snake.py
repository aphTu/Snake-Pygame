class snake:
  def __init__(self, color, appearance):
    self.color = color
    self.appearance = appearance
    self.speed = 0

  def updateAppearance(self, appearance):
    self.appearance = appearance

  def updateSpeed(self):
    self.speed+=1     