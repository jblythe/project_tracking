import os
from tracking.youtrack.Youtrack import Youtrack

track_type = os.getenv("TRACKING_TYPE")
base_url = os.getenv("BASE_URL")
proj_id = os.getenv("PROJ_ID")

if track_type == 'Youtrack':
    proj_track = Youtrack(base_url, proj_id)

else:
    raise f"tracking type: {track_type} is undefined"

#proj_track.project.get_projects()
iss = proj_track.issues.get_issues(proj_id)

print(iss.text)
