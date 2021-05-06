import time
from locust import HttpUser, task, between

class QuickstartUser(HttpUser):
    wait_time = between(1, 2.5)

    @task
    def home(self):
        self.client.get("/")
        self.client.get("/argerich.jpeg")
        self.client.get("/favicon.ico")
        # self.client.get("/hear-tech-wsg-bridge-for-dante.pdf")
        self.client.get("/api/counter/home-counter")

    @task
    def jobs(self):
        self.client.get("/jobs")
        self.client.get("/argerich.jpeg")
        self.client.get("/favicon.ico")
        # self.client.get("/hear-tech-wsg-bridge-for-dante.pdf")
        self.client.get("/api/counter/jobs-counter")

    @task
    def about(self):
        self.client.get("/about")
        self.client.get("/argerich.jpeg")
        self.client.get("/favicon.ico")
        # self.client.get("/hear-tech-wsg-bridge-for-dante.pdf")
        self.client.get("/api/counter/about-counter")

    @task
    def about_legals(self):
        self.client.get("/about/legals")
        self.client.get("/argerich.jpeg")
        self.client.get("/favicon.ico")
        # self.client.get("/hear-tech-wsg-bridge-for-dante.pdf")
        self.client.get("/api/counter/about-legals-counter")

