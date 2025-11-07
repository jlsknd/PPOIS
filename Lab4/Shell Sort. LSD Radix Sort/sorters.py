"""
@file sorters.py
@brief Модуль с реализацией алгоритмов сортировки Shell sort и LSD Radix sort
@details Содержит базовый класс для сортировщиков и два конкретных алгоритма сортировки
"""

from abc import ABC, abstractmethod
from typing import List, TypeVar, Callable, Any
import copy

T = TypeVar('T')


class BaseSorter(ABC):
    """
    @class BaseSorter
    @brief Абстрактный базовый класс для всех алгоритмов сортировки
    @details Определяет общий интерфейс для всех сортировщиков
    """

    @abstractmethod
    def sort(self, data: List[T], key: Callable[[T], Any] = None, reverse: bool = False) -> List[T]:
        """
        @brief Абстрактный метод сортировки
        @param data Список элементов для сортировки
        @param key Функция для извлечения ключа сравнения из элемента
        @param reverse Флаг обратной сортировки (по убыванию)
        @return Отсортированный список
        """
        pass

    def _compare(self, a: T, b: T, key: Callable[[T], Any] = None, reverse: bool = False) -> bool:
        """
        @brief Сравнивает два элемента с учетом функции ключа и направления сортировки
        @param a Первый элемент
        @param b Второй элемент
        @param key Функция для извлечения ключа сравнения
        @param reverse Флаг обратной сортировки
        @return True если a должен идти после b
        """
        val_a = key(a) if key else a
        val_b = key(b) if key else b

        if reverse:
            return val_a < val_b
        return val_a > val_b


class ShellSorter(BaseSorter):
    """
    @class ShellSorter
    @brief Реализация алгоритма сортировки Шелла
    @details Использует последовательность Кнута для определения интервалов

    Алгоритм Shell sort - это усовершенствованная версия сортировки вставками.
    Элементы сравниваются и переставляются на определенном расстоянии друг от друга.
    Это расстояние (gap) постепенно уменьшается, пока не станет равным 1.

    Временная сложность: O(n^(3/2)) в среднем случае
    Пространственная сложность: O(1)
    """

    def __init__(self):
        """
        @brief Конструктор класса ShellSorter
        """
        self.comparisons = 0
        self.swaps = 0

    def sort(self, data: List[T], key: Callable[[T], Any] = None, reverse: bool = False) -> List[T]:
        """
        @brief Сортирует список методом Шелла
        @param data Список для сортировки
        @param key Функция извлечения ключа для сравнения
        @param reverse Флаг сортировки по убыванию
        @return Отсортированный список
        """
        self.comparisons = 0
        self.swaps = 0

        # Создаем копию для сохранения исходных данных
        arr = copy.copy(data)
        n = len(arr)

        # Вычисляем начальный gap по последовательности Кнута: h = 3*h + 1
        gap = 1
        while gap < n // 3:
            gap = 3 * gap + 1

        # Уменьшаем gap и выполняем сортировку вставками для каждого gap
        while gap >= 1:
            # Выполняем сортировку вставками для элементов с интервалом gap
            for i in range(gap, n):
                temp = arr[i]
                j = i

                # Сдвигаем элементы, которые больше temp
                while j >= gap:
                    self.comparisons += 1
                    if self._compare(arr[j - gap], temp, key, reverse):
                        arr[j] = arr[j - gap]
                        j -= gap
                        self.swaps += 1
                    else:
                        break

                arr[j] = temp

            gap //= 3

        return arr

    def get_statistics(self) -> dict:
        """
        @brief Возвращает статистику последней сортировки
        @return Словарь со статистикой (количество сравнений и перестановок)
        """
        return {
            'comparisons': self.comparisons,
            'swaps': self.swaps
        }


