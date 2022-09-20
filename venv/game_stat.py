class GameStat:
    """Track Statistic for alien Invasion"""
    def __init__(self, ai_game):
        """initialise the stats"""
        self.settings = ai_game.settings
        self.reset_stats()
        self.game_active = False

    def reset_stats(self):
        """initialize stats that change during game"""
        self.ship_left = self.settings.ship_limit
        self.score = 0

