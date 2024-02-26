import pygame
from sys import exit
import random

WIDTH, HEIGHT = 500, 500
MAXLENGTH = 10
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

with open("5000words.txt", "r") as wordfile:
    easywords = wordfile.read().split("\n")

easywords = [i for i in easywords if (len(i)>2)]

easywordsdict = {}

for i in range(3, MAXLENGTH+1):
    easywordsdict[i] = [j.lower() for j in easywords if len(j) == i]


with open("words.txt", "r") as wordfile:
    mediumwords = wordfile.read().split("\n")

mediumwords = [i for i in mediumwords if (len(i)>2)]

mediumwordsdict = {}

for i in range(3, MAXLENGTH+1):
    mediumwordsdict[i] = [j.lower() for j in mediumwords if len(j) == i]


with open("words_alpha.txt", "r") as wordfile:
    hellwords = wordfile.read().split("\n")

hellwords = [i for i in hellwords if (len(i)>2)]

hellwordsdict = {}

for i in range(3, MAXLENGTH+1):
    hellwordsdict[i] = [j.lower() for j in hellwords if len(j) == i]

def hangman(win, stage):
    
    if stage >= 0:
        pygame.draw.line(win, BLACK, (250, 10), (250, 40))
        pygame.draw.line(win, BLACK, (50, 10), (250, 10))
        pygame.draw.line(win, BLACK, (50, 10), (50, 350))
        pygame.draw.line(win, BLACK, (30, 350), (400, 350))
        pygame.draw.line(win, BLACK, (100, 10), (50, 60))
        pygame.draw.line(win, BLACK, (100, 350), (50, 300))
    if stage >= 1:
        pygame.draw.circle(win, BLACK, (250, 70), 30)
    if stage >= 2:
        pygame.draw.line(win, BLACK, (250, 100), (250, 250))
    if stage >= 3:
        pygame.draw.line(win, BLACK, (250, 120), (300, 170))
    if stage >= 4:
        pygame.draw.line(win, BLACK, (250, 120), (200, 170))
    if stage >= 5:
        pygame.draw.line(win, BLACK, (250, 250), (300, 300))
    if stage == 6:
        pygame.draw.line(win, BLACK, (250, 250), (200, 300))

def displayText(win, text, x, y, color, font = 'timesnewroman', size = 30):
    Font=pygame.font.SysFont(font, size)
    text = Font.render(text, True, color, WHITE)
    textrect = text.get_rect()
    textrect.center = (x, y)
    win.blit(text, textrect)

def markwrong(win, wrong, len):
    startx = 250 - (len-1)*11.5
    for i in wrong:
        pygame.draw.line(win, RED, (startx + i*23, 440), (startx + i*23 + 10, 460))
        pygame.draw.line(win, RED, (startx + i*23 + 10, 440), (startx + i*23, 460))

def getword(wordsdict):
    # return a word of length level at random
    return random.choice(wordsdict[random.randint(3, MAXLENGTH)])

def main():

    pygame.init()
    win = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()
    pygame.display.set_caption('Hangman Game')

    Icon = pygame.image.load('icon.png')

    pygame.display.set_icon(Icon)

    levels = ["Easy", "Medium", "Hell"]
    level = 0
    wordsdict = easywordsdict
    alphabets = "abcdefghijklmnopqrstuvwxyz"
    word = getword(wordsdict)
    guessed = []
    currentword = ' '.join(['_' for i in word])
    stage = 0
    winstage = -1
    gamerunning = True
    reset = False

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                if 480 <= x <= 500 and 10 <= y <= 30:
                    level = (level + 1) % len(levels)
                    reset = True
                    continue
                if 360 <= x <= 380 and 10 <= y <= 20:
                    level = (level - 1) % len(levels)
                    reset = True
                    continue
                if 400 <= x <= 460 and 50 <= y <= 70:
                    word = getword(wordsdict)
                    guessed = []
                    currentword = ' '.join(['_' for _ in word])
                    stage = 0
                    winstage = -1
                    gamerunning = True
                    continue

            if (event.type == pygame.KEYDOWN) and gamerunning:
                try:
                    char = chr(event.key)
                    if char in alphabets:
                        if char not in guessed:
                            guessed.append(char)
                            if char in word:
                                currentword = ' '.join([i if i in guessed else '_' for i in word])
                            else:
                                stage += 1
                except Exception as e:
                    print(e)
        
        if level == 0:
            wordsdict = easywordsdict
        elif level == 1:
            wordsdict = mediumwordsdict
        else:
            wordsdict = hellwordsdict
        
        if reset == True:
            word = getword(wordsdict)
            guessed = []
            currentword = ' '.join(['_' for _ in word])
            stage = 0
            winstage = -1
            gamerunning = True
            reset = False

        win.fill(WHITE)

        displayText(win, 'Level : ', 310, 20, BLACK, size=20)
        displayText(win, '+', 490, 20, GREEN, size=25)
        displayText(win, levels[level], 430, 20, BLACK, size=20)
        displayText(win, '-', 370, 20, RED, size=25)

        displayText(win, "Restart", 430, 60, BLACK, size=15)

        displayText(win, "", 100, 400, BLACK)

        if (''.join(currentword.split()) == word):
            displayText(win, 'You Win', 250, 310, GREEN)
            if winstage == -1:
                winstage = stage
            else:
                stage = winstage
            gamerunning = False

        if stage >= 6:
            displayText(win, 'Game Over', 250, 310, RED)
            currentword = word
            gamerunning = False
        
            
        hangman(win, stage)

        displayText(win, currentword, 250, 400, BLACK)
        displayText(win, ' '.join(guessed), 250, 450, BLACK)

        wrong = [i for i in range(len(guessed)) if guessed[i] not in word]
        
        markwrong(win, wrong, len(guessed))

        
        pygame.display.update()
        clock.tick(60)

if __name__ == "__main__":
    main()

