from threading import Thread
from time import sleep


class Knight(Thread):
    res = []

    def __init__(self, name, power):
        self.kname = name
        self.power = power
        super().__init__()


    def run(self):
        print(f'{self.kname}, на нас напали!')
        enames = 100
        days = 0
        while enames > 0:
            sleep(1)
            days += 1
            enames -= self.power
            if enames < 0:
                enames = 0
            print(f'{self.kname} сражается {days} суток, осталось {enames} воинов врага.')
        print(f'{self.kname} одержал победу спустя {days} дней(я)!')



knight1 = Knight('Sir Lancelot', 10)
knight2 = Knight("Sir Galahad", 20)
knight1.start()
knight2.start()
knight1.join()
knight2.join()
