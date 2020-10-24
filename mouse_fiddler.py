from pyautogui import position, moveTo
from threading import Thread
from time import sleep
from random import choice

from pogan_feature import PoganFeature


class MouseFiddler(PoganFeature):
    def __init__(self, filename: str, log_dir: str, fistun_level: int = 1, log=True):
        super().__init__("[Mouse Fiddler]", filename, log_dir, log)

        self.fistun_level = fistun_level
        self.runner_thread = Thread(target=self.fiddle)

    def run(self):
        self.logger.write('Started Fistuner!')
        self.runner_thread.start()

    def clean(self):
        self.logger.write('Fistuner stopped!')
        self.kill = True

    def fiddle(self):
        while True:
            if self.kill:
                break

            self.move_mouse()
            sleep(0.1)

    def move_mouse(self):
        pos = position()

        moveTo(pos.x + choice([-1, 1]) * 10 * self.fistun_level, pos.y + choice([-1, 1]) * 10 * self.fistun_level)
