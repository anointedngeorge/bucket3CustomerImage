from datetime import date
from ninja import Schema



class GalleryIn(Schema):
    name: str


class GalleryOut(Schema):
    id:int
    name:str
    size:int
    filename:str
    url:str
    code:str