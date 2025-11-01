# 这是一个用pygame编写一个视觉小说的项目
# 项目名称：我和我的本科同学

import pygame
import sys
import os
import time

# ======================
# 游戏配置
# ======================
# 窗口设置
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60

# 颜色设置
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)

# 文本设置
FONT_SIZE = 24
# 设置中文字体路径（尝试多个常见的中文字体）
FONT_PATH = None
# Try different system fonts
common_fonts = ["Arial", "Times New Roman", "Courier New", "Verdana", "Helvetica"]
for font_name in common_fonts:
    try:
        test_font = pygame.font.SysFont(font_name, 24)
        if test_font.render("Test", True, (0,0,0)):
            FONT_PATH = font_name
            print(f"Successfully using font: {font_name}")
            break
    except:
        pass
DIALOGUE_BOX_HEIGHT = 150
DIALOGUE_PADDING = 20
TRANSITION_SPEED = 255  # 场景切换速度（0-255）

# 游戏状态
GAME_TITLE = "My College Friend and Me"

# ======================
# 资源管理器类
# ======================
class ResourceManager:
    def __init__(self):
        # 存储加载的图像资源
        self.images = {}
        # 存储角色立绘位置信息
        self.character_positions = {}
        # 获取资源目录路径
        self.src_dir = os.path.join(os.path.dirname(__file__), 'src')
    
    def load_all_resources(self):
        """加载所有图像资源"""
        # 加载背景图像（使用src文件夹中的图像作为背景）
        for filename in os.listdir(self.src_dir):
            if filename.endswith(('.png', '.jpg', '.jpeg')):
                # 创建资源ID（不包含扩展名）
                res_id = os.path.splitext(filename)[0]
                # 加载图像
                self.load_image(res_id, filename)
        
        print(f"资源加载完成，共加载 {len(self.images)} 个图像资源")
    
    def load_image(self, res_id, filename):
        """加载单个图像资源"""
        try:
            # 构建完整路径
            file_path = os.path.join(self.src_dir, filename)
            # 加载图像
            image = pygame.image.load(file_path)
            # 存储原始图像
            self.images[res_id] = image
            print(f"成功加载图像: {filename}")
        except pygame.error as e:
            print(f"加载图像失败: {filename}, 错误: {e}")
            # 创建一个备用的占位符图像
            placeholder = pygame.Surface((200, 200))
            placeholder.fill((200, 200, 200))  # 灰色
            self.images[res_id] = placeholder
    
    def get_image(self, res_id):
        """获取已加载的图像"""
        return self.images.get(res_id)
    
    def get_scaled_image(self, res_id, width=None, height=None, fit_screen=False):
        """获取缩放后的图像"""
        image = self.get_image(res_id)
        if image is None:
            return None
        
        # 创建副本避免修改原始图像
        scaled_image = image.copy()
        
        # 根据需求缩放图像
        if fit_screen:
            # 保持纵横比缩放以适应屏幕
            orig_width, orig_height = scaled_image.get_size()
            scale = min(SCREEN_WIDTH / orig_width, SCREEN_HEIGHT / orig_height)
            new_width = int(orig_width * scale)
            new_height = int(orig_height * scale)
            scaled_image = pygame.transform.scale(scaled_image, (new_width, new_height))
        elif width and height:
            # 按指定尺寸缩放
            scaled_image = pygame.transform.scale(scaled_image, (width, height))
        
        return scaled_image
    
    def set_character_position(self, character_id, position):
        """设置角色立绘的位置"""
        self.character_positions[character_id] = position
    
    def get_character_position(self, character_id):
        """获取角色立绘的位置"""
        return self.character_positions.get(character_id, (0, 0))

