import sys
from time import sleep

import pygame

from settings import Settings
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button
from space_ship import SpaceShip
from bullet import Bullet
from alien import Alien

class AlienInvasion:
    """게임 전체 관리"""

    def __init__(self):
        """게임 초기화 및 리소스 생성"""
        pygame.init()

        # 프레임 조절을 위한 clock
        self.clock = pygame.time.Clock()

        # 분리한 setting 파일
        self.settings = Settings()

        # 창모드 - 화면 크기 설정
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))

        # 전체 화면 모드
        # self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        # self.settings.screen_width = self.screen.get_rect().width
        # self.settings.screen_height = self.screen.get_rect().height

        pygame.display.set_caption('Alien Invasion')
        
        # 게임 기록 관리 인스턴스
        self.stats = GameStats(self)

        # 점수판
        self.scoreboard = Scoreboard(self)
        
        self.space_ship = SpaceShip(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        self._create_fleet()

        # 배경 색상 설정 - 기본값은 검은색 화면 : [settings.py]로 넘어감
        # self.bg_color = (230, 230, 230)

        # 게임 활성 상태 관리 플래그 - 비활성 상태로 시작
        self.game_active = False

        # 플레이 버튼 생성 - 인스턴스만 생성, 화면에 출력 필요
        self.play_button = Button(self, "Click to Play")

    def run_game(self):
        """게임의 기능 실행"""
        while True:
            self._check_events()

            if self.game_active:
                # 우주선 바뀐 위치 전달
                self.space_ship.update()
                # 탄환 관리 - 메서드로 분리
                self._update_bullets()
                # 외계인 관리 - 메서드
                self._update_aliens()
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
                self._check_keydown_events(event)
            # KEYUP 이벤트 - 키보드 키가 올라감
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
            # MOUSEBUTTONDOWN 이벤트 - 마우스 클릭
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # 마우스가 클릭된 지점의 좌표를 튜플로 반환
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)

    # key 이벤트 메서드 분리
    def _check_keydown_events(self, event):
        """keydown 이벤트 처리"""
        if event.key == pygame.K_RIGHT:
            self.space_ship.moving_right = True
            # 우측 이동 - 아래 방식으로 사용 시 눌림 상태 감지 불가
            # self.space_ship.rect.x += 1
        elif event.key == pygame.K_LEFT:
            # 좌측 이동
            self.space_ship.moving_left = True
        # Esc 키를 눌러 종료
        elif event.key == pygame.K_ESCAPE:
            sys.exit()
        # Spacebar 를 눌러 탄환 발사
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self, event):
        """keyup 이벤트 처리"""
        if event.key == pygame.K_RIGHT:
            self.space_ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.space_ship.moving_left = False

    def _check_play_button(self, mouse_pos):
        """플레이어가 'play' 버튼을 클릭했는지 여부 확인"""
        # button_clicked 변수 - game_active 활성 상태 비교 목적으로 분리
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        # collidepoint() 메서드로 클릭된 지점(mouse_pos)이 play_button.rect 내부에 있는지 확인
        # if self.play_button.rect.collidepoint(mouse_pos):
        if button_clicked and not self.game_active:
            # 게임 설정 초기화
            self.settings.initialize_dynamic_settings()
            # 게임 기록 초기화
            self.stats.reset_stats()
            self.scoreboard.prep_score()
            self.scoreboard.prep_level()
            self.scoreboard.prep_ships()
            self.game_active = True

            # 남은 탄환 및 외계인 제거
            self.bullets.empty()
            self.aliens.empty()

            # 외계인 부대 새로 생성 후 플레이어 위치 초기화
            self._create_fleet()
            self.space_ship.center_ship()

    def _fire_bullet(self):
        """탄환 추가 후 그룹에 추가"""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        """탄환 위치 업데이트 및 화면 벗어난 탄환 제거 역할 분리"""
        # 탄환 위치 업데이트
        self.bullets.update()

        # 화면 밖의 탄환 제거 - 리스트를 직접 순회해서는 안되기에 .copy() 메서드로 사본 전달
        for bullet in self.bullets.copy():
            # 화면 밖으로 넘어가면
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
            # 탄환의 개수 출력 (테스트용)
            # print(len(self.bullets))

        self._check_bullet_alien_collisions()

    def _check_bullet_alien_collisions(self):
        """탄환과 외계인 충돌 관리"""
        # 탄환과 외계인 충돌(collision) 감지 - 탄환과 외계인 제거
        # True (dokilla) 인수 부분 - 충돌한 요소 제거 groupcollide() - 그룹 요소 사이의 충돌 감지
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)

        if collisions:
            # 탄환에 맞은 외계인 숫자 * 점수
            for aliens in collisions.values():
                self.stats.score += self.settings.alien_points * len(aliens)
            self.scoreboard.prep_score()
            self.scoreboard.check_best_score()

        # 외계인이 남아있지 않을 시
        if not self.aliens:
            # 외계인 제거 및 새 부대 반환
            self.bullets.empty()
            self._create_fleet()
            self.settings.increase_speed()

            # 레벨 증가
            self.stats.level += 1
            self.scoreboard.prep_level()

    def _create_fleet(self):
        """외계인 부대 생성"""
        # 외계인 하나 생성 (공간이 없을 때까지 반복)
        # 사이의 공간은 외계인의 너비와 같음 + 높이
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size

        current_x, current_y = alien_width, alien_height
        # 외계인 + 사이 공간이므로 2 * alien_width
        while current_y < (self.settings.screen_height - 3 * alien_height):
            while current_x < (self.settings.screen_width - 2 * alien_width):
                self._create_alien(current_x, current_y)
                current_x += 2 * alien_width

            # 한 줄이 끝났으니 x값 초기화, y값 증가
            current_x = alien_width
            current_y += 1.5 * alien_height

    def _create_alien(self, x_position, y_position):
        """외계인 하나 생성 후 배치"""
        new_alien = Alien(self)
        new_alien.x = x_position
        new_alien.rect.x = x_position
        new_alien.rect.y = y_position
        self.aliens.add(new_alien)

    def _check_fleet_edges(self):
        """외계인이 화면 경계에 도달 시 실행"""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        """전체 부대를 한 줄 내리고 이동 방향 좌우 반전"""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1
        
    def _ship_hit(self):
        """외계인이 우주선과 충돌 시 실행"""
        if self.stats.space_ships_left > 0:
            # space_ships_left 감소
            self.stats.space_ships_left -= 1

            # 점수판 업데이트
            self.scoreboard.prep_ships()
        
            # 남은 탄환, 외계인 제거
            self.bullets.empty()
            self.aliens.empty()
        
            # 외계인 부대 새로 생성 및 우주선 위치 초기화
            self._create_fleet()
            self.space_ship.center_ship()
        
            # 게임 일시 중지
            sleep(0.5)
        else:
            self.game_active = False
        
    def _check_aliens_bottom(self):
        """화면 하단에 도달한 외계인 감지"""
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= self.settings.screen_height:
                # 우주선이 외계인과 충돌할 때와 같은 반응
                self._ship_hit()
                break

    def _update_aliens(self):
        """부대에 속한 모든 외계인 위치 업데이트"""
        self._check_fleet_edges()
        self.aliens.update()

        # 외계인과 우주선의 충돌 검색 spritecollideany() - 스프라이트와 그룹의 요소 중 충돌 감지
        if pygame.sprite.spritecollideany(self.space_ship, self.aliens):
            # print("Spaceship damaged")
            self._ship_hit()

        # 화면 하단에 도달한 외계인 감지
        self._check_aliens_bottom()

    def _update_screen(self):
        """화면 업데이트 메서드 - run_game()에서 분리"""
        # 매 루프마다 화면 다시 출력
        self.screen.fill(self.settings.bg_color)
        # for 루프로 bullets 내부의 객체들 출력
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        self.space_ship.blitme()
        self.aliens.draw(self.screen)

        # 점수 정보 출력
        self.scoreboard.show_score()

        # game_active 상태가 False 일 경우에만 버튼 출력
        if not self.game_active:
            self.play_button.draw_button()

        # 가장 최근의 화면 출력
        pygame.display.flip()


if __name__ == '__main__':
    # 게임 인스턴스 생성 및 실행
    ai = AlienInvasion()
    ai.run_game()