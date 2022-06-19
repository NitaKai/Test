import os.path
from aiohttp import web
from .views import ShowHandler, UploadHandlerPost, UploadHandlerGet

path = os.path.dirname(__file__)
print(path)


def setup_routes(app):
    app.router.add_get('/show/{id}', ShowHandler)
    app.add_routes([web.static('/app/pictures/img', "app/pictures/img", show_index=True)])
    app.router.add_get('/upload', UploadHandlerGet)
    app.router.add_post('/upload', UploadHandlerPost)



