"""
Get model zip files and metadata from ModelDB.

Robert A. McDougal 2020-05-11 - 2020-06-21

Note: while most models have associated zip files, probably a couple hundred do not.
Those are the "web link to models" (additional information for these models is stored
in the notes -- attribute 24.)

Note: This will only gather zip files on new models.
      To restart, you must delete the contents of zip_dir.
"""

import requests
import json
import base64
import os
import tqdm

# filenames
zip_dir = '/home/bitnami/modeldb-zips'

try:
    os.makedirs(zip_dir)
except FileExistsError:
    pass

prev_model_ids = [int(item.split('.') [0]) for item in os.listdir(zip_dir)]

model_ids = [
    item['id']
    for item in requests.get(
            'https://senselab.med.yale.edu/_site/webapi/object.json/?cl=19'
        ).json()['objects']
]

for model_id in tqdm.tqdm(model_ids):
    # don't reload anything that you already have
    if model_id in prev_model_ids:
        continue

    unprocessed_metadata = requests.get(
        f"https://senselab.med.yale.edu/_site/webapi/object.json/{model_id}"
    ).json()
    metadata = {
        'title': unprocessed_metadata['object_name'],
        'id': model_id
    }
    for item in unprocessed_metadata['object_attribute_values']:
        if item['attribute_id'] == 23:
            # the zip file
            with open(os.path.join(zip_dir, f'{model_id}.zip'), 'wb') as f:
                f.write(base64.standard_b64decode(
                    item['value']['file_content']))
