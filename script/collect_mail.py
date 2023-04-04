import imaplib
import pprint

imap_host='outlook.office365.com'


line = []
with open('credentials.txt', 'r') as f :
    for l in f.readlines():
        line.append((l.rstrip('\n')))
    f.close()
    
imap_user = line[0]
imap_pass = line[1]

# connect to host using SSL
imap = imaplib.IMAP4_SSL(imap_host)

## login to server
imap.login(imap_user, imap_pass)

imap.select('Inbox')

tmp, data = imap.search(None, 'UNSEEN')
for num in data[0].split():
	tmp, data = imap.fetch(num, '(RFC822)')
	print('Message: {0}\n'.format(num))
	pprint.pprint(data[0][1])
	break
imap.close()