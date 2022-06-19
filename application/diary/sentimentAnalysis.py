import requests
import json

urls = [
[0, "https://pixel.mathtag.com/misc/img?mop_seq=0:20&mt_cb=901000&mop_top="],
[0, "https://pixel.mathtag.com/misc/img?mop_seq=10:20&mt_cb=770176&mop_top=4:1655365272|9:1655365272|13:1655365272|3:1655365272|21:1655365272|5:1655365272|10010:1655365272|15:1655365272|10017:1655365272|10074:1655365272|"],
[0, "https://pixel.mathtag.com/misc/img?mop_seq=20:20&mt_cb=482753&check=636c62aa-de35-4200-a1a7-f89d60b447ba&mop_top=4:1655365272|9:1655365272|13:1655365272|3:1655365272|21:1655365272|5:1655365272|10010:1655365272|15:1655365272|10017:1655365272|10074:1655365272|42:1655365272|17:1655365272|46:1655365272|40:1655365272|10041:1655365272|30:1655365272|44:1655365272|10031:1655365272|10025:1655365272|10004:1655365272|"]
]
cookies = {}

for i in range(len(urls)):
    req = requests.get(urls[i][1])
    if(cookies == {}):
        cookies = req.cookies
    else:
        cookies.update(req.cookies)

url = 'https://tone-analyzer-demo.ng.bluemix.net/api/tone'



def analyse(text):
    payload = {'toneInput[text]': text, 'contentLanguage': 'en'}
    res = requests.post(url, data=payload, cookies=cookies)

    result = json.loads(res.text)

    sentiment = [0,""]
    for i in result['document_tone']['tones']:
        if(i['score'] > sentiment[0]):
            sentiment[0] = i['score']
            sentiment[1] = i['tone_id']

    return sentiment[1]

if __name__ == '__main__':
    text = "I met with my school friends today, it was a great day, enjoyed a lot of fun, and I learned a lot about the world."
    sentiment = analyse(text)
    print(sentiment)