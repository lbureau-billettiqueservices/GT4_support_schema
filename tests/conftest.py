"""
Test configuration for pytest
"""

import os
import json

TEST_DIR = "data"
DUMP_DIR = "data/input"
SCHEMA_PATH = "../schema/ticketing_support_schema.json"


def get_schema(name):
    with open(SCHEMA_PATH) as schema_file:
        base = json.load(schema_file)
    if name in ("#", ""):
        return base
    return base["definitions"][name]


def get_dump(name):
    with open(f"{DUMP_DIR}/{name}") as dump:
        return json.load(dump)


def get_test_data(test_item):
    path = TEST_DIR + "/" + test_item
    with open(path) as test:
        return json.load(test)


def pytest_generate_tests(metafunc):
    """
    Function called by pytest to generate all its test_files.

    Generates a test case for each file in data
    """
    test_files = (x for x in os.listdir(TEST_DIR))
    test_files = filter(lambda x: os.path.isfile(os.path.join(TEST_DIR, x)), test_files)

    test_list = []
    test_ids = []

    schema_abs_path = os.path.abspath(SCHEMA_PATH)

    for item in test_files:
        test_data = get_test_data(item)
        dump = get_dump(test_data['input'])
        schema = get_schema(test_data["schema"])

        test_list.append(
            {"filename": item, "json_data": dump, "schema": schema, "expected": test_data["expected"]}
        )

        test_ids.append(item)

    if "test_context" in metafunc.fixturenames:
        metafunc.parametrize("test_context", test_list, ids=test_ids)
