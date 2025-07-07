import pygame
import constants
import player

def main():
    pygame.init()
    py_clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((constants.SCREEN_WIDTH,constants.SCREEN_HEIGHT))
    print("Starting Asteroids!")
    print(f"Screen width: {constants.SCREEN_WIDTH}")
    print(f"Screen height: {constants.SCREEN_HEIGHT}")
    player_object = player.Player(constants.SCREEN_WIDTH / 2,constants.SCREEN_HEIGHT / 2)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0,0,0))
        player_object.update(dt)
        player_object.draw(screen)
        pygame.display.flip()
        val = py_clock.tick(60)
        dt = val / 1000

if __name__ == "__main__":
    main()