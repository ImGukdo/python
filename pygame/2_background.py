import pygame
import os

pygame.init()  # 초기화 (반드시 필요)

#  화면 크기 설정
screen_width = 480  # 가로 크기
screen_height = 640  # 세로 크기
screen = pygame.display.set_mode((screen_width, screen_height))

#  화면 타이틀 설정
pygame.display.set_caption("Game")  # 게임 이름

#  배경 이미지 불러오기
current_path = os.path.dirname(__file__)      # 현재 파일의 위치 
image_path = os.path.join(current_path, "background.png")   # 이미지 파일
background = pygame.image.load(image_path)

#  이벤트 루프
running = True  # 게임이 진행중인가?
while running :
    for event in pygame.event.get() :
        if event.type == pygame.QUIT :  # 창이 닫히는 이벤트가 발생했나?
            running = False  # 게임이 진행중이 아니도록 설정
    
    screen.blit(background, (0, 0)) # 배경 그리기

    pygame.display.update()  # 게임화면을 다시 그리기

#  pygame 종료
pygame.quit()