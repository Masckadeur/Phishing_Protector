from bs4 import BeautifulSoup as sp
import url_finder

f = open('texte2.txt', 'r')
html_doc = f.read()
f.close()
f = open('ban/domaine.txt')
bannedDomain = f.read().split('\n')
f.close()
soup = sp(html_doc, 'html.parser')


def analyse_redirection_fraudulente(soup):
    for link in soup.find_all('a'):
        vis = url_finder.Find(str(link))
        if(len(vis)>0):
            if(len(vis) != vis.count(vis[0])):
                return False
            for ban in bannedDomain:
                if(ban in vis[0]):
                    return False
    return True

print(analyse_redirection_fraudulente(soup))


# href
# redirection fraudulente


#print(soup.find_all('a'))