from constants import *
import pygame
def main():
   pygame.init()
   screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
   
   while True:
        screen.fill(000)
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
             return
if __name__ == "__main__":
   print("Starting asteroids!")
   print(f"Screen width: {SCREEN_WIDTH}")
   print(f"Screen height: {SCREEN_HEIGHT}")
   main()
 

