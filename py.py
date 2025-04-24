import pygame  

pygame.init()

# Терезе параметрлері
width, height = 600, 400
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Page Navigation")

# Түстер
colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255)]  # Қызыл, жасыл, көк

# Бет нөмірі
page = 0  

run = True
while run:
    screen.fill(colors[page])  # Белсенді беттің түсін қолданамыз

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False  
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:  # Оңға басқанда келесі бет
                page = (page + 1) % 3  
            if event.key == pygame.K_LEFT:   # Солға басқанда алдыңғы бет
                page = (page - 1) % 3  

    pygame.display.flip()  # Экранды жаңарту

pygame.quit()
