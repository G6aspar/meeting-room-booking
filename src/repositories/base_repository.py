class BaseRepository:
    def __init__(self):
        self._data = {}
        self._counter = 1

    def add(self, item):
        item_id = self._counter
        self._data[item_id] = item
        self._counter += 1
        return item_id

    def get(self, item_id):
        return self._data.get(item_id)

    def get_all(self):
        return list(self._data.values())

    def update(self, item_id, item):
        self._data[item_id] = item

    def delete(self, item_id):
        if item_id in self._data:
            del self._data[item_id]
