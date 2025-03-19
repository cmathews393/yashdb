import requests
import os


def get_plex_titles():
    api_url = os.getenv("PLEX_API_URL")
    token = os.getenv("PLEX_TOKEN")
    response = requests.get(
        f"{api_url}/library/sections", headers={"X-Plex-Token": token}
    )
    response.raise_for_status()
    sections = response.json()["MediaContainer"]["Directory"]
    total_titles = 0
    for section in sections:
        section_id = section["key"]
        section_response = requests.get(
            f"{api_url}/library/sections/{section_id}/all",
            headers={"X-Plex-Token": token},
        )
        section_response.raise_for_status()
        total_titles += len(section_response.json()["MediaContainer"]["Metadata"])
    return total_titles


def get_plex_missing():
    # Plex does not have a direct API for missing items, this function is a placeholder
    return 0
