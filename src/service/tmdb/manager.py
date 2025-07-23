from httpx import Client
from src.service.tmdb.schemas import TMDBCollection, TMDBMovie, TMDBShow, Season

class TMDBManager:
    _api_key: str
    _client: Client
    
    def __init__(self, api_key: str):
        self._api_key = api_key
        self._client = Client(headers={"Authorization": f"Bearer {self._api_key}"})
        
    def _request(self, url: str, params: dict = None):
        params = params.copy() if params else {}
        params["language"] = "ru-RU"
        response = self._client.get(url, params=params)
        return response
    
    def search_movies(self, query: str):
        response = self._request("https://api.themoviedb.org/3/search/movie", params={"query": query})
        results = response.json()["results"]
        return [
            TMDBMovie(
                id=movie["id"], 
                name=movie["title"], 
                overview=movie["overview"], 
                poster_url=movie["poster_path"]
                ) for movie in results
            ]
    
    def get_movie_by_id(self, id: int):
        response = self._request(f"https://api.themoviedb.org/3/movie/{id}")
        data = response.json()
        return TMDBMovie(
            id=id,
            name=data["title"],
            overview=data["overview"],
            poster_url=data["poster_path"],
        )
    
    def search_collection(self, query: str):
        response = self._request("https://api.themoviedb.org/3/search/collection", params={"query": query})
        results = response.json()["results"]
        return [
            TMDBCollection(
                id=collection["id"], 
                name=collection["name"], 
                overview=collection["overview"], 
                poster_url=collection["poster_path"]
                ) for collection in results
            ]
        
    def get_collection_by_id(self, id: int):
        response = self._request(f"https://api.themoviedb.org/3/collection/{id}")
        data = response.json()
        return TMDBCollection(
            id=id,
            name=data["name"],
            overview=data["overview"],
            poster_url=data["poster_path"],
            parts=[
                TMDBMovie(
                    id=movie["id"], 
                    name=movie["title"], 
                    overview=movie["overview"], 
                    poster_url=movie["poster_path"]
                    ) for movie in data["parts"]
            ]
        )
        
    def search_show(self, query: str):
        response = self._request("https://api.themoviedb.org/3/search/tv", params={"query": query})
        results = response.json()["results"]
        return [
            TMDBShow(
                id=show["id"], 
                name=show["name"], 
                overview=show["overview"], 
                poster_url=show["poster_path"]
                ) for show in results
            ]
        
    def get_show_by_id(self, id: int):
        response = self._request(f"https://api.themoviedb.org/3/tv/{id}")
        data = response.json()
        return TMDBShow(
            id=id,
            name=data["name"],
            overview=data["overview"],
            poster_url=data["poster_path"],
            seasons=[
                Season(
                    id=season["id"], 
                    number=season["season_number"], 
                    episode_count=season["episode_count"], 
                    poster_url=season["poster_path"]
                    ) for season in data["seasons"]
            ]
        )
        
    def search_multi(self, query: str):
        response = self._request("https://api.themoviedb.org/3/search/multi", params={"query": query})
        data = response.json()["results"]
        results = []
        for media in data:
            if media["media_type"] == "movie":
                results.append(
                    TMDBMovie(
                        id=media["id"], 
                        name=media["title"], 
                        overview=media["overview"], 
                        poster_url=media["poster_path"]
                    )
                )
            elif media["media_type"] == "tv":
                results.append(
                    TMDBShow(
                        id=media["id"], 
                        name=media["name"], 
                        overview=media["overview"], 
                        poster_url=media["poster_path"]
                    )
                )
            else:
                return None
    
        return results