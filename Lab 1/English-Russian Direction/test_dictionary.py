import unittest
import tempfile
import os
from dictionary import EnglishRussianDictionary


class TestEnglishRussianDictionary(unittest.TestCase):
    """Тесты для англо-русского словаря."""
    
    def setUp(self):
        """Подготовка тестовых данных."""
        self.initial_data = [("hello", "привет"), ("world", "мир"), ("apple", "яблоко")]
        self.dict = EnglishRussianDictionary(self.initial_data)
    
    def test_initialization(self):
        """Тест инициализации словаря."""
        self.assertEqual(len(self.dict), 3)
        self.assertEqual(self.dict["hello"], "привет")
        self.assertEqual(self.dict["world"], "мир")
    
    def test_add_new_word(self):
        """Тест добавления нового слова."""
        self.dict["python"] = "питон"
        self.assertEqual(self.dict["python"], "питон")
        self.assertEqual(len(self.dict), 4)
    
    def test_update_existing_word(self):
        """Тест обновления существующего слова."""
        self.dict["hello"] = "здравствуйте"
        self.assertEqual(self.dict["hello"], "здравствуйте")
        self.assertEqual(len(self.dict), 3)
    
    def test_get_nonexistent_word(self):
        """Тест получения несуществующего слова."""
        with self.assertRaises(KeyError):
            _ = self.dict["nonexistent"]
    
    def test_contains(self):
        """Тест оператора in."""
        self.assertTrue("hello" in self.dict)
        self.assertFalse("nonexistent" in self.dict)
    
    def test_delete_existing_word(self):
        """Тест удаления существующего слова."""
        del self.dict["hello"]
        self.assertEqual(len(self.dict), 2)
        self.assertFalse("hello" in self.dict)
    
    def test_delete_nonexistent_word(self):
        """Тест удаления несуществующего слова."""
        with self.assertRaises(KeyError):
            del self.dict["nonexistent"]
    
    def test_delete_root_node(self):
        """Тест удаления корневого узла."""
        dict_single = EnglishRussianDictionary([("root", "корень")])
        del dict_single["root"]
        self.assertEqual(len(dict_single), 0)
        self.assertFalse("root" in dict_single)
    
    def test_delete_node_with_two_children(self):
        """Тест удаления узла с двумя детьми."""
        test_dict = EnglishRussianDictionary([("b", "b"), ("a", "a"), ("c", "c")])
        
        del test_dict["b"]
        
        self.assertEqual(len(test_dict), 2)
        self.assertFalse("b" in test_dict)
        self.assertTrue("a" in test_dict)
        self.assertTrue("c" in test_dict)
    
    def test_iadd_operator(self):
        """Тест оператора +=."""
        self.dict += "sun:солнце"
        self.assertEqual(self.dict["sun"], "солнце")
        self.assertEqual(len(self.dict), 4)
    
    def test_iadd_invalid_format(self):
        """Тест оператора += с неверным форматом."""
        with self.assertRaises(ValueError):
            self.dict += "invalid_string"
    
    def test_iteration(self):
        """Тест итерации по словарю."""
        words = [word for word, _ in self.dict]
        self.assertEqual(sorted(words), ["apple", "hello", "world"])
    
    def test_inorder_traversal(self):
        """Тест обхода в порядке возрастания."""
        result = list(self.dict.inorder_traversal())
        expected = [("apple", "яблоко"), ("hello", "привет"), ("world", "мир")]
        self.assertEqual(result, expected)
    
    def test_search_prefix(self):
        """Тест поиска по префиксу."""
        self.dict["application"] = "приложение"
        self.dict["app"] = "приложение короткое"
        
        result = self.dict.search_prefix("app")
        expected_keys = {"app", "apple", "application"}
        result_keys = {key for key, _ in result}
        
        self.assertEqual(result_keys, expected_keys)
    
    def test_empty_prefix_search(self):
        """Тест поиска с пустым префиксом."""
        result = self.dict.search_prefix("")
        self.assertEqual(len(result), 3)
    
    def test_nonexistent_prefix_search(self):
        """Тест поиска с несуществующим префиксом."""
        result = self.dict.search_prefix("xyz")
        self.assertEqual(len(result), 0)
    
    def test_save_and_load_from_txt_file(self):
        """Тест сохранения и загрузки из TXT файла."""
        with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.txt', encoding='utf-8') as f:
            temp_filename = f.name
        
        try:
            # Сохраняем словарь
            self.dict.save_to_file(temp_filename)
            
            # Загружаем словарь
            loaded_dict = EnglishRussianDictionary.load_from_file(temp_filename)
            
            # Проверяем, что данные совпадают
            self.assertEqual(len(self.dict), len(loaded_dict))
            for word, translation in self.dict:
                self.assertEqual(loaded_dict[word], translation)
        
        finally:
            if os.path.exists(temp_filename):
                os.unlink(temp_filename)
    
    def test_load_nonexistent_file(self):
        """Тест загрузки из несуществующего файла."""
        with self.assertRaises(FileNotFoundError):
            EnglishRussianDictionary.load_from_file("nonexistent.txt")
    
    def test_load_txt_file_with_comments(self):
        """Тест загрузки TXT файла с комментариями."""
        with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.txt', encoding='utf-8') as f:
            f.write("# Comment\n")
            f.write("hello:привет\n")
            f.write("\n")  # Пустая строка
            f.write("world:мир\n")
            temp_filename = f.name
        
        try:
            loaded_dict = EnglishRussianDictionary.load_from_file(temp_filename)
            self.assertEqual(len(loaded_dict), 2)
            self.assertEqual(loaded_dict["hello"], "привет")
            self.assertEqual(loaded_dict["world"], "мир")
        finally:
            if os.path.exists(temp_filename):
                os.unlink(temp_filename)
    
    def test_load_txt_file_invalid_format(self):
        """Тест загрузки TXT файла с неверным форматом."""
        with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.txt', encoding='utf-8') as f:
            f.write("invalid_line_without_colon\n")
            temp_filename = f.name
        
        try:
            with self.assertRaises(ValueError):
                EnglishRussianDictionary.load_from_file(temp_filename)
        finally:
            if os.path.exists(temp_filename):
                os.unlink(temp_filename)
    
    def test_load_txt_file_empty_key_value(self):
        """Тест загрузки TXT файла с пустыми ключами/значениями."""
        with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.txt', encoding='utf-8') as f:
            f.write(":empty_key\n")
            f.write("word:\n")
            temp_filename = f.name
        
        try:
            with self.assertRaises(ValueError):
                EnglishRussianDictionary.load_from_file(temp_filename)
        finally:
            if os.path.exists(temp_filename):
                os.unlink(temp_filename)
    
    def test_clear(self):
        """Тест очистки словаря."""
        self.dict.clear()
        self.assertEqual(len(self.dict), 0)
        self.assertFalse("hello" in self.dict)
    
    def test_add_empty_key_or_value(self):
        """Тест добавления с пустым ключом или значением."""
        with self.assertRaises(ValueError):
            self.dict[""] = "значение"
        
        with self.assertRaises(ValueError):
            self.dict["word"] = ""


if __name__ == '__main__':
    unittest.main()