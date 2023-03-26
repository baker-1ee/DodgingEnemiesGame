import random

import pygame

from resize_image import resize_image


class Enemy:
    def __init__(self, width, height):
        resize_image("enemy.png", "_enemy_.png", (width, height))
        self.__object = pygame.image.load("_enemy_.png")
        self.__rect = self.__object.get_rect()
        self.__limit_bottom = None
        self.__limit_right = None
        self.__speed = 0.5
        self.__y_pos = None
        self.__x_pos = None
        self.__width = width
        self.__height = height

    def init_position(self, screen_width, screen_height):
        self.__x_pos = random.randint(0, screen_width - self.__width)
        self.__y_pos = 0
        self.__limit_right = screen_width
        self.__limit_bottom = screen_height

    def move(self, dt, level):
        self.__y_pos += self.__speed * dt * level
        self.__check_exceed_limit_position()
        self.__update_rect_for_collection_detection()

    def __check_exceed_limit_position(self):
        if self.__y_pos > self.__limit_bottom:
            self.__x_pos = random.randint(0, self.__limit_right - self.__width)
            self.__y_pos = 0

    def __update_rect_for_collection_detection(self):
        self.__rect.left = self.__x_pos
        self.__rect.top = self.__y_pos

    def get_rect(self):
        return self.__rect

    def draw_on(self, screen):
        screen.blit(self.__object, (self.__x_pos, self.__y_pos))

