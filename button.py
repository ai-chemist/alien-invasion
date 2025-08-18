import pygame.font
# from pathlib import Path

class Button:
    """게임 내부에 들어갈 버튼"""

    def __init__(self, ai_game, msg):
        """버튼 속성 초기화"""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # 버튼 크기와 속성 설정
        self.width, self.height = 200, 80
        self.button_color = (200, 200, 0)
        self.text_color = (255, 255, 255)

        # 폰트 지정
        # font_path = Path('/fonts/EduNSWACTCursive-Regular.ttf') - 따로 구한 파일 : 설정법 알아낼 것
        # self.font = pygame.font.SysFont(None, 48) - 기본값
        self.font = pygame.font.SysFont(None, 48)

        # 버튼 rect 객체 생성 및 배치
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        # 버튼에 표시할 메시지
        self._prep_msg(msg)

    def _prep_msg(self, msg):
        """msg를 이미지로 렌더링 후 버튼 중앙에 배치"""
        # render() 메서드로 텍스트 렌더링 - True 인수는 안티앨리어싱(Anti-aliasing) 설정 여부
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        """빈 버튼 생성 후 메시지 출력"""
        # 버튼의 사각형 부분 그리기
        self.screen.fill(self.button_color, self.rect)
        # 텍스트 이미지 그리기
        self.screen.blit(self.msg_image, self.msg_image_rect)