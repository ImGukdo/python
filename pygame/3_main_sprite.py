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

#  캐릭터(스프라이트) 불러오기
character_path = os.path.join(current_path, "character.png")
character = pygame.image.load(character_path)
character_size = character.get_rect().size  # 이미지의 크기를 구해옴
character_width = character_size[0]  # 캐릭터의 가로 크기
character_height = character_size[1]  # 캐릭터의 세로 크기
character_x_pos = screen_width / 2 - (character_width / 2) # 화면 가로의 절반크기에 해당하는 곳에 위치
character_y_pos = screen_height - character_height # 화면 세로 크기 가장 아래에 해당하는 곳에 위치


#  이벤트 루프
running = True  # 게임이 진행중인가?
while running :
    for event in pygame.event.get() :
        if event.type == pygame.QUIT :  # 창이 닫히는 이벤트가 발생했나?
            running = False  # 게임이 진행중이 아니도록 설정
    
    screen.blit(background, (0, 0)) # 배경 그리기

    screen.blit(character, (character_x_pos, character_y_pos))  # 캐릭터 그리기

    pygame.display.update()  # 게임화면을 다시 그리기

#  pygame 종료
pygame.quit()