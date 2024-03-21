import json
from json.decoder import JSONDecodeError
from dungeonmaster_data.json_validator import JsonValidator

class CharacterSheetJsonAdapter:
    def __init__(self, schema_path = "./schema/character_sheet_schema.json"):
        self.validator = json_validator.JsonValidator(schema_path)

    def validate(self, character_sheet_json):
        errors = self.validator.validate(character_sheet_json)
        if errors:
            raise ValueError(f"The character sheet is not valid: {errors}")

    def read(self, filename):
        try:
            with open(filename, 'r') as file:
                character_sheet_json = json.load(file)
                if self.validate(character_sheet_json) is None:
                    self.character_sheet = character_sheet_json
                return character_sheet
        except FileNotFoundError:
            raise FileNotFoundError(f"The character sheet file at '{filename}' was not found.")
        except JSONDecodeError as e:
            raise JSONDecodeError(f"The character sheet file '{filename}' is not valid JSON: {e.msg}", e.doc, e.pos)
    
    def write(self, filename, character_sheet):
        if self.validate(character_sheet) is None:
            try:
                with open(filename, 'w') as file:
                    json.dump(character_sheet, file, indent=4)
            except PermissionError as e:
                raise PermissionError(f"Permission denied to write to the character sheet file '{filename}': {e}")
            except Exception as e:
                raise Exception(f"An error occurred while writing to the character sheet file '{filename}': {e}")
