import os
import time
# Подключаем библиотеку tqdm для вывода прогресс бара
from tqdm import tqdm
# Подключаем библиотеку Fore (для изменения цвета)
# и Style (для изменения стиля)
from colorama import Fore
from colorama import Style

# Словарь для загрузки и времени в sec
boot_name = {'loading': ['Начинается загрузка системы...', 3],
             'access_to_data': ['Проверка данных...', 6],
             'network_access': ['Проверка сетевого взаимодействия...', 2],
             'gun_status': ['Проверка статуса оружия...', 4],
             'human_status': ['Проверка человеческих ресурсов...', 7],
             'last_message': ['Система загружена...']}


def progress_bar(delta):
    # Вызываем цикл для tqdm
    for i in tqdm(range(delta), ascii=True, colour='MAGENTA'):
        # Спим 1 секунду
        time.sleep(1)
        # Так как данных нам выводить не надо, то pass
        pass
    # В конце печатаем [ OK ]
    print(f"{Fore.GREEN}[ OK ]")


def boot():
    # Шагаем по словарю
    for i in boot_name:
        # Если i не равно last_message, то
        if i != 'last_message':
            # Печатаем нулевой индекс
            print(f"{Fore.LIGHTRED_EX}{boot_name[i][0]}")
            dl = boot_name[i][1]
            # Вызываем прогресс бар
            progress_bar(dl)
    # Выводим последнее сообщение
    print(f"{Style.RESET_ALL}{Fore.RESET}"
          f"{boot_name['last_message'][0]}. \nЦитаты великих людей:\n"
          f"{Style.BRIGHT}"
          f"Обязательно бахнем! И не раз! Весь мир в труху!… Но потом."
          f"{Fore.RESET}{Style.RESET_ALL}")
    time.sleep(3)
    # Очистка консольного окна
    os.system('cls' if os.name == 'nt' else 'clear')