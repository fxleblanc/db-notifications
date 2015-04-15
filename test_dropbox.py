import dropbox
import smtplib
import schedule
import time
import unittest
import ConfigParser

config = ConfigParser.RawConfigParser()
config.readfp(open('config.cfg'))


class TestDropbox(unittest.TestCase):
    def test_get_folder(self):
        token = config.get('secret', 'token')
        target = config.get('secret', 'target')
        client = dropbox.client.DropboxClient(token)
        folder_metadata = client.metadata(target)
        expected = u'/' + target
        self.assertEqual(expected, folder_metadata['path'])

    def test_read_config(self):
        self.assertNotEqual('', config.get('email', 'from'))
        self.assertNotEqual('', config.get('email', 'to'))
        self.assertNotEqual('', config.get('secret', 'app_key'))
        self.assertNotEqual('', config.get('secret', 'app_secret'))
        self.assertNotEqual('', config.get('secret', 'username'))
        self.assertNotEqual('', config.get('secret', 'password'))
        self.assertNotEqual('', config.get('secret', 'token'))
        self.assertNotEqual('', config.get('secret', 'target'))

if __name__ == '__main__':
    unittest.main()
