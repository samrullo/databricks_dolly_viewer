import sys
sys.path.append(r'C:\Users\amrul\programming\projects\nlp_related\databricks_dolly_viewer\backend')

import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

from django.conf import settings


import pathlib
import requests
import json
from databrick.models import DatabrickModel

data_file=pathlib.Path("../data/databricks-dolly-15k.json")
with open(data_file) as fh:
    all_records=json.load(fh)

objects=[DatabrickModel(**record) for record in all_records]
DatabrickModel.objects.bulk_create(objects)
