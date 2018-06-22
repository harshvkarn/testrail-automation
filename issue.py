import json
import requests
import os


USERNAME = ''
#PASSWORD = os.environ['PASSWORD'] # Passing password in Environment
PASSWORD = ''

# The repository to add this issue to
REPO_OWNER = 'harshvkarn'
REPO_NAME = 'e2e-automation'

def make_github_issue(title, body=None, labels=None):
    '''Create an issue on github.com using the given parameters.'''
    # Our url to create issues via POST
    url = 'https://api.github.com/repos/%s/%s/issues' % (REPO_OWNER, REPO_NAME)
    # Create an authenticated session to create the issue
    session = requests.Session()
    session.auth = (USERNAME, PASSWORD)
    # Create our issue
    issue = {'title': title,
             'body': body,
             'labels': labels}
    # Add the issue to our repository
    r = session.post(url, json.dumps(issue))
    if r.status_code == 201:
        print ('Successfully created Issue "%s"' % (title))
    else:
        print ('Could not create Issue "%s"' % (title))
        print ('Response:', r.content)

#make_github_issue('Issue Title', 'Body text', ['bug'])
