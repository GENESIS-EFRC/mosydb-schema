from jsonschema import validate, Draft7Validator
import json
from pathlib import Path


def main():
    base = Path(".")
    schema_dir = base / "schema"
    data_dir = base / "data"
    schemas = schema_dir.glob("*.json")
    data_files = data_dir.glob("*.json")

    for data_file in data_files:
        for schema_file in schemas:
            if schema_file == data_file:
                with open(schema_file) as f:
                    schema_contents = f.read()
                with open(data_file) as f:
                    data_contents = f.read()

                schema = json.loads(schema_contents)
                data = json.loads(data_contents)
                Draft7Validator.check_schema(schema)
                validate(data, schema)

if __name__ == "__main__":
    main()