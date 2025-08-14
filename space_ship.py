import pygame

class SpaceShip:
    """우주선 - 플레이어"""

    def __init__(self, ai_game):
        """우주선 초기화 및 시작 설정"""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # 우주선 이미지 가져오기
        self.image = pygame.image.load('images/spaceship.bmp')
        self.rect = self.image.get_rect()

        # 우주선 초기 위치 화면 하단 중앙으로 설정
        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        """현재 위치에 우주선 출력"""
        self.screen.blit(self.image, self.rect)