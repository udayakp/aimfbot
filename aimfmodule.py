import aimodule
import requests
import json2html
import json
import json2html.*

def fetch(url,message):
    #render_template('chat.html')
    message = message.replace("fetch","")
    message = message.replace(":","")
    message = message.replace(" ","")
    url1 = url + message
    print(message)
    print(url1)
    myResponse = requests.get(url1,verify = True)
    if(myResponse.ok):
        jData = json.loads(myResponse.content)
        #print("The response contains {0} properties".format(len(jData)))
        #print("\n")
        for key in jData:
            a = key + " : " + jData[key]
    else:
        a = myResponse.raise_for_status()

    b = json2html.convert(json = jData)
    print(json2html.convert(a))
    print(jData)
    print(b)
    return b
