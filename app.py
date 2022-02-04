from flask import Flask, request,Response
import requests
import xmltodict as XD

app = Flask(__name__)

print("running")

@app.route("/", methods=['POST'])
def parse_xml():
    try:
        tree = XD.parse(request.get_data()) #解析傳入的XML內容
        msg = info2String(tree['alert']['info']) #取出資訊,可視需要調整
        telegram_bot_sendtext(msg) #透過BOT傳送訊息
        xmlString ='<?xml version="1.0" encoding="utf-8"?><Data><Status>true</Status></Data>' #回覆民生示警主機
        return Response(xmlString, mimetype='text/xml')

    except:
        telegram_bot_sendtext("something went wrong!!")
        xmlString ='<?xml version="1.0" encoding="utf-8"?><Data><Status>false</Status></Data>'
        return Response(xmlString, mimetype='text/xml')

#解出XML裡的資料, 這裡是取INFO內的 headline、description及areaDesc這三種TAG的資訊
def info2String(info):    
    returnString =""    
    if type(info) is list:
        for i in info:
            returnString +=(i['headline'])+ "\n"
            returnString +=(i['description'])+ "\n"
            returnString += areaDesc2String(i['area']) + "\n"
    else:
        returnString +=(info['headline'])+ "\n"
        returnString +=(info['description'])+ "\n"
        returnString += areaDesc2String(info['area']) + "\n"
    
    return returnString

def areaDesc2String(area):
    returnString =""
    if type(area) is list:
        for a in area:
            returnString += a['areaDesc'] + " "
    else:
        returnString = area['areaDesc']
    
    return returnString
    

#由TELEGRAM API 發送訊息
def telegram_bot_sendtext(bot_message):    
    bot_token = '' #你的TELEGRAM BOT TOKEN
    bot_chatID = '' #你的 TELEGTAM CHAT ID
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message
    response = requests.get(send_text)
    return response.json()
    

if __name__ == '__main__':
    print("Starting flask app")
    app.run(host='0.0.0.0', port=8080, debug=False)