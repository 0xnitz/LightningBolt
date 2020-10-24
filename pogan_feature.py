from logger import Logger


class PoganFeature:
    def __init__(self, header, filename, log_dir, log):
        self.logger = Logger(header, filename, log_dir, log)
        self.kill = False

    def run(self):
        pass

    def clean(self):
        pass
