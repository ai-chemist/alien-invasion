class Settings:
    """게임의 설정 저장 클래스"""

    def __init__(self):
        """게임 정적 설정 초기화"""
        # 화면
        self.screen_width = 1600
        self.screen_height = 1200
        # 연한 회색
        # self.bg_color = (230, 230, 230)
        self.bg_color = (20, 20, 20)

        # 우주선 설정
        self.space_ship_limit = 3

        # 탄막 설정
        self.bullet_width = 5
        self.bullet_height = 15
        self.bullet_color = (220, 190, 10)
        # 탄환 최대 개수 제한
        self.bullets_allowed = 15

        # 외계인 설정
        self.fleet_drop_speed = 50

        # 게임 빨리지는 속도
        self.speedup_scale = 1.2
        self.score_scale = 1.5

        self.initialize_dynamic_settings()


    def initialize_dynamic_settings(self):
        """진행 중 변할 수 있는 설정 초기화"""
        # 속도 관련
        self.ship_speed = 4.5
        self.bullet_speed = 6.5
        self.alien_speed = 2

        # 외계인 이동 방향
        # 1 == right / -1 == left
        self.fleet_direction = 1

        # 점수 설정
        self.alien_points = 50

    def increase_speed(self):
        """속도 및 점수 증가"""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)
        # 점수 증가 확인 용
        # print(self.alien_points)