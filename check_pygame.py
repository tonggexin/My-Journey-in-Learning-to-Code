try:
    import pygame
    print('Pygame已安装，版本:', pygame.version.ver)
except ImportError:
    print('Pygame未安装')