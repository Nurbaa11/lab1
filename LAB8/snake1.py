import random, pygame, sys, time

pygame.init()

width = 600
height = 400
size = (width, height)
screen = pygame.display.set_mode(size)

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
blue = (0, 0, 255)
green = (0, 255, 0)
bg = (138, 140, 168)

snake_block = 10  
snake_speed = 15

clock = pygame.time.Clock()  

score_style = pygame.font.SysFont("arial", 30)
message_style = pygame.font.SysFont("arial", 20)


def total_score(score):
    score_value = score_style.render("Your score: " + str(score), True, blue)
    screen.blit(score_value, [0, 0])  


def total_level(level):
    level_value = score_style.render("Your level: " + str(level), True, blue)
    screen.blit(level_value, [width - 150, 0])


def our_snake(snake_block, snake_list):
    for coordinate in snake_list:
        pygame.draw.rect(screen, black, [coordinate[0], coordinate[1], snake_block, snake_block])


def message(text, color):
    text_to_print = message_style.render(text, True, color)
    screen.blit(text_to_print, [width / 4, height / 2])


def playAgain():
    global snake_speed
    game_over = False
    game_close = False

    x1 = width / 2
    y1 = height / 2

    x1_change = 0
    y1_change = 0

    snake_list = []
    length_of_snake = 1

    level = 1
    food_counter = 0

    food_x = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
    food_y = round(random.randrange(0, height - snake_block) / 10.0) * 10.0

    while not game_over:
        while game_close:
            screen.fill(red)
            message("YOU LOST! PRESS P-PLAY AGAIN OR Q-QUIT", black)
            total_score(length_of_snake - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_p:
                        return  # Restart the game loop instead of calling playAgain() again
                    if event.key == pygame.K_q:
                        pygame.quit()
                        sys.exit()  # Properly quit the game

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    x1_change = 0
                    y1_change = -snake_block
                if event.key == pygame.K_DOWN:
                    x1_change = 0
                    y1_change = snake_block
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                if event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0

        if x1 >= width or x1 < 0 or y1 >= height or y1 < 0:
            game_close = True

        x1 += x1_change
        y1 += y1_change
        screen.fill(bg)
        pygame.draw.rect(screen, green, [food_x, food_y, snake_block, snake_block])

        snake_head = [x1, y1]
        snake_list.append(snake_head)

        if len(snake_list) > length_of_snake:
            del snake_list[0]

        for x in snake_list[:-1]:  
            if x == snake_head:
                game_close = True

        our_snake(snake_block, snake_list)
        total_score(length_of_snake - 1)
        total_level(level)

        pygame.display.update()

        if x1 == food_x and y1 == food_y:
            food_counter += 1
            length_of_snake += 1
            food_x = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
            food_y = round(random.randrange(0, height - snake_block) / 10.0) * 10.0
            if food_counter % 3 == 0:
                level += 1
                snake_speed += 5

        clock.tick(snake_speed)

playAgain()  # Start the game
