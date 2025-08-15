class Settings:
    """게임의 설정 저장 클래스"""

    def __init__(self):
        """게임 설정 초기화"""
        # 화면
        self.screen_width = 1600
        self.screen_height = 1200
        self.bg_color = (230, 230, 230)

        # 우주선 속력
        self.ship_speed = 1.5