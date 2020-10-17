import boot

calculate_t = {'loading': ['Расчет необходимых данных...', 2],
               'angle': ['Вычисляем угол...', 3],
               'time_fly': ['Вычисляем время до цели...', 4],
               'time_boom': ['Устанавливаем взрыватель...', 3],
               'godzilla': ['За это время GODZILLA уничтожила Токио...', 4],
               'last_loading': ['Все загрузилось...', 2], }


def progress_bar_calc(delta):
    for i in boot.tqdm(range(delta), colour='RED'):
        boot.time.sleep(1)
        pass
    print(f"{boot.Fore.GREEN}[ OK ]")


def calculate_main():
    for i in calculate_t:
        print(f"{boot.Fore.LIGHTRED_EX}{calculate_t[i][0]}")
        dl = calculate_t[i][1]
        progress_bar_calc(dl)
    print(f"{boot.Fore.RESET}")
