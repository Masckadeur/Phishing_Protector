import analyse_mail_html as ana
import pytest # importing our library of test
 
# 3 test cases are defined in this test suite

f = open("../../mails/hyperlien/mail_bon_lien.html", 'r')
html_doc = f.read()
f.close()
f.close()
soup1 = sp(html_doc, 'html.parser') 

f = open("../../mails/hyperlien/mail_bon_lien.html", 'r')
html_doc = f.read()
f.close()
f.close()
soup2 = sp(html_doc, 'html.parser') 

f = open("../../mails/hyperlien/mail_bon_lien.html", 'r')
html_doc = f.read()
f.close()
f.close()
soup3 = sp(html_doc, 'html.parser') 

f = open("../../mails/hyperlien/mail_bon_lien.html", 'r')
html_doc = f.read()
f.close()
f.close()
soup4 = sp(html_doc, 'html.parser') 

class TestRedirect:
    def test_lien_correct():
        assert(ana.analyse_redirection_fraudulente(soup1))
 
    def test_lien_rediriger():
        assert(ana.analyse_redirection_fraudulente(soup2))
 
    def test_cliquer_ici_correct():
        assert(ana.analyse_redirection_fraudulente(soup3))

    def test_clicuer_ici_incorect():
        assert(ana.analyse_redirection_fraudulente(soup4))