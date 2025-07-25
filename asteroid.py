import pygame
import random
from circleshape import CircleShape
from constants import *


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2, True, True, True, True)

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        child_radius = self.radius - ASTEROID_MIN_RADIUS
        angle = random.uniform(20, 50)
        child_1 = Asteroid(self.position.x, self.position.y, child_radius)
        child_1.velocity = self.velocity.rotate(angle)
        # child_2_angle = self.position.rotate(-angle)
        child_2 = Asteroid(self.position.x, self.position.y, child_radius)
        child_2.velocity = self.velocity.rotate(-angle)

    def update(self, dt):
        self.position += (self.velocity * dt)
