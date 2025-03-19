import os
from dotenv import load_dotenv

load_dotenv()

active_services = os.getenv("ACTIVE_SERVICES", "").split(",")
radarr_api_url = os.getenv("RADARR_API_URL")
radarr_api_key = os.getenv("RADARR_API_KEY")

sonarr_api_url = os.getenv("SONARR_API_URL")
sonarr_api_key = os.getenv("SONARR_API_KEY")

plex_api_url = os.getenv("PLEX_API_URL")
plex_token = os.getenv("PLEX_TOKEN")

lidarr_api_url = os.getenv("LIDARR_API_URL")
lidarr_api_key = os.getenv("LIDARR_API_KEY")

lazylibrarian_api_url = os.getenv("LAZYLIBRARIAN_API_URL")
lazylibrarian_api_key = os.getenv("LAZYLIBRARIAN_API_KEY")

prowlarr_api_url = os.getenv("PROWLARR_API_URL")
prowlarr_api_key = os.getenv("PROWLARR_API_KEY")

qbittorrent_api_url = os.getenv("QBITTORRENT_API_URL")
qbittorrent_username = os.getenv("QBITTORRENT_USERNAME")
qbittorrent_password = os.getenv("QBITTORRENT_PASSWORD")
