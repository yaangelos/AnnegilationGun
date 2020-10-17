import os
import time
from tqdm import tqdm
from colorama import Fore
from colorama import Style

boot_name = {'loading': ['Начинается загрузка системы...', 3],
             'access_to_data': ['Проверка данных...', 6],
             'network_access': ['Проверка сетевого взаимодействия...', 2],
             'gun_status': ['Проверка статуса оружия...', 4],
             'human_status': ['Проверка человеческих ресурсов...', 7],
             'last_message': ['Система загружена...']}


def progress_bar(delta):
    for i in tqdm(range(delta), ascii=True, colour='MAGENTA'):
        time.sleep(1)
        pass
    print(f"{Fore.GREEN}[ OK ]")


def boot():
    for i in boot_name:
        if i != 'last_message':
            print(f"{Fore.LIGHTRED_EX}{boot_name[i][0]}")
            dl = boot_name[i][1]
            progress_bar(dl)
    print(f"{Style.RESET_ALL}{Fore.RESET}"
          f"{boot_name['last_message'][0]}. \nЦитаты великих людей:\n"
          f"{Style.BRIGHT}"
          f"Обязательно бахнем! И не раз! Весь мир в труху!… Но потом."
          f"{Fore.RESET}{Style.RESET_ALL}")
    time.sleep(3)
    os.system('cls')