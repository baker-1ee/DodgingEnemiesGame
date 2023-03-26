import pygame
import random
from resize_image import resize_image
from character import Character

# 게임 초기화
pygame.init()

# 게임 화면 크기 설정
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

# 게임 제목 설정
pygame.display.set_caption("My Game")

# FPS 설정
clock = pygame.time.Clock()

# 글꼴 설정
game_font = pygame.font.Font(None, 50)

# 이미지를 게임에서 사용하기 위한 고정 필셀로 리사이징
resize_image("background.png", "_background_.png", (640, 860))

resize_image("enemy.png", "_enemy_.png", (70, 70))

# 이미지 로딩
background = pygame.image.load("_background_.png")

enemy = pygame.image.load("_enemy_.png")

# 이미지 크기 설정
enemy_size = enemy.get_rect().size
enemy_width = enemy_size[0]
enemy_height = enemy_size[1]

# 캐릭터 생성 및 위치 초기화
character = Character(70, 70)
character.init_position(screen_width, screen_height)

# 게임 시간 설정
play_time = 5

# 적 위치 초기화
enemy_x_pos = random.randint(0, screen_width - enemy_width)
enemy_y_pos = 0
enemy_speed = 0.5

# 이미지 크기에 맞는 rect 생성
enemy_rect = enemy.get_rect()

# 방향키가 눌린 상태를 나타내는 변수
left_pressed = False
right_pressed = False

level = 1
timer = play_time

# 게임 루프
running = True
while running:
    # FPS 설정
    dt = clock.tick(60)

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
        character.move_left(dt)

    if right_pressed:
        character.move_right(dt)

    # 적 위치 업데이트
    enemy_y_pos += enemy_speed * dt * level

    if enemy_y_pos > screen_height:
        enemy_x_pos = random.randint(0, screen_width - enemy_width)
        enemy_y_pos = 0

    # 충돌 처리
    enemy_rect.left = enemy_x_pos
    enemy_rect.top = enemy_y_pos

    if character.is_collision(enemy_rect):

        # "GAME OVER" 문구 생성
        game_over = game_font.render("GAME OVER", True, (255, 255, 255))

        # "GAME OVER" 문구 화면 가운데 위치 계산
        game_over_rect = game_over.get_rect(center=(screen_width/2, screen_height/2))

        # "GAME OVER" 문구 화면에 그리기
        screen.blit(game_over, game_over_rect)

        # 화면 업데이트
        pygame.display.update()

        # 1초 동안 대기
        pygame.time.delay(1000)

        running = False

    # 타이머 업데이트
    timer -= dt / 1000
    timer_text = game_font.render("LV " + str(level) + " : " + "{:.0f}".format(timer), True, (255, 255, 255))

    # 레벨 업 처리
    if timer < 0:
        level += 1
        timer = play_time
        # "Level Up" 문구 생성
        level_up = game_font.render("Level Up", True, (255, 255, 255))
        # "Level Up" 문구 화면 가운데 위치 계산
        level_up_rect = level_up.get_rect(center=(screen_width/2, screen_height/2))
        # "Level Up" 문구 화면에 그리기
        screen.blit(level_up, level_up_rect)
        # 화면 업데이트
        pygame.display.update()
        # 1초 동안 대기
        pygame.time.delay(1000)

    # 게임 화면 그리기
    screen.blit(background, (0, 0))
    character.draw_on(screen)
    screen.blit(enemy, (enemy_x_pos, enemy_y_pos))
    screen.blit(timer_text, (10, 10))

    # 화면 업데이트
    pygame.display.update()

# 게임 종료
pygame.quit()

