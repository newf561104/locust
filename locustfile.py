from locust import HttpUser, TaskSet, task, between, constant

class UserBehavior(TaskSet):
    @task(1)
    def get(self):
        self.client.get("", headers={'referer': 'rush_test_referer'})

class WebsiteUser(HttpUser):
    tasks = {UserBehavior:1}
    wait_time = constant(1)
