import pygame
import pygame.font

from pygame.locals import *
from gacha_items import GachaItems
from pygame.sprite import Sprite


class GachaImagesShow(Sprite):
    """ガチャのイメージ図を管理するクラス"""
    def __init__(self, ai_game):
        """イメージ図を初期化し、開始時の位置を設定する"""
        super().__init__()
        self.screen = ai_game.screen
        #self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # 登用武将名とレアリティなど表示用のフォントを設定する
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont("meiryomeiryomeiryouimeiryouiitalic", 24)   
        self.items = GachaItems()
        self.rarity_names = {5: "星5", 4: "星4", 3: "星3"}

    def one_time_gacha_image_blitme(self, id):
        """イメージ図の画像を読み込み、サイズを取得する"""
        self.image = pygame.image.load("./images/ID{}.png".format(id))
        self.gacha_image_rect = self.image.get_rect()        

        # イメージ図の水平位置の浮動小数点数を格納する
        #self.x = float(self.gacha_image_rect.x)

        # 新しいイメージ図を画面下部の中央に配置する
        self.gacha_image_rect.center = self.screen_rect.center
        
        """イメージ図を現在位置に描画する"""
        self.screen.blit(self.image, self.gacha_image_rect)

        # 登用武将名、レアリティのテキストを作成する
        self.rarity_names = self.rarity_names
        self.items = self.items.table
        self.items_name = str(self.items[id]["item_name"])
        self.items_rarity = str(self.rarity_names[self.items[id]["rarity"]])
        self.gacha_text_color = self.items[id]["text_color"]

        self.items_name_image = self.font.render(self.items_name, True,
                self.gacha_text_color, (0, 0, 0))
        
        self.items_rarity_image = self.font.render(self.items_rarity, True,
                self.gacha_text_color, (0, 0, 0))

        # ガチャイメージの上下に登用武将名、レアリティのテキストを表示する
        self.items_name_image_rect = self.items_name_image.get_rect()
        self.items_name_image_rect.midtop = self.gacha_image_rect.midbottom

        self.items_rarity_image_rect = self.items_rarity_image.get_rect()
        self.items_rarity_image_rect.midbottom = self.gacha_image_rect.midtop

        self.one_time_gacha_image_blit()

    def one_time_gacha_image_blit(self):
        self.screen.blit(self.items_name_image, self.items_name_image_rect)
        self.screen.blit(self.items_rarity_image, self.items_rarity_image_rect)        
    

    def five_times_gacha_images_blitme(self, id, times, id_lists, gacha_images_file):
        """イメージ図の画像を読み込み、サイズを取得する"""
        self.id = id

        for i in range (0, times + 1):
            for id in id_lists[times:times + 1]:
                self.image = pygame.image.load("{}".format(gacha_images_file[i]))
                self.gacha_image_rect = self.image.get_rect()           
                self.screen_adjust = i*205            

                # イメージ図の水平位置の浮動小数点数を格納する
                #self.x = float(self.gacha_image_rect.x)

                # 新しいイメージ図を画面下部の中央に配置する
                self.gacha_image_rect.centerx = 190 + self.screen_adjust
                self.gacha_image_rect.centery = self.screen_rect.centery

                
                
                
                # 登用武将名、レアリティのテキストを作成する
                self.rarity_names = self.rarity_names
                self.items = GachaItems()
                self.items = self.items.table
                self.items_name = str(self.items[id_lists[i]]["item_name"])
                self.items_rarity = str(self.rarity_names[self.items[id_lists[i]]["rarity"]])
                self.gacha_text_color = self.items[id_lists[i]]["text_color"]

                self.items_name_image = self.font.render(self.items_name, True,
                        self.gacha_text_color, (0, 0, 0))
                
                self.items_rarity_image = self.font.render(self.items_rarity, True,
                        self.gacha_text_color, (0, 0, 0))

                # ガチャイメージの上下に登用武将名、レアリティのテキストを表示する
                self.items_name_image_rect = self.items_name_image.get_rect()
                self.items_name_image_rect.midtop = self.gacha_image_rect.midbottom

                self.items_rarity_image_rect = self.items_rarity_image.get_rect()
                self.items_rarity_image_rect.midbottom = self.gacha_image_rect.midtop
                self.five_times_gacha_image_blit()

    def five_times_gacha_image_blit(self):
        """イメージ図を現在位置に描画する"""
        self.screen.blit(self.image, self.gacha_image_rect)
        self.screen.blit(self.items_name_image, self.items_name_image_rect)
        self.screen.blit(self.items_rarity_image, self.items_rarity_image_rect)
