import docker
from rich import print
from docker.models.containers import Container

class DockerManager:
    _client: docker.DockerClient
    
    def __init__(self):
        self._client = docker.from_env()

    def get_container(self, name: str):
        containers: list[Container] = self.get_containers()
        container = next(filter(lambda c: c.name == name, containers), None)
        return self._client.containers.get(container.id)
        
        
    def get_containers(self):
        containers: list[Container] = self._client.containers.list()
        return containers
    
    def restart_container(self, *names):
        containers: list[Container] = self.get_containers()
        
        for name in names:
            container = next(filter(lambda c: c.name == name, containers), None)
            container = self._client.containers.get(container.id)
            container.stop()
            print(f"{container.name} stopped")
            
            container.start()
            print(f"{container.name} started")
            
if __name__ == "__main__":
    manager = DockerManager()
    manager.restart_container("timetablebot-db-1")
