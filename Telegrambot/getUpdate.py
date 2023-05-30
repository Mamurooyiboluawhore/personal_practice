#!/usr/bin/python3
import requests


#url = "https://api.telegram.org/bot{}/getUpdates".format(
#      "6079555288:AAF7j1X0Y4E6T_o5VnPe6j32RPJj2Alnljc/getUpdates"
#)
url1 = "https://api.telegram.org/bot"
url2 = "6079555288:AAF7j1X0Y4E6T_o5VnPe6j32RPJj2Alnljc"
mainUrl = "{}{}/getUpdates".format(url1, url2)
#res = requests.get(mainUrl)
#resp = res.json()
#print(resp)
para = {
        "offset" : "382262710",
        "limit" : "2"
}
req = requests.get(mainUrl, data = para)
reqs = req.json()
print(reqs)
