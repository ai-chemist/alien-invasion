import pygame
from pygame.sprite import Sprite

# Sprite -> 객체들을 하나의 그룹으로 사용
class Bullet(Sprite):
    """우주선이 발사할 탄환"""

    def __init__(self, ai_game):
        """우주선 현 위치에서 탄환 생성"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        # (0, 0) 좌표에 탄환 생성 후 위치 설정
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect.midtop = ai_game.space_ship.rect.midtop

        # 탄환 위치 부동 소수점화
        self.y = float(self.rect.y)

    def update(self):
        """탄환이 화면 상단으로 이동"""
        # 위치 조정 (왜 y 값을 줄이나?) : pygame 에서는 y좌표 값이 하단(양수), 상단(음수) 방식으로 동작함
        self.y -= self.settings.bullet_speed
        self.rect.y = self.y

    def draw_bullet(self):
        """화면에 탄환 출력"""
        pygame.draw.rect(self.screen, self.color, self.rect)