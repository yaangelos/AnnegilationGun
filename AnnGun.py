import math
import boot
from time import sleep
import calculate
import datetime as dt
G = 9.81
SPEED_B = 1000
CONSOLE_T = 'G.U.N.D.A.M. /># '
DATA_R = 'datarecord.txt'


class Gun:
    def __init__(self, distance):
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
            if self.distance <= 2000:
                angle_g = (self.distance / (SPEED_B ** 2/G))/2
                time_d = 2 * SPEED_B * math.sin(round(math.degrees(math.pi/2 - angle_g), 2))/G
                calculate.calculate_main()
                print(f"{boot.Fore.RED}Расстояние до цели: "
                      f"{boot.Fore.GREEN}{self.distance} {boot.Fore.RED}"
                      f"метров\n"
                      f"{boot.Fore.RED}Необходимый угол: "
                      f"{boot.Fore.GREEN}"
                      f"{round(math.degrees(math.pi/2 - angle_g), 2)}"
                      f" {boot.Fore.RED}"
                      f"градусов\n"
                      f"Необходимое время до цели: {boot.Fore.GREEN}{round(time_d, 2)}"
                      f" {boot.Fore.RED}"
                      f" секунд"
                      f"{boot.Fore.RESET}")
                self.shoot_gui(time_d)
                print("Запись данных в файл...")
                with open(DATA_R, 'a', encoding='utf-8') as fileopen:
                    fileopen.write(f"Время на текущий момент: {dt.datetime.now()}\n"
                                   f"Расстояние до цели: {self.distance} "
                                   f"метров\n"
                                   f"Угол наведения: {round(math.degrees(math.pi/2 - angle_g), 2)}"
                                   f" градусов\n"
                                   f"Время до цели: {round(time_d, 2)} секунд\n")
                    fileopen.close()
                return f"CAAABOOOMMMM"
            else:
                return f"Превышена максимальная дистанция стрельбы..."


boot.boot()
c1 = MotherBoard(int(input(f"{CONSOLE_T}Укажите расстояние до цели(метры):\n>>> ")))
print(c1.shoot(c1.angle_var()))