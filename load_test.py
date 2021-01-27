from locust import HttpUser,TaskSet,task

#定义用户行为
#class UserBehavior(TaskSet):



class WebsiteUser(HttpUser):
    @task
    def baidu_index(self):
        self.client.get('/')
    #task_set=UserBehavior

    min_wait = 3000
    max_wait = 6000