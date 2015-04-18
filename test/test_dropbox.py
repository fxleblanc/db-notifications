import dropbox
import smtplib
import schedule
import time
import unittest
import ConfigParser
from test_config import TestConfig


class TestDropbox(TestConfig):
    def test_get_folder(self):
        token = self.config.get('secret', 'token')
        target = self.config.get('secret', 'target')
        client = dropbox.client.DropboxClient(token)
        folder_metadata = client.metadata(target)
        expected = u'/' + target
        self.assertEqual(expected, folder_metadata['path'])

if __name__ == '__main__':
    unittest.main()
