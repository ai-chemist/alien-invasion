class GameStats:
    """게임 기록 저장"""

    def __init__(self, ai_game):
        """기록 초기화"""
        self.settings = ai_game.settings
        self.reset_stats()

    def reset_stats(self):
        """게임을 진행하는 동안 변하는 기록 초기화"""
        self.space_ships_left = self.settings.space_ship_limit