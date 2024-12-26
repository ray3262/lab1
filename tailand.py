import os
import time

# Цвета для флага
RED = "\033[41m"   # Красный фон
WHITE = "\033[47m"  # Белый фон
BLUE = "\033[44m"   # Синий фон
RESET = "\033[0m"   # Сброс цвета

# Функция для генерации одного кадра
def draw_flag(frame):
    if frame == 1:
        print(RED + " " * 30 + RESET)  # Красная полоса
        print(WHITE + " " * 30 + RESET)  # Белая полоса
        print(BLUE + " " * 30 + RESET)  # Синяя полоса (широкая)
        print(BLUE + " " * 30 + RESET)  # Синяя полоса (широкая)
        print(WHITE + " " * 30 + RESET)  # Белая полоса
        print(RED + " " * 30 + RESET)  # Красная полоса
    elif frame == 2:
        print(WHITE + " " * 30 + RESET)  # Белая полоса
        print(RED + " " * 30 + RESET)  # Красная полоса
        print(BLUE + " " * 30 + RESET)  # Синяя полоса (широкая)
        print(BLUE + " " * 30 + RESET)  # Синяя полоса (широкая)
        print(RED + " " * 30 + RESET)  # Красная полоса
        print(WHITE + " " * 30 + RESET)  # Белая полоса
    elif frame == 3:
        print(BLUE + " " * 30 + RESET)  # Синяя полоса
        print(RED + " " * 30 + RESET)  # Красная полоса
        print(WHITE + " " * 30 + RESET)  # Белая полоса
        print(WHITE + " " * 30 + RESET)  # Белая полоса
        print(RED + " " * 30 + RESET)  # Красная полоса
        print(BLUE + " " * 30 + RESET)  # Синяя полоса

# Анимация из 3 кадров
for i in range(10):  # Повторить 10 раз
    os.system("cls" if os.name == "nt" else "clear")  # Очистка консоли
    draw_flag((i % 3) + 1)  # Отображение кадра (1, 2 или 3)
    time.sleep(0.5)  # Задержка между кадрами

