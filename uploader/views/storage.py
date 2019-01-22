import logging
from aiohttp import web

from uploader.core.storage import FileStorage
from uploader.settings import (
    STORAGE_PATH
)


logger = logging.getLogger('uploader.view')


async def upload_view(request):
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
        storage = FileStorage(storage_path=STORAGE_PATH)
        await storage.save(data=request_data)
        logger.info(f'Storing {filename} {len(request_data)}b')
    except Exception as e:
        logger.error(f'Uploading was failed with error: {e}')
        return web.HTTPBadRequest()
    return web.Response()
