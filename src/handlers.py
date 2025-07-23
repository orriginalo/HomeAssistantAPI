import json
from fastapi import APIRouter, Request, WebSocket, WebSocketDisconnect

from src.schemas import Container, Media
from src.globals import connection_manager, tmdb, matcher, ai, docker_manager

router = APIRouter()

@router.get("/docker/containers/list", tags=["docker"])
async def list_containers(request: Request):
    containers = docker_manager.get_containers()
    resp_containers = []
    for container in containers:
        container = docker_manager.get_container(container.name)
        resp_containers.append(Container(
            name=container.name,
            state=container.status
        ))
    return resp_containers


@router.get("/docker/containers/restart", tags=["docker"])




@router.post("/media/add", tags=["media"])
async def add_movie(media: Media, request: Request):
    media_name = ai.get_kino_name(media.type, media.text)
    match media.type:
        case "movie":
            movies = tmdb.search_movies(media_name)
        case "show":
            movies = tmdb.search_show(media_name)
        case "collection":
            movies = tmdb.search_collection(media_name)
    return movies

@router.get('/process-command')
async def process_command(text: str, request: Request):
    command = matcher.match(text)
    await connection_manager.send_to_user("bob606", json.dumps({'command': command.command}))
    return {'command': command}

@router.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await connection_manager.connect("bob606", websocket)
    try:
        while True:
            data = await websocket.receive_text()
            # ...
    except WebSocketDisconnect:
        connection_manager.disconnect("bob606")