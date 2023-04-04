from bs4 import BeautifulSoup as sp

f = open('texte.txt', 'r')
html_doc = f.read()
f.close()

soup = sp(html_doc, 'html.parser')


for link in soup.find_all('a'):
    print(link.get('href'))

print(soup.find_all('a'))