import platform
print(platform.architecture())

import sys
print(sys.executable)

import pygame
print(pygame.version.ver)  # 应该打印版本号，如 '2.5.2'
pygame.init()
print("Pygame 初始化成功！")