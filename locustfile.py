from locust import User,HttpLocust,TaskSet,task,between

class MyUser(User):
    wait_time = between(2,5) # for a random time between 2 seconds and 5 seconds
    weight = 3
    host = "https://passport.csdn.net"


class TestTask(TaskSet):
    """exec before start running"""
    def on_start(self):
        self.client.post('')



