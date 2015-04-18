import subprocess
import unittest
import time


class TestMailDump(unittest.TestCase):
    process = None
    sender = 'sender@test.com'
    recipient = 'recipient@test.com'
    msg = 'test'

    def setUp(self):
        self.process = subprocess.Popen(["maildump"])
        time.sleep(0.5)  # Start the server

    def tearDown(self):
        self.process.kill()
