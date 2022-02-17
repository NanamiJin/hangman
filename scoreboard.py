import pygame.font

from gacha import Gacha

class Scoreboard:
    """ガチャの情報をレポートするクラス"""

    def __init__(self, ai_game):
        """金珠と登用回数を記録するための属性を初期化する"""
        self.ai_game = ai_game
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.data = Gacha()
        self.settings = ai_game.settings
        self.stats = ai_game.stats
        self.acquired_star5_items_list = []
        # 登用武将、金珠と登用回数など表示用のフォントを設定する
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont("meiryomeiryomeiryouimeiryouiitalic", 24)

        self.prep_images()
    
    def prep_images(self):        
        # 金珠と登用回数等の初期画像を準備する        
        self.prep_total_count()
        self.prep_total_price()        
        self.prep_rarity_probability()
        self.prep_total_star5_items()
        self.prep_limit_star4or5_count()
        self.prep_acquired_star5_items()

    def prep_total_count(self):
        """登用回数を描画用の画像に変換する"""
        self.total_count = self.stats.total_count
        if  self.total_count == 0:
            count_str = ""
        
        elif self.total_count > 0:
            rounded_count = round(self.total_count, 0) 
            count_str = "合計: " + "{:,}".format(rounded_count) + " 回登用しました。"

        self.total_count_image = self.font.render(count_str, True,
                self.text_color, (0, 0, 0))
        
        # 画面の左上に登用回数を表示する
        self.total_count_rect = self.total_count_image.get_rect()
        self.total_count_rect.left = self.screen_rect.left + 20
        self.total_count_rect.top = 20 
    
    def prep_total_price(self):
        """金珠を描画用の画像に変換する"""
        self.total_price = self.stats.total_price
        if  self.total_count == 0:
            price_str = ""
        
        elif self.total_count > 0:
            rounded_price = round(self.total_price, 0) 
            price_str = "合計: " + "{:,}".format(rounded_price) + " 金珠でした。"

        self.total_price_image = self.font.render(price_str, True,
                self.text_color, (0, 0, 0))
        
        # 登用回数の下に合計消費金珠を表示する
        self.total_price_rect = self.total_price_image.get_rect()
        self.total_price_rect.left = self.total_count_rect.left 
        self.total_price_rect.top = self.total_count_rect.bottom + 10

    def prep_rarity_probability(self):
        """各レアリティの出率を描画用の画像に変換する"""
        self.rarity_lists = self.settings.total_rarity_lists
        if  self.total_count == 0:
             rarity_probability = ""
        
        elif self.total_count > 0:
            rarity_probability = "各レアリティの出率は 星3: " + str(round(100*self.rarity_lists.count("星3")/self.total_count, 2)) + "%  星4: " + str(round(100*self.rarity_lists.count("星4")/self.total_count, 2)) + "%  星5: "+ str(round(100*self.rarity_lists.count("星5")/self.total_count, 2)) + "%でした。"            

        self.rarity_probability_image = self.font.render(rarity_probability, True,
                self.text_color, (0, 0, 0))
        
        # 合計消費金珠の下に各レアリティの出率を表示する
        self.rarity_probability_rect = self.rarity_probability_image.get_rect()
        self.rarity_probability_rect.left = self.total_count_rect.left 
        self.rarity_probability_rect.top = self.total_price_rect.bottom + 10

    def prep_total_star5_items(self):
        if  self.total_count == 0:
             total_star5_items = ""
        
        elif self.total_count > 0:         
            total_star5_items = "星5武将は合計: " + str(self.rarity_lists.count("星5")) + " 回登用しました。"

        self.total_star5_items_image = self.font.render(total_star5_items, True,
                self.text_color, (0, 0, 0))
        
        # 各レアリティの出率の下に星5武将の登用回数を表示する
        self.total_star5_items_rect = self.total_star5_items_image.get_rect()
        self.total_star5_items_rect.left = self.total_count_rect.left
        self.total_star5_items_rect.top = self.rarity_probability_rect.bottom + 10

    def prep_limit_star4or5_count(self):
        """レアリティ確定登用回数を描画用の画像に変換する"""
        self.total_count = self.stats.total_count
        limit_star4or5_count = 5 - self.total_count % 5 

        if  self.total_count == 0:
            limit_star4or5_count_str = ""
        
        elif self.total_count > 0:           
            limit_star4or5_count_str = "あと{}回登用すると、必ず星4武将か星5武将を獲得する".format(limit_star4or5_count) 

        self.limit_star4or5_count_image = self.font.render(limit_star4or5_count_str, True,
                self.text_color, (0, 0, 0))
        
        # ガチャアイテムイメージの下にレアリティ確定登用までの回数を表示する
        self.limit_star4or5_count_rect = self.limit_star4or5_count_image.get_rect()
        self.limit_star4or5_count_rect.centerx = self.screen_rect.centerx
        self.limit_star4or5_count_rect.centery = self.screen_rect.centery + 180

    def prep_acquired_star5_items(self):
        #獲得した星5武将を描画用の画像に変換する
        self.total_results = self.settings.total_results
        
        if  self.total_count == 0:
            acquired_star5_items_str = ""
               
        elif self.total_count > 0 and self.rarity_lists.count("星5") == 0:
            acquired_star5_items_str = "獲得した星5武将: なし" 
        
        elif self.total_count > 0 and self.rarity_lists.count("星5") > 0:            
            acquired_star5_items_str = "獲得した星5武将: " + ", ".join(self.total_results)
            self.acquired_star5_items_list = ", ".join(self.total_results)        

        acquired_star5_items_str_text_1 = acquired_star5_items_str[:67]
        acquired_star5_items_str_text_2 = acquired_star5_items_str[67:134]

        if len(acquired_star5_items_str) < 201:
            acquired_star5_items_str_text_3 = acquired_star5_items_str[134:201]
        elif len(acquired_star5_items_str) > 200:
            acquired_star5_items_str_text_3 = acquired_star5_items_str[134:201] + "..."

        self.acquired_star5_items_image_1 = self.font.render(acquired_star5_items_str_text_1, True,
                (255,215,0), (0, 0, 0))
        
        # レアリティ確定登用までの回数の下に獲得した星5武将を表示する
        self.acquired_star5_items_rect_1 = self.acquired_star5_items_image_1.get_rect()
        self.acquired_star5_items_rect_1.left = self.total_count_rect.left
        self.acquired_star5_items_rect_1.top = self.limit_star4or5_count_rect.bottom + 60

        self.acquired_star5_items_image_2 = self.font.render(acquired_star5_items_str_text_2, True,
                (255,215,0), (0, 0, 0))
        
        # レアリティ確定登用までの回数の下に獲得した星5武将を表示する
        self.acquired_star5_items_rect_2 = self.acquired_star5_items_image_2.get_rect()
        self.acquired_star5_items_rect_2.left = self.total_count_rect.left
        self.acquired_star5_items_rect_2.top = self.acquired_star5_items_rect_1.bottom + 5

        self.acquired_star5_items_image_3 = self.font.render(acquired_star5_items_str_text_3, True,
                (255,215,0), (0, 0, 0))
        
        # レアリティ確定登用までの回数の下に獲得した星5武将を表示する
        self.acquired_star5_items_rect_3 = self.acquired_star5_items_image_3.get_rect()
        self.acquired_star5_items_rect_3.left = self.total_count_rect.left
        self.acquired_star5_items_rect_3.top = self.acquired_star5_items_rect_2.bottom + 5

    def show_score(self):
        """画面に金珠と登用回数、各レアリティ出率、星5武将の登用回数と確定登用までの回数を描画する"""
        self.screen.blit(self.total_count_image, self.total_count_rect)
        self.screen.blit(self.total_price_image, self.total_price_rect)                
        self.screen.blit(self.rarity_probability_image, self.rarity_probability_rect)       
        self.screen.blit(self.total_star5_items_image, self.total_star5_items_rect)
        self.screen.blit(self.limit_star4or5_count_image, self.limit_star4or5_count_rect)
        self.screen.blit(self.acquired_star5_items_image_1, self.acquired_star5_items_rect_1)
        self.screen.blit(self.acquired_star5_items_image_2, self.acquired_star5_items_rect_2)
        self.screen.blit(self.acquired_star5_items_image_3, self.acquired_star5_items_rect_3)

