from locust import HttpUser, TaskSet, task
import csv

class WebsiteUser(HttpUser):
    host = "https://api.jyfwyun.com"


    def on_start(self):
        print("start")

    def read_item_CSV(self):
        '''读取条目编码'''
        items=[]
        with open(r'C:/Users/ZL-52S8FFG/Desktop/新建文件夹/压力测试所需数据(1)/条目数据2.csv',encoding='utf-8') as f:
            reader=csv.reader(f)
            for i in reader:
                items.append(i[0])
        return items

    @task
    def buildComposeCode(self):
        '''生成组合码'''
        url = "cloud-service/cross/buildComposeCode"
        headers = {  # 设置http头部信息
            'content-Type': 'application/json'
        }
        items = self.read_item_CSV()
        for item in items:
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
            results = self.client.post(url, headers=headers, json=params).text
            #print(results)