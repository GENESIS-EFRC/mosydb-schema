import json
from pathlib import Path

import jsonschema
import pkg_resources

SCHEMA_DIR = Path(pkg_resources.resource_filename("mosydbschema", "schema"))


class MosySchemaError(Exception):
    """Error in Mosy Schema Package."""
    pass


class Printer:
    """A class to print something if verbose is not zero."""

    def __init__(self, verbose: int = 0):
        self.verbose = verbose

    def print(self, *args, **kwargs):
        if self.verbose > 0:
            print(*args, **kwargs)


class MosyValidator:
    """A validator for mosy db schema."""

    def __init__(self, verbose: int = 0):
        self._printer = Printer(verbose)
        self._schema = {}
        self._load_schemas(SCHEMA_DIR)
        self._check_schemas()

    def _load_schemas(self, schema_dir: Path) -> None:
        for schema_file in schema_dir.rglob("*.json"):
            name = schema_file.stem
            self._printer.print("Load schema {}".format(name))
            with schema_file.open("r") as f:
                self._schema[name] = json.load(f)

    def _check_schemas(self) -> None:
        for name, schema in self._schema.items():
            self._printer.print("Check schema {}".format(name))
            jsonschema.Draft7Validator(schema)

    def __call__(self, name: str, data: str):
        schema = self._schema.get(name, None)
        if schema is None:
            raise MosySchemaError("There is no schema {}".format(name))
        self._printer.print("Validate data against schema {}".format(name))
        jsonschema.validate(data, schema)


def main(verbose: int = 0) -> None:
    """Validate the json in data folder against json in the schema folder."""
    validator = MosyValidator(verbose=verbose)
    data_dir = Path(pkg_resources.resource_filename("mosydbschema", "data"))
    # map data file to schema and validate
    for data_file in data_dir.rglob("*.json"):
        with data_file.open("r") as f:
            data = json.load(f)
        validator(data_file.stem, data)


if __name__ == "__main__":
    main()
