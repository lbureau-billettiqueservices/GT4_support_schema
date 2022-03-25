import argparse
import json
from jsonschema import validate

import os

schema_path = os.path.join(os.path.dirname(__file__), 'schema/ticketing_support_schema.json')

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='validate the file passed as parameter against the schema')
    parser.add_argument("file", help="json file to validate")
    args = parser.parse_args()

    with open(schema_path) as schema_file:
        schema = json.load(schema_file)

    with open(args.file) as f:
        data = json.load(f)

    validate(data, schema)

    print("OK!")
