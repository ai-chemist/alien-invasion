import sys

import pygame

from settings import Settings
from space_ship import SpaceShip

class AlienInvasion:
    """게임 전체 관리"""

    def __init__(self):
        """게임 초기화 및 리소스 생성"""
        pygame.init()

        # 프레임 조절을 위한 clock
        self.clock = pygame.time.Clock()

        # 분리한 setting 파일
        self.settings = Settings()

        #
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))

        pygame.display.set_caption('Alien Invasion')
        self.space_ship = SpaceShip(self)

        # 배경 색상 설정 - 기본값은 검은색 화면 : [settings.py]로 넘어감
        # self.bg_color = (230, 230, 230)

    def run_game(self):
        """게임의 기능 실행"""
        while True:
            # 사용자 입력에 응답
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # 매 루프마다 화면 다시 출력
            self.screen.fill(self.settings.bg_color)
            self.space_ship.blitme()

            # 가장 최근의 화면 출력
            pygame.display.flip()

            # 프레임 전달 - 초당 60 프레임
            self.clock.tick(60)

if __name__ == '__main__':
    # 게임 인스턴스 생성 및 실행
    ai = AlienInvasion()
    ai.run_game()