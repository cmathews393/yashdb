import requests
import os


def get_prowlarr_titles():
    api_url = os.getenv("PROWLARR_API_URL")
    api_key = os.getenv("PROWLARR_API_KEY")
    response = requests.get(f"{api_url}/api/v1/indexer", headers={"X-Api-Key": api_key})
    response.raise_for_status()
    return len(response.json())


def get_prowlarr_missing():
    # Prowlarr does not have a direct API for missing items, this function is a placeholder
    return 0
