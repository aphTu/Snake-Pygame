## playing board the snake
import pygame

class Board():
  def __init__(self, width, length, screenWidth, screenLength):
    self.width = width
    self.length = length
    self.rectangle = [[1 for _ in range(length)] for _ in range(width)]
    self.screenWidth = screenWidth
    self.screenLength = screenLength
  
  def printBoard(self):
  
    for i in range(self.length):
      print("|  ", end="")
      for j in range(self.width):
        print(f"{self.rectangle[j][i]} ", end="")
      print(" |", end="")
      print("")
  
  def initBoard(self, screen):
    color = (0,255,0)
    for i in range(self.length):
     
      for j in range(self.width):
        if color != (0,255,0):
          color = (0,255,0)
        else:
          color = (0,102,0)
        # print(screenLength/self.length)
        # print(f"Drawing at {self.screenLength/self.length * i, self.screenWidth/self.width * j}")
        pygame.draw.rect(screen,color,pygame.Rect(self.screenLength/self.length * i, self.screenWidth/self.width * j, self.screenLength/self.length, self.screenWidth/self.width))
 
  def getWidth(self):
    return self.width
  
  def getLength(self):
    return self.length

  def insidePlayableArea(self, Coord):
    leftMost = 0
    upMost = 0
    rightMost = self.screenLength/self.length * (self.length -1)
    botMost = self.screenWidth/self.width * (self.width - 1)

    if Coord[0] < leftMost or Coord[0] > rightMost or Coord[1] < upMost or Coord[1] > botMost:
      return False
    return True
  
  def getBoundary(self):
    return [(0,0), (self.screenLength/self.length * (self.length -1),  self.screenWidth/self.width * (self.width - 1))]
# board = Board(9,7)
# board.printBoard()