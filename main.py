from src.service.matcher.matcher import Matcher
from src.handlers import router

from contextlib import asynccontextmanager
from fastapi import FastAPI
import uvicorn

@asynccontextmanager
async def lifespan(app: FastAPI):
    matcher = Matcher()
    
    app.state.matcher = matcher
    app.include_router(router)
    yield
    
app = FastAPI(lifespan=lifespan)
    
if __name__ == "__main__":
    uvicorn.run(app)