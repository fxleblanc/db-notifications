import subprocess
import unittest
import time
import requests
import smtplib
from test_utils import TestMailDump


class TestSendMail(TestMailDump):
    host = '127.0.0.1'
    http_port = '1080'
    smtp_port = '1025'  # TODO put in TestMailDump
    url = 'http://' + host + ':' + http_port

    def test_get_index(self):
        res = requests.get(self.url)
        self.assertEquals(200, res.status_code)

    def test_get_messages_empty(self):
        res = requests.get(self.url + '/messages/')
        self.assertEquals(200, res.status_code)
        json = res.json()
        self.assertEquals(0, len(json.get('messages')))

    def test_send_mail(self):
        mail = smtplib.SMTP(self.host, self.smtp_port)
        mail.sendmail(self.sender, self.recipient, self.msg)
        sentMail = self.get_email()
        text = sentMail.text
        self.assertEquals(self.msg, text)

    def get_email(self):
        res = requests.get(self.url + '/messages/')
        self.assertEquals(200, res.status_code)
        json = res.json()
        self.assertEquals(1, len(json.get('messages')))
        sent = json.get('messages')[0]
        self.assertEquals(self.sender, sent.get('sender'))
        self.assertEquals(self.recipient, sent.get('recipients').get('to')[0])
        return requests.get(self.url + '/messages/1.plain')

if __name__ == '__main__':
    unittest.main()
