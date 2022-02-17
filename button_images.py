import pygame.font
import pygame

from pygame.locals import *


class Button:


    def __init__(self, ai_game, msg_reset):
        """ボタンの属性を初期化する"""
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()

        # 登用ボタンの大きさと属性を設定する
        self.width, self.height = 200, 50
        self.reset_button_color = (0, 0, 0)
        
        self.text_color = (240, 240, 240)
        self.font = pygame.font.SysFont("meiryomeiryomeiryouimeiryouiitalic", 24)

        #　一回登用ボタンのイメージをロードする
        self.one_time_gacha_image = pygame.image.load("images/one_time_gacha_button.png")
        self.one_time_gacha_image_rect = self.one_time_gacha_image.get_rect()
        #　5回登用ボタンのイメージをロードする
        self.five_times_gacha_image = pygame.image.load("images/five_times_gacha_button.png")
        self.five_times_gacha_image_rect = self.five_times_gacha_image.get_rect()

        # ボタンのrectオブジェクトを生成し画面に配置する
        self.msg_gacha_one_time_rect = self.one_time_gacha_image_rect
        self.msg_gacha_one_time_rect.center = (345, 602)

        self.msg_gacha_five_times_rect = self.five_times_gacha_image_rect
        self.msg_gacha_five_times_rect.center = (840, 602)

        self.msg_reset_rect = pygame.Rect(0, 0, self.width, self.height)
        self.msg_reset_rect.center = (600, 602)

        # ボタンのメッセージは一度だけ準備する必要がある
        self._prep_msg(msg_reset)

    def _prep_msg(self, msg_reset):
        """リセットボタンを画像に変換し、ボタンを配置する"""
        self.msg_reset_image = self.font.render(msg_reset, True, self.text_color, self.reset_button_color)
        self.msg_reset_image_rect = self.msg_reset_image.get_rect()
        self.msg_reset_image_rect.center = self.msg_reset_rect.center 

    def draw_button(self):
        # ボタンを描画する
        self.screen.fill(self.reset_button_color, self.msg_reset_image_rect)
        #self.screen.fill(self.gacha_five_times_button_color, self.msg_gacha_five_times_rect)
        
        self.screen.blit(self.one_time_gacha_image, self.msg_gacha_one_time_rect)
        self.screen.blit(self.five_times_gacha_image, self.msg_gacha_five_times_rect)
        self.screen.blit(self.msg_reset_image, self.msg_reset_image_rect)

        
