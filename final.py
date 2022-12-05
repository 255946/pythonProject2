import pygame
import math
import time
import random


#screen setup
pygame.init()
WIDTH, HEIGHT = 800,500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Navy Hangman')

#button variables
RADIUS = 20
GAP = 15
letters = []
startx = round((WIDTH - (RADIUS * 2 + GAP) * 13) / 2)
starty = 400
A = 65
for i in range(26):
    x = startx + GAP * 2 + ((RADIUS * 2 +GAP) * (i % 13))
    y = starty + ((i // 13) * (GAP + RADIUS * 2))
    letters.append([x, y, chr(A + i), True])

#fonts
font = pygame.font.SysFont('gabriola', 25)
font2 = pygame.font.SysFont('gabriola', 60)
font3 = pygame.font.SysFont('gabriola', 100)
font4 = pygame.font.SysFont('gabriola', 75)

#load images
images = []
for x in range(7):
    image = pygame.image.load('hangman' + str(x) + '.png')
    images.append(image)


#game variables
mid_level = 0
list = ['ABOARD', 'AFT', 'ALONGSIDE', 'ANCHOR', 'ANCHORAGE', 'BARNACLE', 'BELAY', 'BERTH', 'BERTHING', 'BILLET', 'BOW', 'BRIDGE', 'BRIG', 'BULKHEAD', 'CAPTAIN', 'CHAPLAIN', 'COMMISSARY', 'COMMISSION', 'COMMODORE', 'COMPARTMENT', 'CONUS', 'COURSE', 'CRUISE', 'DECK', 'DETAILER', 'DEPLOY', 'EMBARK', 'ENLISTED', 'ENSIGN', 'XO', 'FATHOM', 'FLAG', 'FORECASTLE', 'FROGMAN', 'GALLEY', 'GANGPLANK', 'GANGWAY', 'GOUGE', 'HEAD', 'HONORS', 'KNOT', 'LADDER', 'LEATHERNECK', 'LOOKOUT', 'MAST', 'MESS', 'MID', 'MIDSHIPMAN', 'MILITARY', 'MUSTER', 'PASSAGEWAY', 'POD', 'PORT', 'QUARTERDECK', 'QUARTERS', 'RANK', 'RATE', 'RATING', 'SAILOR', 'SCUTTLEBUTT', 'SHIPMATE', 'SKIPPER', 'STARBOARD', 'STERN', 'STOW', 'SWAB', 'TOPSIDE', 'TRICARE', 'WARDROOM', 'WATCH', 'AWOL', 'CHOW', '`NEX', 'OCONUS', 'OVERBOARD', 'MOORING', 'LOG', 'ADMIRAL', 'CHIT', 'SAILING', 'RACK', 'PROPULSION']
words = random.choice(list)
guesses = []


def draw():
    screen.fill((255, 255, 255))

    #draw title
    title = font4.render('NAVY HANGMAN', 1, (0,0,255))
    screen.blit(title, (WIDTH/2 - title.get_width()/2, 20))

    #draw buttons
    for letter in letters:
        x, y, ltr, visible = letter
        if visible:
            pygame.draw.circle(screen, (0,0,0), (x, y), RADIUS, 3)
            text = font.render(ltr, 1, (0,0,0))
            screen.blit(text, (x - text.get_width()/2 , y - text.get_height()/2))

    #draw words
    word = ''
    for letter in words:
        if letter in guesses:
          word += letter + ' '
        else:
          word += '_ '
    text = font2.render(word, 1, (0,0,0))
    screen.blit(text, (400, 200))

    screen.blit(images[mid_level], (150, 100))
    pygame.display.update()

#setup game loop
while True:

        draw()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos_x, pos_y = pygame.mouse.get_pos()
                for letter in letters:
                    x, y, ltr, visible = letter
                    if visible:
                        distance = math.sqrt((x - pos_x)**2 + (y - pos_y)**2)
                        if distance < RADIUS:
                            letter[3] = False
                            guesses.append(ltr)
                            if ltr not in words:
                                mid_level += 1
        draw()

        win = True
        for letter in words:
            if letter not in guesses:
                win = False
                break
        if win:
            pygame.time.delay(1500)
            screen.fill((255, 255, 255))
            winner = font3.render("YOU WON!", 1, (0, 0, 0))
            screen.blit(winner, (WIDTH/2 - winner.get_width()/2, HEIGHT/2 - winner.get_height()/2))
            pygame.display.update()
            pygame.time.delay(3000)
            break
        if mid_level == 6:
            pygame.time.delay(1500)
            screen.fill((255, 255, 255))
            looser = font3.render("YOU LOST!", 1, (0, 0, 0))
            screen.blit(looser, (WIDTH / 2 - looser.get_width() / 2, HEIGHT / 2 - looser.get_height() / 2))
            pygame.display.update()
            pygame.time.delay(3000)
            break
pygame.quit()


