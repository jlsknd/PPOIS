"""
Модуль реализует англо-русский словарь на основе бинарного дерева поиска.

Классы:
    TreeNode - узел бинарного дерева
    EnglishRussianDictionary - основной класс словаря

Исключения:
    KeyError - когда слово не найдено
    ValueError - при неверных аргументах
    FileNotFoundError - когда файл не найден
"""

from typing import Optional, List, Tuple, Iterator


class TreeNode:
    """
    Узел бинарного дерева поиска для хранения пар слово-перевод.
    
    Атрибуты:
        key (str): Английское слово
        value (str): Русский перевод
        left (Optional[TreeNode]): Левый потомок
        right (Optional[TreeNode]): Правый потомок
        height (int): Высота узла для балансировки
    """
    
    def __init__(self, key: str, value: str):
        """
        Инициализирует узел дерева.
        
        Args:
            key: Английское слово
            value: Русский перевод
        """
        self.key = key
        self.value = value
        self.left: Optional['TreeNode'] = None
        self.right: Optional['TreeNode'] = None
        self.height = 1


class EnglishRussianDictionary:
    """
    Англо-русский словарь на основе самобалансирующегося бинарного дерева поиска (AVL).
    
    Реализует основные операции: добавление, удаление, поиск, обходы.
    Поддерживает загрузку данных из TXT файла.
    
    Примеры:
        >>> dictionary = EnglishRussianDictionary()
        >>> dictionary["hello"] = "привет"
        >>> print(dictionary["hello"])
        привет
        
        >>> dictionary += "world:мир"
        >>> del dictionary["hello"]
    """
    
    def __init__(self, initial_data: Optional[List[Tuple[str, str]]] = None):
        """
        Инициализирует словарь.
        
        Args:
            initial_data: Начальные данные в формате [(слово, перевод), ...]
            
        Пример:
            >>> dict = EnglishRussianDictionary([("hello", "привет"), ("world", "мир")])
        """
        self._root: Optional[TreeNode] = None
        self._size = 0
        
        if initial_data:
            for key, value in initial_data:
                self[key] = value
    
    def __setitem__(self, key: str, value: str) -> None:
        """
        Добавляет или обновляет пару слово-перевод.
        
        Args:
            key: Английское слово
            value: Русский перевод
            
        Raises:
            ValueError: Если ключ или значение пустые
            
        Пример:
            >>> dictionary["python"] = "питон"
        """
        if not key or not value:
            raise ValueError("Ключ и значение не могут быть пустыми")
        
        self._root = self._insert(self._root, key, value)
    
    def __getitem__(self, key: str) -> str:
        """
        Возвращает перевод для указанного слова.
        
        Args:
            key: Английское слово
            
        Returns:
            Русский перевод
            
        Raises:
            KeyError: Если слово не найдено в словаре
            
        Пример:
            >>> translation = dictionary["hello"]
        """
        node = self._search(self._root, key)
        if node is None:
            raise KeyError(f"Слово '{key}' не найдено в словаре")
        return node.value
    
    def __delitem__(self, key: str) -> None:
        """
        Удаляет слово из словаря.
        
        Args:
            key: Английское слово для удаления
            
        Raises:
            KeyError: Если слово не найдено в словаре
            
        Пример:
            >>> del dictionary["hello"]
        """
        if key not in self:
            raise KeyError(f"Слово '{key}' не найдено в словаре")
        
        self._root = self._delete(self._root, key)
        self._size -= 1
    
    def __contains__(self, key: str) -> bool:
        """
        Проверяет наличие слова в словаре.
        
        Args:
            key: Слово для проверки
            
        Returns:
            True если слово есть в словаре, иначе False
            
        Пример:
            >>> if "hello" in dictionary:
            >>>     print("Слово найдено")
        """
        return self._search(self._root, key) is not None
    
    def __len__(self) -> int:
        """
        Возвращает количество слов в словаре.
        
        Returns:
            Количество слов
            
        Пример:
            >>> word_count = len(dictionary)
        """
        return self._size
    
    def __iter__(self) -> Iterator[Tuple[str, str]]:
        """
        Возвращает итератор по парам слово-перевод в отсортированном порядке.
        
        Yields:
            Пары (английское слово, русский перевод)
            
        Пример:
            >>> for word, translation in dictionary:
            >>>     print(f"{word} -> {translation}")
        """
        return self.inorder_traversal()
    
    def __iadd__(self, pair_str: str) -> 'EnglishRussianDictionary':
        """
        Добавляет пару из строки формата 'слово:перевод'.
        
        Args:
            pair_str: Строка в формате 'слово:перевод'
            
        Returns:
            self
            
        Raises:
            ValueError: Если строка имеет неверный формат
            
        Пример:
            >>> dictionary += "sun:солнце"
        """
        if ':' not in pair_str:
            raise ValueError("Строка должна быть в формате 'слово:перевод'")
        
        key, value = pair_str.split(':', 1)
        self[key.strip()] = value.strip()
        return self
    
    def _height(self, node: Optional[TreeNode]) -> int:
        """Возвращает высоту узла."""
        if node is None:
            return 0
        return node.height
    
    def _update_height(self, node: TreeNode) -> None:
        """Обновляет высоту узла."""
        node.height = 1 + max(self._height(node.left), self._height(node.right))
    
    def _balance_factor(self, node: TreeNode) -> int:
        """Вычисляет баланс-фактор узла."""
        if node is None:
            return 0
        return self._height(node.left) - self._height(node.right)
    
    def _rotate_right(self, y: TreeNode) -> TreeNode:
        """Правый поворот для балансировки."""
        x = y.left
        T2 = x.right
        
        x.right = y
        y.left = T2
        
        self._update_height(y)
        self._update_height(x)
        
        return x
    
    def _rotate_left(self, x: TreeNode) -> TreeNode:
        """Левый поворот для балансировки."""
        y = x.right
        T2 = y.left
        
        y.left = x
        x.right = T2
        
        self._update_height(x)
        self._update_height(y)
        
        return y
    
    def _balance(self, node: TreeNode) -> TreeNode:
        """Балансирует узел при необходимости."""
        balance = self._balance_factor(node)
        
        # Left Left Case
        if balance > 1 and self._balance_factor(node.left) >= 0:
            return self._rotate_right(node)
        
        # Right Right Case
        if balance < -1 and self._balance_factor(node.right) <= 0:
            return self._rotate_left(node)
        
        # Left Right Case
        if balance > 1 and self._balance_factor(node.left) < 0:
            node.left = self._rotate_left(node.left)
            return self._rotate_right(node)
        
        # Right Left Case
        if balance < -1 and self._balance_factor(node.right) > 0:
            node.right = self._rotate_right(node.right)
            return self._rotate_left(node)
        
        return node
    
    def _insert(self, node: Optional[TreeNode], key: str, value: str) -> TreeNode:
        """Рекурсивно вставляет новый узел."""
        if node is None:
            self._size += 1
            return TreeNode(key, value)
        
        if key < node.key:
            node.left = self._insert(node.left, key, value)
        elif key > node.key:
            node.right = self._insert(node.right, key, value)
        else:
            # Ключ уже существует - обновляем значение
            node.value = value
            return node
        
        self._update_height(node)
        return self._balance(node)
    
    def _search(self, node: Optional[TreeNode], key: str) -> Optional[TreeNode]:
        """Рекурсивно ищет узел по ключу."""
        if node is None or node.key == key:
            return node
        
        if key < node.key:
            return self._search(node.left, key)
        return self._search(node.right, key)
    
    def _min_value_node(self, node: TreeNode) -> TreeNode:
        """Находит узел с минимальным значением в поддереве."""
        current = node
        while current.left is not None:
            current = current.left
        return current
    
    def _delete(self, node: Optional[TreeNode], key: str) -> Optional[TreeNode]:
        """Рекурсивно удаляет узел по ключу."""
        if node is None:
            return node
        
        if key < node.key:
            node.left = self._delete(node.left, key)
        elif key > node.key:
            node.right = self._delete(node.right, key)
        else:
            # Узел для удаления найден
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            else:
                # Узел с двумя детьми
                temp = self._min_value_node(node.right)
                node.key = temp.key
                node.value = temp.value
                node.right = self._delete(node.right, temp.key)
        
        if node is None:
            return node
        
        self._update_height(node)
        return self._balance(node)
    
    def inorder_traversal(self) -> Iterator[Tuple[str, str]]:
        """
        Возвращает итератор по парам слово-перевод в отсортированном порядке.
        
        Yields:
            Пары (английское слово, русский перевод)
            
        Пример:
            >>> for word, translation in dictionary.inorder_traversal():
            >>>     print(f"{word}: {translation}")
        """
        def _inorder(node: Optional[TreeNode]):
            if node:
                yield from _inorder(node.left)
                yield (node.key, node.value)
                yield from _inorder(node.right)
        
        return _inorder(self._root)
    
    def search_prefix(self, prefix: str) -> List[Tuple[str, str]]:
        """
        Находит все слова, начинающиеся с указанного префикса.
        
        Args:
            prefix: Префикс для поиска
            
        Returns:
            Список пар слово-перевод
            
        Пример:
            >>> results = dictionary.search_prefix("app")
            >>> for word, trans in results:
            >>>     print(f"{word} -> {trans}")
        """
        result = []
        
        def _search_prefix(node: Optional[TreeNode], prefix: str):
            if node is None:
                return
            
            if node.key.startswith(prefix):
                result.append((node.key, node.value))
                _search_prefix(node.left, prefix)
                _search_prefix(node.right, prefix)
            elif prefix < node.key:
                _search_prefix(node.left, prefix)
            else:
                _search_prefix(node.right, prefix)
        
        _search_prefix(self._root, prefix)
        return sorted(result, key=lambda x: x[0])
    
    @classmethod
    def load_from_file(cls, filename: str) -> 'EnglishRussianDictionary':
        """
        Загружает словарь из текстового файла.
        
        Формат файла: каждая строка содержит пару 'слово:перевод'
        
        Args:
            filename: Путь к файлу
            
        Returns:
            Новый экземпляр словаря
            
        Raises:
            FileNotFoundError: Если файл не существует
            ValueError: Если строка имеет неверный формат
            
        Пример:
            >>> dictionary = EnglishRussianDictionary.load_from_file("words.txt")
        """
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                lines = f.readlines()
        except FileNotFoundError:
            raise FileNotFoundError(f"Файл {filename} не найден")
        
        dictionary = cls()
        
        for line_num, line in enumerate(lines, 1):
            line = line.strip()
            if not line or line.startswith('#'):  # Пропускаем пустые строки и комментарии
                continue
                
            if ':' not in line:
                raise ValueError(f"Неверный формат в строке {line_num}: {line}")
            
            key, value = line.split(':', 1)
            key = key.strip()
            value = value.strip()
            
            if not key or not value:
                raise ValueError(f"Пустой ключ или значение в строке {line_num}: {line}")
            
            dictionary[key] = value
        
        return dictionary
    
    def save_to_file(self, filename: str) -> None:
        """
        Сохраняет словарь в текстовый файл.
        
        Args:
            filename: Путь к файлу для сохранения
            
        Пример:
            >>> dictionary.save_to_file("my_dictionary.txt")
        """
        with open(filename, 'w', encoding='utf-8') as f:
            for key, value in self:
                f.write(f"{key}:{value}\n")
    
    def clear(self) -> None:
        """Очищает словарь."""
        self._root = None
        self._size = 0