# ======================
# 对话系统类
# ======================
class DialogueSystem:
    def __init__(self):
        # 当前对话索引
        self.current_line_index = 0
        # 对话文本列表
        self.dialogue_lines = []
        # 对话是否完成
        self.is_complete = False
        # 初始化字体
        self.font = pygame.font.SysFont(FONT_PATH, FONT_SIZE) if FONT_PATH else pygame.font.SysFont(None, FONT_SIZE)
        # 文本打字机效果
        self.typing = False
        self.typing_index = 0
        self.typing_speed = 20  # 字符/秒
        self.last_typing_time = 0
        # 创建对话框表面
        self.dialogue_box = pygame.Surface((SCREEN_WIDTH, DIALOGUE_BOX_HEIGHT))
        self.dialogue_box.fill(GRAY)
        self.dialogue_box.set_alpha(200)  # 半透明
        # 对话框位置
        self.box_position = (0, SCREEN_HEIGHT - DIALOGUE_BOX_HEIGHT)
    
    def set_dialogue(self, lines):
        """设置对话内容"""
        self.dialogue_lines = lines
        self.current_line_index = 0
        self.is_complete = False
        self.typing = False
        self.typing_index = 0
    
    def next_line(self):
        """前进到下一行对话"""
        # 如果正在打字，立即显示全部文本
        if self.typing:
            self.typing = False
            return True
            
        if self.current_line_index < len(self.dialogue_lines) - 1:
            self.current_line_index += 1
            self.typing = True
            self.typing_index = 0
            self.last_typing_time = time.time()
            return True
        else:
            self.is_complete = True
            return False
    
    def get_current_line(self):
        """获取当前对话行"""
        if 0 <= self.current_line_index < len(self.dialogue_lines):
            line = self.dialogue_lines[self.current_line_index]
            # 处理打字机效果
            if self.typing:
                elapsed = (time.time() - self.last_typing_time) * self.typing_speed
                self.typing_index = min(int(elapsed), len(line))
                return line[:self.typing_index]
            return line
        return None
    
    def draw(self, screen):
        """绘制对话系统到屏幕上"""
        if not self.dialogue_lines:
            return
        
        # 绘制对话框背景
        screen.blit(self.dialogue_box, self.box_position)
        
        # 获取当前对话行
        current_line = self.get_current_line()
        if current_line:
            # 解析对话格式: "角色名: 对话内容"
            if ": " in current_line:
                speaker, content = current_line.split(": ", 1)
                # 绘制说话人名字
                speaker_text = self.font.render(speaker + ":", True, BLACK)
                screen.blit(speaker_text, (self.box_position[0] + DIALOGUE_PADDING, self.box_position[1] + DIALOGUE_PADDING))
                
                # 绘制对话内容
                self._draw_wrapped_text(screen, content, 
                    (self.box_position[0] + DIALOGUE_PADDING, 
                     self.box_position[1] + DIALOGUE_PADDING + FONT_SIZE + 10),
                    SCREEN_WIDTH - DIALOGUE_PADDING * 2, 
                    DIALOGUE_BOX_HEIGHT - DIALOGUE_PADDING * 2 - FONT_SIZE - 10)
            else:
                # 没有说话人，直接绘制内容
                self._draw_wrapped_text(screen, current_line, 
                    (self.box_position[0] + DIALOGUE_PADDING, 
                     self.box_position[1] + DIALOGUE_PADDING),
                    SCREEN_WIDTH - DIALOGUE_PADDING * 2, 
                    DIALOGUE_BOX_HEIGHT - DIALOGUE_PADDING * 2)
    
    def _draw_wrapped_text(self, screen, text, position, max_width, max_height):
        """绘制自动换行的文本"""
        words = text.split(' ')
        space_width = self.font.size(' ')[0]
        current_line = ""
        current_y = position[1]
        
        for word in words:
            test_line = current_line + word + ' '
            test_width = self.font.size(test_line)[0]
            
            if test_width > max_width:
                # 绘制当前行
                if current_line:
                    text_surface = self.font.render(current_line, True, BLACK)
                    screen.blit(text_surface, (position[0], current_y))
                    current_y += FONT_SIZE + 5
                    
                    # 检查是否超出最大高度
                    if current_y > position[1] + max_height:
                        break
                
                # 开始新行
                current_line = word + ' '
            else:
                current_line = test_line
        
        # 绘制最后一行
        if current_line and current_y <= position[1] + max_height:
            text_surface = self.font.render(current_line, True, BLACK)
            screen.blit(text_surface, (position[0], current_y))

