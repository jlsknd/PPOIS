"""
@file main.py
@brief Главный модуль для демонстрации работы алгоритмов сортировки
@details Демонстрирует использование Shell sort и LSD Radix sort на различных типах данных
"""

from sorters import ShellSorter, LSDRadixSorter, SorterFactory
from custom_classes import Student, Product, Book
from typing import List
import random


def print_separator(title: str = ""):
    """
    @brief Печатает разделительную линию
    @param title Заголовок секции
    """
    print("\n" + "=" * 80)
    if title:
        print(f" {title} ".center(80, "="))
        print("=" * 80)


def demonstrate_integer_sorting():
    """
    @brief Демонстрация сортировки целых чисел
    """
    print_separator("СОРТИРОВКА ЦЕЛЫХ ЧИСЕЛ")

    # Генерируем случайный массив
    data = [random.randint(1, 100) for _ in range(15)]
    print(f"\nИсходный массив: {data}")

    # Shell Sort
    print("\n--- Shell Sort ---")
    shell_sorter = ShellSorter()
    result_shell = shell_sorter.sort(data)
    print(f"Отсортированный массив: {result_shell}")
    stats = shell_sorter.get_statistics()
    print(f"Статистика: Сравнений = {stats['comparisons']}, Перестановок = {stats['swaps']}")

    # Radix Sort
    print("\n--- LSD Radix Sort ---")
    radix_sorter = LSDRadixSorter()
    result_radix = radix_sorter.sort(data)
    print(f"Отсортированный массив: {result_radix}")
    stats = radix_sorter.get_statistics()
    print(f"Статистика: Проходов = {stats['passes']}")


def demonstrate_string_sorting():
    """
    @brief Демонстрация сортировки строк
    """
    print_separator("СОРТИРОВКА СТРОК")

    words = ["python", "java", "javascript", "c++", "ruby", "go", "rust", "swift"]
    print(f"\nИсходный список слов: {words}")

    # Shell Sort
    print("\n--- Shell Sort (по алфавиту) ---")
    shell_sorter = ShellSorter()
    result = shell_sorter.sort(words)
    print(f"Отсортированный список: {result}")

    # Сортировка по длине
    print("\n--- Shell Sort (по длине) ---")
    result = shell_sorter.sort(words, key=lambda x: len(x))
    print(f"Отсортированный список: {result}")


def demonstrate_student_sorting():
    """
    @brief Демонстрация сортировки объектов Student
    """
    print_separator("СОРТИРОВКА СТУДЕНТОВ")

    students = [
        Student("Иванов Иван", 22, 4.5, 12345),
        Student("Петрова Мария", 20, 4.8, 12340),
        Student("Сидоров Петр", 23, 4.2, 12350),
        Student("Козлова Анна", 21, 4.9, 12342),
        Student("Смирнов Алексей", 19, 4.3, 12338)
    ]

    print("\nИсходный список студентов:")
    for student in students:
        print(f"  {student}")

    # Сортировка по возрасту (по умолчанию)
    print("\n--- Shell Sort (по возрасту) ---")
    shell_sorter = ShellSorter()
    result = shell_sorter.sort(students)
    print("Отсортированные студенты:")
    for student in result:
        print(f"  {student}")

    # Сортировка по среднему баллу
    print("\n--- Shell Sort (по среднему баллу) ---")
    result = shell_sorter.sort(students, key=lambda s: s.grade, reverse=True)
    print("Отсортированные студенты:")
    for student in result:
        print(f"  {student}")

    # Сортировка по ID с помощью Radix Sort
    print("\n--- LSD Radix Sort (по ID студента) ---")
    radix_sorter = LSDRadixSorter()
    result = radix_sorter.sort(students, key=lambda s: s.student_id)
    print("Отсортированные студенты:")
    for student in result:
        print(f"  {student}")


def demonstrate_product_sorting():
    """
    @brief Демонстрация сортировки объектов Product
    """
    print_separator("СОРТИРОВКА ТОВАРОВ")

    products = [
        Product("Ноутбук Dell XPS", 89999.99, 5, "Электроника"),
        Product("Мышь Logitech", 1299.00, 50, "Электроника"),
        Product("Клавиатура Keychron", 7999.00, 20, "Электроника"),
        Product("Монитор Samsung", 25999.00, 10, "Электроника"),
        Product("Наушники Sony", 4599.00, 30, "Аудио")
    ]

    print("\nИсходный список товаров:")
    for product in products:
        print(f"  {product}")

    # Сортировка по цене
    print("\n--- Shell Sort (по цене) ---")
    shell_sorter = ShellSorter()
    result = shell_sorter.sort(products)
    print("Отсортированные товары:")
    for product in result:
        print(f"  {product}")

    # Сортировка по количеству
    print("\n--- LSD Radix Sort (по количеству на складе) ---")
    radix_sorter = LSDRadixSorter()
    result = radix_sorter.sort(products, key=lambda p: p.quantity, reverse=True)
    print("Отсортированные товары:")
    for product in result:
        print(f"  {product}")


