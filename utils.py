import json
from iota import Address, Hash

class IotaJSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Address):
            return str(obj)
        if isinstance(obj, Hash):
            return str(obj)
        return json.JSONEncoder.default(self, obj)
