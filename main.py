import pygame
from constants import *
from players import Player
from asteroids import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
from scoreboard import ScoreBoard

def main():
	pygame.init()
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	
	clock = pygame.time.Clock()
	dt = 0
	
	updatable = pygame.sprite.Group()
	drawable = pygame.sprite.Group()
	asteroids = pygame.sprite.Group()
	shots = pygame.sprite.Group()
 
	Player.containers = (updatable, drawable)
	Asteroid.containers = (asteroids, updatable, drawable)	
	AsteroidField.containers = (updatable,)
	Shot.containers = (shots, updatable, drawable)
	
	scoreboard = ScoreBoard()

	player = Player(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
	asteroid_field = AsteroidField()
	
	print("Starting Asteroids!")
	print(f"Screen width: {SCREEN_WIDTH}")
	print(f"Screen height: {SCREEN_HEIGHT}")
 
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return
		
		updatable.update(dt)
		# Check for collisions between player and asteroids
		for asteroid in asteroids:
			if player.collides_with(asteroid):
				print("Game Over!")
				pygame.quit()
				return

		# Check for collisions between shots and asteroids
		for asteroid in asteroids:
			for shot in shots:
				if asteroid.collides_with(shot):
					asteroid.split()
					shot.kill()
					scoreboard.increment()

		screen.fill("black")
		for sprite in drawable:
			sprite.draw(screen)
		scoreboard.draw(screen)
		pygame.display.flip()
		dt = clock.tick(60)/1000
		
if __name__ == "__main__":
	main()

