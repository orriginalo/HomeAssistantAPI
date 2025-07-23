from httpx import AsyncClient
from config import QBITTORRENT_PASSWORD, QBITTORRENT_USERNAME, SERVER_IP

class TorrentManager:
    _client: AsyncClient
    
    def __init__(self, client: AsyncClient):
        self._client = client
  
    async def authorize(self):
        await self._client.post(f"{SERVER_IP}:8080/api/v2/auth/login", data={"username": QBITTORRENT_USERNAME, "password": QBITTORRENT_PASSWORD})
    
    async def _get_torrents(self):
        torrents = await self._client.get(f"{SERVER_IP}:8080/api/v2/torrents/info", params={"filter": "paused"}).json()
        return torrents
    
    async def _get_paused_torrents(self):
        torrents = await self._get_torrents()
        torrents = list(filter(lambda t: t["state"] == "stoppedDL", torrents))
        return torrents
    
    async def start_all_torrents(self):
        torrents = await self._get_paused_torrents()
        hashes = "|".join([torrent["hash"] for torrent in torrents])
        print(hashes)
        self._client.post(f"{SERVER_IP}:8080/api/v2/torrents/start", data={"hashes": hashes})
        
    async def stop_all_torrents(self):
        torrents = await self._get_torrents()
        hashes = "|".join([torrent["hash"] for torrent in torrents])
        self._client.post(f"{SERVER_IP}:8080/api/v2/torrents/stop", data={"hashes": hashes})