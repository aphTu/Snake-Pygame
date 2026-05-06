import pygame 
from pygame._sdl2.video import Window
pygame.init()
SCREEN_HEIGHT = 800
SCREEN_WIDTH = 800
screen = pygame.display.set_mode((0,0), pygame.RESIZABLE)
window = Window.from_display_module()
window.maximize()


player = pygame.Rect((300, 250, 50, 50))
run = True
while run:
  screen.fill((0,0,0))
  
  pygame.draw.rect(screen, (0,255,255), player)

  key = pygame.key.get_pressed()
  if key[pygame.K_a] or key[pygame.K_LEFT]:
    player.move_ip(-1, 0)
  elif key[pygame.K_d] or key[pygame.K_RIGHT]:
    player.move_ip(1,0)
  elif key[pygame.K_w] or key[pygame.K_UP]:
    player.move_ip(0,-1)
  elif key[pygame.K_s] or key[pygame.K_DOWN]:
    player.move_ip(0,1)
  for event in pygame.event.get():
    if(event.type == pygame.QUIT):
      run = False
  pygame.display.update()

pygame.quit()