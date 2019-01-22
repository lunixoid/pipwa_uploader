import os
import glob
import aiofiles
import uuid


class StorageInterface:
    async def save(self, data):
        raise NotImplementedError

    async def load(self, image_name) -> bytes:
        raise NotImplementedError

    def get_latest(self) -> str:
        raise NotImplementedError


class FileStorage(StorageInterface):
    def __init__(self, storage_path: str):
        super().__init__()
        if not os.path.isdir(storage_path):
            os.mkdir(storage_path)
        self._storage_path = storage_path

    async def save(self, data):
        filename = os.path.join(self._storage_path, str(uuid.uuid1()))
        async with aiofiles.open(filename, 'wb') as f:
            await f.write(data)

    async def load(self, filename):
        async with aiofiles.open(filename, 'rb') as f:
            return await f.read()

    def get_latest(self) -> str:
        f_list = glob.glob(os.path.join(self._storage_path, '*'))
        return max(f_list, key=os.path.getctime)
