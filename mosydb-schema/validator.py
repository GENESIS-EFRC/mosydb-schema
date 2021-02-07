from jsonschema import validate, Draft7Validator
import json
from pathlib import Path




def main():
    base = Path(".")
    schema_dir = base / "schema"
    data_dir = base / "schema"
    schemas = schema_dir.glob("*.json")
    data_files = data_dir.glob("*.json")

    test_schema = schema_dir / "test.json"
    test_data = data_dir / "test.json"

    for data_file in data_files:
        if data_file in schemas:
            with open(test_schema) as f:
                schema_contents = f.read()

            with open(test_data) as f:
                data_contents = f.read()

            schema = json.loads(schema_contents)
            data = json.loads(data_contents)

            Draft7Validator.check_schema(schema)
            validate(data, schema)

if __name__ == "__main__":
    main()