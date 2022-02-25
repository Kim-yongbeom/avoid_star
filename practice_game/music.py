import pygame
import random

#######################################################################################################
# 반드시 해야하는 것들
pygame.init()
music_file = "메이플스토리 BGM - 행복한 마을(Happy Town).mp3"
pygame.mixer.init
pygame.mixer.music.load(music_file)
pygame.mixer.music.play(-1)

screen_width = 480  # 가로 크기
screen_height = 640  # 세로 크기
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면타이틀 설정
pygame.display.set_caption("미니 별피하기")  # 게임이름

# FPS
clock = pygame.time.Clock()
#######################################################################################################

# 1. 사용자 게임 초기화 (배경화면, 게임 이미지, 좌표, 폰트 등...)


background = pygame.image.load("C:\\Python\\Python_study\\pygame_basic\\background.png")  # 배경이미지 불러오기

character = pygame.image.load("C:\\Python\\Python_study\\pygame_basic\\zxc.png")  # 캐릭터 불러오기
character_size = character.get_rect().size
character_width = character_size[0]  # 가로크기
character_height = character_size[1]  # 세로크기
character_x_pos = (screen_width / 2) - (character_width / 2)  # 화면 가로의 절반 크기에 위치
character_y_pos = screen_height - 70  # 화면 세로 위치

to_x = 0  # 이동할 좌표
life = 3
score = 0
level = 1

character_speed = 0.6  # 이동속도

enemy = pygame.image.load("C:\\Python\\Python_study\\pygame_basic\\enemy.png")  # 적 불러오기
enemy_size = enemy.get_rect().size
enemy_width = enemy_size[0]  # 가로크기
enemy_height = enemy_size[1]  # 세로크기
enemy_x_pos = random.randint(0, screen_width - enemy_width)
enemy_y_pos = 0
enemy_speed = 0.6

game_font = pygame.font.Font(None, 30)  # 폰트 객체 생성 (폰트, 크기)

# 2. 이벤트 처리 (키보드, 마우스 등...)
running = True  # 게임이 진행중인가?
while running:
    dt = clock.tick(60)  # 초당 프레임 수

    for event in pygame.event.get():  # 어떤 이벤트가 발생하엿는가?
        if event.type == pygame.QUIT:  # 창이 닫히는 이벤트가 발생했는가?
            running = False  # 게임이 진행중이 아님

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_x -= character_speed
            elif event.key == pygame.K_RIGHT:
                to_x += character_speed

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0

    # 3. 게임 캐릭터 위치 정의
    character_x_pos += to_x * dt

    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > (screen_width - character_width):
        character_x_pos = (screen_width - character_width)

    enemy_y_pos += enemy_speed * dt

    if enemy_y_pos > screen_height:
        enemy_y_pos = 0
        enemy_x_pos = random.randint(0, screen_width - enemy_width)
        if enemy_y_pos == 0:
            score += 1

    # 4. 충돌 처리
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_x_pos
    enemy_rect.top = enemy_y_pos

    if character_rect.colliderect(enemy_rect):
        life -= 1
        pygame.time.delay(1000)  # 1초 딜레이
        if life == 0:
            running = False

    if score == 20:
        enemy_speed = 1.0
        level = 2
    elif score == 50:
        enemy_speed = 1.2
        level = 3
    elif score == 100:
        enemy_speed = 1.4
        level = 4
    elif score == 150:
        enemy_speed = 1.6
        level = 5

    # 5. 배경 그리기
    screen.blit(background, (0, 0))
    screen.blit(character, (character_x_pos, character_y_pos))
    screen.blit(enemy, (enemy_x_pos, enemy_y_pos))

    life_left = game_font.render("LIFE : " + str(int(life)), True, (255, 255, 255))  # (출력할 정보, True, 글자 색상)
    if life <= 0:
        print("목숨이 없습니다.")
        running = False

    score_left1 = game_font.render("SCORE : " + str(int(score)), True, (255, 255, 255))  # (출력할 정보, True, 글자 색상)
    level_left = game_font.render("LEVEL : " + str(int(level)), True, (255, 255, 255))  # (출력할 정보, True, 글자 색상)

    screen.blit(life_left, (400, 10))
    screen.blit(score_left1, (10, 10))
    screen.blit(level_left, (210, 10))
    pygame.display.update()  # 게임화면을 다시 그리기 (꼭있어야함)

if pygame.mixer.music.get_busy():
    clock.tick(30)
pygame.mixer.quit()
##반드시 필요

pygame.quit()