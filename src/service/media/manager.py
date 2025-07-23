from src.service.tmdb.manager import TMDBManager

class MediaManager:
    tmdb: TMDBManager
    
    def __init__(self, tmdb: TMDBManager):
        self.tmdb = tmdb
    
    def add_movie_to_radarr(self, query: str):
        return self.tmdb.search_movies(query)