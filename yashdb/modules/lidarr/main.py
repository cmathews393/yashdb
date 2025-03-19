import requests
import os


def get_lidarr_titles():
    api_url = os.getenv("LIDARR_API_URL")
    api_key = os.getenv("LIDARR_API_KEY")
    response = requests.get(f"{api_url}/api/v1/artist", headers={"X-Api-Key": api_key})
    response.raise_for_status()
    return len(response.json())


def get_lidarr_missing():
    api_url = os.getenv("LIDARR_API_URL")
    api_key = os.getenv("LIDARR_API_KEY")
    response = requests.get(
        f"{api_url}/api/v1/wanted/missing", headers={"X-Api-Key": api_key}
    )
    response.raise_for_status()
    return len(response.json())
