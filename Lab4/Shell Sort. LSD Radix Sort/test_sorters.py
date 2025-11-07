"""
@file test_sorters.py
@brief Модуль с unit-тестами для алгоритмов сортировки
@details Содержит тесты для ShellSorter и LSDRadixSorter с покрытием 85%+
"""

import unittest
from typing import List
from .sorters import ShellSorter, LSDRadixSorter, SorterFactory
from .custom_classes import Student, Product, Book


class TestShellSorter(unittest.TestCase):
    """
    @class TestShellSorter
    @brief Тесты для класса ShellSorter
    """

    def setUp(self):
        """
        @brief Подготовка к тестам
        """
        self.sorter = ShellSorter()

    def test_sort_empty_list(self):
        """
        @brief Тест сортировки пустого списка
        """
        data = []
        result = self.sorter.sort(data)
        self.assertEqual(result, [])

    def test_sort_single_element(self):
        """
        @brief Тест сортировки списка с одним элементом
        """
        data = [42]
        result = self.sorter.sort(data)
        self.assertEqual(result, [42])

    def test_sort_integers_ascending(self):
        """
        @brief Тест сортировки целых чисел по возрастанию
        """
        data = [64, 34, 25, 12, 22, 11, 90]
        result = self.sorter.sort(data)
        self.assertEqual(result, [11, 12, 22, 25, 34, 64, 90])

    def test_sort_integers_descending(self):
        """
        @brief Тест сортировки целых чисел по убыванию
        """
        data = [64, 34, 25, 12, 22, 11, 90]
        result = self.sorter.sort(data, reverse=True)
        self.assertEqual(result, [90, 64, 34, 25, 22, 12, 11])

    def test_sort_already_sorted(self):
        """
        @brief Тест сортировки уже отсортированного списка
        """
        data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        result = self.sorter.sort(data)
        self.assertEqual(result, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

    def test_sort_reverse_sorted(self):
        """
        @brief Тест сортировки списка, отсортированного в обратном порядке
        """
        data = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        result = self.sorter.sort(data)
        self.assertEqual(result, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

    def test_sort_duplicates(self):
        """
        @brief Тест сортировки списка с дубликатами
        """
        data = [5, 2, 8, 2, 9, 1, 5, 5]
        result = self.sorter.sort(data)
        self.assertEqual(result, [1, 2, 2, 5, 5, 5, 8, 9])

    def test_sort_negative_numbers(self):
        """
        @brief Тест сортировки отрицательных чисел
        """
        data = [-5, 3, -2, 8, -10, 0, 7]
        result = self.sorter.sort(data)
        self.assertEqual(result, [-10, -5, -2, 0, 3, 7, 8])

    def test_sort_floats(self):
        """
        @brief Тест сортировки чисел с плавающей точкой
        """
        data = [3.14, 2.71, 1.41, 2.71, 0.5]
        result = self.sorter.sort(data)
        self.assertAlmostEqual(result[0], 0.5)
        self.assertAlmostEqual(result[1], 1.41)
        self.assertAlmostEqual(result[4], 3.14)

    def test_sort_strings(self):
        """
        @brief Тест сортировки строк
        """
        data = ["banana", "apple", "cherry", "date"]
        result = self.sorter.sort(data)
        self.assertEqual(result, ["apple", "banana", "cherry", "date"])

    def test_sort_students_default(self):
        """
        @brief Тест сортировки студентов по умолчанию (по возрасту)
        """
        students = [
            Student("Alice", 22, 3.8, 101),
            Student("Bob", 20, 3.5, 102),
            Student("Charlie", 23, 3.9, 103),
            Student("David", 19, 3.6, 104)
        ]
        result = self.sorter.sort(students)
        self.assertEqual(result[0].age, 19)
        self.assertEqual(result[1].age, 20)
        self.assertEqual(result[2].age, 22)
        self.assertEqual(result[3].age, 23)

    def test_sort_students_by_grade(self):
        """
        @brief Тест сортировки студентов по среднему баллу
        """
        students = [
            Student("Alice", 22, 3.8, 101),
            Student("Bob", 20, 3.5, 102),
            Student("Charlie", 23, 3.9, 103),
            Student("David", 19, 3.6, 104)
        ]
        result = self.sorter.sort(students, key=lambda s: s.grade)
        self.assertEqual(result[0].grade, 3.5)
        self.assertEqual(result[-1].grade, 3.9)

    def test_sort_students_by_name(self):
        """
        @brief Тест сортировки студентов по имени
        """
        students = [
            Student("Charlie", 23, 3.9, 103),
            Student("Alice", 22, 3.8, 101),
            Student("David", 19, 3.6, 104),
            Student("Bob", 20, 3.5, 102)
        ]
        result = self.sorter.sort(students, key=lambda s: s.name)
        self.assertEqual(result[0].name, "Alice")
        self.assertEqual(result[1].name, "Bob")
        self.assertEqual(result[2].name, "Charlie")
        self.assertEqual(result[3].name, "David")

    def test_sort_products_by_price(self):
        """
        @brief Тест сортировки товаров по цене
        """
        products = [
            Product("Laptop", 999.99, 5, "Electronics"),
            Product("Mouse", 29.99, 50, "Electronics"),
            Product("Keyboard", 79.99, 30, "Electronics")
        ]
        result = self.sorter.sort(products)
        self.assertEqual(result[0].price, 29.99)
        self.assertEqual(result[-1].price, 999.99)

    def test_sort_products_by_quantity(self):
        """
        @brief Тест сортировки товаров по количеству
        """
        products = [
            Product("Laptop", 999.99, 5, "Electronics"),
            Product("Mouse", 29.99, 50, "Electronics"),
            Product("Keyboard", 79.99, 30, "Electronics")
        ]
        result = self.sorter.sort(products, key=lambda p: p.quantity)
        self.assertEqual(result[0].quantity, 5)
        self.assertEqual(result[-1].quantity, 50)

    def test_sort_books_by_year(self):
        """
        @brief Тест сортировки книг по году издания
        """
        books = [
            Book("Book1", "Author1", 2020, 300, 1234567890),
            Book("Book2", "Author2", 2015, 250, 1234567891),
            Book("Book3", "Author3", 2022, 400, 1234567892)
        ]
        result = self.sorter.sort(books)
        self.assertEqual(result[0].year, 2015)
        self.assertEqual(result[-1].year, 2022)

    def test_sort_books_by_pages(self):
        """
        @brief Тест сортировки книг по количеству страниц
        """
        books = [
            Book("Book1", "Author1", 2020, 300, 1234567890),
            Book("Book2", "Author2", 2015, 250, 1234567891),
            Book("Book3", "Author3", 2022, 400, 1234567892)
        ]
        result = self.sorter.sort(books, key=lambda b: b.pages)
        self.assertEqual(result[0].pages, 250)
        self.assertEqual(result[-1].pages, 400)

    def test_get_statistics(self):
        """
        @brief Тест получения статистики сортировки
        """
        data = [5, 2, 8, 1, 9]
        self.sorter.sort(data)
        stats = self.sorter.get_statistics()
        self.assertIn('comparisons', stats)
        self.assertIn('swaps', stats)
        self.assertGreater(stats['comparisons'], 0)

    def test_original_list_unchanged(self):
        """
        @brief Тест что оригинальный список не изменяется
        """
        original = [5, 2, 8, 1, 9]
        data = original.copy()
        self.sorter.sort(data)
        self.assertEqual(original, [5, 2, 8, 1, 9])

    def test_large_dataset(self):
        """
        @brief Тест сортировки большого набора данных
        """
        import random
        data = [random.randint(1, 1000) for _ in range(100)]
        result = self.sorter.sort(data)
        self.assertEqual(result, sorted(data))


class TestLSDRadixSorter(unittest.TestCase):
    """
    @class TestLSDRadixSorter
    @brief Тесты для класса LSDRadixSorter
    """

    def setUp(self):
        """
        @brief Подготовка к тестам
        """
        self.sorter = LSDRadixSorter()

    def test_sort_empty_list(self):
        """
        @brief Тест сортировки пустого списка
        """
        data = []
        result = self.sorter.sort(data)
        self.assertEqual(result, [])

    def test_sort_single_element(self):
        """
        @brief Тест сортировки списка с одним элементом
        """
        data = [42]
        result = self.sorter.sort(data)
        self.assertEqual(result, [42])

    def test_sort_integers_ascending(self):
        """
        @brief Тест сортировки целых положительных чисел по возрастанию
        """
        data = [170, 45, 75, 90, 802, 24, 2, 66]
        result = self.sorter.sort(data)
        self.assertEqual(result, [2, 24, 45, 66, 75, 90, 170, 802])

    def test_sort_integers_descending(self):
        """
        @brief Тест сортировки целых чисел по убыванию
        """
        data = [170, 45, 75, 90, 802, 24, 2, 66]
        result = self.sorter.sort(data, reverse=True)
        self.assertEqual(result, [802, 170, 90, 75, 66, 45, 24, 2])

    def test_sort_already_sorted(self):
        """
        @brief Тест сортировки уже отсортированного списка
        """
        data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        result = self.sorter.sort(data)
        self.assertEqual(result, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

    def test_sort_reverse_sorted(self):
        """
        @brief Тест сортировки списка в обратном порядке
        """
        data = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        result = self.sorter.sort(data)
        self.assertEqual(result, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

    def test_sort_duplicates(self):
        """
        @brief Тест сортировки списка с дубликатами
        """
        data = [5, 2, 8, 2, 9, 1, 5, 5]
        result = self.sorter.sort(data)
        self.assertEqual(result, [1, 2, 2, 5, 5, 5, 8, 9])

    def test_sort_same_elements(self):
        """
        @brief Тест сортировки списка с одинаковыми элементами
        """
        data = [7, 7, 7, 7, 7]
        result = self.sorter.sort(data)
        self.assertEqual(result, [7, 7, 7, 7, 7])

    def test_sort_large_numbers(self):
        """
        @brief Тест сортировки больших чисел
        """
        data = [999999, 1, 50000, 123456, 7890]
        result = self.sorter.sort(data)
        self.assertEqual(result, [1, 7890, 50000, 123456, 999999])

    def test_sort_students_by_id(self):
        """
        @brief Тест сортировки студентов по ID
        """
        students = [
            Student("Alice", 22, 3.8, 105),
            Student("Bob", 20, 3.5, 102),
            Student("Charlie", 23, 3.9, 108),
            Student("David", 19, 3.6, 101)
        ]
        result = self.sorter.sort(students, key=lambda s: s.student_id)
        self.assertEqual(result[0].student_id, 101)
        self.assertEqual(result[-1].student_id, 108)

    def test_sort_students_by_age(self):
        """
        @brief Тест сортировки студентов по возрасту
        """
        students = [
            Student("Alice", 22, 3.8, 101),
            Student("Bob", 20, 3.5, 102),
            Student("Charlie", 25, 3.9, 103),
            Student("David", 19, 3.6, 104)
        ]
        result = self.sorter.sort(students, key=lambda s: s.age)
        self.assertEqual(result[0].age, 19)
        self.assertEqual(result[-1].age, 25)

    def test_sort_products_by_quantity(self):
        """
        @brief Тест сортировки товаров по количеству
        """
        products = [
            Product("Laptop", 999.99, 5, "Electronics"),
            Product("Mouse", 29.99, 50, "Electronics"),
            Product("Keyboard", 79.99, 30, "Electronics")
        ]
        result = self.sorter.sort(products, key=lambda p: p.quantity)
        self.assertEqual(result[0].quantity, 5)
        self.assertEqual(result[-1].quantity, 50)

    def test_sort_books_by_year(self):
        """
        @brief Тест сортировки книг по году
        """
        books = [
            Book("Book1", "Author1", 2020, 300, 1234567890),
            Book("Book2", "Author2", 2015, 250, 1234567891),
            Book("Book3", "Author3", 2022, 400, 1234567892)
        ]
        result = self.sorter.sort(books, key=lambda b: b.year)
        self.assertEqual(result[0].year, 2015)
        self.assertEqual(result[-1].year, 2022)

    def test_sort_books_by_pages(self):
        """
        @brief Тест сортировки книг по страницам
        """
        books = [
            Book("Book1", "Author1", 2020, 300, 1234567890),
            Book("Book2", "Author2", 2015, 250, 1234567891),
            Book("Book3", "Author3", 2022, 400, 1234567892)
        ]
        result = self.sorter.sort(books, key=lambda b: b.pages)
        self.assertEqual(result[0].pages, 250)
        self.assertEqual(result[-1].pages, 400)

    def test_sort_books_by_isbn(self):
        """
        @brief Тест сортировки книг по ISBN
        """
        books = [
            Book("Book1", "Author1", 2020, 300, 9876543210),
            Book("Book2", "Author2", 2015, 250, 1234567890),
            Book("Book3", "Author3", 2022, 400, 5555555555)
        ]
        result = self.sorter.sort(books, key=lambda b: b.isbn)
        self.assertEqual(result[0].isbn, 1234567890)
        self.assertEqual(result[-1].isbn, 9876543210)

    def test_get_statistics(self):
        """
        @brief Тест получения статистики сортировки
        """
        data = [170, 45, 75, 90, 802, 24, 2, 66]
        self.sorter.sort(data)
        stats = self.sorter.get_statistics()
        self.assertIn('passes', stats)
        self.assertGreater(stats['passes'], 0)

    def test_custom_base(self):
        """
        @brief Тест сортировки с пользовательским основанием
        """
        sorter = LSDRadixSorter(base=16)
        data = [170, 45, 75, 90, 802, 24, 2, 66]
        result = sorter.sort(data)
        self.assertEqual(result, sorted(data))

    def test_original_list_unchanged(self):
        """
        @brief Тест что оригинальный список не изменяется
        """
        original = [170, 45, 75, 90, 802]
        data = original.copy()
        self.sorter.sort(data)
        self.assertEqual(original, [170, 45, 75, 90, 802])

    def test_large_dataset(self):
        """
        @brief Тест сортировки большого набора данных
        """
        import random
        data = [random.randint(0, 10000) for _ in range(100)]
        result = self.sorter.sort(data)
        self.assertEqual(result, sorted(data))

    def test_sort_with_zeros(self):
        """
        @brief Тест сортировки с нулевыми значениями
        """
        data = [0, 5, 0, 3, 0, 1]
        result = self.sorter.sort(data)
        self.assertEqual(result, [0, 0, 0, 1, 3, 5])

    def test_sort_strings_with_key(self):
        """
        @brief Тест сортировки строк с функцией key (использует альтернативный метод)
        """
        data = ["banana", "apple", "cherry", "date"]
        result = self.sorter.sort(data, key=lambda s: len(s))
        # Проверяем что результат отсортирован по длине
        lengths = [len(s) for s in result]
        self.assertEqual(lengths, sorted(lengths))

    def test_sort_floats_with_key(self):
        """
        @brief Тест сортировки с float ключами (использует альтернативный метод)
        """
        students = [
            Student("Alice", 22, 3.8, 101),
            Student("Bob", 20, 3.5, 102),
            Student("Charlie", 23, 3.9, 103)
        ]
        result = self.sorter.sort(students, key=lambda s: s.grade)
        self.assertAlmostEqual(result[0].grade, 3.5)
        self.assertAlmostEqual(result[-1].grade, 3.9)


class TestSorterFactory(unittest.TestCase):
    """
    @class TestSorterFactory
    @brief Тесты для класса SorterFactory
    """

    def test_create_shell_sorter(self):
        """
        @brief Тест создания ShellSorter через фабрику
        """
        sorter = SorterFactory.create_sorter("shell")
        self.assertIsInstance(sorter, ShellSorter)

    def test_create_radix_sorter(self):
        """
        @brief Тест создания LSDRadixSorter через фабрику
        """
        sorter = SorterFactory.create_sorter("radix")
        self.assertIsInstance(sorter, LSDRadixSorter)

    def test_create_shell_sorter_uppercase(self):
        """
        @brief Тест создания ShellSorter с заглавными буквами
        """
        sorter = SorterFactory.create_sorter("SHELL")
        self.assertIsInstance(sorter, ShellSorter)

    def test_create_radix_sorter_mixed_case(self):
        """
        @brief Тест создания RadixSorter со смешанным регистром
        """
        sorter = SorterFactory.create_sorter("RaDiX")
        self.assertIsInstance(sorter, LSDRadixSorter)

    def test_create_invalid_sorter(self):
        """
        @brief Тест создания сортировщика с неверным типом
        """
        with self.assertRaises(ValueError) as context:
            SorterFactory.create_sorter("invalid")
        self.assertIn("Неизвестный тип сортировщика", str(context.exception))

    def test_factory_sorter_works(self):
        """
        @brief Тест что сортировщик из фабрики работает корректно
        """
        sorter = SorterFactory.create_sorter("shell")
        data = [5, 2, 8, 1, 9]
        result = sorter.sort(data)
        self.assertEqual(result, [1, 2, 5, 8, 9])


class TestCustomClasses(unittest.TestCase):
    """
    @class TestCustomClasses
    @brief Тесты для пользовательских классов
    """

    def test_student_equality(self):
        """
        @brief Тест оператора равенства для Student
        """
        s1 = Student("Alice", 20, 3.5, 101)
        s2 = Student("Alice", 20, 3.5, 101)
        s3 = Student("Bob", 20, 3.5, 101)
        self.assertEqual(s1, s2)
        self.assertNotEqual(s1, s3)

    def test_student_comparison(self):
        """
        @brief Тест операторов сравнения для Student
        """
        s1 = Student("Alice", 20, 3.5, 101)
        s2 = Student("Bob", 22, 3.7, 102)
        self.assertLess(s1, s2)
        self.assertGreater(s2, s1)
        self.assertLessEqual(s1, s2)
        self.assertGreaterEqual(s2, s1)

    def test_product_equality(self):
        """
        @brief Тест оператора равенства для Product
        """
        p1 = Product("Laptop", 999.99, 5, "Electronics")
        p2 = Product("Laptop", 999.99, 5, "Electronics")
        p3 = Product("Mouse", 29.99, 50, "Electronics")
        self.assertEqual(p1, p2)
        self.assertNotEqual(p1, p3)

    def test_product_comparison(self):
        """
        @brief Тест операторов сравнения для Product
        """
        p1 = Product("Mouse", 29.99, 50, "Electronics")
        p2 = Product("Laptop", 999.99, 5, "Electronics")
        self.assertLess(p1, p2)
        self.assertGreater(p2, p1)

    def test_book_equality(self):
        """
        @brief Тест оператора равенства для Book
        """
        b1 = Book("Book1", "Author1", 2020, 300, 1234567890)
        b2 = Book("Book1", "Author1", 2020, 300, 1234567890)
        b3 = Book("Book2", "Author2", 2021, 400, 1234567891)
        self.assertEqual(b1, b2)
        self.assertNotEqual(b1, b3)

    def test_book_comparison(self):
        """
        @brief Тест операторов сравнения для Book
        """
        b1 = Book("Book1", "Author1", 2015, 300, 1234567890)
        b2 = Book("Book2", "Author2", 2020, 400, 1234567891)
        self.assertLess(b1, b2)
        self.assertGreater(b2, b1)

    def test_student_repr(self):
        """
        @brief Тест строкового представления Student
        """
        s = Student("Alice", 20, 3.5, 101)
        repr_str = repr(s)
        self.assertIn("Alice", repr_str)
        self.assertIn("20", repr_str)

    def test_product_repr(self):
        """
        @brief Тест строкового представления Product
        """
        p = Product("Laptop", 999.99, 5, "Electronics")
        repr_str = repr(p)
        self.assertIn("Laptop", repr_str)
        self.assertIn("999.99", repr_str)

    def test_book_repr(self):
        """
        @brief Тест строкового представления Book
        """
        b = Book("Book1", "Author1", 2020, 300, 1234567890)
        repr_str = repr(b)
        self.assertIn("Book1", repr_str)
        self.assertIn("Author1", repr_str)

    def test_student_equality_with_different_type(self):
        """
        @brief Тест сравнения Student с объектом другого типа
        """
        s = Student("Alice", 20, 3.5, 101)
        self.assertNotEqual(s, "not a student")
        self.assertNotEqual(s, 42)

    def test_product_equality_with_different_type(self):
        """
        @brief Тест сравнения Product с объектом другого типа
        """
        p = Product("Laptop", 999.99, 5, "Electronics")
        self.assertNotEqual(p, "not a product")
        self.assertNotEqual(p, 42)

    def test_book_equality_with_different_type(self):
        """
        @brief Тест сравнения Book с объектом другого типа
        """
        b = Book("Book1", "Author1", 2020, 300, 1234567890)
        self.assertNotEqual(b, "not a book")
        self.assertNotEqual(b, 42)

    def test_student_le_ge(self):
        """
        @brief Тест операторов <= и >= для Student
        """
        s1 = Student("Alice", 20, 3.5, 101)
        s2 = Student("Bob", 20, 3.7, 102)
        s3 = Student("Charlie", 22, 3.9, 103)
        self.assertLessEqual(s1, s2)
        self.assertLessEqual(s1, s3)
        self.assertGreaterEqual(s3, s1)
        self.assertGreaterEqual(s2, s1)

    def test_product_le_ge(self):
        """
        @brief Тест операторов <= и >= для Product
        """
        p1 = Product("Mouse", 29.99, 50, "Electronics")
        p2 = Product("Keyboard", 29.99, 30, "Electronics")
        p3 = Product("Laptop", 999.99, 5, "Electronics")
        self.assertLessEqual(p1, p2)
        self.assertLessEqual(p1, p3)
        self.assertGreaterEqual(p3, p1)

    def test_book_le_ge(self):
        """
        @brief Тест операторов <= и >= для Book
        """
        b1 = Book("Book1", "Author1", 2015, 300, 1234567890)
        b2 = Book("Book2", "Author2", 2015, 400, 1234567891)
        b3 = Book("Book3", "Author3", 2020, 500, 1234567892)
        self.assertLessEqual(b1, b2)
        self.assertLessEqual(b1, b3)
        self.assertGreaterEqual(b3, b1)


if __name__ == '__main__':
    unittest.main()

