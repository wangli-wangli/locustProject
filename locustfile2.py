from locust import HttpUser, TaskSet, task
import requests

class WebsiteUser(HttpUser):
    host = "https://api.jyfwyun.com"
    #min_wait = 50#时间单位为秒
    #max_wait = 50
    wait_time=0
    web_host = "127.0.0.1"

    def on_start(self):
        print("start")

    @task(3)
    def search(self):
        url = "/cloud-service/cross/search"
        headers = {  # 设置http头部信息
            'content-Type': 'application/json'
        }
        params = {
            "searchType": "item",
            "pageNum": 1,
            "industryCodes": [],
            "busiCombosObj": {},
            "ac": "110000",
            "industryTypes": ["8190", "1431", "7725", "1340", "4021"],
            "pageSize": 5,
            "keyword": "基站天线",
            "authCode": "af1d02b9e1"
        }
        # json格式
        results = self.client.post(url, headers=headers, json=params).text
        print(results)

        @task(1)
        def buildComposeCode(self):
            url = "cloud-service/cross/buildComposeCode"
            headers = {  # 设置http头部信息
                'content-Type': 'application/json'
            }
            params = {
    "itemList": [
        "0136683055f24ad3a5b17fca1ca914a6",
        "016f1c436c58ce3bac2be7761b6d23ae"
    ],
    "first": "per",
    "jyfwStr": "一般项目：家用视听设备销售。（除依法须经批准的项目外，凭营业执照依法自主开展经营活动）",
    "branchList": [],
    "ac": "120000"
}
            # json格式
            results = self.client.post(url, headers=headers, json=params).text
            print(results)