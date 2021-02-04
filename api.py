import requests

def buildComposeCode():
    '''生成组合码'''
    url = "https://api.jyfwyun.com/cloud-service/cross/buildComposeCode"
    headers = {  # 设置http头部信息
        'content-Type': 'application/json'
    }

    params = {
        "itemList": [
            "0058f18a2e734541915677f1c7f30907",
            "005e3db78d8841d8a6d7f36977fdb8ae"

        ],
        "first": "per",
        "jyfwStr": "一般项目：家用视听设备销售。（除依法须经批准的项目外，凭营业执照依法自主开展经营活动）",
        "branchList": [],
        "ac": "120000"
    }
    # json格式
    results = requests.post(url, headers=headers, json=params).text
    print(results)

if __name__ == '__main__':
    buildComposeCode()
