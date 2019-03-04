#!/usr/bin/python
#
# This program can recognize and convert Images to Docx via ABBYY Cloud OCR SDK Technologies
#
# Application Id and Password are registered on Andrey Aksenov (aksenov.andrey95@yandex.ru)
#
import base64
import os
import requests
import sys
import time
import xml.dom.minidom

APP_ID = 'Test-App-Id'
PASSWORD_ID = 'vWS56lEDeOEFiPZFrQu9NN84'
URL = "https://cloud.ocrsdk.com/"
LANGUAGE = 'Russian'
EXPORT_FORMAT = 'docx'
FILE = '[Untitled]001.jpg' # as an example
DOWNLOAD_URL = None
TASK_ID = None
TASK_STATUS = None


def fs(path_to_file):  # function witch split way, name and extension of file
    base = os.path.basename(path_to_file)
    way = os.path.split(path_to_file)[0]
    name = os.path.splitext(base)[0]
    ext = os.path.splitext(base)[1]
    return [way, name, ext]


def processImage(server):
	return server+"processImage"


def getTaskStatus(server):
	return server+"getTaskStatus"


def auth_info(ApplicationId, Password):
	toEncode = '{}:{}'.format(ApplicationId, Password)
	baseEncoded = str(base64.b64encode(bytes(toEncode, encoding='iso-8859-1')))[2:-1]
	return {'Authorization': 'Basic '+baseEncoded}


def post_request(url, filepath, language, exportFormat):
	payload = {'language': language, 'exportFormat': exportFormat}
	auth = auth_info(APP_ID, PASSWORD_ID)
	with open(filepath, 'rb') as fp:
		f = {'file': fp}
		r = requests.post(url, data=payload, headers=auth, files=f)
	return str(r.text)


def response(xml_response):
	global TASK_ID
	global TASK_STATUS
	global DOWNLOAD_URL
	dom = xml.dom.minidom.parseString(xml_response)
	task_node = dom.getElementsByTagName("task")[0] 
	TASK_ID = task_node.getAttribute("id")
	TASK_STATUS = task_node.getAttribute("status")
	if TASK_STATUS == "Completed":
		DOWNLOAD_URL = task_node.getAttribute("resultUrl")
	return [TASK_ID, TASK_STATUS, DOWNLOAD_URL]


def get_request(url):
	global TASK_ID
	auth = auth_info(APP_ID, PASSWORD_ID)
	taskid = TASK_ID
	payload = {'taskId': taskid}
	r = requests.get(url, params=payload, headers=auth)
	return str(r.text)

print(response(post_request(processImage(URL), FILE, LANGUAGE, EXPORT_FORMAT))[1])

while TASK_STATUS == "InProgress" or TASK_STATUS == "Queued":
	time.sleep(5)
	sys.stdout.write(".")
	print(TASK_STATUS)
	response(get_request(getTaskStatus(URL)))
if TASK_STATUS == "Completed" and DOWNLOAD_URL != None:
	print(TASK_STATUS)
if TASK_STATUS == 'NotEnoughCredits':
	print("Not enough credits to process the document.")
	print("Please add more pages to your application`s account:")
	print("https://cloud.ocrsdk.com/Account/Welcome")
	sys.exit()
else:
	print("ERROR, try again")

new_file = "{0}{1}_ocr.docx".format(fs(FILE)[0], fs(FILE)[1])
with open(new_file, "wb") as document:
	req = requests.get(DOWNLOAD_URL, stream=True)
	for chunk in req.iter_content(1024):
		document.write(chunk)
print("File saved:", new_file)
