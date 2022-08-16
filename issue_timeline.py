import requests
import os

SECRET_KEY = os.environ['PERSONAL_GITHUB_TOKEN']

class issue_timeline_api():     
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
    ### Get
    def list_labels_for_an_issue(owner,repo,issue_number):
        try:
            headers = issue_timeline_api.headers_()
            response = requests.get(f'https://api.github.com/repos/{owner}/{repo}/issues/{issue_number}/timeline', headers=headers)
            status_code = response.status_code
            issue_timeline_api.status_codes_(status_code)
            json_response = response.json()
            print(json_response)
        except TimeoutError:
            print("Timeout")