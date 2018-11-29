class Settings():
    """存储外星人入侵 的所有设置的类"""

    def __init__(self):
        """初始化游戏的设置"""
        # 屏幕设置
        self.screen_width = 1200
        self.screen_height = 600
        self.bg_color = (230, 230, 230)
        # 飞船速度的设置
        self.ship_speed_factor = 10.5
        # 子弹设置
        self.bullet_speed_factor = 10
        self.bullet_width = 3
        self.bullet_height = 5
        self.bullet_color = (60, 60, 60)
        self.bullet_allowed = 6 #一屏允许的最大子弹数
        self.alien_speed_factor = 3 #外星人移动速度
