import subprocess
import unittest
import time


class TestMailDump(unittest.TestCase):
    process = None

    def setUp(self):
        self.process = subprocess.Popen(["maildump"])
        time.sleep(0.5)  # Start the server
        print self.process.pid

    def tearDown(self):
        self.process.kill()
