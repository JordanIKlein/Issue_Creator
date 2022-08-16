import requests
import os

SECRET_KEY = os.environ['PERSONAL_GITHUB_TOKEN']

class issue_milestones_api():     
    def headers_():
        headers = {
                "Accept": "application/vnd.github+json",
                "Authorization": f"token {SECRET_KEY}"
            }
        return headers
    def status_codes_(status_code):
        match status_code:
            case 200:
                print("OK")
            case 204:
                print("No content")
            case 404:
                print("Resource not found")
            case 422:
                print("Validation failed")
            case 503:
                print("Service unavailable, GitHub Service issue")   
                # If an exact match is not confirmed, this last case will be used if provided
            case _:
                print("Something else is wrong.")
        print(status_code)
    ### Get
    def list_milestones(owner,repo):
        try:
            headers = issue_milestones_api.headers_()
            response = requests.get(f'https://api.github.com/repos/{owner}/{repo}/milestones', headers=headers)
            status_code = response.status_code
            issue_milestones_api.status_codes_(status_code)
            json_response = response.json()
            print(json_response)
        except TimeoutError:
            print("Timeout")
    def get_a_milestones(owner,repo,milestone_number):
        try:
            headers = issue_milestones_api.headers_()
            response = requests.get(f'https://api.github.com/repos/{owner}/{repo}/milestones/{milestone_number}', headers=headers)
            status_code = response.status_code
            issue_milestones_api.status_codes_(status_code)
            json_response = response.json()
            print(json_response)
        except TimeoutError:
            print("Timeout")
    ### Post
    def create_a_milestone(owner,repo):
        try:
            data = {
            "title":"v1.0",
            "state":"open",
            "description":"Tracking milestone for version 1.0",
            "due_on":"2012-10-09T23:39:01Z"
            }
            headers = issue_milestones_api.headers_()
            response = requests.post(f'https://api.github.com/repos/{owner}/{repo}/milestones', headers=headers, data = data)
            status_code = response.status_code
            issue_milestones_api.status_codes_(status_code)
            json_response = response.json()
            print(json_response)
        except TimeoutError:
            print("Timeout")
    ### Update
    def update_a_milestone(owner,repo,milestone_number):
        try:
            data = {
            "title":"v1.0",
            "state":"open",
            "description":"Tracking milestone for version 1.0",
            "due_on":"2012-10-09T23:39:01Z"
            }
            headers = issue_milestones_api.headers_()
            response = requests.patch(f'https://api.github.com/repos/{owner}/{repo}/milestones', headers=headers, data = data)
            status_code = response.status_code
            issue_milestones_api.status_codes_(status_code)
            json_response = response.json()
            print(json_response)
        except TimeoutError:
            print("Timeout")
    ### Delete
    def delete_a_milestones(owner,repo,milestone_number):
        try:
            headers = issue_milestones_api.headers_()
            response = requests.delete(f'https://api.github.com/repos/{owner}/{repo}/milestones/{milestone_number}', headers=headers)
            status_code = response.status_code
            issue_milestones_api.status_codes_(status_code)
        except TimeoutError:
            print("Timeout")