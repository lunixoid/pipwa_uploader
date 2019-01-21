import io
import aiofiles
from PIL import Image


class StorageInterface:
    async def save(self, data):
        raise NotImplementedError

    @staticmethod
    def verify(data):
        bytes_data = io.BytesIO(data)
        cache = Image.Image()
        cache.frombytes(data=bytes_data)
        if cache.verify():
            return True
        return False


class FileStorage(StorageInterface):
    def __init__(self, storage_path: str):
        super().__init__()
        self._storage_path = storage_path

    async def save(self, data):
        with aiofiles.open(self._storage_path, 'wb') as f:
            await f.write(data=data)
