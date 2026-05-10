import pygame 
from pygame._sdl2.video import Window
from snake import Snake
from board import Board
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
        snake.updateDirection(event.key)
        allow_input = False
  if key[pygame.K_ESCAPE]:
    run = False
  curr_pos = snake.getPosition()
  # print(f"{curr_pos[1]/(SCREEN_WIDTH/7)} and {curr_pos[0]/(SCREEN_LENGTH/10)}")
  if(board.validPosition(curr_pos[0],curr_pos[1], SCREEN_LENGTH, SCREEN_WIDTH)):
    # print(f"gotta be true right, {curr_pos[0], curr_pos[1]}")
    allow_input = True
  match(snake.direction):
    case 'l':
      # print(curr_pos)
      snake.appearance.move_ip(-snake_size[0] * 4 * dt , 0)
    case 'r':
      # print(curr_pos)

      snake.appearance.move_ip(snake_size[0] * dt * 4 ,0)
    case 'u':
      # print(curr_pos)
      
      snake.appearance.move_ip(0, -snake_size[1] * dt * 4)
    case 'd':
      # print(curr_pos)
      
      snake.appearance.move_ip(0, snake_size[1] * dt * 4)
    case _:
      pass
  pygame.display.update()
pygame.quit()