from PyDictionary import PyDictionary
import random
import smtplib

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class Word_Definitions(object):
    def __init__(self):
        words = open('word_list.txt','r')
        word_list = []
        [word_list.append(x.strip()) for x in words]
        random.shuffle(word_list)
        word = word_list[0]
        dictionary = PyDictionary()
        definition = dictionary.meaning(word)

        type = (", ".join(list(definition.keys())))
        mydef = ("\n".join(list(definition.values())[0]))
        message = "\n"+word+"\n"+type+"\n"+mydef

        fromaddr = "jakesmorrison@gmail.com"
        toaddr = "2083183228@txt.att.net"
        msg = MIMEMultipart()
        msg['From'] = fromaddr
        msg['To'] = toaddr
        msg['Subject'] = "\n"

        body = message
        msg.attach(MIMEText(body, 'plain'))

        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(fromaddr, "BrettFavre13")
        text = msg.as_string()
        server.sendmail(fromaddr, toaddr, text)
        server.quit()

Word_Definitions()