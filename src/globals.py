from arrapi import RadarrAPI, SonarrAPI
from httpx import AsyncClient
from config import TMDB_API_KEY
from src.service.actions.docker.manager import DockerManager
from src.service.actions.system.manager import SystemManager
from src.service.actions.torrent.manager import TorrentManager
from src.service.ai.manager import AI
from src.service.matcher.matcher import Matcher
from src.service.tmdb.manager import TMDBManager
from src.ws.manager import ConnectionManager

client = AsyncClient()

docker_manager = DockerManager()
system_manager = SystemManager(client)
torrent_manager = TorrentManager(client)
connection_manager = ConnectionManager()
ai = AI("http://127.0.0.1:1234/v1")
matcher = Matcher()
tmdb = TMDBManager(TMDB_API_KEY)

sonarr = SonarrAPI("http://192.168.1.61:9003", "ca8b1ac268884d96819c16b16baa0509")
radarr = RadarrAPI("http://192.168.1.61:9002", "ad9a6d195ad74dbc9ba777ffa7d1d26d")