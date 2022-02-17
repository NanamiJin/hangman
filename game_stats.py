class GameStats:
    """ガチャシミュレーターの統計情報を記録する"""

    def __init__(self, ai_game):
        """"統計情報を初期化する"""
        self.settings = ai_game.settings
        self.set_stats()

        # 獲得した星5武将はリストにする
        #acquired_star5_list = []
   
    def set_stats(self):
        """ゲーム中に変更される統計情報を初期化する"""
        self.total_price = self.settings.price
        self.total_count = self.settings.count
        #self.total_rarity_lists = self.settings.total_rarity_lists

        # ガチャシミュレーターをアクティブな状態で開始する
        self.game_active = False  
