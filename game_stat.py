import json


class GameStat:
    """Track Statistic for alien Invasion"""

    def __init__(self, ai_game):
        """initialise the stats"""
        self.settings = ai_game.settings
        self.reset_stats()
        self.game_active = False
        self.load_data()

    def reset_stats(self):
        """initialize stats that change during game"""
        self.ship_left = self.settings.ship_limit
        self.score = 0
        self.level = 1

    def load_data(self):
        try:
            with open('save_data/hiscore.json') as f:
                self.high_score = json.load(f)
        except FileNotFoundError:
            self.high_score = 0
