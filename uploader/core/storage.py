import os
import aiofiles


class StorageInterface:
    async def save(self, data):
        raise NotImplementedError


class FileStorage(StorageInterface):
    def __init__(self, storage_path: str):
        super().__init__()
        self._storage_path = storage_path

    async def save(self, data):
        dir_name = os.path.dirname(self._storage_path)
        if not os.path.isdir(dir_name):
            os.mkdir(dir_name)
        async with aiofiles.open(self._storage_path, 'wb') as f:
            await f.write(data)
