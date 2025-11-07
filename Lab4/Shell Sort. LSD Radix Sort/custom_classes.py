"""
@file custom_classes.py
@brief Модуль с пользовательскими классами для демонстрации сортировки
@details Содержит пользовательские классы для тестирования алгоритмов сортировки
"""

from dataclasses import dataclass
from typing import Any


@dataclass
class Student:
    """
    @class Student
    @brief Класс представляющий студента
    @details Используется для демонстрации сортировки пользовательских объектов
    """

    name: str  #< Имя студента
    age: int   #< Возраст студента
    grade: float  #< Средний балл студента
    student_id: int  #< Идентификатор студента

    def __lt__(self, other: 'Student') -> bool:
        """
        @brief Оператор "меньше" для сравнения студентов
        @param other Другой студент
        @return True если текущий студент меньше другого (по возрасту)
        """
        return self.age < other.age

    def __le__(self, other: 'Student') -> bool:
        """
        @brief Оператор "меньше или равно"
        @param other Другой студент
        @return True если текущий студент меньше или равен другому
        """
        return self.age <= other.age

    def __gt__(self, other: 'Student') -> bool:
        """
        @brief Оператор "больше"
        @param other Другой студент
        @return True если текущий студент больше другого
        """
        return self.age > other.age

    def __ge__(self, other: 'Student') -> bool:
        """
        @brief Оператор "больше или равно"
        @param other Другой студент
        @return True если текущий студент больше или равен другому
        """
        return self.age >= other.age

    def __eq__(self, other: Any) -> bool:
        """
        @brief Оператор равенства
        @param other Другой объект
        @return True если объекты равны
        """
        if not isinstance(other, Student):
            return False
        return (self.name == other.name and
                self.age == other.age and
                self.grade == other.grade and
                self.student_id == other.student_id)

    def __repr__(self) -> str:
        """
        @brief Строковое представление студента
        @return Строка с информацией о студенте
        """
        return f"Student(name='{self.name}', age={self.age}, grade={self.grade}, id={self.student_id})"


@dataclass
class Product:
    """
    @class Product
    @brief Класс представляющий товар
    @details Используется для демонстрации сортировки товаров по различным критериям
    """

    name: str  #< Название товара
    price: float  #< Цена товара
    quantity: int  #< Количество товара
    category: str  #< Категория товара

    def __lt__(self, other: 'Product') -> bool:
        """
        @brief Оператор "меньше" для сравнения товаров
        @param other Другой товар
        @return True если текущий товар дешевле
        """
        return self.price < other.price

    def __le__(self, other: 'Product') -> bool:
        """
        @brief Оператор "меньше или равно"
        @param other Другой товар
        @return True если текущий товар дешевле или равен по цене
        """
        return self.price <= other.price

    def __gt__(self, other: 'Product') -> bool:
        """
        @brief Оператор "больше"
        @param other Другой товар
        @return True если текущий товар дороже
        """
        return self.price > other.price

    def __ge__(self, other: 'Product') -> bool:
        """
        @brief Оператор "больше или равно"
        @param other Другой товар
        @return True если текущий товар дороже или равен по цене
        """
        return self.price >= other.price

    def __eq__(self, other: Any) -> bool:
        """
        @brief Оператор равенства
        @param other Другой объект
        @return True если объекты равны
        """
        if not isinstance(other, Product):
            return False
        return (self.name == other.name and
                self.price == other.price and
                self.quantity == other.quantity and
                self.category == other.category)

    def __repr__(self) -> str:
        """
        @brief Строковое представление товара
        @return Строка с информацией о товаре
        """
        return f"Product(name='{self.name}', price={self.price}, qty={self.quantity}, category='{self.category}')"


@dataclass
class Book:
    """
    @class Book
    @brief Класс представляющий книгу
    @details Используется для демонстрации сортировки книг
    """

    title: str  #< Название книги
    author: str  #< Автор книги
    year: int  #< Год издания
    pages: int  #< Количество страниц
    isbn: int  #< ISBN номер

    def __lt__(self, other: 'Book') -> bool:
        """
        @brief Оператор "меньше" для сравнения книг
        @param other Другая книга
        @return True если текущая книга старше (год издания меньше)
        """
        return self.year < other.year

    def __le__(self, other: 'Book') -> bool:
        """
        @brief Оператор "меньше или равно"
        @param other Другая книга
        @return True если текущая книга старше или того же года издания
        """
        return self.year <= other.year

    def __gt__(self, other: 'Book') -> bool:
        """
        @brief Оператор "больше"
        @param other Другая книга
        @return True если текущая книга новее
        """
        return self.year > other.year

    def __ge__(self, other: 'Book') -> bool:
        """
        @brief Оператор "больше или равно"
        @param other Другая книга
        @return True если текущая книга новее или того же года издания
        """
        return self.year >= other.year

    def __eq__(self, other: Any) -> bool:
        """
        @brief Оператор равенства
        @param other Другой объект
        @return True если объекты равны
        """
        if not isinstance(other, Book):
            return False
        return (self.title == other.title and
                self.author == other.author and
                self.year == other.year and
                self.pages == other.pages and
                self.isbn == other.isbn)

    def __repr__(self) -> str:
        """
        @brief Строковое представление книги
        @return Строка с информацией о книге
        """
        return f"Book(title='{self.title}', author='{self.author}', year={self.year}, pages={self.pages}, isbn={self.isbn})"

