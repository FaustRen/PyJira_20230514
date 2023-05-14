#%%
from jira import JIRA
import requests
from requests.auth import HTTPBasicAuth
import json
import pandas as pd
from IPython.display import display


class PyJira:
    
    #  def __init__(self, url, *args, **kwargs):
    def __init__(self, api_token, server_url, user_mail_address):
        self.api_token = api_token
        self.server_url = server_url
        self.user_mail_address = user_mail_address
        self.jira = self._connect()
        print("Jira connection is connected sucessfully.")
    
    def _connect(self):
        options = {"server": self.server_url} # 要建立 Issue 的 Project Key(default: "https://f109156120.atlassian.net")
        return JIRA(options, basic_auth=(self.user_mail_address, self.api_token))       # difault_address = "f109156120@nkust.edu.tw")
        
    def requestsJira(self,domain_name_input, issue_key_input):
        """ request Jira API, this func used to get Jira Issue Info """
        url = f"https://{domain_name_input}.atlassian.net/rest/api/3/issue/{issue_key_input}"   # Jira domain issue url
        auth = HTTPBasicAuth(self.user_mail_address, self.api_token)                    # request issue 權限
        headers = {"Accept": "application/json"}
        response = requests.request("GET", url=url, headers=headers,auth=auth)
        return response
    
    def getIssue(self, issue_key_input):
        """Get Jira Issue"""
        return self.jira.issue(issue_key_input)
    
    def updateIssue(self, issue_key_input, update_fields):
        """Update Jira Issue's information"""
        issue = self.getIssue(issue_key_input)
        issue.update(fields=update_fields)
        print(f"Issue({issue_key_input}) is updated successfully.")    
    
    def createIssue(self, issue_info):
        """create a new issue and add it to the Jira project
        Args:
            project_key_input (str): issue belongs to which project
            issue_info (dict):       Jira information
                - example:
                    issue_dict = { # 新 Issue 的相關資訊
                                    "project": {"key": project_key},
                                    "summary": "New issue summary",å
                                    "description": "This is a new issue",
                                    "issuetype": {"name": "Bug"}, }
        """
        issue_output = self.jira.create_issue(fields=issue_info)
        return issue_output
    


# parameters for Jira RESTful API
api_token = "API token for Jira"
server_url = "Jira server name"#https://your_server_name.atlassian.net
user_mail_address = "user_email_address"
# Connect your Jira server
jira = PyJira(api_token, server_url, user_mail_address)

#%% -- Method

## ------------------------------------------------
# Get Issue info
issue_key = "Input Issue key"
issue1 = jira.getIssue(issue_key)
print(issue1.fields.description)
print(issue1.fields.summary)
print(issue1.fields.issuetype)

# Update issue info
update_fields ={
                "summary": "hahahahaha",
                "description": "updated description: hahahaha"
                }
jira.updateIssue(issue_key, update_fields)

# After updating issue, show issue's info again
issue1_new = jira.getIssue(issue_key)
print(issue1_new.fields.description)
print(issue1_new.fields.summary)

## ------------------------------------------------
#%%




        
        
    



# %%


"""  ------------ jira.fields.method ------------
fields.issuetype：取得 issue 的類型。
fields.priority：取得 issue 的優先順序。
fields.assignee：取得 issue 的負責人。
fields.reporter：取得 issue 的報告人。
fields.created：取得 issue 的建立日期和時間。
fields.updated：取得 issue 的最近更新日期和時間。
fields.status：取得 issue 的狀態。
fields.resolution：取得 issue 的解決結果。
fields.comments：取得 issue 的評論列表。
fields.labels：取得 issue 的標籤列表。
fields.components：取得 issue 的組件列表。
fields.fixVersions：取得 issue 的修復版本列表。
fields.affectedVersions：取得 issue 的受影響版本列表。
fields.duedate：取得 issue 的截止日期。
"""