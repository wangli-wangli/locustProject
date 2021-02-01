from locust import HttpUser, TaskSet, task
import csv

class WebsiteUser(HttpUser):
    host = "https://api.jyfwyun.com"
    wait_time=0

    def on_start(self):
        print("start")

    def readCSV(self):
        keywords=[]
        with open(r'C:\Users\ZL-52S8FFG\Desktop\新建文件夹\压力测试所需数据(1)\搜索数据.csv',encoding='utf-8') as f:
            reader=csv.reader(f)
            for i in reader:
                keywords.append(i[0])
        return keywords



    @task(3)
    def search(self):
        url = "/cloud-service/cross/search"
        headers = {  # 设置http头部信息
            'content-Type': 'application/json'
        }
        keywords=self.readCSV()
        for keyword in keywords:
            params = {
                "searchType": "item",
                "pageNum": 1,
                "industryCodes": [],
                "busiCombosObj": {},
                "ac": "110000",
                "pageSize": 5,
                "keyword": keyword,
                "authCode": "af1d02b9e1"
            }
            # json格式
            results = self.client.post(url, headers=headers, json=params).text
            print(params)
            #print(results)

        @task(0)
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
            #print(results)