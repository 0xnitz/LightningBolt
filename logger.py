from os import chdir, path, remove

from exceptions import PoganException


class Logger:
    def __init__(self, header: str, filename: str, log_dir: str):
        self.header = header
        self.filename = filename
        self.log_dir = log_dir

        if path.exists(self.log_dir):
            chdir(self.log_dir)
            try:
                remove(self.filename)
            except FileNotFoundError:
                pass

    def write(self, buf):
        if path.exists(self.log_dir):
            chdir(self.log_dir)
        else:
            raise PoganException

        try:
            open(self.filename, 'a').write(self.header + buf)
        except (OSError, FileNotFoundError):
            raise PoganException

    def get_log_dir(self):
        return self.log_dir
