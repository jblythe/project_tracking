import requests

from tracking.base.BaseIssues import BaseIssues


class Issues(BaseIssues):

    def set_url(self):
        self.url = f"{self.base_url}/api/issues"

    def get_issues(self, proj_name):
        params = {
            "query": proj_name,
            "fields": "id,description,summary,customFields(name,value(name))",
            "customFields": ["assignee"]
        }
        iss = requests.get(self.url, headers=self.header, params=params)

        return iss
