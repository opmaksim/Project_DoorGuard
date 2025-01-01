import requests
import json
#import server1


#1.
with open(r"D:\Study\Academy\Project_DoorGuard\API\kakao_code.json","r") as fp:
    tokens = json.load(fp)
	


url="https://kapi.kakao.com/v2/api/talk/memo/default/send"

# kapi.kakao.com/v2/api/talk/memo/default/send 

headers={
    "Authorization" : "Bearer " + tokens["access_token"]
}

data={
    "template_object": json.dumps({
        "object_type":"text",
        "text":"사람이 감지되었습니다. 지금 바로 확인하세요! http://localhost/detect.php",
        "link":{
            "web_url":"http://localhost/detect.php"
        }
    })
}

response = requests.post(url, headers=headers, data=data)
response.status_code
if response.json().get('result_code') == 0:
	print('메시지를 성공적으로 보냈습니다.')
else:
	print('메시지를 성공적으로 보내지 못했습니다. 오류메시지 : ' + str(response.json()))