# -*- coding:utf-8 -*-
import pygame

pygame.init()  # 초기화

# 화면크기설정
screen_width = 480  # 가로크기
screen_height = 640  # 세로크기
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀
pygame.display.set_caption("My Game")

# 배경 이미지 불러오기
background = pygame.image.load("background.png")

# 캐릭터 불러오기
character = pygame.image.load("chracter.png")
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = screen_width / 2
character_y_pos = screen_height - character_height

# 이벤트 루프
running = True  # 게임이 진행 중인지 확인
while running:
    for event in pygame.event.get():  # 어떤 이벤트가 발생하였는가?
        if event.type == pygame.QUIT:  # 창이 닫히는 이벤트가 발생하였는가?
            running = False  # 게임이 진행중이 아님

    screen.blit(background, (0, 0))  # 배경 그리기
    screen.blit(character, (character_x_pos, character_y_pos))
    pygame.display.update()

# pygame 종료
pygame.quit()
