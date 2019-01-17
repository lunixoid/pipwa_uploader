import argparse
import asyncio
import logging
from aiohttp import web

from uploader.router import setup_routes


logging.basicConfig(
    format='[%(asctime)s] [%(name)s] [%(levelname)s] %(message)s',
    level=logging.DEBUG
)
logger = logging.getLogger('pipwa_uploader.main')


def get_cmd_params():
    parser = argparse.ArgumentParser()
    parser.add_argument('-v', '--verbose', help='verbose output',
                        action='store_true', default=False)
    parser.add_argument('-H', '--host', help='hostname or IP',
                        default='127.0.0.1')
    parser.add_argument('-P', '--port', type=int, help='port',
                        default=7777)
    return parser.parse_args()


def get_app():
    try:
        loop = asyncio.get_event_loop()
    except RuntimeError:
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)

    application = web.Application(loop=loop)
    setup_routes(application)
    return application


app = get_app()
if __name__ == '__main__':
    params = get_cmd_params()
    if params.verbose:
        print('Server started on {}:{}'.format(params.host, params.port))
    web.run_app(app, host=params.host, port=params.port)
