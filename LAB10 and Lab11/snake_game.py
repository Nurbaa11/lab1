import pygame
import psycopg2
import random
import time

# Инициализация базы данных
conn = psycopg2.connect(
    host="localhost",
    database="pp2",
    user="postgres",
    password="postgres",
    port=5432
)
cur = conn.cursor()

# Создание таблиц, если нет
cur.execute("""
CREATE TABLE IF NOT EXISTS users (
    username VARCHAR(50) PRIMARY KEY,
    level INT DEFAULT 1
)
""")

cur.execute("""
CREATE TABLE IF NOT EXISTS user_score (
    id SERIAL PRIMARY KEY,
    username VARCHAR(50) REFERENCES users(username),
    score INT,
    level INT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
""")
conn.commit()

# Получение имени игрока
username = input("Введите имя пользователя: ")
cur.execute("SELECT level FROM users WHERE username = %s", (username,)) # users
user = cur.fetchone()

if user:
    level = user[0]
    print(f"Добро пожаловать, {username}! Ваш уровень: {level}")
else:
    level = 1
    cur.execute("INSERT INTO users (username) VALUES (%s)", (username,))
    conn.commit()
    print(f"Создан новый пользователь: {username}, уровень 1")

# Настройки игры
pygame.init()
WHITE = (255, 255, 255)
GREEN = (0, 200, 0)
RED = (255, 0, 0)
BLOCK = 20
W, H = 600, 400
win = pygame.display.set_mode((W, H))
pygame.display.set_caption("Snake Game")

clock = pygame.time.Clock()
speed = 5 + level * 2  # скорость зависит от уровня

font = pygame.font.SysFont(None, 35)

def draw_snake(snake_list):
    for block in snake_list:
        pygame.draw.rect(win, GREEN, [block[0], block[1], BLOCK, BLOCK])

def message(msg, color):
    text = font.render(msg, True, color)
    win.blit(text, [W / 6, H / 3])

def game_loop():
    global level
    game_over = False
    game_close = False

    x, y = W / 2, H / 2
    dx, dy = 0, 0

    snake = []
    length = 1
    score = 0

    food_x = round(random.randrange(0, W - BLOCK) / BLOCK) * BLOCK
    food_y = round(random.randrange(0, H - BLOCK) / BLOCK) * BLOCK

    while not game_over:
        while game_close:
            win.fill(WHITE)
            message("Нажмите Q - выход или C - продолжить", RED)
            pygame.display.update()

            for e in pygame.event.get():
                if e.type == pygame.KEYDOWN:
                    if e.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if e.key == pygame.K_c:
                        game_loop()

        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                game_over = True
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_LEFT:
                    dx = -BLOCK
                    dy = 0
                elif e.key == pygame.K_RIGHT:
                    dx = BLOCK
                    dy = 0
                elif e.key == pygame.K_UP:
                    dy = -BLOCK
                    dx = 0
                elif e.key == pygame.K_DOWN:
                    dy = BLOCK
                    dx = 0
                elif e.key == pygame.K_p:
                    print("Пауза... Сохраняем прогресс")
                    save_progress(score)
                    time.sleep(2)

        x += dx
        y += dy

        if x >= W or x < 0 or y >= H or y < 0:
            game_close = True

        win.fill(WHITE)
        pygame.draw.rect(win, RED, [food_x, food_y, BLOCK, BLOCK])

        snake.append([x, y])
        if len(snake) > length:
            del snake[0]

        for part in snake[:-1]:
            if part == [x, y]:
                game_close = True

        draw_snake(snake)

        pygame.display.update()

        if x == food_x and y == food_y:
            food_x = round(random.randrange(0, W - BLOCK) / BLOCK) * BLOCK
            food_y = round(random.randrange(0, H - BLOCK) / BLOCK) * BLOCK
            length += 1
            score += 10

        clock.tick(speed)

    save_progress(score)
    pygame.quit()
    quit()

def save_progress(score):
    global level
    cur.execute("""
    INSERT INTO user_score (username, score, level)
    VALUES (%s, %s, %s)
    """, (username, score, level))

    # Поднимаем уровень за каждый запуск
    level += 1
    cur.execute("UPDATE users SET level = %s WHERE username = %s", (level, username))
    conn.commit()
    print(f"Сохранено! Счёт: {score}, Уровень: {level}")

game_loop()
