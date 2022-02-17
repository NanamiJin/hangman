from cgitb import reset
import streamlit as st
import random
#from settings import Settings
#from gacha_items import GachaItems
#from gacha_images_show import GachaImagesShow

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
 


 
#ガチャの抽選プログラム   
    def __init__(self):
        #super().__init__()
        self._count = 0
        self._price = 0
        
        self.total_results = []
        self.total_id_lists = []
        self.total_rarity_lists = []
        self.rarity_names = {5: "星5", 4: "星4", 3: "星3"}
    
    #ガチャのテーブルプログラム
    def gacha_table(self):
        self.table = {
            # 星5武将
            5001:{"weight": 8, "rarity": 5, "item_name": "孫堅", "text_color": (255,215,0)},
            5002:{"weight": 8, "rarity": 5, "item_name": "董卓", "text_color": (255,215,0)},
            5003:{"weight": 8, "rarity": 5, "item_name": "張角", "text_color": (255,215,0)},
            5004:{"weight": 8, "rarity": 5, "item_name": "袁紹", "text_color": (255,215,0)},
            5005:{"weight": 8, "rarity": 5, "item_name": "蔡琰", "text_color": (255,215,0)},
            5006:{"weight": 8, "rarity": 5, "item_name": "夏侯惇", "text_color": (255,215,0)},
            5007:{"weight": 8, "rarity": 5, "item_name": "呂蒙", "text_color": (255,215,0)},
            5008:{"weight": 8, "rarity": 5, "item_name": "顔良", "text_color": (255,215,0)},
            5009:{"weight": 8, "rarity": 5, "item_name": "程昱", "text_color": (255,215,0)},
            5010:{"weight": 8, "rarity": 5, "item_name": "于禁", "text_color": (255,215,0)},
            5011:{"weight": 8, "rarity": 5, "item_name": "程普", "text_color": (255,215,0)},
            5012:{"weight": 8, "rarity": 5, "item_name": "華雄", "text_color": (255,215,0)},
            5013:{"weight": 8, "rarity": 5, "item_name": "夏侯淵", "text_color": (255,215,0)},
            5014:{"weight": 8, "rarity": 5, "item_name": "曹仁", "text_color": (255,215,0)},
            5015:{"weight": 8, "rarity": 5, "item_name": "甘寧", "text_color": (255,215,0)},
            5016:{"weight": 8, "rarity": 5, "item_name": "華佗", "text_color": (255,215,0)},
            5017:{"weight": 8, "rarity": 5, "item_name": "鄧艾", "text_color": (255,215,0)},
            5018:{"weight": 8, "rarity": 5, "item_name": "法正", "text_color": (255,215,0)},
            5019:{"weight": 8, "rarity": 5, "item_name": "馬騰", "text_color": (255,215,0)},
            5020:{"weight": 8, "rarity": 5, "item_name": "黄蓋", "text_color": (255,215,0)},
            5021:{"weight": 8, "rarity": 5, "item_name": "左慈", "text_color": (255,215,0)},
            5022:{"weight": 8, "rarity": 5, "item_name": "黄忠", "text_color": (255,215,0)},
            5023:{"weight": 8, "rarity": 5, "item_name": "貂蝉", "text_color": (255,215,0)},
            5024:{"weight": 8, "rarity": 5, "item_name": "文醜", "text_color": (255,215,0)},
            5025:{"weight": 8, "rarity": 5, "item_name": "荀彧", "text_color": (255,215,0)},            
            5026:{"weight": 8, "rarity": 5, "item_name": "曹丕", "text_color": (255,215,0)},
            5027:{"weight": 8, "rarity": 5, "item_name": "孫策", "text_color": (255,215,0)},
            5028:{"weight": 8, "rarity": 5, "item_name": "張昭", "text_color": (255,215,0)},
            5029:{"weight": 8, "rarity": 5, "item_name": "高順", "text_color": (255,215,0)},
            5030:{"weight": 8, "rarity": 5, "item_name": "陳到", "text_color": (255,215,0)},
            5031:{"weight": 8, "rarity": 5, "item_name": "郭嘉", "text_color": (255,215,0)},
            5032:{"weight": 8, "rarity": 5, "item_name": "徐庶", "text_color": (255,215,0)},
            5033:{"weight": 8, "rarity": 5, "item_name": "陳羣", "text_color": (255,215,0)},
            5034:{"weight": 8, "rarity": 5, "item_name": "田豊", "text_color": (255,215,0)},
            5035:{"weight": 8, "rarity": 5, "item_name": "徐晃", "text_color": (255,215,0)},
            5036:{"weight": 8, "rarity": 5, "item_name": "大喬", "text_color": (255,215,0)},
            5037:{"weight": 8, "rarity": 5, "item_name": "曹純", "text_color": (255,215,0)},
            5038:{"weight": 8, "rarity": 5, "item_name": "于吉", "text_color": (255,215,0)},
            5039:{"weight": 8, "rarity": 5, "item_name": "李儒", "text_color": (255,215,0)},
            5040:{"weight": 8, "rarity": 5, "item_name": "公孫瓚", "text_color": (255,215,0)},
            5041:{"weight": 8, "rarity": 5, "item_name": "小喬", "text_color": (255,215,0)},
            5042:{"weight": 8, "rarity": 5, "item_name": "祝融", "text_color": (255,215,0)},
            5043:{"weight": 8, "rarity": 5, "item_name": "王平", "text_color": (255,215,0)},
            5044:{"weight": 8, "rarity": 5, "item_name": "兀突骨", "text_color": (255,215,0)},
            5045:{"weight": 8, "rarity": 5, "item_name": "曹植", "text_color": (255,215,0)},
            5046:{"weight": 8, "rarity": 5, "item_name": "張紘", "text_color": (255,215,0)},
            5047:{"weight": 8, "rarity": 5, "item_name": "張氏", "text_color": (255,215,0)},
            5048:{"weight": 8, "rarity": 5, "item_name": "龐徳", "text_color": (255,215,0)},
            5049:{"weight": 8, "rarity": 5, "item_name": "甄氏", "text_color": (255,215,0)},
            5050:{"weight": 8, "rarity": 5, "item_name": "張郃", "text_color": (255,215,0)},
            5051:{"weight": 8, "rarity": 5, "item_name": "黄月英", "text_color": (255,215,0)},
            5052:{"weight": 8, "rarity": 5, "item_name": "孟獲", "text_color": (255,215,0)},
            5053:{"weight": 8, "rarity": 5, "item_name": "馬雲騄", "text_color": (255,215,0)},
            5054:{"weight": 8, "rarity": 5, "item_name": "陳宮", "text_color": (255,215,0)},
            5055:{"weight": 8, "rarity": 5, "item_name": "呂玲綺", "text_color": (255,215,0)},
            5056:{"weight": 8, "rarity": 5, "item_name": "鍾会", "text_color": (255,215,0)},
            5057:{"weight": 8, "rarity": 5, "item_name": "司馬徽", "text_color": (255,215,0)},
            5058:{"weight": 4, "rarity": 5, "item_name": "張飛", "text_color": (255,215,0)},
            5059:{"weight": 4, "rarity": 5, "item_name": "馬超", "text_color": (255,215,0)},
            5060:{"weight": 4, "rarity": 5, "item_name": "周瑜", "text_color": (255,215,0)},
            5061:{"weight": 4, "rarity": 5, "item_name": "趙雲", "text_color": (255,215,0)},
            5062:{"weight": 4, "rarity": 5, "item_name": "関羽", "text_color": (255,215,0)},
            5063:{"weight": 4, "rarity": 5, "item_name": "曹操", "text_color": (255,215,0)},
            5064:{"weight": 4, "rarity": 5, "item_name": "諸葛亮", "text_color": (255,215,0)},
            5065:{"weight": 4, "rarity": 5, "item_name": "劉備", "text_color": (255,215,0)},
            5066:{"weight": 4, "rarity": 5, "item_name": "呂布", "text_color": (255,215,0)},
            5067:{"weight": 4, "rarity": 5, "item_name": "太史慈", "text_color": (255,215,0)},
            5068:{"weight": 4, "rarity": 5, "item_name": "孫尚香", "text_color": (255,215,0)},
            5069:{"weight": 4, "rarity": 5, "item_name": "龐統", "text_color": (255,215,0)},
            5070:{"weight": 4, "rarity": 5, "item_name": "許褚", "text_color": (255,215,0)},
            5071:{"weight": 4, "rarity": 5, "item_name": "張遼", "text_color": (255,215,0)},
            5072:{"weight": 4, "rarity": 5, "item_name": "楽進", "text_color": (255,215,0)},
            5073:{"weight": 4, "rarity": 5, "item_name": "司馬懿", "text_color": (255,215,0)},
            5074:{"weight": 4, "rarity": 5, "item_name": "陸遜", "text_color": (255,215,0)},
            5075:{"weight": 4, "rarity": 5, "item_name": "典韋", "text_color": (255,215,0)},
            5076:{"weight": 3, "rarity": 5, "item_name": "孫権", "text_color": (255,215,0)},
            
            # 星4武将
            4001:{"weight": 61, "rarity": 4, "item_name": "徐盛", "text_color": (255,0,255)},
            4002:{"weight": 61, "rarity": 4, "item_name": "潘璋", "text_color": (255,0,255)},
            4003:{"weight": 61, "rarity": 4, "item_name": "廖化", "text_color": (255,0,255)},
            4004:{"weight": 61, "rarity": 4, "item_name": "曹真", "text_color": (255,0,255)},
            4005:{"weight": 61, "rarity": 4, "item_name": "呂範", "text_color": (255,0,255)},
            4006:{"weight": 61, "rarity": 4, "item_name": "顧雍", "text_color": (255,0,255)},
            4007:{"weight": 61, "rarity": 4, "item_name": "諸葛瑾", "text_color": (255,0,255)},
            4008:{"weight": 61, "rarity": 4, "item_name": "歩練師", "text_color": (255,0,255)},
            4009:{"weight": 61, "rarity": 4, "item_name": "韓当", "text_color": (255,0,255)},
            4010:{"weight": 61, "rarity": 4, "item_name": "丁奉", "text_color": (255,0,255)},
            4011:{"weight": 61, "rarity": 4, "item_name": "鍾繇", "text_color": (255,0,255)},
            4012:{"weight": 61, "rarity": 4, "item_name": "曹洪", "text_color": (255,0,255)},
            4013:{"weight": 61, "rarity": 4, "item_name": "郭淮", "text_color": (255,0,255)},
            4014:{"weight": 61, "rarity": 4, "item_name": "劉曄", "text_color": (255,0,255)},
            4015:{"weight": 61, "rarity": 4, "item_name": "陳琳", "text_color": (255,0,255)},
            4016:{"weight": 61, "rarity": 4, "item_name": "楊脩", "text_color": (255,0,255)},
            4017:{"weight": 61, "rarity": 4, "item_name": "曹彰", "text_color": (255,0,255)},
            4018:{"weight": 61, "rarity": 4, "item_name": "李典", "text_color": (255,0,255)},
            4019:{"weight": 61, "rarity": 4, "item_name": "臧覇", "text_color": (255,0,255)},
            4020:{"weight": 61, "rarity": 4, "item_name": "馬謖", "text_color": (255,0,255)},
            4021:{"weight": 61, "rarity": 4, "item_name": "簡雍", "text_color": (255,0,255)},
            4022:{"weight": 61, "rarity": 4, "item_name": "董允", "text_color": (255,0,255)},
            4023:{"weight": 61, "rarity": 4, "item_name": "費禕", "text_color": (255,0,255)},
            4024:{"weight": 61, "rarity": 4, "item_name": "李厳", "text_color": (255,0,255)},
            4025:{"weight": 61, "rarity": 4, "item_name": "関平", "text_color": (255,0,255)},
            4026:{"weight": 61, "rarity": 4, "item_name": "劉封", "text_color": (255,0,255)},
            4027:{"weight": 61, "rarity": 4, "item_name": "沙摩柯", "text_color": (255,0,255)},
            4028:{"weight": 61, "rarity": 4, "item_name": "張宝", "text_color": (255,0,255)},
            4029:{"weight": 61, "rarity": 4, "item_name": "朱儁", "text_color": (255,0,255)},
            4030:{"weight": 61, "rarity": 4, "item_name": "盧植", "text_color": (255,0,255)},
            4031:{"weight": 61, "rarity": 4, "item_name": "馬鉄", "text_color": (255,0,255)},
            4032:{"weight": 61, "rarity": 4, "item_name": "張任", "text_color": (255,0,255)},
            4033:{"weight": 61, "rarity": 4, "item_name": "張梁", "text_color": (255,0,255)},
            4034:{"weight": 61, "rarity": 4, "item_name": "蒋欽", "text_color": (255,0,255)},
            4035:{"weight": 61, "rarity": 4, "item_name": "張繍", "text_color": (255,0,255)},
            4036:{"weight": 61, "rarity": 4, "item_name": "管亥", "text_color": (255,0,255)},
            4037:{"weight": 61, "rarity": 4, "item_name": "紀霊", "text_color": (255,0,255)},
            4038:{"weight": 61, "rarity": 4, "item_name": "劉表", "text_color": (255,0,255)},
            4039:{"weight": 61, "rarity": 4, "item_name": "皇甫嵩", "text_color": (255,0,255)},
            4040:{"weight": 61, "rarity": 4, "item_name": "文聘", "text_color": (255,0,255)},
            4041:{"weight": 61, "rarity": 4, "item_name": "馬良", "text_color": (255,0,255)},
            4042:{"weight": 61, "rarity": 4, "item_name": "朱桓", "text_color": (255,0,255)},
            4043:{"weight": 61, "rarity": 4, "item_name": "陳武", "text_color": (255,0,255)},
            4044:{"weight": 61, "rarity": 4, "item_name": "董襲", "text_color": (255,0,255)},
            4045:{"weight": 61, "rarity": 4, "item_name": "糜竺", "text_color": (255,0,255)},
            4046:{"weight": 61, "rarity": 4, "item_name": "黄権", "text_color": (255,0,255)},
            4047:{"weight": 61, "rarity": 4, "item_name": "審配", "text_color": (255,0,255)},
            4048:{"weight": 61, "rarity": 4, "item_name": "李傕", "text_color": (255,0,255)},
            4049:{"weight": 61, "rarity": 4, "item_name": "張曼成", "text_color": (255,0,255)},
            4050:{"weight": 61, "rarity": 4, "item_name": "張燕", "text_color": (255,0,255)},
            4051:{"weight": 61, "rarity": 4, "item_name": "王朗", "text_color": (255,0,255)},
            4052:{"weight": 61, "rarity": 4, "item_name": "周倉", "text_color": (255,0,255)},
            4053:{"weight": 61, "rarity": 4, "item_name": "韓遂", "text_color": (255,0,255)},
            4054:{"weight": 61, "rarity": 4, "item_name": "張魯", "text_color": (255,0,255)},
            4055:{"weight": 61, "rarity": 4, "item_name": "郭汜", "text_color": (255,0,255)},
            4056:{"weight": 61, "rarity": 4, "item_name": "逢紀", "text_color": (255,0,255)},
            4057:{"weight": 61, "rarity": 4, "item_name": "郭図", "text_color": (255,0,255)},
            4058:{"weight": 61, "rarity": 4, "item_name": "胡車児", "text_color": (255,0,255)},
            4059:{"weight": 61, "rarity": 4, "item_name": "孔融", "text_color": (255,0,255)},
            
            # 星3武将
            3001:{"weight": 183, "rarity": 3, "item_name": "曹休", "text_color": (100,149,237)},
            3002:{"weight": 183, "rarity": 3, "item_name": "夏侯恩", "text_color": (100,149,237)},
            3003:{"weight": 183, "rarity": 3, "item_name": "孫皓", "text_color": (100,149,237)},
            3004:{"weight": 183, "rarity": 3, "item_name": "劉繇", "text_color": (100,149,237)},
            3005:{"weight": 183, "rarity": 3, "item_name": "歩騭", "text_color": (100,149,237)},
            3006:{"weight": 183, "rarity": 3, "item_name": "潘濬", "text_color": (100,149,237)},
            3007:{"weight": 183, "rarity": 3, "item_name": "朱然", "text_color": (100,149,237)},
            3008:{"weight": 183, "rarity": 3, "item_name": "傅士仁", "text_color": (100,149,237)},
            3009:{"weight": 183, "rarity": 3, "item_name": "糜芳", "text_color": (100,149,237)},
            3010:{"weight": 183, "rarity": 3, "item_name": "闞沢", "text_color": (100,149,237)},
            3011:{"weight": 183, "rarity": 3, "item_name": "全琮", "text_color": (100,149,237)},
            3012:{"weight": 183, "rarity": 3, "item_name": "董昭", "text_color": (100,149,237)},
            3013:{"weight": 183, "rarity": 3, "item_name": "虞翻", "text_color": (100,149,237)},
            3014:{"weight": 183, "rarity": 3, "item_name": "毛玠", "text_color": (100,149,237)},
            3015:{"weight": 183, "rarity": 3, "item_name": "華歆", "text_color": (100,149,237)},
            3016:{"weight": 183, "rarity": 3, "item_name": "呂虔", "text_color": (100,149,237)},
            3017:{"weight": 183, "rarity": 3, "item_name": "孫乾", "text_color": (100,149,237)},
            3018:{"weight": 183, "rarity": 3, "item_name": "諸葛瞻", "text_color": (100,149,237)},
            3019:{"weight": 183, "rarity": 3, "item_name": "鄧芝", "text_color": (100,149,237)},
            3020:{"weight": 183, "rarity": 3, "item_name": "劉巴", "text_color": (100,149,237)},
            3021:{"weight": 183, "rarity": 3, "item_name": "劉禅", "text_color": (100,149,237)},
            3022:{"weight": 183, "rarity": 3, "item_name": "呉懿", "text_color": (100,149,237)},
            3023:{"weight": 183, "rarity": 3, "item_name": "宋憲", "text_color": (100,149,237)},
            3024:{"weight": 183, "rarity": 3, "item_name": "向寵", "text_color": (100,149,237)},
            3025:{"weight": 183, "rarity": 3, "item_name": "費詩", "text_color": (100,149,237)},
            3026:{"weight": 183, "rarity": 3, "item_name": "陶謙", "text_color": (100,149,237)},
            3027:{"weight": 183, "rarity": 3, "item_name": "王允", "text_color": (100,149,237)},
            3028:{"weight": 183, "rarity": 3, "item_name": "卞喜", "text_color": (100,149,237)},
            3029:{"weight": 183, "rarity": 3, "item_name": "車冑", "text_color": (100,149,237)},
            3030:{"weight": 183, "rarity": 3, "item_name": "丁原", "text_color": (100,149,237)},
            3031:{"weight": 183, "rarity": 3, "item_name": "何進", "text_color": (100,149,237)},
            3032:{"weight": 183, "rarity": 3, "item_name": "潘鳳", "text_color": (100,149,237)},
        }

    
              
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
        #self.settings = Settings()
        self.items = gacha_table()       
        #self.gacha_images_show = GachaImagesShow(ai_game = self.settings)
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
                #self.gacha_images_show.one_time_gacha_image_blitme(id)
                    

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
                #self.gacha_images_show.one_time_gacha_image_blitme(id)
                
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
                #self.gacha_images_show.one_time_gacha_image_blitme(id)
       
        return self.results 
    
    def rare_gacha_five_times(self):
        """5回ガチャ回すときのカウンター"""        
        #self.settings = Settings()
        self.items = gacha_table()
        #self.gacha_images_show = GachaImagesShow(ai_game = self.settings)
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
                #self.gacha_images_file.append("./images" + "/ID{}.png".format(id))
                #self.gacha_images_show.five_times_gacha_images_blitme(id, times, self.id_lists, self.gacha_images_file)

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
                #self.gacha_images_file.append("./images" + "/ID{}.png".format(id))
                #self.gacha_images_show.five_times_gacha_images_blitme(id, times, self.id_lists, self.gacha_images_file)
                
        return self.results
    
    def rest(self):
        self._count = 0
        self._price = 0
        
        self.total_results = []
        self.total_id_lists = []
        self.total_rarity_lists = []

        return  


