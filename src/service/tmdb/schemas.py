from pydantic import BaseModel, field_validator

class TMDBItem(BaseModel):
    id: int
    name: str
    overview: str
    poster_url: str | None = None
    
    @field_validator("poster_url")
    @classmethod
    def add_tmdb_prefix(cls, v: str) -> str:
        if v:
            return f"https://image.tmdb.org/t/p/original{v}"
        return v
    
class TMDBMovie(TMDBItem):
    pass

class Season(BaseModel):
    id: int
    number: int
    episode_count: int
    poster_url: str | None = None
    
    @field_validator("poster_url")
    @classmethod
    def add_tmdb_prefix(cls, v: str) -> str:
        if v:
            return f"https://image.tmdb.org/t/p/original{v}"
        return v
    

class TMDBShow(TMDBItem):
    seasons: list[Season] = None


class TMDBCollection(TMDBItem):
    parts: list[TMDBMovie] = None
    