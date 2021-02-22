from locust import HttpUser, TaskSet, task
import json
from sendCode import sendCode
from locust import events


class WebsiteUser(HttpUser):
    host = "https://api.huxin315.com"

    @events.test_start.add_listener
    def on_test_start(environment, **kwargs):
        print("A new test is starting")
        #sendCode()

    @events.test_stop.add_listener
    def on_test_stop(environment, **kwargs):
        print("A new test is ending")

    def on_start(self):
        print("start")

    def read_item_txt(self):
        '''读取条目编码'''
        items = []
        with open('C:\\Users\\ZL-52S8FFG\\Desktop\\6位手机验证码.txt', encoding='utf-8') as f:
            for line in f.readlines():
                line = line.strip('\n')
                items.append(line)
        return items

    @task
    def login(self):
        url = "/passport-service/mobileLogin"
        authorization='eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJleHAiOjE2MTQ1NjMxNDYsInVzZXJJZCI6IlVJOXNuYkVQV0NVbUpzSXgyMmVud1hHeXRScVAwZ29jclZPems4S1FLU2RvRnJIdm5kTGwvdm5BOHk5dDdid0J5UDdYLzVITXpSZndva0tWb0ltN0lxNldOMXVIV3kyMThJRmNTM2I2UUl3NnR6YVNGNmYzRm9jeCtKYTZzZjY5cUNyYllyc2ExeEwxb09tSUIyVW1oV0syZGlSZUhpSW5HVTRLYzdIM3NvND0iLCJpYXQiOjE2MTM5NTgzNDZ9.LegO-Rvri_T4y7xT9_k2aNcNFDx6kw9FxDVuI2hohpHD2_neGpx2MK_NXw4OXEpUZDtZ4ncVpTbHArgF5cRB-I3KGwaQ3LTsEjuPcBnsdPewusJhOyh39bthnkwc99lTwFjV5lo66f3Aksy2QMgq8o1eNRjCO-GGUxxgLkQ0dFzJbWQ1E7iAJlQsy2b-45HTfCsWGv_XV3u2W-xRUTIW4Z5k-KLSvrbsbgWTyPQvd-s5mtNVQgJo6VwB0skCwOT53-duoL-W69YgrhvS1Y0XoOXo_oyVc_QnyK7VnzAT9eEWEipFlPWf0YwbMJGyOU1SsDz4U7sy-Fu0ei3qCC_UwA'
        headers = {  # 设置http头部信息
            'content-Type': 'application/x-www-form-urlencoded',
            'authorization':authorization
        }
        items = self.read_item_txt()
        with open('C:\\Users\\ZL-52S8FFG\\Desktop\\结果.txt', 'a+', encoding='utf8') as f:
            for item in items:
                params = {
                    'data0': '13372102635',
                    'data1': item
                }
                # json格式

                result=self.client.post(url,params, headers=headers).text
                #print(result)
                f.write(item+"    "+result+ "\n")
                result_dic = json.loads(result)
                msg = result_dic['msg']
                if msg=='success':
                    with open('C:\\Users\\ZL-52S8FFG\\Desktop\\6位手机验证码.txt', 'a+', encoding='utf8') as f:
                        f.write(item)
                    exit(0)

