"""
Schema tester file
"""
import pytest
from jsonschema import validate, Draft7Validator, RefResolver
from jsonschema.exceptions import ValidationError
import json

SCHEMA_PATH = "../schema/ticketing_support_schema.json"


def get_root_schema():
    with open(SCHEMA_PATH) as schema_file:
        return json.load(schema_file)


def test_file(test_context):
    """Main test function. Just uses the data that comes from json in to_test"""
    json_data = test_context["json_data"]
    expected = test_context["expected"]
    schema = test_context["schema"]

    Draft7Validator.check_schema(schema)

    resolver = RefResolver.from_schema(get_root_schema())

    if expected["result"] == "ok":
        validate(json_data, schema, resolver=resolver)
    else:
        with pytest.raises(ValidationError) as excinfo:
            validate(json_data, schema)
        assert expected["error_message"] in str(excinfo.value)
