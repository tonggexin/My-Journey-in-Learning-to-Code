import pygame
import os

# Get the directory where this script is located
script_dir = os.path.dirname(os.path.abspath(__file__))

pygame.init()

pygame.display.set_caption("Pygame 4")

screen = pygame.display.set_mode((700, 500))

# Create the full path to the image file
image_path = os.path.join(script_dir, "spider_girl.png")
image = pygame.image.load(image_path).convert_alpha()
rect = image.get_rect()
rect.center = screen.get_rect().center

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255, 255, 255))
    screen.blit(image, rect)

    pygame.display.update()

pygame.quit()