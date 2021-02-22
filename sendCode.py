import requests
def sendCode():
    url = "https://api.huxin315.com/passport-service/getSmsVerCode"
    headers = {  # 设置http头部信息
        'Host': 'api.huxin315.com',
        'Authorization': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJleHAiOjE2MTQ1NjMxNDYsInVzZXJJZCI6IlVJOXNuYkVQV0NVbUpzSXgyMmVud1hHeXRScVAwZ29jclZPems4S1FLU2RvRnJIdm5kTGwvdm5BOHk5dDdid0J5UDdYLzVITXpSZndva0tWb0ltN0lxNldOMXVIV3kyMThJRmNTM2I2UUl3NnR6YVNGNmYzRm9jeCtKYTZzZjY5cUNyYllyc2ExeEwxb09tSUIyVW1oV0syZGlSZUhpSW5HVTRLYzdIM3NvND0iLCJpYXQiOjE2MTM5NTgzNDZ9.LegO-Rvri_T4y7xT9_k2aNcNFDx6kw9FxDVuI2hohpHD2_neGpx2MK_NXw4OXEpUZDtZ4ncVpTbHArgF5cRB-I3KGwaQ3LTsEjuPcBnsdPewusJhOyh39bthnkwc99lTwFjV5lo66f3Aksy2QMgq8o1eNRjCO-GGUxxgLkQ0dFzJbWQ1E7iAJlQsy2b-45HTfCsWGv_XV3u2W-xRUTIW4Z5k-KLSvrbsbgWTyPQvd-s5mtNVQgJo6VwB0skCwOT53-duoL-W69YgrhvS1Y0XoOXo_oyVc_QnyK7VnzAT9eEWEipFlPWf0YwbMJGyOU1SsDz4U7sy-Fu0ei3qCC_UwA',
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    params={
"mobile":"15176128570",
"state":"0"
}

    result=requests.post(url, params,headers=headers).text
    print(result)

if __name__ == '__main__':
    sendCode()