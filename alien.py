import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """외계인"""

    def __init__(self, ai_game):
        """초기화"""
        super().__init__()
        self.screen = ai_game.screen
        # 설정 가져오기
        self.settings = ai_game.settings

        # rect 속성 설정
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        # 좌측 상단 근처에 생성
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # 정확한 가로 위치 계산
        self.x = float(self.rect.x)

    def check_edges(self):
        """화면 경계 도달 시 True 반환"""
        screen_rect = self.screen.get_rect()
        return (self.rect.right >= screen_rect.right) or (self.rect.left <= 0)

    def update(self):
        """외계인을 우측 혹은 좌측으로 이동시키기"""
        self.x += self.settings.alien_speed * self.settings.fleet_direction
        self.rect.x = self.x