class LSDRadixSorter(BaseSorter):
    """
    @class LSDRadixSorter
    @brief Реализация алгоритма поразрядной сортировки (LSD Radix Sort)
    @details LSD (Least Significant Digit) - сортировка начинается с младшего разряда

    Алгоритм Radix sort - это непосредственно сортировка, которая обрабатывает
    целые числа поразрядно, начиная с младшего разряда (LSD).

    Временная сложность: O(d * (n + k)), где d - количество разрядов, k - основание системы счисления
    Пространственная сложность: O(n + k)
    """

    def __init__(self, base: int = 10):
        """
        @brief Конструктор класса LSDRadixSorter
        @param base Основание системы счисления (по умолчанию 10)
        """
        self.base = base
        self.passes = 0

    def sort(self, data: List[T], key: Callable[[T], Any] = None, reverse: bool = False) -> List[T]:
        """
        @brief Сортирует список методом LSD Radix sort
        @param data Список для сортировки
        @param key Функция извлечения числового ключа
        @param reverse Флаг сортировки по убыванию
        @return Отсортированный список
        """
        self.passes = 0

        if not data:
            return []

        # Создаем копию для сохранения исходных данных
        arr = copy.copy(data)
        n = len(arr)

        # Извлекаем числовые значения
        if key:
            values = [key(item) for item in arr]
        else:
            values = arr

        # Проверяем, что все значения - целые числа
        if not all(isinstance(v, int) and v >= 0 for v in values):
            # Для нецелочисленных типов используем альтернативный метод
            return self._sort_with_key(arr, key, reverse)

        # Находим максимальное значение для определения количества разрядов
        max_val = max(values)

        # Выполняем поразрядную сортировку
        exp = 1
        while max_val // exp > 0:
            arr = self._counting_sort_by_digit(arr, exp, key)
            exp *= self.base
            self.passes += 1

        if reverse:
            arr.reverse()

        return arr

    def _counting_sort_by_digit(self, arr: List[T], exp: int, key: Callable[[T], Any] = None) -> List[T]:
        """
        @brief Вспомогательный метод сортировки подсчетом по определенному разряду
        @param arr Массив для сортировки
        @param exp Текущий разряд (1, 10, 100, ...)
        @param key Функция извлечения ключа
        @return Отсортированный по данному разряду массив
        """
        n = len(arr)
        output = [None] * n
        count = [0] * self.base

        # Подсчитываем количество элементов для каждой цифры
        for i in range(n):
            value = key(arr[i]) if key else arr[i]
            digit = (value // exp) % self.base
            count[digit] += 1

        # Преобразуем count в массив позиций
        for i in range(1, self.base):
            count[i] += count[i - 1]

        # Строим выходной массив
        for i in range(n - 1, -1, -1):
            value = key(arr[i]) if key else arr[i]
            digit = (value // exp) % self.base
            output[count[digit] - 1] = arr[i]
            count[digit] -= 1

        return output

    def _sort_with_key(self, arr: List[T], key: Callable[[T], Any] = None, reverse: bool = False) -> List[T]:
        """
        @brief Альтернативный метод сортировки для нецелочисленных типов
        @param arr Массив для сортировки
        @param key Функция извлечения ключа
        @param reverse Флаг обратной сортировки
        @return Отсортированный массив
        """
        # Используем встроенную сортировку для нецелочисленных типов
        result = sorted(arr, key=key, reverse=reverse)
        return result

    def get_statistics(self) -> dict:
        """
        @brief Возвращает статистику последней сортировки
        @return Словарь со статистикой (количество проходов)
        """
        return {
            'passes': self.passes
        }


class SorterFactory:
    """
    @class SorterFactory
    @brief Фабрика для создания объектов сортировщиков
    @details Реализует паттерн "Фабрика" для создания различных типов сортировщиков
    """

    @staticmethod
    def create_sorter(sorter_type: str) -> BaseSorter:
        """
        @brief Создает объект сортировщика заданного типа
        @param sorter_type Тип сортировщика ("shell" или "radix")
        @return Объект сортировщика
        @throws ValueError если указан неверный тип сортировщика
        """
        sorter_type = sorter_type.lower()

        if sorter_type == "shell":
            return ShellSorter()
        elif sorter_type == "radix":
            return LSDRadixSorter()
        else:
            raise ValueError(f"Неизвестный тип сортировщика: {sorter_type}. "
                           f"Доступные типы: 'shell', 'radix'")

