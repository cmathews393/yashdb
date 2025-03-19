import qbittorrentapi
import os


def get_qbittorrent_titles():
    client = qbittorrentapi.Client(
        host=os.getenv("QBITTORRENT_API_URL"),
        username=os.getenv("QBITTORRENT_USERNAME"),
        password=os.getenv("QBITTORRENT_PASSWORD"),
    )
    client.auth_log_in()
    torrents = client.torrents_info()
    return len(torrents)


def get_qbittorrent_missing():
    # Qbittorrent does not have a direct API for missing items, this function is a placeholder
    return 0
