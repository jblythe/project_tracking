import os

import tracking.youtrack.auth
from tracking.youtrack.Issues import Issues
from tracking.youtrack.Project import Project
from tracking.base.BaseTracking import BaseTracking


class Youtrack(BaseTracking):

    def __init__(self, base_url, proj_id):
        self.project = Project(base_url, proj_id)
        self.issues = Issues(base_url, proj_id)