# ======================
# 场景和场景管理器类
# ======================
class Scene:
    def __init__(self, name, resource_manager, dialogue_system):
        # 场景名称
        self.name = name
        # 资源管理器引用
        self.resource_manager = resource_manager
        # 对话系统引用
        self.dialogue_system = dialogue_system
        # 当前背景图像ID
        self.background_id = None
        # 当前角色列表
        self.characters = []
        # 角色入场动画相关
        self.animating_characters = []
        self.character_speed = 500  # 角色移动速度（像素/秒）
    
    def set_background(self, background_id):
        """设置场景背景"""
        self.background_id = background_id
    
    def add_character(self, character_id, position=None):
        """添加角色到场景"""
        if character_id not in self.characters:
            self.characters.append(character_id)
            # 设置角色位置
            if position:
                self.resource_manager.set_character_position(character_id, position)
    
    def remove_character(self, character_id):
        """从场景移除角色"""
        if character_id in self.characters:
            self.characters.remove(character_id)
    
    def clear_characters(self):
        """清空所有角色"""
        self.characters = []
    
    def set_dialogue(self, dialogue_lines):
        """设置场景对话"""
        self.dialogue_system.set_dialogue(dialogue_lines)
    
    def start_character_entrance(self):
        """开始角色入场动画"""
        self.animating_characters = self.characters.copy()
        
    def update(self, dt):
        """更新场景状态"""
        # 更新角色入场动画
        for character_id in self.animating_characters[:]:
            current_pos = list(self.resource_manager.get_character_position(character_id))
            target_x = SCREEN_WIDTH // 3 if self.characters.index(character_id) == 0 else SCREEN_WIDTH * 2 // 3
            
            if current_pos[0] < target_x:
                # 角色向右移动
                current_pos[0] += self.character_speed * dt
                if current_pos[0] >= target_x:
                    current_pos[0] = target_x
                    self.animating_characters.remove(character_id)
                
                self.resource_manager.set_character_position(character_id, tuple(current_pos))
    
    def draw(self, screen):
        """绘制场景"""
        # 绘制背景
        if self.background_id:
            background_image = self.resource_manager.get_scaled_image(self.background_id, fit_screen=True)
            if background_image:
                # 计算居中位置
                bg_rect = background_image.get_rect(center=screen.get_rect().center)
                screen.blit(background_image, bg_rect)
        
        # 绘制角色
        for character_id in self.characters:
            character_image = self.resource_manager.get_image(character_id)
            if character_image:
                # 获取角色位置
                position = self.resource_manager.get_character_position(character_id)
                # 计算缩放尺寸
                char_width, char_height = character_image.get_size()
                # 按比例缩放角色图像
                target_height = int(screen.get_height() * 0.8)  # 角色高度为屏幕高度的80%
                scale = target_height / char_height
                new_width = int(char_width * scale)
                new_height = target_height
                
                # 缩放图像
                scaled_char = self.resource_manager.get_scaled_image(character_id, new_width, new_height)
                if scaled_char:
                    # 计算底部对齐的位置
                    char_x = position[0] if position[0] is not None else 0
                    char_y = screen.get_height() - new_height - 150  # 底部留出对话框空间
                    screen.blit(scaled_char, (char_x, char_y))
        
        # 绘制对话
        self.dialogue_system.draw(screen)
    
    def handle_event(self, event):
        """处理场景事件"""
        # 默认实现：点击鼠标左键或空格键推进对话
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            # 鼠标点击推进对话
            if self.dialogue_system.is_complete:
                return "dialogue_complete"
            else:
                self.dialogue_system.next_line()
                return True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                # 空格键推进对话
                if self.dialogue_system.is_complete:
                    return "dialogue_complete"
                else:
                    self.dialogue_system.next_line()
                    return True
        return False

