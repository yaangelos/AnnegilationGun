import math
# Импортируем файл boot.py
import boot
from time import sleep
# Импортируем файл calculate.py
import calculate
import datetime as dt
# Импортируем библеотеки операционной системы
import os

# Устанавливаем силу свободного падения
G = 9.81
# Скорость заряда в м/с
SPEED_B = 1000
# Часть консоли
CONSOLE_T = 'G.U.N.D.A.M. /># '
# Имя файла куда будут записыватся данные
DATA_R = 'datarecord.txt'


class Gun:
    def __init__(self, distance):
        # Проверка хочет ли оператор прочитать файл
        if distance == 1:
            # Проверяем существует ли файл
            if os.path.exists(DATA_R):
                with open(DATA_R, 'r', encoding='utf-8') as fileopen:
                    print(fileopen.read())
                    fileopen.close()
                    exit(0)
            else:
                print("Файла несуществует!!!")
                exit(0)
        else:
            self.distance = distance

    def shoot(self, rec):
        self.rec = rec
        return self.rec


class MotherBoard(Gun):

    def shoot_gui(self, delta_time):
        self.delta_time = delta_time
        print("Производим выстрел...")
        for i in boot.tqdm(range(int(self.delta_time))):
            sleep(1)
            pass

    def angle_var(self):
        # Проверяет, что бы входное значение для расстояния до цели
        # было меньше или равно 2000 метров
        if self.distance <= 2000:
            angle_g = (self.distance / (SPEED_B ** 2 / G)) / 2
            time_d = 2 * SPEED_B * math.sin(round(math.degrees(math.pi / 2 - angle_g), 2)) / G
            # Вызов интерфейса
            calculate.calculate_main()
            print(f"{boot.Fore.RED}Расстояние до цели: "
                  f"{boot.Fore.GREEN}{self.distance} {boot.Fore.RED}"
                  f"метров\n"
                  f"{boot.Fore.RED}Необходимый угол: "
                  f"{boot.Fore.GREEN}"
                  f"{round(math.degrees(math.pi / 2 - angle_g), 2)}"
                  f" {boot.Fore.RED}"
                  f"градусов\n"
                  f"Необходимое время до цели: {boot.Fore.GREEN}{round(time_d, 2)}"
                  f" {boot.Fore.RED}"
                  f" секунд"
                  f"{boot.Fore.RESET}")
            self.shoot_gui(time_d)
            print("Запись данных в файл...")
            # Открываем файл в формате добавление данных с кодировкой
            # UTF-8
            with open(DATA_R, 'a', encoding='utf-8') as fileopen:
                fileopen.write(f"Время на текущий момент: {dt.datetime.now()}\n"
                               f"Расстояние до цели: {self.distance} "
                               f"метров\n"
                               f"Угол наведения: {round(math.degrees(math.pi / 2 - angle_g), 2)}"
                               f" градусов\n"
                               f"Время до цели: {round(time_d, 2)} секунд\n")
                fileopen.close()
            return f"CAAABOOOMMMM"
        else:
            return f"Превышена максимальная дистанция стрельбы..."


# Запускаем эмуляцию загрузки операционной системы
boot.boot()
# Вводим данные
c1 = MotherBoard(int(input(f"{CONSOLE_T}Укажите расстояние "
                           f"до цели(метры) или наберите 1 для просмотра записей:\n>>> ")))
print(c1.shoot(c1.angle_var()))
