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
        self.bullet_speed_factor = 20
        self.bullet_width = 60
        self.bullet_height = 5
        self.bullet_color = (60, 60, 60)
        self.bullet_allowed = 60 #一屏允许的最大子弹数
        self.alien_speed_factor = 10 #外星人移动速度
        self.fleet_drop_speed = 50
        self.fleet_direction = 1#1 表示右移, -1表示左移
        self.ship_limit = 3#玩家最多拥有的飞船数量

