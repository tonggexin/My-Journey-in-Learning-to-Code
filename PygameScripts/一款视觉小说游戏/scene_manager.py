# 场景管理器 - 负责管理游戏中的不同场景和转换

class SceneManager:
    def __init__(self):
        # 当前场景
        self.current_scene = None
        # 场景字典
        self.scenes = {}
        # 场景转换中的标志
        self.is_transitioning = False
    
    def add_scene(self, scene_id, scene):
        """添加场景"""
        self.scenes[scene_id] = scene
    
    def set_scene(self, scene_id):
        """切换到指定场景"""
        if scene_id in self.scenes:
            self.current_scene = self.scenes[scene_id]
            self.is_transitioning = False
            print(f"切换到场景: {scene_id}")
            return True
        return False
    
    def update(self, dt):
        """更新当前场景"""
        if self.current_scene:
            self.current_scene.update(dt)
    
    def draw(self, screen):
        """绘制当前场景"""
        if self.current_scene:
            self.current_scene.draw(screen)
    
    def handle_event(self, event):
        """处理当前场景的事件"""
        if self.current_scene:
            return self.current_scene.handle_event(event)
        return False

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
    
    def update(self, dt):
        """更新场景状态"""
        pass
    
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

# 导入pygame，因为在Scene类中使用了pygame事件
import pygame