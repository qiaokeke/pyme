
def getAccessToken(url='https://api.weixin.qq.com/cgi-bin/token',grant_type='client_credential',
                   appid='wx3a85c1e2dde93fa1',secret='48e05b2d7191fef778d6d5af3a885982'
                   ):
    import requests
    params = {
        'grant_type':grant_type,
        'appid':appid,
        'secret':secret
        }

    r = requests.get(url=url,params=params)
    return r.text

r = getAccessToken()
print(r)