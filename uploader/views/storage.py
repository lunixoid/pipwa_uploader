import logging
from aiohttp import web
from os import path

from uploader.core.storage import FileStorage
from uploader.settings import (
    STORAGE_PATH
)


logger = logging.getLogger('pipwa_uploader.view')


async def upload_view(request):
    logger.info('Uploading request')
    try:
        reader = await request.multipart()

        next_file = await reader.next()
        if not next_file:
            return web.HTTPBadRequest()

        filename = next_file.filename
        if not filename:
            return web.HTTPBadRequest()

        request_data = await next_file.read()
        if not request_data:
            return web.HTTPBadRequest()

        # Store new file in
        storage = FileStorage(storage_path=path.join(STORAGE_PATH, filename))
        logger.info(f'Storing {path.join(STORAGE_PATH, filename)} {len(request_data)}b')
        if storage.verify(request_data):
            await storage.save(data=request_data)
        else:
            return web.HTTPBadRequest()
    except Exception as e:
        logger.error(f'Uploading was failed with error: {e}')
        return web.HTTPServerError()
    return web.Response()
