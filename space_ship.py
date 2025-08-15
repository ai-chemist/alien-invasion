import pygame

class SpaceShip:
    """우주선 - 플레이어"""

    def __init__(self, ai_game):
        """우주선 초기화 및 시작 설정"""
        self.screen = ai_game.screen
        # 설정 가져오기
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # 우주선 이미지 가져오기
        self.image = pygame.image.load('images/spaceship.bmp')
        self.rect = self.image.get_rect()

        # 우주선 초기 위치 화면 하단 중앙으로 설정
        self.rect.midbottom = self.screen_rect.midbottom

        # 가로 좌표 부동 소수점으로 변경
        self.x = float(self.rect.x)

        # 움직임 플래그 - default : 정지 상태
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """움직임 플래그 기반으로 위치 업데이트"""
        # self.rect.x -> self.x [rect 속성은 정수 값만 저장 가능]
        # and 이하 절 추가 - 화면 우측 끝을 벗어나지 않게 하기 위함
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        # 동시에 두가지 키가 눌릴 가능성이 있기에 elif 가 아닌 if 작성 - 우선순위 부여 X
        # right와 마찬가지로 and 이하 절 추가 - 좌측 끝의 값은 0 이므로 0으로 설정
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        # self.x를 이용해 self.rect.x 값 업데이트 - 화면에 표시될 값은 rect.x 의 영향을 받기에 반드시 설정해야 함
        self.rect.x = self.x

    def blitme(self):
        """현재 위치에 우주선 출력"""
        self.screen.blit(self.image, self.rect)