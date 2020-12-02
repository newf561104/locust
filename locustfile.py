import time
from locust import HttpUser, task

class QuickstartUser(HttpUser):
    @task
    def simple_call(self):
        res = self.client.get("", headers={'referer': 'rush_test_referer'})
        time.sleep(1)
