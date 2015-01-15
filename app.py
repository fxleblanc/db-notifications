import dropbox
import smtplib
import schedule
import time

app_key=''
app_secret=''
username = ''
password = ''
fromaddr = ''
toaddr = ''

msg = 'Subject: %s\n\n%s' % ('File added to dropbox', 'A new File has been added to your Dropbox folder')

flow = dropbox.client.DropboxOAuth2FlowNoRedirect(app_key, app_secret)

authorize_url = flow.start()
print authorize_url
code = raw_input("Enter the authorization code here: ").strip()
access_token, user_id = flow.finish(code)
client = dropbox.client.DropboxClient(access_token)
email = False

def job():
	global email
	folder_metadata = client.metadata('/felix-helene')
	folder = folder_metadata['contents']
	if(len(folder) == 0):
		print 'The folder is empty'
		email = True
	else:
		print 'A file has been detected'
		if email:
			server = smtplib.SMTP('smtp.gmail.com:587')
			server.starttls()
			server.login(username, password)
			server.sendmail(fromaddr, toaddr, msg)
			server.quit()			
			email = False

schedule.every().hour.do(job)

while True:
	schedule.run_pending()
	time.sleep(1)
