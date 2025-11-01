# 资源管理器 - 负责加载和管理游戏中的图像资源

import pygame
import os
from config import SCREEN_WIDTH, SCREEN_HEIGHT

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