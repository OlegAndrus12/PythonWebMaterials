import json

import requests


class UsersListView:
    def __init__(self, users, path):
        self.users = users
        self.path = path

    def export(self):
        formatted_results = []
        for user in self.users:
            formatted_results.append(
                self.format_user(user)
            )

        with open(self.path) as f:
            try:
                json.dump(formatted_results, f)
            except json.JSONDecodeError as e:
                print(e)
    
    def format_user(self, user):
        return {
                "name": user["first_name"] + user["last_name"],
                "experience": user["years_of_experience"],
                "salary": user["annual_salary"],
        }


class UsersListViewAPI(UsersListView):
    # only export name, and shirt_size
    def format_user(self, user):
        return {
            "name": user["first_name"] + user["last_name"],
            "shirt_size": user["shirt_size"],
        }
