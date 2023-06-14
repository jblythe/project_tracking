
import os

token = os.getenv("PROJ_TRACK_TOKEN")


def get_header():
    header = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/json",
        "Cache-Control": "no-cache",
        "Content-Type": "application/json"
    }

    return header
