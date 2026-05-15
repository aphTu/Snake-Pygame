## playing board the snake
import pygame
import math
class Board():
  def __init__(self, width, length):
    self.width = width
    self.length = length
    self.rectangle = [[1 for _ in range(length)] for _ in range(width)]
  
  def printBoard(self):
  
    for i in range(self.length):
      print("|  ", end="")
      for j in range(self.width):
        print(f"{self.rectangle[j][i]} ", end="")
      print(" |", end="")
      print("")
  
  def initBoard(self, screenWidth, screenLength, screen):
    color = (0,255,0)
    for i in range(self.length):
     
      for j in range(self.width):
        if color != (0,255,0):
          color = (0,255,0)
        else:
          color = (0,102,0)
        # print(screenLength/self.length)
        # print(f"Drawing at {screenLength/self.length * i, screenWidth/self.width * j}")
        pygame.draw.rect(screen,color,pygame.Rect(screenLength/self.length * i, screenWidth/self.width * j, screenLength/self.length, screenWidth/self.width))
 
  # is the snake head currently in a valid square or not
  def validPosition(self, x, y, screenLength, screenWidth):
    actual_x = abs(x/(screenLength/self.length))
    actual_y = abs(y/(screenWidth/self.width))
    close_x = False
    close_y = False

    if(math.isclose(actual_x,  math.ceil(actual_x), abs_tol=0.05)):
      print("burhufhuewhfuw")
      close_x = True
    if (math.isclose(actual_y, math.ceil(actual_y), abs_tol=0.05)):
      print("are we deadass")
      close_y = True
    print(f"acutal_x:{actual_x}")
    print(f"actual_y: {actual_y}")
    # if actual_x.is_integer() and actual_y.is_integer():
    if close_x and close_y:
      return True
    return False



board = Board(9,7)
board.printBoard()