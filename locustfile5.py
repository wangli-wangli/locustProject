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
    def openAnalysisComCode(self):
        '''生成组合码'''
        url = "/cloud-service/cross/openAnalysisComCode?cNo=1200-d24370ae0&ac=120000"
        headers = {  # 设置http头部信息
            'content-Type': 'application/json'
        }
            # json格式
        results = self.client.post(url, headers=headers).text
        #print(results)