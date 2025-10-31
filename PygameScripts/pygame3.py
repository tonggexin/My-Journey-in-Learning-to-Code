import pygame

pygame.init()

pygame.display.set_caption("Pygame3")

img_width = 400
img_height = 300
screen = pygame.display.set_mode((img_width, img_height))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # 首先清空screen，为绘制做准备
    screen.fill((255, 255, 255))
    # 绘制一个圆形，圆形坐标在中间，颜色为粉红色
    pygame.draw.circle(screen, (255, 100, 100), (320, 240), 50)
    # 绘制文本"我爱李欣远"。解决中文乱码问题。 
    # 加载中文字体（使用双反斜杠或原始字符串避免转义问题）
    font = pygame.font.Font("C:\\Windows\\Fonts\\STKAITI.TTF", 36)
    # 设置粗体
    font.set_bold(True)
    
    # 将文本分为三部分，分别渲染
    # 1. 渲染"我爱"（不带下划线）
    font.set_underline(False)
    text1 = font.render("我爱", True, (0, 10, 0))
    
    # 2. 渲染"李欣远"（带下划线）
    font.set_underline(True)
    text2 = font.render("李欣远", True, (0, 10, 0))
    
    # 3. 渲染"！"（不带下划线）
    font.set_underline(False)
    text3 = font.render("！", True, (0, 10, 0))
    
    # 依次绘制文本，确保它们紧密排列
    x_pos = 100
    screen.blit(text1, (x_pos, 100))
    x_pos += text1.get_width()
    screen.blit(text2, (x_pos, 100))
    x_pos += text2.get_width()
    screen.blit(text3, (x_pos, 100))
    
    # 更新显示
    pygame.display.update()

pygame.quit()