import os
import random

from locust import TaskSet, between, task, Locust
from locust.contrib.fasthttp import FastHttpLocust
from locust.contrib.fasthttp import FastHttpSession


URLS = {(f"http://localhost:800{i}/item", f"host {i:03}") for i in range(7)}


class Itemer(TaskSet):
    def __init__(self, *args, **kwargs):
        self.__url, self.__host = random.sample(URLS, 1)[0]
        super().__init__(*args, **kwargs)

    @task
    def get_item(self):
        for i in range(10):
            self.client.get(self.__url, name=self.__host)


class MultipleHostsLocust(FastHttpLocust):
    abstract = True

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.api_client = FastHttpSession(base_url=os.environ.get("API_HOST"))


class HostRunner(MultipleHostsLocust):
    task_set = Itemer
    wait_time = between(0, 0.1)
