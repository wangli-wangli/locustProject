from locust import HttpUser, TaskSet, task
import csv

class WebsiteUser(HttpUser):
    host = "https://api.jyfwyun.com"


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

    @task
    def search(self):
        '''关键词搜索'''
        url = "/cloud-service/cross/search"
        headers = {  # 设置http头部信息
            'content-Type': 'application/json'
        }
        keywords=self.read_keyword_CSV()
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