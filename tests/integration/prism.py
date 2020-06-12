import logging
import shlex
import subprocess
import sys
import threading

logger = logging.getLogger(__name__)


class MockServer(object):
    def __init__(self, cmd=None, quiet=True):
        super().__init__()
        self.cmd = cmd
        self.quiet = quiet
        self._proc = None
        self._thread = None
        self._ready = False

        assert self.cmd is not None, "Must provide Prism CLI command"
        logger.info(self.cmd)

    def _process(self):
        self._proc = subprocess.Popen(
            shlex.split(self.cmd),
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            universal_newlines=True
        )

        while True:
            line = self._proc.stdout.readline()  # blocking call
            if not line:
                break
            if line != "":
                if not self.quiet:
                    sys.stdout.write(line)
                if "Prism is listening" in line:
                    self._ready = True
                    logger.info(line.rstrip('\n'))

        logger.info("Server process completed...")

    def start(self):
        logger.info("Server process initialise...")
        self._thread = threading.Thread(target=self._process)
        self._thread.start()

    def stop(self):
        logger.info("Server process stopping...")
        if self._thread.is_alive():
            self._proc.terminate()
            self._thread.join()

    close: stop

    @property
    def ready(self):
        return self._ready
