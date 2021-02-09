import json
from pathlib import Path

import jsonschema
import pkg_resources


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


def main(verbose: int = 0) -> None:
    """Validate the json in data folder against json in the schema folder."""
    printer = Printer(verbose=verbose)
    package = "mosydbschema"
    schema_dir = Path(pkg_resources.resource_filename(package, "schema"))
    data_dir = Path(pkg_resources.resource_filename(package, "data"))
    schemas = {}
    # map schema name to file schema
    for schema_file in schema_dir.rglob("*.json"):
        with schema_file.open("r") as f:
            schemas[schema_file.stem] = json.load(f)
    # check the schemas
    for name, schema in schemas.items():
        printer.print("Check schema {}".format(name))
        jsonschema.Draft7Validator.check_schema(schema)
    # map data file to schema and validate
    for data_file in data_dir.rglob("*.json"):
        schema = schemas.get(data_file.stem, None)
        if schema is None:
            raise MosySchemaError("No schema is matched with data file {}".format(data_file.name))
        printer.print("Validate data file {}".format(data_file.name))
        with data_file.open("r") as f:
            data = json.load(f)
        jsonschema.validate(data, schema)


if __name__ == "__main__":
    main()
