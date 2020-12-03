from locust import HttpUser, TaskSet, task, between, constant
import json

class UserBehavior(TaskSet):
    @task(1)
    def get(self):
        with self.client.get("", headers={'referer': 'rush_test_referer'}, catch_response = True) as response:
            if response.status_code != 200:
                response.failure("Failed.")
            if json.loads(response.text)['result_code'] != '00101':
                response.failure("scenario does not load.")
class WebsiteUser(HttpUser):
    tasks = {UserBehavior:1}
    wait_time = constant(1)
