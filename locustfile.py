from locust import HttpUser, TaskSet, task



# 定义用户行为
class UserBehavior(TaskSet):
    def on_start(self):
        print("start")

    @task
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

        self.client.post(url, headers=headers, json=params)
    # print(results)


class WebsiteUser(HttpUser):
    host = "https://api.jyfwyun.com"
    task_set = UserBehavior
    min_wait = 1500
    max_wait = 5000
