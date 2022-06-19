import logging

from aiohttp import web
import aiohttp_jinja2
import jinja2
import nest_asyncio

from app.pictures.routes import setup_routes

app = web.Application()
aiohttp_jinja2.setup(app, loader=jinja2.FileSystemLoader('templates'))

if __name__ == '__main__':
    nest_asyncio.apply()
    logging.basicConfig(level=logging.DEBUG)
    setup_routes(app)
    web.run_app(app)

