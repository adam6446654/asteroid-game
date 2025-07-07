import CircleShape
import constants
import pygame
import shot

class Player(CircleShape.CircleShape):
    containers = ()
    def __init__ (self,x,y):
        pygame.sprite.Sprite.__init__(self)
        CircleShape.CircleShape.__init__(self, x, y, constants.PLAYER_RADIUS)
        self.rotation = 0
        self.shoot_timer = 0
        for group in self.containers:
            group.add(self)

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self,screen):
        pygame.draw.polygon(screen,(255,255,255),self.triangle(),2)

    def rotate(self,dt):
        self.rotation += (constants.PLAYER_TURN_SPEED * dt)

    def update(self, dt):
        keys = pygame.key.get_pressed()

        if self.shoot_timer > 0:
            self.shoot_timer -= dt
        if keys[pygame.K_a]:
            self.rotate(-1*dt)
        if keys[pygame.K_d]:
            self.rotate(dt) 
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_SPACE] and self.shoot_timer <= 0:
            self.shoot()
            self.shoot_timer = constants.PLAYER_SHOOT_COOLDOWN

    def move(self,dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * constants.PLAYER_SPEED * dt

    def shoot(self):
        forward = pygame.Vector2(0,1)
        forward = forward.rotate(self.rotation)
        a = self.position + forward * self.radius
        bullet = shot.Shot(a.x,a.y,constants.SHOT_RADIUS)
        bullet.velocity = forward * constants.PLAYER_SHOOT_SPEED
