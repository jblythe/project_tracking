from tracking.youtrack.auth import get_header


class BaseProject:

    def __init__(self, base_url, proj_id=""):
        self.proj_id = proj_id
        self.base_url = base_url
        self.header = get_header()
        self.url = ""
        self.set_url()

    def set_url(self):
        pass
