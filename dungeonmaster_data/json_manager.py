import json
from dungeonmaster_data.json_validator import JsonValidator
from jsonschema.exceptions import ValidationError

class JsonManager:
    def __init__(self, params = {}):
        self.character_sheet_schema = params.get('character_sheet_schema')
        self.character_sheet_file_path = params.get('character_sheet_file_path')
        self.validator = JsonValidator(self.character_sheet_schema)
        self.character_data = {}
    
    def load_character_data(self):
        with open(self.character_sheet_file_path, 'r') as file:
            character_data = json.load(file)
            self.validator.validate(character_data, "none")
            self.character_data = character_data
            return self.character_data
    
    def save_character_data(self):
        with open(self.character_sheet_file_path, 'w') as file:
            self.validator.validate(self.character_data, "none")
            json.dump(self.character_data, file, indent=4)
            return self.character_data
    
    def diff_character_data(self, new_data, saved_data):
        new_data = set(new_data.items())
        saved_data = set(saved_data.items())
        return new_data ^ saved_data

    def update_property(self, property, new_data):
        mutated_character_data = self.character_data
        mutated_character_data.update({property: new_data})
        self.validator.validate(mutated_character_data, "none")
        self.character_data = mutated_character_data
        return self.character_data