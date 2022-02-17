from cgitb import reset
import streamlit as st
import random
from settings import Settings
from gacha_items import GachaItems
from gacha_images_show import GachaImagesShow

"""
# 三国志真戦名将ガチャシミュレーター仕様_ver.1.0について

・5.6%の確率で星5武将を獲得する

・36%の確率で星4武将を獲得する

・58.4%の確率で星3武将を獲得する

・5回登用するたびに、星4武将または星5武将を必ず獲得する

・登用すると30回以内に必ず星5武将を獲得できる。星5武将を獲得すると回数のカウントはリセットされ、そこからまた更に30以内に星5武将を獲得できる
　各種登用の確定枠は、別々に統計している

・シリーズ2までの各武将の登用出率が公式サイトに従い、設定されている

・リセットボタンを押すと、今までのガチャデータをリセットする（もう一回登用ボタンを押す、画面に反映される）
　ガチャシミュレーター終了後に獲得した星5武将のcsvデータが./outputに出力される

・メインアプリプログラム`/streamlit_app.py` は以下のように示す。
"""

with st.echo(code_location='below'):
    one_time_gacha_button = st.button('1回登用')
    five_times_gacha_button = st.button('5回登用')
    reset_button = st.button('リセット')
    
    def __init__(self):
        #super().__init__()
        self._count = 0
        self._price = 0
        
        self.total_results = []
        self.total_id_lists = []
        self.total_rarity_lists = []
        self.rarity_names = {5: "星5", 4: "星4", 3: "星3"}
              
    # ガチャの値段と回数に関する設定
    def getcount(self):
        return self._count

    def setcount(self, count):
        self._count = count

    def getprice(self):
        return self._price

    def setprice(self, price):
        self._price = price
   
    count = property(getcount, setcount)
    price = property(getprice, setprice)

    def gacha(self,gacha_items: dict, times: int=1) -> list:
        # 抽選に必要な、IDと重みの辞書を作成
        lots = {key: info["weight"] for key, info in gacha_items.items()}
        return random.choices(tuple(lots), weights=lots.values(), k=times)

    def gacha_omake(self, gacha_items: dict, times: int, omake_rarity: int) -> list:
        # おまけの対象をレアリティ制限で辞書を作成
        omake = {key: info for key, info in gacha_items.items() if info["rarity"] >= omake_rarity}
        ids = self.gacha(gacha_items, times)
        ids.extend(self.gacha(omake))
        return ids

    def rare_gacha_one_time(self):
        """1回ガチャ回すときのカウンター"""
        self.settings = Settings()
        self.items = GachaItems()       
        self.gacha_images_show = GachaImagesShow(ai_game = self.settings)
        self.price = self.price + 198
        self.count = self.count + 1
                
        """1回登用"""       
        self.results = []
        self.total_results = self.total_results
        self.id_lists = []
        self.total_id_lists = self.total_id_lists
        self.rarity_lists = self.total_rarity_lists
        
        self.rarity_names = self.rarity_names
        self.items = self.items.table
        
        if self.count % 5 > 0:
            times = 1
            ids = self.gacha(self.items, times)
            
            for id in ids:
                self.results.append("ID:%d, %s, %s" % (id, self.rarity_names[self.items[id]["rarity"]], self.items[id]["item_name"]))
                if id > 5000:
                    self.total_results.append(self.items[id]["item_name"])
                self.id_lists.append(id)
                self.total_id_lists.append(id)
                self.rarity_lists.append(self.rarity_names[self.items[id]["rarity"]])
                #self.settings.total_rarity_lists.append(self.rarity_names[self.items[id]["rarity"]])
                self.gacha_images_show.one_time_gacha_image_blitme(id)
                    

        elif self.count % 5 == 0 and self.count % 30 == 0 and self.rarity_lists.count("星5") == 0:
            times = 0
            omake_rarity = 5
            ids = self.gacha_omake(self.items, times, omake_rarity)
            
            for id in ids:           
                self.results.append("ID:%d, %s, %s" % (id, self.rarity_names[self.items[id]["rarity"]], self.items[id]["item_name"]))
                if id > 5000:
                    self.total_results.append(self.items[id]["item_name"])
                self.id_lists.append(id)
                self.total_id_lists.append(id)
                self.rarity_lists.append(self.rarity_names[self.items[id]["rarity"]])
                #self.settings.total_rarity_lists.append(self.rarity_names[self.items[id]["rarity"]])
                self.gacha_images_show.one_time_gacha_image_blitme(id)
                
        elif self.count % 5 == 0:
            times = 0
            omake_rarity = 4
            ids = self.gacha_omake(self.items, times, omake_rarity)
            
            for id in ids:           
                self.results.append("ID:%d, %s, %s" % (id, self.rarity_names[self.items[id]["rarity"]], self.items[id]["item_name"]))
                if id > 5000:
                    self.total_results.append(self.items[id]["item_name"])
                self.id_lists.append(id)
                self.total_id_lists.append(id)
                self.rarity_lists.append(self.rarity_names[self.items[id]["rarity"]])
                #self.settings.total_rarity_lists.append(self.rarity_names[self.items[id]["rarity"]])
                self.gacha_images_show.one_time_gacha_image_blitme(id)
       
        return self.results 
    
    def rare_gacha_five_times(self):
        """5回ガチャ回すときのカウンター"""        
        self.settings = Settings()
        self.items = GachaItems()
        self.gacha_images_show = GachaImagesShow(ai_game = self.settings)
        self.price = self.price + 948
        self.count = self.count + 5
        
        """5回登用"""
        self.results = []
        self.total_results = self.total_results
        self.id_lists = []
        self.total_id_lists = self.total_id_lists
        self.rarity_lists = self.total_rarity_lists
        self.items = self.items.table
        self.gacha_images_file = []

        if self.count % 5 == 0 and self.count % 30 == 0 and self.rarity_lists.count("星5") == 0:
            times = 4
            omake_rarity = 5
            ids = self.gacha_omake(self.items, times, omake_rarity)

            for id in ids:           
                self.results.append("ID:%d, %s, %s" % (id, self.rarity_names[self.items[id]["rarity"]], self.items[id]["item_name"]))
                if id > 5000:
                    self.total_results.append(self.items[id]["item_name"])
                self.id_lists.append(id)
                self.total_id_lists.append(id)
                self.rarity_lists.append(self.rarity_names[self.items[id]["rarity"]])
                #self.settings.total_rarity_lists.append(self.rarity_names[self.items[id]["rarity"]])
                self.gacha_images_file.append("./images" + "/ID{}.png".format(id))
                self.gacha_images_show.five_times_gacha_images_blitme(id, times, self.id_lists, self.gacha_images_file)

        elif self.count % 5 == 0 or self.count % 5 > 0:
            times = 4
            omake_rarity = 4
            ids = self.gacha_omake(self.items, times, omake_rarity)
            
            for id in ids:           
                self.results.append("ID:%d, %s, %s" % (id, self.rarity_names[self.items[id]["rarity"]], self.items[id]["item_name"]))
                if id > 5000:
                    self.total_results.append(self.items[id]["item_name"])
                self.id_lists.append(id)
                self.total_id_lists.append(id)
                self.rarity_lists.append(self.rarity_names[self.items[id]["rarity"]])
                #self.settings.total_rarity_lists.append(self.rarity_names[self.items[id]["rarity"]])
                self.gacha_images_file.append("./images" + "/ID{}.png".format(id))
                self.gacha_images_show.five_times_gacha_images_blitme(id, times, self.id_lists, self.gacha_images_file)
                
        return self.results
    
    def rest(self):
        self._count = 0
        self._price = 0
        
        self.total_results = []
        self.total_id_lists = []
        self.total_rarity_lists = []

        return  


