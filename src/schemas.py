from pydantic import BaseModel

class Media(BaseModel):
    type: str
    text: str
    
class Container(BaseModel):
    name: str
    state: str