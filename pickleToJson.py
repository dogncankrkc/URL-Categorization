import json
import os
import sys
import pickle

with open(sys.argv[1], 'rb') as infile:
    obj = pickle.load(infile)

json_obj = json.loads(json.dumps(obj, default=str))

with open(
        os.path.splitext(sys.argv[1])[0] + '.json',
        'w',
        encoding='utf-8'
    ) as outfile:
    json.dump(json_obj, outfile, ensure_ascii=False, indent=4)