#!/usr/bin/python3
import requests
import time 


#url = "https://api.telegram.org/bot{}/getUpdates".format(
#      "6079555288:AAF7j1X0Y4E6T_o5VnPe6j32RPJj2Alnljc/getUpdates"
#)
url1 = "https://api.telegram.org/bot"
url2 = "6079555288:AAF7j1X0Y4E6T_o5VnPe6j32RPJj2Alnljc"
mainUrl = "{}{}/sendMessage".format(url1, url2)
#res = requests.get(mainUrl)
#resp = res.json()
#print(resp)
YOUseries = ["Hi Joe, I know It's you", "I will find you Joe", "You cant't run away for too long", "That's a promise"]
for seriess in YOUseries:
    time.sleep(5)
    para = {
            "chat_id" : "-739708965",
            "text" : seriess
    }

    req = requests.get(mainUrl, data = para)
#reqs = req.json()
#print(reqs)

