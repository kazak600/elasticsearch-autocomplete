import logging
from aiohttp import web
from datetime import datetime

routes = web.RouteTableDef()


@routes.get('/')
async def index(request):
    return web.json_response({'status': 'OK'})


def main():
    app = web.Application()
    app.add_routes(routes)
    logging.basicConfig(level=logging.DEBUG)
    web.run_app(app)


if __name__ == '__main__':
    main()
