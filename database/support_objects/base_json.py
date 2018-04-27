import json


class BaseJson:

    def to_json(self) -> str:
        return json.dumps(self.__dict__)

    def from_json(self, data: str):
        self.__dict__ = json.loads(data)
        return self
