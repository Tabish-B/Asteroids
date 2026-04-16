import pygame
from constants import *
from logger import *
from player import *
from asteroidfield import *
import sys
from circleshape import *
from shot import *

def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH} \n Screen height: {SCREEN_HEIGHT} ")
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


    #Add objects to groups
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)
    Shot.containers = (shots, drawable, updatable)

    AsteroidField()

    player = Player(x = SCREEN_WIDTH / 2, y = SCREEN_HEIGHT / 2)

    while True:
        log_state()
        dt = (clock.tick(60))/1000
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        updatable.update(dt)
        
        for shot in shots:
            for aster in asteroids:
                if shot.collides_with(aster):
                    log_event("asteroid_shot")
                    shot.kill()
                    aster.split()


        for aster in asteroids:
            if(player.collides_with(aster) == True):
                log_event("player_hit")
                print("Game over!")
                sys.exit(1)

        screen.fill("black")
        for dr in drawable:
            dr.draw(screen)

        pygame.display.flip()





if __name__ == "__main__":
    main()
