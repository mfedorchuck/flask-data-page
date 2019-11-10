import os
import json
import boto3
from datetime import datetime

s3_client = boto3.client('s3')
s3_resource = boto3.resource('s3')


class DataFile:
    def __init__(self):
        time = str(datetime.now())
        time = time.split('.')[0]

        for p in [':', ' ']:
            time = time.replace(p, '-')
        self.time = time
        self.name = time.__add__('.json')

    def data_record(self, **kwargs):
        data = {
            "system": os.uname()[0],
            "time": self.time}
        data.update(kwargs)

        with open(self.time, 'w') as f:
            json.dump(data, f)

        # bucket = s3_resource.Bucket(name='tar')
        # data_object = s3_resource.Object(bucket_name='preacher-page', key=first_file_name)
        # data_object.upload_file(self.name)

        # os.remove(self.name)
        print('Done it', end='\n\n')
