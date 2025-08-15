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

        # 화면 크기 설정
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))

        pygame.display.set_caption('Alien Invasion')
        self.space_ship = SpaceShip(self)

        # 배경 색상 설정 - 기본값은 검은색 화면 : [settings.py]로 넘어감
        # self.bg_color = (230, 230, 230)

    def run_game(self):
        """게임의 기능 실행"""
        while True:
            self._check_events()
            # 우주선 바뀐 위치 전달
            self.space_ship.update()
            self._update_screen()
            # 프레임 전달 - 초당 60 프레임
            self.clock.tick(60)

    # _method() - 보조 메서드(클래스 내부에서만 사용하는 메서드) 를 나타내기 위해 _method_name() 방식으로 작성
    def _check_events(self):
        """사용자 입력에 응답 - run_game()에서 분리"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            # KEYDOWN 이벤트 - 키 눌림 상태
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    self.space_ship.moving_right = True
                    # 우측 이동 - 아래 방식으로 사용 시 눌림 상태 감지 불가
                    # self.space_ship.rect.x += 1
                elif event.key == pygame.K_LEFT:
                    # 좌측 이동
                    self.space_ship.moving_left = True
            # KEYUP 이벤트 - 키보드 키가 올라감
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    self.space_ship.moving_right = False
                elif event.key == pygame.K_LEFT:
                    self.space_ship.moving_left = False

    def _update_screen(self):
        """화면 업데이트 메서드 - run_game()에서 분리"""
        # 매 루프마다 화면 다시 출력
        self.screen.fill(self.settings.bg_color)
        self.space_ship.blitme()

        # 가장 최근의 화면 출력
        pygame.display.flip()


if __name__ == '__main__':
    # 게임 인스턴스 생성 및 실행
    ai = AlienInvasion()
    ai.run_game()