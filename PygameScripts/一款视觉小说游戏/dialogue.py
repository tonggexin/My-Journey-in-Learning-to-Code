# 对话系统 - 负责管理和显示游戏中的对话内容

import pygame
from config import (
    SCREEN_WIDTH, SCREEN_HEIGHT, WHITE, BLACK, GRAY, 
    FONT_SIZE, FONT_PATH, DIALOGUE_BOX_HEIGHT, DIALOGUE_PADDING
)

class DialogueSystem:
    def __init__(self):
        # 当前对话索引
        self.current_line_index = 0
        # 对话文本列表
        self.dialogue_lines = []
        # 对话是否完成
        self.is_complete = False
        # 初始化字体
        self.font = pygame.font.SysFont(None, FONT_SIZE) if FONT_PATH is None else pygame.font.Font(FONT_PATH, FONT_SIZE)
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
    
    def next_line(self):
        """前进到下一行对话"""
        if self.current_line_index < len(self.dialogue_lines) - 1:
            self.current_line_index += 1
            return True
        else:
            self.is_complete = True
            return False
    
    def get_current_line(self):
        """获取当前对话行"""
        if 0 <= self.current_line_index < len(self.dialogue_lines):
            return self.dialogue_lines[self.current_line_index]
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
                # 绘制说话人名字（粗体）
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