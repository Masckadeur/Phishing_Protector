import open_file as op

def verif(str):
    ban = op.open_file("ban/emetteur.txt")
    if str in ban:
        return False
    else:
        return True