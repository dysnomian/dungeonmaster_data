import unittest
from dungeonmaster_data.json_manager import JsonManager
from jsonschema.exceptions import ValidationError
import os

class TestJsonManager(unittest.TestCase):
    def setUp(self):
        self.manager = JsonManager({
            'character_sheet_schema': './tests/fixtures/simplified_character_sheet_schema.json',
            'character_sheet_file_path': './tests/fixtures/simplest_character_sheet.json'
            })
    
    def tearDown(self) -> None:
        file_path = './tests/temp/temp_character_sheet.json'
        if os.path.exists(file_path):
            os.remove(file_path)
        return super().tearDown()
    
    def test_load_valid_character_data(self):
        self.manager.load_character_data()
        self.assertIsNotNone(self.manager.character_data)
        self.assertIsNot(self.manager.character_data, {})
        self.assertEqual(self.manager.character_data['name'], 'Test Character')
    
    def test_load_invalid_character_data(self):
        self.manager.character_sheet_file_path = './tests/fixtures/invalid_character_sheet.json'
        with self.assertRaises(ValidationError):
            self.manager.load_character_data()
        self.assertEqual(self.manager.character_data, {})

    def test_load_nonexistent_character_data(self):
        self.manager.character_sheet_file_path = 'nonexistent_file.json'
        with self.assertRaises(FileNotFoundError):
            self.manager.load_character_data()
        self.assertEqual(self.manager.character_data, {})

    def test_set_name(self):
        self.manager.load_character_data()
        self.manager.character_data['name'] = 'New Name'
        self.assertEqual(self.manager.character_data['name'], 'New Name')

    def test_save_valid_character_data(self):
        self.manager.load_character_data()
        self.manager.character_sheet_file_path = './tests/temp/temp_character_sheet.json'
        self.manager.character_data['name'] = 'New Name'
        self.manager.save_character_data()
        self.manager.load_character_data()
        self.assertEqual(self.manager.character_data['name'], 'New Name')
    
    def test_save_invalid_character_data(self):
        self.manager.load_character_data()
        self.manager.character_sheet_file_path = './tests/temp/temp_character_sheet.json'
        del self.manager.character_data['name']
        with self.assertRaises(ValidationError):
            self.manager.save_character_data()
    
    def test_diff_character_data(self):
        original_data = self.manager.load_character_data()
        new_data = original_data
        new_data['name'] = 'New Name'
        diff = self.manager.diff_character_data(new_data, original_data)
        self.assertEqual(diff, {('name', 'New Name')})

    # def test_update_property(self):
    #     self.manager.load_character_data()
    #     self.manager.character_sheet_file_path = './tests/temp/temp_character_sheet.json'
    #     self.manager.update_property("name", 'New Name')
    #     self.assertEqual(self.manager.character_data['name'], 'New Name')
    #     self.manager.character_sheet_file_path = './tests/fixtures/simplest_character_sheet.json'
    #     self.manager.load_character_data()
    #     self.assertEqual(self.manager.character_data['name'], 'Test Character')