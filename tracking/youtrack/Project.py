import requests

from tracking.base.BaseProject import BaseProject


class Project(BaseProject):

    def set_url(self):
        self.url = f"{self.base_url}/api/admin/projects"

    def get_projects(self):

        params = {
            "fields": "id,name,shortName"
        }
        proj = requests.get(self.url, headers=self.header, params=params)

        return proj

    def get_project_id(self, name):

        params = {
            "query": name
        }

        proj = requests.get(self.url, headers=self.header, params=params)

        return proj
