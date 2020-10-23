from pyautogui import position, moveTo
from threading import Thread
from time import sleep

from pogan_feature import PoganFeature


class MouseFiddler(PoganFeature):
    def __init__(self, filename: str, log_dir: str, fistun_level: int = 1):
        super().__init__("[Mouse Fiddler]", filename, log_dir)

        self.fistun_level = fistun_level
        self.runner_thread = Thread(target=fiddle)

    def run(self):
        self.runner_thread.start()

    def clean(self):
        self.runner_thread.join()

    def fiddle(self):
        while True:
            pass

