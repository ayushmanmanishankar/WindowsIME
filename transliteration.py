import requests
import keyboard
import time

def getSuggestions(str):
    url = "https://revapi.reverieinc.com/"
    headers = {
        "Content-Type": "application/json",
        "REV-API-KEY": "172c5bb5af18516905473091fd58d30afe740b3f",
        "REV-APP-ID": "rev.transliteration",
        "REV-APPNAME": "transliteration",
        "src_lang": "en",
        "tgt_lang": "hi",
        "domain": "1",
        "cnt_lang": "en",
    }

    data = {
        "data": [str],
        "isBulk": False,
        "ignoreTaggedEntities": False,
        "noOfSuggestions": 5
    }

    try:
        response = requests.post(url, headers=headers, json=data)

        if response.status_code == 200:
            return (response.json()['responseList'][0]['outString'])
        else:
            print(f"Request failed with status code {response.status_code}")

    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
# dic=['kaise','ho','aap','?','kya','aap','theek','ho','?']
# time.sleep(2)
# for i in range(0,len(dic)):
#     suggestList=getSuggestions(dic[i])
#     time.sleep(1)
#     keyboard.write(suggestList[0]+' ')
    