def demonstrate_book_sorting():
    """
    @brief Демонстрация сортировки объектов Book
    """
    print_separator("СОРТИРОВКА КНИГ")

    books = [
        Book("Война и мир", "Лев Толстой", 1869, 1225, 9785170123456),
        Book("Преступление и наказание", "Федор Достоевский", 1866, 671, 9785170234567),
        Book("Мастер и Маргарита", "Михаил Булгаков", 1967, 470, 9785170345678),
        Book("Анна Каренина", "Лев Толстой", 1877, 864, 9785170456789),
        Book("Идиот", "Федор Достоевский", 1869, 640, 9785170567890)
    ]

    print("\nИсходный список книг:")
    for book in books:
        print(f"  {book}")

    # Сортировка по году издания
    print("\n--- Shell Sort (по году издания) ---")
    shell_sorter = ShellSorter()
    result = shell_sorter.sort(books)
    print("Отсортированные книги:")
    for book in result:
        print(f"  {book}")

    # Сортировка по количеству страниц
    print("\n--- Shell Sort (по количеству страниц) ---")
    result = shell_sorter.sort(books, key=lambda b: b.pages, reverse=True)
    print("Отсортированные книги:")
    for book in result:
        print(f"  {book}")

    # Сортировка по ISBN
    print("\n--- LSD Radix Sort (по ISBN) ---")
    radix_sorter = LSDRadixSorter()
    result = radix_sorter.sort(books, key=lambda b: b.isbn)
    print("Отсортированные книги:")
    for book in result:
        print(f"  {book}")


def demonstrate_factory_pattern():
    """
    @brief Демонстрация использования фабрики
    """
    print_separator("ИСПОЛЬЗОВАНИЕ ФАБРИКИ")

    data = [64, 34, 25, 12, 22, 11, 90, 88, 45, 50]
    print(f"\nИсходный массив: {data}")

    # Используем фабрику для создания сортировщиков
    sorter_types = ["shell", "radix"]

    for sorter_type in sorter_types:
        print(f"\n--- {sorter_type.upper()} Sorter (через фабрику) ---")
        sorter = SorterFactory.create_sorter(sorter_type)
        result = sorter.sort(data)
        print(f"Отсортированный массив: {result}")


def demonstrate_performance_comparison():
    """
    @brief Демонстрация сравнения производительности
    """
    print_separator("СРАВНЕНИЕ ПРОИЗВОДИТЕЛЬНОСТИ")

    import time

    # Тест на большом массиве
    size = 1000
    data = [random.randint(0, 10000) for _ in range(size)]

    print(f"\nРазмер массива: {size} элементов")
    print(f"Диапазон значений: [0, 10000]")

    # Shell Sort
    print("\n--- Shell Sort ---")
    shell_sorter = ShellSorter()
    start_time = time.time()
    result_shell = shell_sorter.sort(data)
    shell_time = time.time() - start_time
    stats = shell_sorter.get_statistics()
    print(f"Время выполнения: {shell_time:.6f} секунд")
    print(f"Сравнений: {stats['comparisons']}")
    print(f"Перестановок: {stats['swaps']}")

    # Radix Sort
    print("\n--- LSD Radix Sort ---")
    radix_sorter = LSDRadixSorter()
    start_time = time.time()
    result_radix = radix_sorter.sort(data)
    radix_time = time.time() - start_time
    stats = radix_sorter.get_statistics()
    print(f"Время выполнения: {radix_time:.6f} секунд")
    print(f"Проходов: {stats['passes']}")

    # Сравнение
    print("\n--- Результаты ---")
    print(f"Shell Sort быстрее на: {abs(radix_time - shell_time):.6f} секунд"
          if shell_time < radix_time else
          f"Radix Sort быстрее на: {abs(radix_time - shell_time):.6f} секунд")

    # Проверка корректности
    print(f"\nОба алгоритма дали корректный результат: {result_shell == result_radix == sorted(data)}")


def main():
    """
    @brief Главная функция программы
    """
    print("\n" + "=" * 80)
    print(" ДЕМОНСТРАЦИЯ РАБОТЫ АЛГОРИТМОВ СОРТИРОВКИ ".center(80, "="))
    print(" Shell Sort и LSD Radix Sort ".center(80, "="))
    print("=" * 80)

    try:
        # Демонстрация различных типов сортировки
        demonstrate_integer_sorting()
        demonstrate_string_sorting()
        demonstrate_student_sorting()
        demonstrate_product_sorting()
        demonstrate_book_sorting()
        demonstrate_factory_pattern()
        demonstrate_performance_comparison()

        print_separator()
        print("\n✓ Демонстрация завершена успешно!\n")

    except Exception as e:
        print(f"\n✗ Произошла ошибка: {e}\n")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    main()

