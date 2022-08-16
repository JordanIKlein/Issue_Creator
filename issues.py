import requests
import json
import os

SECRET_KEY = os.environ['PERSONAL_GITHUB_TOKEN']

class issue_creator():
    def headers_():
        headers = {
                "Accept": "application/vnd.github+json",
                "Authorization": f"token {SECRET_KEY}"
            }
        return headers
    def status_codes_(status_code):
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
        print(status_code)
    ### Post Functions
    def create_issue(owner,repo,title,issue_body,labels,assignees):
        try:
            headers = issue_creator.headers_()
            data = {
                "title": title,
                "body": issue_body,
                "labels": labels,
                "assignees": assignees
                }
            json_data = json.dumps(data)
            response = requests.post(f'https://api.github.com/repos/{owner}/{repo}/issues', headers=headers, data= json_data)
            status_code = response.status_code 
            issue_creator.status_codes_(status_code)
        except TimeoutError:
            print("Timeout")
    ### Get Functions
    def get_issues_for_authenticated_users():
        try:
            headers = issue_creator.headers_()
            response = requests.get(f'https://api.github.com/issues', headers=headers)
            status_code = response.status_code
            issue_creator.status_codes_(status_code)
            json_response = response.json()
            print(json_response)
        except TimeoutError:
            print("Timeout")
    def get_user_account_issues_for_authenticated_users(user):
        try:
            headers = issue_creator.headers_()
            response = requests.get(f'https://api.github.com/{user}/issues', headers=headers)
            status_code = response.status_code
            issue_creator.status_codes_(status_code)
            json_response = response.json()
            print(json_response)
        except TimeoutError:
            print("Timeout")
    def get_issues_for_authenticated_users_in_organization(org):
        try:
            headers = issue_creator.headers_()
            response = requests.get(f'https://api.github.com/{org}/issues', headers=headers)
            status_code = response.status_code
            issue_creator.status_codes_(status_code)
            json_response = response.json()
            print(json_response)
        except TimeoutError:
            print("Timeout")
    def list_of_issues_for_repo(owner,repo):
        try:
            headers = issue_creator.headers_()
            response = requests.get(f'https://api.github.com/repos/{owner}/{repo}/issues', headers=headers)
            status_code = response.status_code
            issue_creator.status_codes_(status_code)
            json_response = response.json()
            print(json_response)
        except TimeoutError:
            print("Timeout")
    def get_issue_info(owner,repo,issue_number):
        try:
            headers = issue_creator.headers_()
            response = requests.get(f'https://api.github.com/repos/{owner}/{repo}/issues/{issue_number}', headers=headers)
            status_code = response.status_code
            issue_creator.status_codes_(status_code)
            json_response = response.json()
            print(json_response)
        except TimeoutError:
            print("Timeout")
    ### Put
    def put_lock_issue(lock_reason,owner,repo,issue_number):
        data = {
                "lock_reason": {lock_reason},
                }
        try:
            headers = issue_creator.headers_()
            response = requests.get(f'https://api.github.com/repos/{owner}/{repo}/issues/{issue_number}/lock', headers=headers, data = data)
            status_code = response.status_code
            issue_creator.status_codes_(status_code)
            json_response = response.json()
            print(json_response)
        except TimeoutError:
            print("Timeout")
    ### Delete
    def delete_lock_issue(lock_reason,owner,repo,issue_number):
        try:
            headers = issue_creator.headers_()
            response = requests.delete(f'https://api.github.com/repos/{owner}/{repo}/issues/{issue_number}/lock', headers=headers)
            status_code = response.status_code
            issue_creator.status_codes_(status_code)
            json_response = response.json()
            print(json_response)
        except TimeoutError:
            print("Timeout")
    ### Patch
    def update_issue(owner,repo,issue_number,title,issue_body,assignees,labels):
        try:
            headers = issue_creator.headers_()
            data = {
                "title": title,
                "body": issue_body,
                "labels": labels,
                "assignees": assignees
                }
            json_data = json.dumps(data)    
            response = requests.patch(f'https://api.github.com/repos/{owner}/{repo}/issues/{issue_number}', data = json_data, headers = headers)
            status_code = response.status_code
            issue_creator.status_codes_(status_code)
        except TimeoutError:
            print("Timeout")
    
    

    def main():
        issue_creator.get_issues_for_authenticated_users()
        
if __name__ == "__main__":
    issue_creator.main()