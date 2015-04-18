import unittest
import ConfigParser


class TestConfig(unittest.TestCase):
    config = None

    def setUp(self):
        self.config = ConfigParser.RawConfigParser()
        self.config.readfp(open('config.cfg'))

    def test_read_config(self):
        self.assertNotEqual('', self.config.get('email', 'from'))
        self.assertNotEqual('', self.config.get('email', 'to'))
        self.assertNotEqual('', self.config.get('secret', 'app_key'))
        self.assertNotEqual('', self.config.get('secret', 'app_secret'))
        self.assertNotEqual('', self.config.get('secret', 'username'))
        self.assertNotEqual('', self.config.get('secret', 'password'))
        self.assertNotEqual('', self.config.get('secret', 'token'))
        self.assertNotEqual('', self.config.get('secret', 'target'))
