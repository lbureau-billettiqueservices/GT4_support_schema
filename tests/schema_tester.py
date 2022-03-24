"""
Schema tester file
"""
import pytest
import jsonschema


def test_file(test_context):
    """Main test function. Just uses the data that comes from json in to_test"""
    json_data = test_context["json_data"]
    expected = test_context["expected"]
    schema = test_context["schema"]
    if expected["result"] == "ok":
        jsonschema.validate(json_data, schema)
    else:
        with pytest.raises(jsonschema.exceptions.ValidationError) as excinfo:
            jsonschema.validate(json_data, schema)
        assert expected["error_message"] in str(excinfo.value)
