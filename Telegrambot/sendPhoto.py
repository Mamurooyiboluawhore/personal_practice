#!/usr/bin/python3
import requests
import time 


url1 = "https://api.telegram.org/bot"
url2 = "6079555288:AAF7j1X0Y4E6T_o5VnPe6j32RPJj2Alnljc"
mainUrl = "{}{}/sendPhoto".format(url1, url2)
photos = ["https://unsplash.com/photos/dVNoqURVajk", "https://unsplash.com/photos/dSZnxGNlP30", "https://unsplash.com/photos/D61LodCA3go"]
for photo in photos:
    time.sleep(60) 
    para = {
            "chat_id" : "-739708965",
            "photo" : photo
    }

    req = requests.get(mainUrl, data = para)
#reqs = req.json()
#print(reqs)

