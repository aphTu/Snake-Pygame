import pygame 
from pygame._sdl2.video import Window
from snake import Snake
from board import Board
from queue import Queue
from apple import Apple
pygame.init()
screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
# window = Window.from_display_module()
# window.maximize()
SCREEN_LENGTH, SCREEN_WIDTH = pygame.display.get_window_size()
print(SCREEN_LENGTH, SCREEN_WIDTH)

snake_size = (SCREEN_LENGTH/10, SCREEN_WIDTH/7)
print(f"Snake size aka divded space {snake_size[0], snake_size[1]}")
snake = Snake((0,255,255),snake_size)
board = Board(7, 10, SCREEN_WIDTH, SCREEN_LENGTH)
clock = pygame.time.Clock()
run = True
allow_input = True
input_queue = Queue()
time_elapsed = 0
apple = Apple(0 + snake_size[0]/2,0+ snake_size[1]/2, (snake_size[0]/2, snake_size[1]/2))
while run:
  dt = clock.tick(60)/1000
  screen.fill((0,0,0))
  board.initBoard(screen)
  apple.drawApple(screen)
  snake.drawSnake(screen)
  
  key = pygame.key.get_pressed()
  for event in pygame.event.get():
    if(event.type == pygame.QUIT):
      run = False
    elif event.type == pygame.KEYDOWN:
      snake.updateDirection(event.key)
  if key[pygame.K_ESCAPE]:
    run = False

  if(snake.hitBody()): 
    run = False
    print("snake hit itself, lose game")

  if not board.insidePlayableArea(snake.getPositionHead()):
    snake.outOfBound(board.getBoundary())
  if snake.timeDelay - time_elapsed <= 0:
    time_elapsed = 0
    match(snake.direction):
      case 'l':
        snake.updatePositionHead((-snake_size[0], 0), False)
      case 'r':
        snake.updatePositionHead((snake_size[0], 0), False)
      case 'u':
        snake.updatePositionHead((0, -snake_size[1]), False)
      case 'd':
        snake.updatePositionHead((0, snake_size[1]), False)
      case _:
        pass
  snake.hitApple(apple)
  if apple.eaten:
    apple.newPosition(10,7, snake.getPosition(), snake_size, board.getBoundary())
    apple.updateEaten()
  time_elapsed+=dt
  pygame.display.update()
pygame.quit()