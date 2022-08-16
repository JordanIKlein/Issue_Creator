import requests
import json
import os

SECRET_KEY = os.environ['PERSONAL_GITHUB_TOKEN']

class issue_comments_api():     
    def headers_():
        headers = {
                "Accept": "application/vnd.github+json",
                "Authorization": f"token {SECRET_KEY}"
            }
        return headers

    def status_codes_(status_code):
        print(status_code)
        match status_code:
            case 200:
                print("Listed Comments")
            case 201:
                print("Created Issue")
            case 301:	
                print("Moved permanently")
            case 403:
                print("Forbidden")
            case 404:
                print("Resource not found")
            case 410:
                print("Issues are disabled in the repo")
            case 422:
                print("Validation failed, token issues, could also be JSON issue")
            case 503:
                print("Service unavailable, GitHub Service issue")   
                # If an exact match is not confirmed, this last case will be used if provided
            case _:
                print("Something else is wrong, but I am unsure as to the specific issue")
    ### Post
    def create_issue_comment(comment_body,OWNER,REPO,ISSUE_NUMBER):
        try:
            headers = issue_comments_api.headers_()
            data = {"body": comment_body}
            json_data = json.dumps(data)
            response = requests.post(f'https://api.github.com/repos/{OWNER}/{REPO}/issues/{ISSUE_NUMBER}/comments', headers=headers, data= json_data)
            status_code = response.status_code
            issue_comments_api.status_codes_(status_code)
        except TimeoutError:
            print("Timeout")
    ### Get     
    def get_list_issue_comments(owner,repo,issue_number):
        try:
            headers = issue_comments_api.headers_()
            response = requests.get(f'https://api.github.com/repos/{owner}/{repo}/issues/{issue_number}/comments', headers=headers)
            json_response = response.json()
            status_code = response.status_code
            issue_comments_api.status_codes_(status_code)
            print(json_response)
        except TimeoutError:
            print("Timeout")
    def get_list_issue_comments_for_repo(owner,repo):
        try:
            headers = issue_comments_api.headers_()
            response = requests.get(f'https://api.github.com/repos/{owner}/{repo}/issues/comments', headers=headers)
            status_code = response.status_code
            issue_comments_api.status_codes_(status_code)
            json_data = response.json()
            print(json_data)
        except TimeoutError:
            print("Timeout")
    def get_an_issue_comment(owner,repo,comment_id):
        try:
            headers = issue_comments_api.headers_()
            response = requests.get(f'https://api.github.com/repos/{owner}/{repo}/issues/comments/{comment_id}', headers=headers)
            status_code = response.status_code
            issue_comments_api.status_codes_(status_code)
            json_data = response.json()
            print(json_data)
        except TimeoutError:
            print("Timeout")
    
    ### Delete
    def delete_issue_comment(owner,repo,comment_id):
        try:
            headers = issue_comments_api.headers_()
            response = requests.delete(f'https://api.github.com/repos/{owner}/{repo}/issues/comments/{comment_id}', headers=headers)
            status_code = response.status_code
            issue_comments_api.status_codes_(status_code)
            json_data = response.json()
            print(json_data)
        except TimeoutError:
            print("Timeout")
    ### Patch
    def update_issue_comment(owner,repo,comment_id,issue_body):
        try:
            headers = issue_comments_api.headers_()
            data = {
                "body": issue_body
                }
            json_data = json.dumps(data)    
            response = requests.patch(f'https://api.github.com/repos/{owner}/{repo}/issues/{comment_id}', data = json_data, headers = headers)
            status_code = response.status_code
            issue_comments_api.status_codes_(status_code)
        except TimeoutError:
            print("Timeout")
    