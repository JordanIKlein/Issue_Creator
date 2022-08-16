import requests

import os

SECRET_KEY = os.environ['PERSONAL_GITHUB_TOKEN']

class issue_labels_api():     
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
            case 201:
                print("Created")
            case 204:
                print("No content")
            case 404:
                print("Resource not found")
            case 410:
                print("Gone")
            case 422:
                print("Validation failed, token issues, could also be JSON issue")
            case 503:
                print("Service unavailable, GitHub Service issue")   
                # If an exact match is not confirmed, this last case will be used if provided
            case _:
                print("Something else is wrong, but I am unsure as to the specific issue")
        print(status_code)
    ### Get
    def list_labels_for_an_issue(owner,repo,issue_number):
        try:
            headers = issue_labels_api.headers_()
            response = requests.get(f'https://api.github.com/repos/{owner}/{repo}/issues/{issue_number}/labels', headers=headers)
            status_code = response.status_code
            issue_labels_api.status_codes_(status_code)
            json_response = response.json()
            print(json_response)
        except TimeoutError:
            print("Timeout")
    def list_labels_for_a_repository(owner,repo):
        try:
            headers = issue_labels_api.headers_()
            response = requests.get(f'https://api.github.com/repos/{owner}/{repo}/labels', headers=headers)
            status_code = response.status_code
            issue_labels_api.status_codes_(status_code)
            json_response = response.json()
            print(json_response)
        except TimeoutError:
            print("Timeout")
    def get_a_label(owner,repo,label_name):
        try:
            headers = issue_labels_api.headers_()
            response = requests.get(f'https://api.github.com/repos/{owner}/{repo}/labels/{label_name}', headers=headers)
            status_code = response.status_code
            issue_labels_api.status_codes_(status_code)
            json_response = response.json()
            print(json_response)
        except TimeoutError:
            print("Timeout")
    def list_labels_for_issues_in_a_milestone(owner,repo,milestone_number):
        try:
            headers = issue_labels_api.headers_()
            response = requests.get(f'https://api.github.com/repos/{owner}/{repo}/milestones/{milestone_number}/labels', headers=headers)
            status_code = response.status_code
            issue_labels_api.status_codes_(status_code)
            json_response = response.json()
            print(json_response)
        except TimeoutError:
            print("Timeout")
    ### Post
    def add_labels_to_an_issue(owner,repo,issue_number,labels):
        try:
            headers = issue_labels_api.headers_()
            data = {
                "labels": [labels]
            }
            response = requests.post(f'https://api.github.com/repos/{owner}/{repo}/issues/{issue_number}/labels', headers=headers, data=data)
            status_code = response.status_code
            issue_labels_api.status_codes_(status_code)
            json_response = response.json()
            print(json_response)
        except TimeoutError:
            print("Timeout")
    def create_a_label(owner,repo,issue_number,labels):
        try:
            headers = issue_labels_api.headers_()
            data = {
                "labels": [labels]
            }
            response = requests.post(f'https://api.github.com/repos/{owner}/{repo}/issues/{issue_number}/labels', headers=headers, data=data)
            status_code = response.status_code
            issue_labels_api.status_codes_(status_code)
            json_response = response.json()
            print(json_response)
        except TimeoutError:
            print("Timeout")
    ### Put
    def set_labels_for_an_issue(owner,repo,label_name,label_description,label_color):
        try:
            headers = issue_labels_api.headers_()
            data = {
                "name": {label_name}, #only required field
                "description": {label_description},
                "color": {label_color}
                }
            response = requests.put(f'https://api.github.com/repos/{owner}/{repo}/labels', headers=headers, data=data)
            status_code = response.status_code
            issue_labels_api.status_codes_(status_code)
        except TimeoutError:
            print("Timeout")
    def update_a_label(label_name,label_description,label_color,owner,repo): #https://api.github.com/repos/OWNER/REPO/labels/NAME
        try:
            headers = issue_labels_api.headers_()
            data = {
                "new_name": {label_name}, #only required field
                "description": {label_description},
                "color": {label_color}
                }
            response = requests.patch(f'https://api.github.com/repos/{owner}/{repo}/labels', headers=headers, data=data)
            status_code = response.status_code
            issue_labels_api.status_codes_(status_code)
        except TimeoutError:
            print("Timeout")
    ### Delete
    def remove_all_labels_from_an_issue(owner,repo,issue_number):
        try:
            headers = issue_labels_api.headers_()
            response = requests.delete(f'https://api.github.com/repos/{owner}/{repo}/issues/{issue_number}/labels', headers=headers)
            status_code = response.status_code
            issue_labels_api.status_codes_(status_code)
        except TimeoutError:
            print("Timeout")
    def remove_a_label_from_an_issue(owner,repo,issue_number,label_name):
        try:
            headers = issue_labels_api.headers_()
            response = requests.delete(f'https://api.github.com/repos/{owner}/{repo}/issues/{issue_number}/labels/{label_name}', headers=headers)
            status_code = response.status_code
            issue_labels_api.status_codes_(status_code)
        except TimeoutError:
            print("Timeout")
    def delete_a_label(owner,repo,label_name):
        try:
            headers = issue_labels_api.headers_()
            response = requests.delete(f'https://api.github.com/repos/{owner}/{repo}/labels/{label_name}', headers=headers)
            status_code = response.status_code
            issue_labels_api.status_codes_(status_code)
        except TimeoutError:
            print("Timeout")
    
    
    

    