from ninja import NinjaAPI
from image.apifolder.v1.media import router as router1

api = NinjaAPI()

api.add_router("/media/", router1)

