import pygame
import os

# 初始化pygame
pygame.init()

# 设置窗口标题
pygame.display.set_caption("Pygame Sprite示例")

# 获取脚本所在目录
script_dir = os.path.dirname(os.path.abspath(__file__))

# 设置屏幕尺寸
screen_width = 700
screen_height = 500
screen = pygame.display.set_mode((screen_width, screen_height))

# 定义颜色
WHITE = (255, 255, 255)

# 创建一个继承自pygame.sprite.Sprite的玩家类
class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        # 调用父类的初始化方法
        super().__init__()
        
        # 加载图像并设置路径
        image_path = os.path.join(script_dir, "spider_girl.png")
        original_image = pygame.image.load(image_path).convert_alpha()
        
        # 缩小图像（设置为原图的10%大小）
        original_rect = original_image.get_rect()
        new_width = int(original_rect.width * 0.1)
        new_height = int(original_rect.height * 0.1)
        self.image = pygame.transform.scale(original_image, (new_width, new_height))
        
        # 设置精灵的rect属性
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        
        # 添加移动速度属性
        self.speed_x = 0
        self.speed_y = 0
    
    def update(self):
        # 更新精灵的位置
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
        
        # 确保精灵不会移出屏幕
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > screen_width:
            self.rect.right = screen_width
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > screen_height:
            self.rect.bottom = screen_height

# 创建精灵组
all_sprites = pygame.sprite.Group()

# 创建玩家实例并添加到精灵组
player = Player(screen_width // 2, screen_height // 2)
all_sprites.add(player)

# 设置游戏循环的时钟
clock = pygame.time.Clock()
FPS = 60

# 游戏主循环
running = True
while running:
    # 保持循环以正确的速度运行
    clock.tick(FPS)
    
    # 处理事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        # 处理键盘按下事件
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.speed_x = -5
            elif event.key == pygame.K_RIGHT:
                player.speed_x = 5
            elif event.key == pygame.K_UP:
                player.speed_y = -5
            elif event.key == pygame.K_DOWN:
                player.speed_y = 5
        
        # 处理键盘释放事件
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT and player.speed_x < 0:
                player.speed_x = 0
            elif event.key == pygame.K_RIGHT and player.speed_x > 0:
                player.speed_x = 0
            elif event.key == pygame.K_UP and player.speed_y < 0:
                player.speed_y = 0
            elif event.key == pygame.K_DOWN and player.speed_y > 0:
                player.speed_y = 0
    
    # 更新所有精灵
    all_sprites.update()
    
    # 绘制
    screen.fill(WHITE)
    # 在屏幕上绘制所有精灵
    all_sprites.draw(screen)
    
    # 更新屏幕显示
    pygame.display.flip()

# 退出游戏
pygame.quit()