import pygame


class Settings():
    """"ガチャシミュレーターの全設定を格納するクラス"""
   
    def __init__(self):
        """ゲームの初期設定"""
        # 画面に関する設定
        self.screen_width = 1200
        self.screen_height = 750
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        self.img_bg = pygame.image.load('images\gacha_background_image.png')        
        self.bg_color = (230, 230, 230)
        self.price = 0
        self.count = 0
        self.total_rarity_lists = []
        self.total_results = []  
