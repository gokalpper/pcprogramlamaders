import pygame
pygame.init()
ekran = pygame.display.set_mode()
x, y = ekran.get_size()
pygame.display.quit()
print(x,y)