import pygame.font
from pygame.sprite import Group

from space_ship import SpaceShip

class Scoreboard:
    """점수 기록"""

    def __init__(self, ai_game):
        """점수 기록에 필요한 속성 초기화"""
        self.ai_game = ai_game
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.stats = ai_game.stats

        # 점수 정보에 사용할 폰트
        self.text_color = (200, 50, 100)
        self.font = pygame.font.SysFont('arial', 48)

        # 초기 점수 이미지
        self.prep_score()
        self.prep_best_score()
        self.prep_level()
        self.prep_ships()


    def prep_score(self):
        """점수를 이미지로 렌더링"""
        # 부동소수점 인수를 음수로 주어 가장 가까운 10^n 승의 값으로 반올림
        rounded_score = round(self.stats.score, -1)
        # :, - 적절한 자리에 ',' 삽입
        score_str = f"{rounded_score:,}"
        self.score_image = self.font.render(score_str, True, self.text_color, self.settings.bg_color)

        # 화면 우상단에 점수 표시
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 30
        self.score_rect.top = 30

    def prep_best_score(self):
        """최고 점수 렌더링"""
        best_score = round(self.stats.best_score, -1)
        best_score_str = f"{best_score:,}"
        self.best_score_image = self.font.render(best_score_str, True, self.text_color, self.settings.bg_color)

        # 최고 점수를 화면 상단 중앙에 표시
        self.best_score_rect = self.best_score_image.get_rect()
        self.best_score_rect.centerx = self.screen_rect.centerx
        self.best_score_rect.top = self.score_rect.top

    def check_best_score(self):
        """최고 점수 갱신 확인"""
        if self.stats.score > self.stats.best_score:
            self.stats.best_score = self.stats.score
            self.prep_best_score()

    def prep_level(self):
        """레벨 이미지로 렌더링"""
        level_str = str(self.stats.level)
        self.level_image = self.font.render(level_str, True, self.text_color, self.settings.bg_color)

        # 레벨을 점수 아래에 표시
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 20

    def prep_ships(self):
        """플레이어의 남은 우주선 표시"""
        self.space_ships = Group()
        for ship_number in range(self.stats.space_ships_left):
            space_ship = SpaceShip(self.ai_game)
            space_ship.rect.x = 10 + ship_number * space_ship.rect.width
            space_ship.rect.y = 10
            self.space_ships.add(space_ship)

    def show_score(self):
        """점수, 레벨, 남은 우주선을 화면에 출력"""
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.best_score_image, self.best_score_rect)

        # 현재 레벨 화면에 출력
        self.screen.blit(self.level_image, self.level_rect)

        # 남은 우주선 화면에 출력
        self.space_ships.draw(self.screen)

