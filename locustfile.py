"""
Test script for load testing user exercises rest API service
"""
import random
from locust import HttpLocust, TaskSet, task


class UserBehavior(TaskSet):
    """
    UserBehavior class to hold user tasks
    """
    @task(2)
    def post_user(self):
        """ Posts/creates a new user """
        self.client.post("/api/users", data=None, json={"name": "8ct2zuh", "postcode": "dvwycos"})

    @task(1)
    def get_users(self):
        """ Gets all users """
        self.client.get("/api/users/")

    @task(1)
    def get_user(self):
        """ Gets all users then picks a random user to get """
        random_user = random.choice((self.client.get("/api/users").json()))
        self.client.get("/api/users/" + str(random_user["id"]))

    @task(2)
    def post_exercise(self):
        """ Posts a new exercise """
        self.client.post("/api/exercises", data=None, json={"description": "8ct2zuh"})

    @task(2)
    def get_exercise(self):
        """ Gets all exercises then picks a random exercise to get """
        random_exercise = random.choice((self.client.get("/api/exercises").json()))
        self.client.get("/api/exercises/" + str(random_exercise["id"]))

    @task(4)
    def post_exercise_log(self):
        """ Gets all exercises and users then picks random ones to post as a new exercise log """
        random_exercise = random.choice((self.client.get("/api/exercises").json()))
        random_user = random.choice((self.client.get("/api/users").json()))
        self.client.post(
            "/api/log/",
            data=None,
            json={"userId": str(random_user["id"]),
                  "exerciseId": random_exercise["id"],
                  "date": "2019-01-01"}
        )


class WebsiteUser(HttpLocust):
    """ Locust class to handle behaviour """
    task_set = UserBehavior
    min_wait = 500
    max_wait = 1000
