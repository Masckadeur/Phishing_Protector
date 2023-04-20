def open_file(str):
    f = open(str, 'r')
    txt = f.read()
    f.close()
    return txt