import subprocess
import unittest
import time
import requests


class TestMailDump(unittest.TestCase):
    process = None

    def setUp(self):
        self.process = subprocess.Popen(["maildump"])
        time.sleep(0.5)  # Start the server
        print self.process.pid

    def tearDown(self):
        self.process.kill()


class TestSendMail(TestMailDump):
    url_ = 'http://127.0.0.1:1080'

    def test_get_index(self):
        res = requests.get(self.url_)
        self.assertEquals(200, res.status_code)

    def test_get_messages_empty(self):
        res = requests.get('http://127.0.0.1:1080/messages/')
        self.assertEquals(200, res.status_code)
        json = res.json()
        self.assertEquals(0, len(json.get('messages')))

if __name__ == '__main__':
    unittest.main()
