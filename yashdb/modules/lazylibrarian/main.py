import requests
import os


def get_lazylibrarian_titles():
    api_url = os.getenv("LAZYLIBRARIAN_API_URL")
    api_key = os.getenv("LAZYLIBRARIAN_API_KEY")
    response = requests.get(f"{api_url}/api?cmd=getIndex&apikey={api_key}")
    response.raise_for_status()
    return len(response.json()["books"])


def get_lazylibrarian_missing():
    api_url = os.getenv("LAZYLIBRARIAN_API_URL")
    api_key = os.getenv("LAZYLIBRARIAN_API_KEY")
    response = requests.get(f"{api_url}/api?cmd=getWanted&apikey={api_key}")
    response.raise_for_status()
    return len(response.json()["books"])
