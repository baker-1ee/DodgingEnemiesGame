import pygame

from resize_image import resize_image
from character import Character
from enemy import Enemy


class Game:
    def __init__(self, screen_width, screen_height):
        # 게임 초기화
        self.timer_text = None
        pygame.init()
        # 게임 제목 설정
        pygame.display.set_caption("My Game")
        # 게임 화면 크기 설정
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        # FPS 설정
        self.clock = pygame.time.Clock()
        # 글꼴 설정
        self.game_font = pygame.font.Font(None, 50)
        self.level = 1
        self.level_text = self.game_font.render("Lv : " + str(self.level), True, (255, 255, 255))
        self.play_time = 5
        self.timer = self.play_time
        # 배경 이미지 설정
        resize_image("background.png", "_background_.png", (640, 860))
        self.background = pygame.image.load("_background_.png")
        # 캐릭터 생성 
        self.character = Character(70, 70)
        self.character.init_position(screen_width, screen_height)
        # 적 생성 
        self.enemy = Enemy(70, 70)
        self.enemy.init_position(screen_width, screen_height)

    def run(self):
        left_pressed = False
        right_pressed = False
        running = True
        
        while running:
            # FPS 설정
            dt = self.clock.tick(60)
            # 이벤트 처리
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        left_pressed = True
                    elif event.key == pygame.K_RIGHT:
                        right_pressed = True

                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT:
                        left_pressed = False
                    elif event.key == pygame.K_RIGHT:
                        right_pressed = False

            # 캐릭터 위치 업데이트
            if left_pressed:
                self.character.move_left(dt)

            if right_pressed:
                self.character.move_right(dt)

            # 적 위치 업데이트
            self.enemy.move(dt, self.level)

            # 충돌 처리
            if self.character.is_collision(self.enemy.get_rect()):
                self.game_over()
                running = False

            # 타이머 업데이트
            self.update_timer(dt)

            # 레벨 업 처리
            if self.timer < 0:
                self.level_up()

            # 게임 화면 그리기
            self.draw_game()

        # 게임 종료
        pygame.quit()

    def game_over(self):
        # GAME OVER 문구 생성
        game_over = self.game_font.render("GAME OVER", True, (255, 255, 255))
        game_over_rect = game_over.get_rect(center=(self.screen_width/2, self.screen_height/2))
        self.screen.blit(game_over, game_over_rect)
        pygame.display.update()
        pygame.time.delay(1000)

    def update_timer(self, dt):
        self.timer -= dt / 1000
        self.timer_text = self.game_font.render("{:.0f}".format(self.timer), True, (255, 255, 255))

    def level_up(self):
        self.level += 1
        self.timer = self.play_time
        level_up = self.game_font.render("Level Up", True, (255, 255, 255))
        level_up_rect = level_up.get_rect(center=(self.screen_width/2, self.screen_height/2))
        self.screen.blit(level_up, level_up_rect)
        pygame.display.update()
        pygame.time.delay(1000)
        self.level_text = self.game_font.render("Lv : " + str(self.level), True, (255, 255, 255))

    def draw_game(self):
        self.screen.blit(self.background, (0, 0))
        self.character.draw_on(self.screen)
        self.enemy.draw_on(self.screen)
        self.screen.blit(self.timer_text, (10, 10))
        self.screen.blit(self.level_text, (self.screen_width - 100, 10))
        pygame.display.update()

