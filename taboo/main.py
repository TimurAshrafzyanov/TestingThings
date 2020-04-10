import pygame
from Buttons import Button, Slider
import time

from WorkwithAPI import Generate_Words

WIDTH = 800
HEIGHT = 510
FPS = 50

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
PINK = (226, 85, 106)
PURPLE = (74, 66, 135)
DARKPURPLE = (20, 15, 61)
ORANGE = (242, 159, 125)

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Taboo")
clock = pygame.time.Clock()

difficulty = 0
# buttons
rules = pygame.image.load('images/Buttons/rules.png').convert_alpha()
start = pygame.image.load('images/Buttons/startofgame.png').convert_alpha()
back = pygame.image.load('images/Buttons/back.png').convert_alpha()
num1 = pygame.image.load('images/Buttons/1.png').convert_alpha()
num2 = pygame.image.load('images/Buttons/2.png').convert_alpha()
num1pressed = pygame.image.load('images/Buttons/1pressed.png').convert_alpha()
num2pressed = pygame.image.load('images/Buttons/2pressed.png').convert_alpha()
next = pygame.image.load('images/Buttons/next.png').convert_alpha()
skip = pygame.image.load('images/Buttons/skip.png').convert_alpha()

# background
background = pygame.image.load('images/Backgrounds/background2.jpg').convert_alpha()

# stars
stars = pygame.image.load('images/StarsImage/stars.png').convert_alpha()
stars1 = pygame.image.load('images/StarsImage/stars1.png').convert_alpha()
stars2 = pygame.image.load('images/StarsImage/stars2.png').convert_alpha()
stars3 = pygame.image.load('images/StarsImage/stars3.png').convert_alpha()

# others
rules_text = pygame.image.load('images/others/rules_txt.png').convert_alpha()
logo = pygame.image.load('images/others/russian_logo.png').convert_alpha()

# texts
font = pygame.font.SysFont('Consolas', 30)
text1 = pygame.image.load('text1.png').convert_alpha()
text2 = pygame.image.load('text2.png').convert_alpha()

running = True
words = list()
words1 = Generate_Words(1)
words2 = Generate_Words(2)


def one_round(difficulty):
    score = 0
    nextb = Button(WIDTH - next.get_width(), HEIGHT - next.get_height(), screen, next)
    skipb = Button(WIDTH - next.get_width() - skip.get_width() - 20,
                   HEIGHT - next.get_height(),
                   screen, skip)
    if difficulty == 1:
        words = words1
    else:
        words = words2

    counter, text = 60, '60'.rjust(3)
    while counter > 0:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
        text = str(counter).rjust(3) if counter > 0 else 'boom!'
        counter -= 0.1
        screen.blit(background, (0, 0))
        nextb.drawbutton()
        skipb.drawbutton()
        for i in range(6):
            screen.blit(font.render(str(words[i]), True, WHITE), (500, i * 50 + 20))
        screen.blit(font.render("Score:" + str(score), True, WHITE), (30, HEIGHT / 2))
        screen.blit(font.render(text, True, (0, 0, 0)), (30, 50))
        if nextb.ispressed():
            score += 10
            words = Generate_Words(difficulty)
        if skipb.ispressed():
            score -= 5
            words = Generate_Words(difficulty)
        pygame.display.flip()
        time.sleep(0.1)
    return score


def Game(difficulty, numberofteams):
    if numberofteams == 1:
        score = [0]
    else:
        score = [0, 0]
    currentteam = 0
    startb = Button(WIDTH - start.get_width(), HEIGHT - start.get_height(), screen, start)
    if difficulty == 1:
        words = words1
    else:
        words = words2
    global running
    running = True
    nextwords = tuple()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.blit(background, (0, 0))
        startb.drawbutton()
        for i in range(len(score)):
            screen.blit(font.render("Score:" + str(score[i]), True, WHITE), (0, HEIGHT / 2 + 50 * i))
        pygame.display.flip()
        if startb.ispressed():
            score[currentteam] += one_round(difficulty)
            currentteam += 1
            currentteam %= numberofteams


def nextwords():
    global words
    for i in range(100):
        words.append(Generate_Words())
    print('OK')


def choose_mode():
    global running
    num1b = Button(WIDTH / 2 - num1.get_width() - 30, 100, screen, num1, num1pressed)
    num2b = Button(WIDTH / 2 + 30, 100, screen, num2, num2pressed)
    star = Slider(WIDTH / 2 - stars.get_width() / 2, 300, screen, stars, stars1, stars2, stars3)
    startb = Button(WIDTH - start.get_width(), HEIGHT - start.get_height(), screen, start)
    numberofteams = 0
    difficulty = 0
    while running:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()

        screen.blit(background, (0, 0))
        screen.blit(text1, (WIDTH / 2 - text1.get_width() / 2, 0))
        screen.blit(text2, (WIDTH / 2 - text2.get_width() / 2, 250))
        num1b.drawbutton()
        num2b.drawbutton()
        startb.drawbutton()
        star.drawbutton()
        screen.blit(font.render(str(numberofteams), True, WHITE), (0, HEIGHT / 2 + 50))
        screen.blit(font.render(str(difficulty), True, WHITE), (0, HEIGHT / 2 + 100))
        pygame.display.flip()
        ispressed = star.ispressed()
        if not ispressed == 0 :
            difficulty = ispressed
        if num1b.ispressed():
            num2b.currentim = num2b.image
            numberofteams = 1
        if num2b.ispressed():
            num1b.currentim = num1b.image
            numberofteams = 2
        if startb.ispressed():
            Game(difficulty, numberofteams)


def rulesonscreen():
    global running
    backb = Button(30, HEIGHT - back.get_height() - 30, screen, back)
    while running:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
            if backb.ispressed():
                start_scenery()
        screen.fill(BLACK)
        screen.blit(rules_text, (0, 0))
        backb.drawbutton()
        pygame.display.flip()


def start_scenery():
    global running
    startb = Button(WIDTH / 2 + 70, HEIGHT / 2, screen, start)
    rulesb = Button(WIDTH / 2 + 70, HEIGHT / 2 - start.get_height() - 20, screen, rules)
    screen.blit(background, (0, 0))
    startb.drawbutton()
    rulesb.drawbutton()
    screen.blit(logo, (10, 10))  # (WIDTH/2-logo.get_width()/2,0))
    pygame.display.flip()
    while running:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        if startb.ispressed():
            choose_mode()
        if rulesb.ispressed():
            rulesonscreen()


def run_game():
    start_scenery()
    pygame.quit()


run_game()
