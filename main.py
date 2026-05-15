import pygame 
from pygame._sdl2.video import Window
from snake import Snake
from board import Board
from queue import Queue
import math
pygame.init()
screen = pygame.display.set_mode((0,0), pygame.RESIZABLE)
window = Window.from_display_module()
window.maximize()
SCREEN_LENGTH, SCREEN_WIDTH = pygame.display.get_window_size()
print(SCREEN_LENGTH, SCREEN_WIDTH)

snake_size = (SCREEN_LENGTH/10, SCREEN_WIDTH/7)
print(f"Snake size aka divded space {snake_size[0], snake_size[1]}")
snake = Snake((0,255,255),pygame.Rect((0, 0, snake_size[0], snake_size[1])))

board = Board(7, 10)
clock = pygame.time.Clock()
run = True
allow_input = True
input_queue = Queue()
current_input = None
while run:
  dt = clock.tick(60)/1000
  screen.fill((0,0,0))
  board.initBoard(SCREEN_WIDTH, SCREEN_LENGTH, screen)
  pygame.draw.rect(screen, snake.color, snake.appearance)
  key = pygame.key.get_pressed()
  # if key.__contains__(True):
  #   print(key)
  #   snake.updateDirection(key)
  for event in pygame.event.get():
    if(event.type == pygame.QUIT):
      run = False
    elif event.type == pygame.KEYDOWN:
      if allow_input:
        input_queue.enqueue(event.key)
        
        allow_input = False
  if key[pygame.K_ESCAPE]:
    run = False
  curr_pos = snake.getPosition()
  if(board.validPosition(curr_pos[0],curr_pos[1], SCREEN_LENGTH, SCREEN_WIDTH)):
    print("what?")
    if not input_queue.isEmpty():
      print(input_queue)
      snake.updateDirection(input_queue.dequeue())   
      print(snake.direction) 
  match(snake.direction):
    case 'l':
      snake.appearance.move_ip(-snake_size[0] * 4 * dt , 0)
    case 'r':
      snake.appearance.move_ip(math.floor(snake_size[0] * dt * 4),0)
    case 'u':
      
      snake.appearance.move_ip(0, -snake_size[1] * dt * 4)
    case 'd':
      
      snake.appearance.move_ip(0, snake_size[1] * dt * 4)
    case _:
      pass
  pygame.display.update()
pygame.quit()