class SceneManager:
    def __init__(self):
        # 当前场景
        self.current_scene = None
        # 场景字典
        self.scenes = {}
        # 场景转换相关
        self.is_transitioning = False
        self.transition_alpha = 0
        self.transition_type = 'none'  # 'fade_in', 'fade_out'
        self.next_scene_id = None
        # 显示提示文字
        self.show_continue_hint = False
        self.hint_timer = 0
    
    def add_scene(self, scene_id, scene):
        """添加场景"""
        self.scenes[scene_id] = scene
    
    def set_scene(self, scene_id):
        """切换到指定场景"""
        if scene_id in self.scenes:
            # 开始淡出效果
            self.transition_type = 'fade_out'
            self.transition_alpha = 0
            self.next_scene_id = scene_id
            self.is_transitioning = True
            return True
        return False
    
    def update_transition(self, dt):
        """更新场景过渡效果"""
        if not self.is_transitioning:
            return False
            
        # 更新透明度
        if self.transition_type == 'fade_out':
            self.transition_alpha += TRANSITION_SPEED * dt
            if self.transition_alpha >= 255:
                # 淡出完成，切换场景
                self.transition_alpha = 255
                self.current_scene = self.scenes[self.next_scene_id]
                print(f"切换到场景: {self.next_scene_id}")
                self.transition_type = 'fade_in'
                # 重置角色入场动画
                for character_id in self.current_scene.characters:
                    self.current_scene.resource_manager.set_character_position(character_id, 
                                                                           (-300, 0))  # 角色从屏幕左侧进入
        elif self.transition_type == 'fade_in':
            self.transition_alpha -= TRANSITION_SPEED * dt
            if self.transition_alpha <= 0:
                # 淡入完成
                self.transition_alpha = 0
                self.is_transitioning = False
                self.transition_type = 'none'
                # 开始角色入场动画
                self.current_scene.start_character_entrance()
                
        return True
    
    def update_hint(self, dt):
        """更新继续提示"""
        if self.current_scene and self.current_scene.dialogue_system.is_complete:
            # 对话完成后显示提示
            self.show_continue_hint = True
            self.hint_timer += dt
        else:
            self.show_continue_hint = False
            self.hint_timer = 0
    
    def update(self, dt):
        """更新当前场景"""
        # 更新过渡效果
        transitioning = self.update_transition(dt)
        
        # 更新提示
        self.update_hint(dt)
        
        # 如果不在过渡中，更新场景
        if not transitioning and self.current_scene:
            self.current_scene.update(dt)
    
    def draw(self, screen):
        """绘制当前场景"""
        if self.current_scene:
            self.current_scene.draw(screen)
            
            # 绘制过渡效果
            if self.is_transitioning:
                transition_surface = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
                transition_surface.fill(BLACK)
                transition_surface.set_alpha(int(self.transition_alpha))
                screen.blit(transition_surface, (0, 0))
            
            # Draw continue hint
            if self.show_continue_hint:
                # Blinking effect
                if int(self.hint_timer * 2) % 2 == 0:
                    font = pygame.font.SysFont(FONT_PATH, FONT_SIZE)
                    hint_text = font.render("Click left mouse button or press SPACE to continue", True, WHITE)
                    text_rect = hint_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT - 50))
                    # Add text background for better readability
                    bg_rect = text_rect.inflate(20, 10)
                    pygame.draw.rect(screen, (0, 0, 0, 128), bg_rect)
                    screen.blit(hint_text, text_rect)
    
    def handle_event(self, event):
        """处理当前场景的事件"""
        if self.current_scene:
            return self.current_scene.handle_event(event)
        return False

# ======================
# 剧本类
# ======================
class DramaScript:
    def __init__(self):
        # Define scene information
        self.scenes = {
            "intro": {
                "background": "z1",  # Using z1.png as background
                "characters": ["z2"],  # Using z2.jpg as main character
                "dialogue": [
                    "Narrator: This is a story about college memories...",
                    "Li Ming: Hey, long time no see!",
                    "Li Ming: Back at our alma mater today, everything feels the same.",
                    "Li Ming: I remember we used to chat here often during college."
                ]
            },
            "flashback": {
                "background": "z3",  # Using z3.jpg as flashback scene background
                "characters": ["z2", "z4"],  # Two characters in flashback
                "dialogue": [
                    "Narrator: Memories flash back to four years ago...",
                    "Zhang Hua: Li Ming, look at this club recruitment poster!",
                    "Li Ming: Wow, the photography club looks interesting!",
                    "Zhang Hua: Let's join together, we can learn photography!",
                    "Li Ming: Sure, this will definitely enrich our college life."
                ]
            },
            "cafe": {
                "background": "z6",  # Using z6.jpg as cafe background
                "characters": ["z2"],  # Li Ming alone in the cafe
                "dialogue": [
                    "Li Ming: After graduation, everyone went their separate ways.",
                    "Li Ming: I wonder how Zhang Hua is doing now?",
                    "Li Ming: I remember we used to study here at this cafe."
                ]
            },
            "reunion": {
                "background": "z7",  # Using z7.jpg as reunion scene background
                "characters": ["z2", "z8"],  # Li Ming and Zhang Hua reunion
                "dialogue": [
                    "Zhang Hua: Li Ming! It's really you!",
                    "Li Ming: Zhang Hua! I never expected to meet you here!",
                    "Zhang Hua: You haven't changed much, still the same.",
                    "Li Ming: Neither have you, still full of energy.",
                    "Zhang Hua: After graduation, I became a photographer.",
                    "Li Ming: Really? That's amazing!",
                    "Li Ming: It's all because of the photography club we joined in college.",
                    "Zhang Hua: Yes, that time really changed my life."
                ]
            },
            "ending": {
                "background": "z9",  # Using z9.jpg as ending scene background
                "characters": ["z2", "z8"],  # Both main characters together
                "dialogue": [
                    "Narrator: Sometimes, a small decision can change a person's life.",
                    "Narrator: College time is short, but leaves the most precious memories.",
                    "Narrator: Friendship is the most beautiful scenery in life.",
                    "Narrator: The story ends, but memories last forever..."
                ]
            }
        }
        
        # 场景顺序
        self.scene_order = ["intro", "flashback", "cafe", "reunion", "ending"]
    
    def get_scene_info(self, scene_id):
        """获取场景信息"""
        return self.scenes.get(scene_id)
    
    def get_scene_order(self):
        """获取场景顺序"""
        return self.scene_order
    
    def get_next_scene(self, current_scene_id):
        """获取下一个场景ID"""
        if current_scene_id in self.scene_order:
            current_index = self.scene_order.index(current_scene_id)
            if current_index < len(self.scene_order) - 1:
                return self.scene_order[current_index + 1]
        return None

