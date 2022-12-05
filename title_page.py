import pygame

pygame.init()
WIDTH, HEIGHT = 800,500
menu_screen = pygame.display.set_mode((WIDTH, HEIGHT))
mouse = pygame.mouse.get_pos()
start = False

font5 = pygame.font.SysFont('gabriola', 100)
rect_width = 175
rect_height= 50
def draw_title():
    menu_screen.fill((255, 255, 255))
    caption = font5.render('NAVY HANGMAN', 1, (0,0,255))
    menu_screen.blit(caption, (WIDTH / 2 - caption.get_width() / 2, 20))
    pygame.draw.rect(menu_screen, (0,255,0), (320,250, rect_width,rect_height))
    pygame.display.update()

while True:
    draw_title()
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            if (mouse[0] > 320) and (mouse[0] < 495) and (mouse[1] > 250) and (mouse[1] < 300):
                start = True





