import os
import datetime
import json


class UserData:
    def __init__(self):
        self.c_time = datetime.datetime.now()
        self.meta = os.uname()

    def data_record(self, **kwargs):
        json_obj = {
            "system": os.uname()[0],
            "creation ": str(datetime.datetime.today())
        }

        json_obj.update(kwargs)
        with open('local_copy.json', 'w') as f:
            json.dump(json_obj, f)

        return 'data saved!'
