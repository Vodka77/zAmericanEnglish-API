import requests,random,string

def register():
    RandomUser = ''.join(random.choice(string.ascii_letters) for i in range(6))
    data = {
        "fcmId": "",
        "email": f"Bot{RandomUser}@gmail.com",
        "deviceToken": "fCatwPKabTE:APA91bHZcota9QV9qqjd6xOl1j1QXPbYsascuM60Yz1IxSw3RT63e4cEtpUW0Z4iuU5Ya1cq34-TflHBRLjW_GFdOpaicCzsVXYINIniCqMSd1CScaaKS6nV0fvCvQ3CWrqcWNnoU7JW",
        "fullName": f"theBot_{RandomUser}",
        "password": "123ya123@!X"
    }
    r = requests.post('https://staging.zamericanenglish.com:8004/v2/users/signup', data=data).json()
    if r['message'] == 'User was successfully registered':
        return r['data']['sid']
    else:
        return 'error'

def getCategory(sid):
    data = {
        "levelId": "5af2970727f13a137cbd1a39"
    }
    headers = {
        'Sid': sid,
    }
    r = requests.post('https://staging.zamericanenglish.com:8004/v2/study/categories', data=data, headers=headers).json()
    return r

sid = register()
print(getCategory(sid))


