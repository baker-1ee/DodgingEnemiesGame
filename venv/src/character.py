import pygame

from resize_image import resize_image


class Character:
    def __init__(self, width, height):
        resize_image("character.png", "_character_.png", (width, height))
        self.__width = width
        self.__height = height
        self.__object = pygame.image.load("_character_.png")
        self.__rect = self.__object.get_rect()
        self.__y_pos = None
        self.__x_pos = None
        self.__limit_right = None
        self.__limit_left = None
        self.__speed = 0.5

    def init_position(self, screen_width, screen_height):
        """
        캐릭터 초기 위치 설정
        :param screen_width: 캐릭터 의 배경 스크린 너비
        :param screen_height: 캐릭터 의 배경 스크린 높이
        :return: void
        """
        # 초기 위치 설정
        self.__x_pos = (screen_width / 2) - (self.__width / 2)
        self.__y_pos = screen_height - self.__height
        # 캐릭터의 왼쪽, 오른쪽 위치 한계 설정
        self.__limit_left = 0
        self.__limit_right = screen_width - self.__width

    def move_left(self, dt):
        """
        왼쪽 으로 이동
        :param dt: dt
        :return: void
        """
        self.__x_pos -= self.__speed * dt
        self.__check_exceed_limit_position()
        self.__update_rect_for_collection_detection()

    def move_right(self, dt):
        """
        오른쪽 으로 이동
        :param dt: dt
        :return: void
        """
        self.__x_pos += self.__speed * dt
        self.__check_exceed_limit_position()
        self.__update_rect_for_collection_detection()

    def __check_exceed_limit_position(self):
        # 캐릭터가 좌측, 우측 경계 포지션을 이탈하지 못하도록 위치 체크 및 조정
        if self.__x_pos < self.__limit_left:
            self.__x_pos = self.__limit_left
        elif self.__x_pos > self.__limit_right:
            self.__x_pos = self.__limit_right

    def __update_rect_for_collection_detection(self):
        # 캐릭터 충돌 감지를 위해 캐릭터 위치 이동 시 항상 rect 정보를 업데이트 해주어야 한다
        self.__rect.left = self.__x_pos
        self.__rect.top = self.__y_pos

    def is_collision(self, enemy_rect):
        """
        충돌 여부를 판단
        :param enemy_rect: 적의 rect 정보
        :return: True or False
        """
        return self.__rect.colliderect(enemy_rect)

    def draw_on(self, screen):
        """
        screen 에 캐릭터 를 그림
        :param screen: 캐릭터 를 그릴 대상
        :return: void
        """
        screen.blit(self.__object, (self.__x_pos, self.__y_pos))

