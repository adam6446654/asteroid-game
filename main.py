import pygame
import constants
import player
import asteroid
import asteroidfield

def main():
    pygame.init()
    py_clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((constants.SCREEN_WIDTH,constants.SCREEN_HEIGHT))
    print("Starting Asteroids!")
    print(f"Screen width: {constants.SCREEN_WIDTH}")
    print(f"Screen height: {constants.SCREEN_HEIGHT}")
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    player.Player.containers = (updatable,drawable)
    asteroid.Asteroid.containers = (asteroids, updatable, drawable)
    asteroidfield.AsteroidField.containers = (updatable,)
    player_object = player.Player(constants.SCREEN_WIDTH / 2,constants.SCREEN_HEIGHT / 2)
    asteroid_field = asteroidfield.AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
                
        screen.fill((0,0,0))
        updatable.update(dt)
        for asteroid_obj in asteroids:
            if player_object.collision(asteroid_obj):
                print("Game over!")
                pygame.quit()
                return

        for obj in drawable:
            obj.draw(screen)
        pygame.display.flip()
        dt = py_clock.tick(60) / 1000

if __name__ == "__main__":
    main()