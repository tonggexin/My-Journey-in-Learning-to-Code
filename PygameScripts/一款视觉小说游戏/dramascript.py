# 剧本文件 - 包含游戏中的对话和场景信息

# 定义故事场景和对话
# 故事内容："我和我的本科同学"

class DramaScript:
    def __init__(self):
        # 定义场景信息
        self.scenes = {
            "intro": {
                "background": "z1",  # 使用z1.png作为背景
                "characters": ["z2"],  # 使用z2.jpg作为主要角色
                "dialogue": [
                    "旁白: 这是一个关于大学回忆的故事...",
                    "李明: 嗨，好久不见啊！",
                    "李明: 今天回到母校，感觉一切都没变呢。",
                    "李明: 记得大学时我们经常在这里聊天。"
                ]
            },
            "flashback": {
                "background": "z3",  # 使用z3.jpg作为回忆场景背景
                "characters": ["z2", "z4"],  # 两个角色在回忆场景中
                "dialogue": [
                    "旁白: 记忆回到了四年前...",
                    "张华: 李明，你看这个社团招新的海报！",
                    "李明: 哇，摄影社团看起来很有趣！",
                    "张华: 我们一起报名吧，正好可以学习拍照！",
                    "李明: 好啊，这一定能丰富我们的大学生活。"
                ]
            },
            "cafe": {
                "background": "z6",  # 使用z6.jpg作为咖啡厅背景
                "characters": ["z2"],  # 李明独自在咖啡厅
                "dialogue": [
                    "李明: 毕业后大家都各奔东西了。",
                    "李明: 不知道张华现在怎么样了？",
                    "李明: 记得以前我们经常来这家咖啡厅复习。"
                ]
            },
            "reunion": {
                "background": "z7",  # 使用z7.jpg作为重逢场景背景
                "characters": ["z2", "z8"],  # 李明和张华重逢
                "dialogue": [
                    "张华: 李明！真的是你！",
                    "李明: 张华！没想到在这里遇见你！",
                    "张华: 你变化不大，还是老样子。",
                    "李明: 你也是啊，还是那么有活力。",
                    "张华: 毕业后我成为了一名摄影师。",
                    "李明: 真的吗？太棒了！",
                    "李明: 这都是因为大学时我们一起参加的摄影社团。",
                    "张华: 是啊，那段时光真的改变了我的人生。"
                ]
            },
            "ending": {
                "background": "z9",  # 使用z9.jpg作为结尾场景背景
                "characters": ["z2", "z8"],  # 两位主角在一起
                "dialogue": [
                    "旁白: 有时候，一个小小的决定可以改变人的一生。",
                    "旁白: 大学时光虽然短暂，却留下了最珍贵的回忆。",
                    "旁白: 友情，是人生中最美丽的风景。",
                    "旁白: 故事结束，但回忆永存..."
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