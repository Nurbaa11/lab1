import pygame

pygame.init()

screen = pygame.display.set_mode((600, 300))
pygame.display.set_caption("Click to Change Words")


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

font = pygame.font.Font(None, 60)

word1 = "Hello"
word2 = "World"


rect1 = pygame.Rect(100, 100, 150, 60)
rect2 = pygame.Rect(350, 100, 150, 60)

running = True
while running:
    screen.fill(WHITE)

    text1 = font.render(word1, True, BLACK)
    text2 = font.render(word2, True, BLACK)

    screen.blit(text1, rect1.topleft)
    screen.blit(text2, rect2.topleft)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if rect1.collidepoint(event.pos):
                
                word1 = "World" if word1 == "Hello" else "Hello"
            elif rect2.collidepoint(event.pos):

                word2 = "Hello" if word2 == "World" else "World"

    pygame.display.flip()

pygame.quit()
