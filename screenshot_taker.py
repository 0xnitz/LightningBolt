from threading import Thread
from numpy import array
from cv2 import cvtColor, imwrite, COLOR_RGB2BGR
from pyautogui import screenshot
from os import chdir, remove, path
from time import sleep

from pogan_feature import PoganFeature
from exceptions import PoganException


class ScreenshotTaker(PoganFeature):
    def __init__(self, screenshot_filename: str, filename: str, log_dir: str):
        super().__init__("[Screenshot Taker]", filename, log_dir)

        self.screenshot_filename = screenshot_filename
        self.runner_thread = Thread(target=self.screenshot_manager)

    def run(self):
        self.runner_thread.start()

    def clean(self):
        self.runner_thread.join()

    def screenshot_manager(self):
        while True:
            self.take_screenshot()
            self.send_screenshot()
            self.delete_screenshot()
            sleep(1)

    def take_screenshot(self):
        image = screenshot()
        image = cvtColor(array(image), COLOR_RGB2BGR)

        if path.exists(self.logger.get_log_dir()):
            chdir(self.logger.get_log_dir())
        else:
            raise PoganException

        imwrite(self.screenshot_filename, image)

        self.logger.write('Took screenshot!\n')

    def delete_screenshot(self):
        if path.exists(self.logger.get_log_dir()):
            chdir(self.logger.get_log_dir())
            try:
                remove(self.screenshot_filename)
            except (FileNotFoundError, OSError):
                raise PoganException

        self.logger.write('Delete screenshot!\n')

    def send_screenshot(self):
        pass
