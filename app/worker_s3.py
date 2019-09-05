import os
import boto3
import uuid

s3_client = boto3.client('s3')
s3_resource = boto3.resource('s3')


def create_temp_file(size, file_name, file_content):
    random_file_name = ''.join([str(uuid.uuid4().hex[:6]), file_name])
    with open(random_file_name, 'w') as f:
        f.write(str(file_content) * size)
    return random_file_name


first_file_name = create_temp_file(300, 'firstfile.txt', 'f')

first_bucket = s3_resource.Bucket(name='tar')
first_object = s3_resource.Object(bucket_name='preacher-page', key=first_file_name)

first_object.upload_file(first_file_name)
os.remove(first_file_name)


print('Done it', end='\n\n')
