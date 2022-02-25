import pygame

pygame.init() #반드시필요 (초기화)

screen_width = 480 # 가로 크기
screen_height = 640 # 세로 크기
screen = pygame.display.set_mode((screen_width, screen_height))

#화면타이틀 설정
pygame.display.set_caption("YB Game") #게임이름

#FPS
clock = pygame.time.Clock()

#배경이미지 불러오기
background = pygame.image.load("C:\\Python\\Python_study\\pygame_basic\\background.png")

#캐릭터 불러오기
character = pygame.image.load("C:\\Python\\Python_study\\pygame_basic\\zxc.png")
character_size = character.get_rect().size
character_width = character_size[0] #가로크기
character_height = character_size[1]#세로크기
character_x_pos = (screen_width / 2)  - (character_width / 2) #화면 가로의 절반 크기에 위치
character_y_pos = screen_height - 70    #화면 세로 위치


#이동할 좌표
to_x = 0
to_y = 0

#이동속도
character_speed = 0.5

#이벤트 루프
running = True #게임이 진행중인가?
while running:
    dt = clock.tick(60)                 #초당 프레임 수

    for event in pygame.event.get():    #어떤 이벤트가 발생하엿는가?
        if event.type == pygame.QUIT:   #창이 닫히는 이벤트가 발생했는가?
            running = False             #게임이 진행중이 아님

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_x -= character_speed
            elif event.key == pygame.K_RIGHT:
                to_x += character_speed
            elif event.key == pygame.K_UP:
                to_y -= character_speed
            elif event.key == pygame.K_DOWN:
                to_y += character_speed

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y = 0

    character_x_pos += to_x * dt
    character_y_pos += to_y * dt

#가로 경계
    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > (screen_width - character_width):
        character_x_pos = (screen_width - character_width)

    if character_y_pos < 0:
        character_y_pos = 0
    elif character_y_pos > (screen_height - character_height):
        character_y_pos = (screen_height - character_height)


    screen.blit(background, (0,0))      #배경 그리기
    screen.blit(character, (character_x_pos, character_y_pos))

    pygame.display.update()             #게임화면을 다시 그리기 (꼭있어야함)

pygame.quit()