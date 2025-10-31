import pygame

pygame.init()


screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("李欣远")

# # 绘制一个红色的矩形
# pygame.draw.rect(screen, (255, 0, 0), (100, 100, 50, 50))
# # 绘制一个绿色的三角形
# pygame.draw.polygon(screen, (0, 255, 0), [(200, 200), (300, 200), (300, 300)])
# # 绘制一个蓝色的正六边形，放在右下角，填充白色
# pygame.draw.polygon(screen, (0, 0, 255), [(500, 300), (600, 300), (600, 400), (500, 400), (400, 400), (400, 300)], 0)
# # 绘制一个五边形，放在左下角，width=3
# pygame.draw.polygon(screen, (255, 205, 0), [(100, 300), (200, 300), (200, 400), (100, 400), (50, 350)], 3)
# # 绘制一个8边形，放在左下角，width=10
# pygame.draw.polygon(screen, (255, 0, 255), [(150, 400), (200, 400), (200, 500), (100, 500), (50, 450), (50, 350), (100, 300), (200, 300)], 10)
# # 绘制一个圆，中心坐标(10,10)，半径=50，width=0
# pygame.draw.circle(screen, (0, 255, 255), (60, 70), 50, 0)
# # 绘制一个圆，中心坐标(100,100)，半径=50，width=3
# pygame.draw.circle(screen, (255, 255, 0), (100, 100), 50, 3)
# # 绘制一个四分之一圆，draw_top_right=true，width=5
# pygame.draw.circle(screen, (255, 0, 255), (200, 200), 50, 5, True)
# 绘制一段弧形，中心坐标(300,300)，半径=50，start_angle=0，stop_angle=90，width=3
pygame.draw.arc(screen, (0, 25, 255), (250, 250, 100, 100), -3.14/2, 3.14/2, 3)

pygame.display.update()
pygame.time.wait(5000)
# 游戏主循环应该放在这里
# 主循环是游戏的核心，它持续运行直到用户退出游戏
# 主循环通常包含以下几个部分：
# 1. 事件处理 - 处理用户输入（按键、鼠标等）
# 2. 更新游戏状态 - 移动对象、更新游戏逻辑等
# 3. 渲染 - 绘制游戏画面

# 以下是一个简单的游戏主循环示例：
running = True
# while running:
#     # 事件处理
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
    
    # 更新游戏状态
    # 这里可以添加游戏逻辑更新代码
    # pygame.draw.rect(screen, (255, 0, 0), (100, 100, 50, 50))
    # # 渲染
    # screen.fill((255, 255, 255))  # 清空屏幕
    # # 这里可以添加绘制代码
    # pygame.display.update()  # 更新显示

pygame.quit()