def main():
    """Основная функция для демонстрации работы словаря."""
    # Создаем словарь с начальными данными
    dictionary = EnglishRussianDictionary([
        ("hello", "привет"),
        ("world", "мир"),
        ("python", "питон"),
        ("programming", "программирование"),
        ("algorithm", "алгоритм")
    ])
    
    print("Англо-русский словарь")
    print("=" * 30)
    
    # Демонстрация основных операций
    print("1. Исходный словарь:")
    for eng, rus in dictionary:
        print(f"   {eng} -> {rus}")
    
    print(f"\n2. Количество слов: {len(dictionary)}")
    
    print("\n3. Добавляем новые слова:")
    dictionary["computer"] = "компьютер"
    dictionary["science"] = "наука"
    
    print("   computer ->", dictionary["computer"])
    print("   science ->", dictionary["science"])
    
    print("\n4. Поиск по префиксу 'pro':")
    for word, translation in dictionary.search_prefix("pro"):
        print(f"   {word} -> {translation}")
    
    print("\n5. Использование оператора +=:")
    dictionary += "data:данные"
    print("   data ->", dictionary["data"])
    
    # Сохраняем в файл
    dictionary.save_to_file("dictionary.txt")
    print("\n6. Словарь сохранен в файл 'dictionary.txt'")
    
    # Загружаем из файла
    try:
        loaded_dict = EnglishRussianDictionary.load_from_file("dictionary.txt")
        print(f"7. Загружено слов из файла: {len(loaded_dict)}")
        
        print("\n8. Загруженные слова:")
        for word, translation in list(loaded_dict)[:5]:  # Покажем первые 5
            print(f"   {word} -> {translation}")
            
    except FileNotFoundError:
        print("7. Файл для загрузки не найден")


if __name__ == "__main__":
    main()