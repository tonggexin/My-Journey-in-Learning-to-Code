import pygame

pygame.init()

pygame.display.set_caption("Pygame2")
# 获取图像的尺寸，为后面的窗口设置做准备，图像路径是：images\118048871_p0_master1200.jpg
img = pygame.image.load("images/xx.jpg")
img_width, img_height = img.get_size()

screen = pygame.display.set_mode((img_width, img_height))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # 绘制一个圆形，圆形坐标在中间，颜色为粉红色
    pygame.draw.circle(screen, (255, 100, 100), (320, 240), 50)
    # 清空screen，为后面的绘制做准备
    screen.fill((255, 255, 255))
    # 绘制图片
    screen.blit(img, (0, 0))
    # 更新显示
    pygame.display.update()

pygame.quit()