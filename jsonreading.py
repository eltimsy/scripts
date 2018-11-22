import json
import os

path = os.path.dirname(__file__)
json_data = open(path + 'blog.json').read()

json.loads(json_data)