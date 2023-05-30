#!/usr/bin/python3
import requests
import time 


url1 = "https://api.telegram.org/bot"
url2 = "6079555288:AAF7j1X0Y4E6T_o5VnPe6j32RPJj2Alnljc"
mainUrl = "{}{}/sendDocument".format(url1, url2)
doc = open("AirBnB_clone_v2/1-pack_web_static.py", "rb")
print(doc)

para = {
            "chat_id" : "-739708965",
            "caption" : "here is a document"
}

files = {
        "document" : doc
}

req = requests.post(mainUrl, data = para, files=files)
reqs = req.json()
print(reqs)

