"""
Test configuration for pytest
"""

import os
import json

TEST_DIR = "data"
DUMP_DIR = "data/input"


def pytest_generate_tests(metafunc):
    """
    Function called by pytest to generate all its test_files.

    Generates a test case for each file in to_test
    """

    def get_schema(name):
        with open(f"../schema/{name}") as schema_file:
            return json.load(schema_file)

    def get_dump(name):
        with open(f"{DUMP_DIR}/{name}") as dump:
            return json.load(dump)

    test_files = (x for x in os.listdir(TEST_DIR))
    test_files = filter(lambda x: os.path.isfile(os.path.join(TEST_DIR, x)), test_files)

    test_list = []
    test_ids = []

    for item in test_files:
        path = TEST_DIR + "/" + item
        with open(path) as test:
            test_data = json.load(test)

            dump = get_dump(test_data['input'])

            schema = get_schema(test_data["schema"])

            test_list.append(
                {"filename": item, "json_data": dump, "schema": schema, "expected": test_data["expected"]}
            )
            test_ids.append(item)

    if "test_context" in metafunc.fixturenames:
        metafunc.parametrize("test_context", test_list, ids=test_ids)
