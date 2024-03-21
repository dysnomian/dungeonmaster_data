import json
from json.decoder import JSONDecodeError
import jsonschema
from typing_extensions import Annotated

class JsonValidator:
    """
    A class to validate character sheet JSON data against the JSON schema.
    """

    def __init__(self, schema_file_path):
        try:
            with open(schema_file_path) as schema_file:
                self.schema = json.load(schema_file)
                self.validator = jsonschema.Draft7Validator(self.schema)
        except FileNotFoundError:
            raise FileNotFoundError(f"The schema file '{schema_file_path}' was not found.")
        except JSONDecodeError as e:
            raise JSONDecodeError(f"The schema file '{schema_file_path}' is not valid JSON: {e.msg}", e.doc, e.pos)

    def validate(self, character_sheet_json, formatter="readable") -> Annotated[str, "Formatted error messages"]:
        """
        Validate the character sheet JSON data against the schema and return a list of errors.

        :param character_sheet_json: The character sheet JSON data to validate.
        """

        errors = sorted(self.validator.iter_errors(character_sheet_json), key=lambda e: e.path)
        
        if formatter == "readable":
            return self.readable_error_formatter(errors)
        elif formatter == "none":
            for error in errors:
                raise jsonschema.ValidationError(f"Error at {self.error_path(error)}: {error.message}")

    def readable_error_formatter(self, errors) -> Annotated[str, "Formatted error messages"]:
        """
        Format the validation errors into a human- and LLM-readable string.
        """
        error_messages = str(len(errors)) + " validation error(s) found."

        if errors:
            error_messages += "\n\nErrors:\n=======\n"

            for error in errors:
                error_messages += f"Error at {self.error_path(error)}: {error.message}\n"
        return error_messages

    def error_path(self, error):
        """
        Return the path of the error in the JSON data.
        """
        path = ""

        if error.path:
            path += '->'.join(map(str, error.path))
        else:
            path = "document root"

        return path