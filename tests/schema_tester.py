"""
Schema tester file
"""
import pytest
from jsonschema import validate, Draft7Validator
from jsonschema.exceptions import ValidationError


def test_file(test_context):
    """Main test function. Just uses the data that comes from json in to_test"""
    json_data = test_context["json_data"]
    expected = test_context["expected"]
    schema = test_context["schema"]

    Draft7Validator.check_schema(schema)
    validator = Draft7Validator(schema)

    if expected["result"] == "ok":
        validate(json_data, schema)
    else:
        with pytest.raises(ValidationError) as excinfo:
            validate(json_data, schema)
        assert expected["error_message"] in str(excinfo.value)
