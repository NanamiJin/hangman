from datetime import datetime
import sys
import pygame

from pygame.locals import *
from time import sleep
from settings import Settings
from game_stats import GameStats
from scoreboard import Scoreboard
from button_images import Button
from gacha import Gacha
from gacha_images_show import GachaImagesShow


# Main
class GachaSimulator():
    """ゲームのアセットと動作を管理する全体的なクラス"""
    
    def __init__(self):
        """ゲームを初期化し、ゲームのリソースを作成する"""
        pygame.init()
        
        self.settings = Settings()
        self.gacha = Gacha()
        self.gis = GachaImagesShow(ai_game = self.settings)
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        self.bfull = False
        self.icon = pygame.image.load('images/gacha_ico_image.ico')
        pygame.display.set_icon(self.icon)       
        pygame.display.set_caption("ようこそ、三国志真戦の名将ガチャシミュレーター")
        self.screen.blit(self.settings.img_bg, (0, 67))
        
        # ゲームの統計情報を格納するインスタンスを生成する
        self.stats = GameStats(self)
        self.sb = Scoreboard(self)
          
        # リセットボタンを作成する
        self.play_button = Button(self, "リセット")
    
    def run_game(self):
        """ゲームのメインループを開始する"""
        
        while True:            
            self._check_keyboard_events()            
            self._update_screen()
       
    def _check_keyboard_events(self):
        # キーボードとマウスのイベントを監視する
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                now = datetime.now()
                filename = './output/acquired_star5_list_' + now.strftime('%Y%m%d_%H%M') + '.csv'
                with open (filename, "w", encoding="utf_8_sig") as acquired_star5_list:
                    acquired_star5_list.write("日付: " + now.strftime('%Y/%m/%d_%H%M') + "; "+ str(self.sb.acquired_star5_items_list))
                                                                  
                sys.exit()
           
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)

            #elif event.type == pygame.KEYUP:
                #self._check_keyup_events(event)
            
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)
    

    def _check_keydown_events(self, event):
        """キーを押すイベントに対応する"""
        if event.key == pygame.K_F2:
            if self.bfull:
                self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
                self.bfull = False            
            else:
                self.screen = pygame.display.set_mode((0, 0), FULLSCREEN)
                self.bfull = True
       
        elif event.key == pygame.K_q:
            sys.exit()

        #elif event.key == pygame.K_SPACE:
            #self._fire_bullet()

    def _check_play_button(self, mouse_pos):
        """プレイヤーがPlayボタンをクリックしたら新規ゲームを開始する"""
        button_gacha_one_time_clicked = self.play_button.msg_gacha_one_time_rect.collidepoint(mouse_pos)
        button_gacha_five_times_clicked = self.play_button.msg_gacha_five_times_rect.collidepoint(mouse_pos)
        button_reset_clicked = self.play_button.msg_reset_rect.collidepoint(mouse_pos)
        
        if button_gacha_one_time_clicked and not self.stats.game_active:
            # ゲームの設定値をセットする           
            self.gacha.rare_gacha_one_time()
            self.stats.total_count = self.stats.total_count + 1
            self.stats.total_price = self.stats.total_price + 198
            self.settings.total_rarity_lists = self.gacha.total_rarity_lists
            self.settings.total_results = self.gacha.total_results

            # ゲームの統計情報をセットする
            self.sb.prep_images()

        if button_gacha_five_times_clicked and not self.stats.game_active:
            # ゲームの設定値をセットする
            self.gacha.rare_gacha_five_times()
            self.stats.total_count = self.stats.total_count + 5
            self.stats.total_price = self.stats.total_price + 948
            self.settings.total_rarity_lists = self.gacha.total_rarity_lists
            self.settings.total_results = self.gacha.total_results

            # ゲームの統計情報をセットする
            self.sb.prep_images()

        if button_reset_clicked and not self.stats.game_active:
            # ゲームの設定値をリセットする
            self.gacha.rest()
            self.stats.total_price = 0
            self.stats.total_count = 0
            self.total_rarity_lists = []
            self.total_results = []
            self.sb.show_score()
            
            # 一時停止する
            sleep(0.01)
            
    def _update_screen(self):    
        #画面上の画像を更新し、新しい画面に切り替える
        #self.screen.fill(self.settings.bg_color)

        # ガチャ情報を描画する
        self.sb.show_score()
        
        # ゲームが非アクティブ状態のときに「Play」ボタンを描画する
        if not self.stats.game_active:
            self.play_button.draw_button()
            

        # 最新の状態の画面を表示する        
        pygame.display.flip()

if __name__ == '__main__':
    # ゲームのインスタンスを作成し、ゲームを実行する
    ai = GachaSimulator()
    ai.run_game()    
