#!/usr/bin/python3
import requests


url1 = "https://api.telegram.org/bot"
url2 = "6079555288:AAF7j1X0Y4E6T_o5VnPe6j32RPJj2Alnljc"
mainUrl = "{}{}/".format(url1, url2)

def update():
    para = {
            "offset" : "382262717",
            "limit" : "29"
    }
    req = requests.get(mainUrl + "getUpdates", data = para)
    print(req)
    reqs = req.json()
    print(reqs)
    for r in reqs.get("result"):
        if "blablabla" in r["message"]["text"]:
            send()

def send():
    para = {
            "chat_id" : "-739708965",
            "text" : "documentation"
    }

    req = requests.get(mainUrl + "sendMessage", data = para)
    reqs = req.json()
    print(reqs)

update()
