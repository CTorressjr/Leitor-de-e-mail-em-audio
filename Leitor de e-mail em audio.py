from imbox import Imbox
import html2text
from gtts import gTTS 
import urllib.parse
import requests

host = 'imap.gmail.com'
email = 'carlostorressjrdev@gmail.com'
password = 'hjqe tkom neqk bcuf'

with Imbox(host, username=email, password=password, ssl=True) as imbox:
    messages = imbox.messages(unread=True)
    for uid, message in messages:
        if message.sent_from[0] == {'name': 'Thiago Faria, AlgaWorks', 'email': 'contato@algaworks.com'}:
            titulo = (f"Assunto: {message.subject}")
            corpo_plain = message.body['plain'][0]
            if isinstance(corpo_plain, bytes):
                corpo_plain = corpo_plain.decode('utf-8')
            
            corpo = corpo_plain.replace('\r\n', ' ').strip()

text_maker = html2text.HTML2Text()
text_maker.ignore_links = True
text = text_maker.handle(corpo)
Email = titulo + '\n' + text

tts = gTTS(Email, lang='pt')
tts.save('audio.OGG')



