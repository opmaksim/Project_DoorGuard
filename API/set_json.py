import requests

# Read the data from tmp_data.txt file
with open('API/code_data.txt', 'r') as f:
    authorize_code = f.read()

# Now tmp2 contains the data from tmp1 (i.e., 'abc')
print(authorize_code)  # This will print 'abc'

url = 'https://kauth.kakao.com/oauth/token'
rest_api_key = 'c91a351774d89d3a1d7ed1077eb6bef0'
redirect_uri = 'https://example.com/oauth'
#authorize_code = '4TSG8GMB2P5EZ0gjEmA1AWeiqDEl_nuHVTzG0QWULVWqXXA7ESWAkgAAAAQKPXMYAAABkbaI8KSSBpCp5rpDbg'

data = {
    'grant_type':'authorization_code',
    'client_id':rest_api_key,
    'redirect_uri':redirect_uri,
    'code': authorize_code,
    }

response = requests.post(url, data=data)
tokens = response.json()
#print(tokens)

# json 저장
import json
#1.
with open(r"D:\Study\Academy\Project_DoorGuard\API\kakao_code.json","w") as fp:
#with open(r"D:/intel_5_jh/6.projects/vision/Kakao_api.json","w") as fp:
    json.dump(tokens, fp)
