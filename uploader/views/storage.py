import logging
from aiohttp import web


logger = logging.getLogger('pipwa_uploader.view')


async def upload_view(request):
    logger.info(f'Uploading request')
    return web.Response()
