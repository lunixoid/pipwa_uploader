import logging
import aiohttp_cors

from uploader import views


logger = logging.getLogger('pipwa_uploader.router')


def setup_routes(app):
    """Setup routes and appropriate CORS headers."""
    resources = {
        '/uploader/store': {
            'POST': views.storage.upload_view
        },
    }
    logger.info('Routes registered:')

    cors = aiohttp_cors.setup(app, defaults={
        # allow to read all resources for all
        '*': aiohttp_cors.ResourceOptions(
            allow_credentials=True,
            expose_headers='*',
            allow_headers='*',
            allow_methods=['OPTIONS'],
            max_age=3600),
    })

    for path, methods in resources.items():
        res = cors.add(app.router.add_resource(path))
        for method, handler in methods.items():
            cors.add(res.add_route(method, handler))
            logger.info('CORS: [{}] handler <{}:{}> on path "{}" wrapped.'.format(
                method, handler.__module__, handler.__name__, path))
