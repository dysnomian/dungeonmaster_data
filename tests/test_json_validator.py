import unittest
from dungeonmaster_data.json_validator import JsonValidator
import json
from jsonschema.exceptions import ValidationError

class TestJsonValidator(unittest.TestCase):
    validator = JsonValidator('./tests/fixtures/test_character_sheet_schema.json')

    def load_json(self, json_file_path):
        with open(json_file_path, 'r') as file:
            return json.load(file)

    def test_validate_character_sheet(self):
        valid_json = self.load_json('./tests/fixtures/simplest_character_sheet.json')
        errors = self.validator.validate(valid_json)
        self.assertEqual(errors, "0 validation error(s) found.")

    def test_validate_character_sheet_with_errors(self):
        invalid_json = self.load_json('./tests/fixtures/invalid_character_sheet.json')
        with self.assertRaises(ValidationError):
            self.validator.validate(invalid_json, formatter="none")

    def test_invalid_character_sheet(self):
        invalid_json = self.load_json('./tests/fixtures/invalid_character_sheet.json')
        expected_error_message = "2 validation error(s) found.\n\nErrors:\n=======\nError at document root: 'name' is a required property\nError at hit_points: 'maximum' is a required property\n"
        self.assertEqual(self.validator.validate(invalid_json), expected_error_message)

    def test_malformed_schema(self):
        with self.assertRaises(ValueError):
            JsonValidator('./tests/fixtures/malformed_schema.json')

    def test_missing_schema(self):
        with self.assertRaises(FileNotFoundError):
            JsonValidator('nonexistent_schema.json')
    
if __name__ == '__main__':
    unittest.main()