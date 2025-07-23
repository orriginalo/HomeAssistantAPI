from httpx import AsyncClient

class SystemManager:
    def __init__(self, client: AsyncClient):
        self._client = client
    
    async def _check_connection_to(self, url: str):
        try:
            response = await self._client.get(url)
            return response.status_code == 200
        except Exception as e:
            print(e)
    
    
            
if __name__ == "__main__":
    manager = SystemManager()
    print(manager._check_connection_to("http://192.168.1.61"))