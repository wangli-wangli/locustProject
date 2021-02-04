from locust import HttpUser, TaskSet, task
import requests
import csv

class WebsiteUser(HttpUser):

    #min_wait = 50#时间单位为秒
    #max_wait = 50
    # wait_time=0
    # web_host = "127.0.0.1"

    def on_start(self):
        print("start")

    def read_keyword_CSV(self):
        '''读取关键词'''
        keywords=[]
        with open(r'C:\Users\ZL-52S8FFG\Desktop\新建文件夹\压力测试所需数据(1)\搜索数据.csv',encoding='utf-8') as f:
            reader=csv.reader(f)
            for i in reader:
                keywords.append(i[0])
        return keywords

    def read_item_CSV(self):
        '''读取条目编码'''
        items=[]
        with open(r'C:/Users/ZL-52S8FFG/Desktop/新建文件夹/压力测试所需数据(1)/条目数据2.csv',encoding='utf-8') as f:
            reader=csv.reader(f)
            for i in reader:
                items.append(i[0])
        return items

    @task(1)
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
        #print(results)

    @task(1)
    def buildComposeCode(self):
        url = "/cloud-service/cross/buildComposeCode"
        headers = {  # 设置http头部信息
            'content-Type': 'application/json'
        }
        items = self.read_item_CSV()
        for item in items:
            params = {
                "itemList": [
                    item,
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

    @task(1)
    def openAnalysisComCode(self):
        '''生成组合码'''
        url = "/cloud-service/cross/openAnalysisComCode?cNo=1200-d24370ae0&ac=120000"
        headers = {  # 设置http头部信息
            'content-Type': 'application/json'
        }
        # json格式
        results = self.client.post(url, headers=headers).text
        # print(results)