# ======================
# 游戏主循环
# ======================

def main():
    # 初始化Pygame
    pygame.init()
    
    # 创建游戏窗口
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption(GAME_TITLE)
    
    # 创建时钟对象控制帧率
    clock = pygame.time.Clock()
    
    # 初始化游戏组件
    resource_manager = ResourceManager()
    dialogue_system = DialogueSystem()
    scene_manager = SceneManager()
    drama_script = DramaScript()
    
    # 加载所有资源
    print("正在加载游戏资源...")
    resource_manager.load_all_resources()
    
    # 根据剧本创建场景
    current_scene_id = None
    for scene_id in drama_script.get_scene_order():
        # 获取场景信息
        scene_info = drama_script.get_scene_info(scene_id)
        if scene_info:
            # 创建场景
            scene = Scene(scene_id, resource_manager, dialogue_system)
            
            # 设置场景属性
            scene.set_background(scene_info["background"])
            
            # 添加角色并设置位置
            for i, character_id in enumerate(scene_info["characters"]):
                # 根据角色索引设置不同的位置
                position_x = SCREEN_WIDTH // 3 if i == 0 else SCREEN_WIDTH * 2 // 3
                scene.add_character(character_id, (position_x, 0))
            
            # 设置对话
            scene.set_dialogue(scene_info["dialogue"])
            
            # 添加场景到管理器
            scene_manager.add_scene(scene_id, scene)
            
            # 设置第一个场景为当前场景
            if current_scene_id is None:
                current_scene_id = scene_id
    
    # 切换到第一个场景
    if current_scene_id:
        scene_manager.set_scene(current_scene_id)
    
    # 游戏主循环标志
    running = True
    
    # 游戏主循环
    print("Game started!")
    while running:
        # 计算帧时间
        dt = clock.tick(FPS) / 1000.0  # 转换为秒
        
        # 处理事件
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                # 按ESC键退出游戏
                if event.key == pygame.K_ESCAPE:
                    running = False
            else:
                # 处理场景事件
                result = scene_manager.handle_event(event)
                if result == "dialogue_complete":
                    # 对话完成，切换到下一个场景
                    if current_scene_id:
                        next_scene_id = drama_script.get_next_scene(current_scene_id)
                        if next_scene_id:
                            current_scene_id = next_scene_id
                            scene_manager.set_scene(current_scene_id)
                        else:
                            # All scenes completed, show end message
                            print("Game completed!")
                            running = False
        
        # 更新场景
        scene_manager.update(dt)
        
        # 清空屏幕
        screen.fill(WHITE)
        
        # 绘制场景
        scene_manager.draw(screen)
        
        # 更新显示
        pygame.display.flip()
    
    # 退出游戏
    print("Thank you for playing!")
    pygame.quit()
    sys.exit()

# 运行游戏
if __name__ == "__main__":
    main()