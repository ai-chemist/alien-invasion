class Settings:
    """게임의 설정 저장 클래스"""

    def __init__(self):
        """게임 설정 초기화"""
        # 화면
        self.screen_width = 1600
        self.screen_height = 1200
        # 연한 회색
        # self.bg_color = (230, 230, 230)
        self.bg_color = (20, 20, 20)

        # 우주선 속력
        self.ship_speed = 2.5

        # 탄막 설정
        self.bullet_speed = 4.5
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (220, 190, 10)
        # 탄환 최대 개수 제한
        self.bullets_allowed = 20

        # 외계인 설정
        self.alien_speed = 1.5
        self.fleet_drop_speed = 15
        # 1 == right / -1 == left
        self.fleet_direction = 1