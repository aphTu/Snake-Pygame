import pygame 
from pygame._sdl2.video import Window
from snake import Snake
from board import Board
pygame.init()
screen = pygame.display.set_mode((0,0), pygame.RESIZABLE)
window = Window.from_display_module()
window.maximize()
SCREEN_HEIGHT, SCREEN_WIDTH = pygame.display.get_window_size()
print(SCREEN_HEIGHT, SCREEN_WIDTH)

snake_size = (SCREEN_HEIGHT/10, SCREEN_WIDTH/7)
print(f"Snake size aka divded space {snake_size[0], snake_size[1]}")
snake = Snake((0,255,255),pygame.Rect((0, 0, snake_size[0], snake_size[1])))

board = Board(7, 10)

run = True
while run:
  screen.fill((0,0,0))
  board.initBoard(SCREEN_WIDTH, SCREEN_HEIGHT, screen)
  pygame.draw.rect(screen, snake.color, snake.appearance)
  key = pygame.key.get_pressed()
  if key[pygame.K_a] or key[pygame.K_LEFT]:
    snake.appearance.move_ip(-snake.speed * snake_size[1], 0)
    print(f"moved:{-snake.speed * snake_size[1]} ")
  elif key[pygame.K_d] or key[pygame.K_RIGHT]:
    snake.appearance.move_ip(snake.speed * snake_size[1],0)
  elif key[pygame.K_w] or key[pygame.K_UP]:
    snake.appearance.move_ip(0,-snake.speed * snake_size[0])
  elif key[pygame.K_s] or key[pygame.K_DOWN]:
    snake.appearance.move_ip(0,snake.speed * snake_size[0])
  elif key[pygame.K_ESCAPE]:
    run = False
  for event in pygame.event.get():
    if(event.type == pygame.QUIT):
      run = False
  pygame.time.delay(10)
  pygame.display.update()
pygame.quit()