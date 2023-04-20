import imaplib
import email
from email.header import decode_header
import os
import analyse_emmeteur as ae
import analyse_extension as aex


print("entrez 1 pour l'utilisation par l'host par defaut : outlook.office365.com")
print("entrez 2 pour utiliser un autre host")
host = input()


imap_host='outlook.office365.com'
if host > '1' :
    print("entré votre host :")
    imap_host = input()


line = []
print("utilisation d'un fichier credentials ? (O/N)")
if input() == 'N' :
    print("entrez votre email :")
    line.append(input())
    print("entrez votre mot de passe :")
    line.append(input())
else :
    with open('credentials.txt', 'r') as f :
        for l in f.readlines():
            line.append((l.rstrip('\n')))
        f.close()
    
username = line[0]
password = line[1]

imap = imaplib.IMAP4_SSL(imap_host)
## authenticate
imap.login(username, password)
print("\nLongin sucessful")

status, messages = imap.select("Inbox")

N = int(input("Entrez le nombre de mail à récupérer :\n"))
print("-"*100)

messages = int(messages[0])
###
for i in range(messages, messages-N, -1):
    res, msg = imap.fetch(str(i), "(RFC822)")
    for response in msg:
        
        if isinstance(response, tuple):
            msg = email.message_from_bytes(response[1])
            subject = decode_header(msg["Subject"])[0][0]
            if isinstance(subject, bytes):
                subject = subject.decode('latin-1')
            
            print("Subject:", subject)
            emetteur = msg.get("From") 
            print("From:", emetteur)
            if not ae.verif(emetteur):	# check émetteur parmis une liste ban (pour les test adresse email erwan.benard@epita.fr et *@epita.fr)
            	print("émetteur interdit")

            if msg.is_multipart():
                for part in msg.walk():
                    content_type = part.get_content_type()
                    content_disposition = str(part.get("Content-Disposition"))
                    try:
                        body = part.get_payload(decode=True).decode('latin-1')
                    except:
                        pass
                    if content_type == "text/html" and "attachment" not in content_disposition:
                        index = str(part).find('<')
                        body = str(part)[index:]
                    elif content_type == "text/plain" and "attachment" not in content_disposition:
                        print(body)
                    elif "attachment" in content_disposition:
                        filename = part.get_filename()
                        if not aex.verif(filename.split('.')[-1]):
                            print(filename, " !!! fichier interdit") #Vérifie si l'extension est autorisé

                        
                        if filename:
                            filepath = os.path.join('.', 'pieces_jointes', filename)
                            open(filepath, "wb").write(part.get_payload(decode=True))

            print("="*100)

imap.close()
imap.logout()