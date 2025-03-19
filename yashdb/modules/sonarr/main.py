import requests
import os

def get_sonarr_titles():
    api_url = os.getenv("SONARR_API_URL")
    api_key = os.getenv("SONARR_API_KEY")
    response = requests.get(f"{api_url}/api/v3/series", headers={"X-Api-Key": api_key})
    response.raise_for_status()
    return len(response.json())

def get_sonarr_missing():
    api_url = os.getenv("SONARR_API_URL")
    api_key = os.getenv("SONARR_API_KEY")
    response = requests.get(f"{api_url}/api/v3/wanted/missing", headers={"X-Api-Key": api_key})
    response.raise_for_status()
    return len(response.json())
```
# Define your functions and classes for Sonarr here
