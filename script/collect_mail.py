import imaplib
import pprint

print("entré 1 pour l'utilisation par l'host par defaut : outlook.office365.com")
print("entré 2 pour utiliser un autre host")
host = input()


imap_host='outlook.office365.com'
if host > '1' :
    print("entré votre host :")
    imap_host = input()


line = []
print("utilisation d'un fichier credentials ? (O/N)")
if input() == 'N' :
    print("entré votre email :")
    line.append(input())
    print("entré votre mot de passe :")
    line.append(input())
else :
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

print("veuillé faire voter choix de mailbox.\n par defaut \"Inbox\"")
print("entré votre boite au lettre : ")
imap.select(input())
#imap.select('Inbox')

tmp, data = imap.search(None, 'ALL')
for num in data[0].split():
    tmp, data = imap.fetch(num, '(RFC822)')
    print('Message: {0}\n'.format(num))
    pprint.pprint(data[0][1])
    break

imap.close()