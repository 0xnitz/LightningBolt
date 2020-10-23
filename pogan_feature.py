from logger import Logger


class PoganFeature:
    def __init__(self, header, filename, log_dir):
        self.logger = Logger(header, filename, log_dir)

    def run(self):
        pass

    def clean(self):
        pass
