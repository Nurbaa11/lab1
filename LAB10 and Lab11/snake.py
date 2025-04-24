import psycopg2
import time

# Подключение к базе данных
conn = psycopg2.connect(
    host="localhost",
    database="pp2",
    user="postgres",
    password="postgres",
    port=5432
)
cur = conn.cursor()

# Создание таблиц, если их ещё нет
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

# Ввод имени пользователя
username = input("Введите имя пользователя: ")

cur.execute("SELECT level FROM users WHERE username = %s", (username,))
user = cur.fetchone()

if user:
    print(f"Добро пожаловать, {username}! Ваш уровень: {user[0]}")
else:
    cur.execute("INSERT INTO users (username) VALUES (%s)", (username,))
    conn.commit()
    print(f"Создан новый пользователь: {username}, уровень 1")

# Примерные данные игры
score = 0
level = user[0] if user else 1

print("\nИгра началась!")

# Простая имитация игры
for i in range(5):
    time.sleep(1)
    score += 10
    print(f"Счёт: {score}")
    
    # Пример паузы
    if i == 2:
        pause = input("Нажмите 'p' для паузы: ")
        if pause == 'p':
            print("Пауза! Сохраняем прогресс...")

            # Сохраняем результат
            cur.execute("""
            INSERT INTO user_score (username, score, level)
            VALUES (%s, %s, %s)
            """, (username, score, level))

            # Обновляем уровень (например, +1)
            level += 1
            cur.execute("UPDATE users SET level = %s WHERE username = %s", (level, username))

            conn.commit()
            print(f"Прогресс сохранён: счёт {score}, уровень {level}")
            break

cur.close()
conn.close()
