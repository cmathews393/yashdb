
import os
import httpx
from loguru import logger


class Radarr:
    """Radarr API Class"""
    def __init__(self: "Radarr", api_url: str, api_key: str) -> None:
        self.api_url = api_url
        self.api_key = api_key
        self.client = httpx.Client()
    
    def _make_request(self: "Radarr", endpoint: str) -> dict:

        url = f"{self.api_url}/{endpoint}"
        headers = {"X-Api-Key": self.api_key}
        try:
            response = httpx.get(url=url, headers=headers)
            response.raise_for_status()
            return response.json()
        except (httpx.HTTPStatusError, httpx.HTTPError):
            logger.exception('Request failed with error.')
            return None

    
    def get_radarr_titles(self: "Radarr"):
        return self._make_request("api/v3/movie")
    def get_radarr_titles_count(self: "Radarr"):
        return (len(self.get_radarr_titles()))

    def get_radarr_missing(self: "Radarr"):
        return self._make_request("/api/v3/wanted/missing")
                

    def get_radarr_missing_count(self: "Radarr"):
        return (len(self.get_radarr_missing()))