import time
from locust import HttpUser, task

class QuickstartUser(HttpUser):
    @task
    def simple_call(self):
        res = self.client.get("?card_code=rush_test_101&status=&metadata=&button_log=", headers={'referer': 'rush_test_referer'})
        time.sleep(1)

    # def on_start(self):
    #     self.client.post("/login", json={"username":"foo", "password":"bar"})
