import pygame
from constants import *
from players import Player

def main():
	pygame.init()
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	
	clock = pygame.time.Clock()
	dt = 0
	
	player = Player(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
	
	print("Starting Asteroids!")
	print(f"Screen width: {SCREEN_WIDTH}")
	print(f"Screen height: {SCREEN_HEIGHT}")

	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return
		
		player.update(dt)
		screen.fill("black")
		player.draw(screen)
		pygame.display.flip()
		dt = clock.tick(60)/1000
		
if __name__ == "__main__":
	main()

