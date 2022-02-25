import pygame

pygame.init() #반드시필요 (초기화)

screen_width = 480 # 가로 크기
screen_height = 640 # 세로 크기
screen = pygame.display.set_mode((screen_width, screen_height))

#화면타이틀 설정
pygame.display.set_caption("YB Game") #게임이름

#배경이미지 불러오기
background = pygame.image.load("C:\\Python\\Python_study\\pygame_basic\\background.png")

#캐릭터 불러오기
character = pygame.image.load("C:\\Python\\Python_study\\pygame_basic\\zxc.png")
character_size = character.get_rect().size
character_width = character_size[0] #가로크기
character_height = character_size[1]#세로크기
character_x_pos = (screen_width / 2)  - (character_width / 2) #화면 가로의 절반 크기에 위치
character_y_pos = screen_height - 70    #화면 세로 위치


#이벤트 루프
running = True #게임이 진행중인가?
while running:
    for event in pygame.event.get():    #어떤 이벤트가 발생하엿는가?
        if event.type == pygame.QUIT:   #창이 닫히는 이벤트가 발생했는가?
            running = False             #게임이 진행중이 아님

    
    screen.blit(background, (0,0))      #배경 그리기
    screen.blit(character, (character_x_pos, character_y_pos))

    pygame.display.update()             #게임화면을 다시 그리기 (꼭있어야함)

pygame.quit()