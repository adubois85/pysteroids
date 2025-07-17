# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
import sys
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
from constants import *


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    timer = pygame.time.Clock()
    dt = 0
    
    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    
    # Note: remember to create the class variable for containers before creating any players
    # otherwise those instances won't have that variable and won't update correctly
    Player.containers = (updateable, drawable)
    Asteroid.containers = (asteroids, updateable, drawable)
    AsteroidField.containers = (updateable)
    Shot.containers = (shots, updateable, drawable)
    
    player = Player((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2))
    asteroid_field = AsteroidField()
    
    playing = True
    while playing == True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0, 0, 0))
        # player.update(dt)
        # player.draw(screen)
        updateable.update(dt)
        for asteroid in asteroids:
            if asteroid.detect_collision(player):
                sys.exit("Game over!")
            for shot in shots:
                if asteroid.detect_collision(shot):
                    asteroid.split()
                    shot.kill()
        for item in drawable:
            item.draw(screen)
        pygame.display.flip()
        dt = timer.tick(60) / 1000
    
    # print("Starting Asteroids!")
    # print(f"Screen width: {SCREEN_WIDTH}")
    # print(f"Screen height: {SCREEN_HEIGHT}")


if __name__ == "__main__":
    main()
