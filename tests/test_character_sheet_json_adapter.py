import unittest
from unittest.mock import patch
from dungeonmaster_data.character_sheet_json_adapter import CharacterSheetJsonAdapter

class TestCharacterSheetJsonAdapter(unittest.TestCase):
    def setUp(self):
        self.adapter = CharacterSheetJsonAdapter()
    
    def test_read(self):
        # Test case 1: Valid JSON file
        filename = "tests/fixtures/valid_character_sheet.json"
        character_sheet = self.adapter.read(filename)
        self.assertIsNotNone(character_sheet)
        # Add more assertions to validate the imported character sheet data
        
        # Test case 2: Non-existent file
        filename = "nonexistent_file.json"
        with self.assertRaises(FileNotFoundError):
            character_sheet = self.adapter.read(filename)
        # Add more assertions to validate the error message
        
        # Test case 3: Invalid JSON format
        filename = "tests/fixtures/invalid_character_sheet.json"
        with self.assertRaises(ValueError):
            character_sheet = self.adapter.read(filename)
        # Add more assertions to validate the error message