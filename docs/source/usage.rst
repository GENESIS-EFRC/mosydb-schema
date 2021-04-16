=============================================
Using the Schema and Validating Your Database
=============================================

Once you have installed the package, to validate any document database you create against the schema, you need
to use the class ``MosyValidator``.

Assuming that you have load data in a dictionary, you would like to validate it against schemas called `test`.

.. code-block:: python

    data = {"name": "Eggs", "price": 34.99}
    schema = "test"
    validator = MosyValidator()
    validator(schema, data)

Here, "test" is a predefined data schema in the mosydbschema package. If it succeed, it won't show any error,
otherwise an error message will show up telling where the data does not obey the schema. If you enter a schema not
defined in mosydbschema, it will raise an ``MosySchemaError``.

To let the validator prints out more messages like what schemas are loaded, you can switch the verbose to 1.

.. code-block:: python

    validator = MosyValidator(verbose=1)
