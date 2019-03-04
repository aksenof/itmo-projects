#!/usr/bin/env

# Autor: Andrey Aksenov
# Contacts: 
# E-mail: aksenov.andrey95@yandex.ru
# Tel: +7(920)460-40-10

# yandex-translate api

import requests
import string
import re

def autoswitch(text):
	en = list(string.ascii_letters)
	for i in text:
		if i in en:
			return 'ru'
		else:
			return 'en'

def translation(text, lang):
	url = 'https://translate.yandex.net/api/v1.5/tr/translate?'
	key = 'trnsl.1.1.20171005T121221Z.0b297e03b06ce40a.6bebdb267a946d905b74313a0ff0518da5a1df11'
	r = requests.post(url, data={'key': key, 'text': text, 'lang': lang})
	return r.text

data = input("Enter text: ")
result = re.findall(r'<text>(.+)</text>', translation(data, autoswitch(data)))
print("Translation:", "".join(result))
