"""
Модуль реализует класс многочлена от одной переменной.

Классы:
    Polynomial - класс многочлена от одной переменной

Исключения:
    ValueError - при неверных аргументах
    ZeroDivisionError - при делении на нулевой многочлен
"""

from typing import Union, List, Tuple


class Polynomial:
    """
    Класс многочлена от одной переменной.
    
    Многочлен представляется в виде: a_n*x^n + a_(n-1)*x^(n-1) + ... + a_1*x + a_0
    
    Атрибуты:
        coefficients (List[float]): Список коэффициентов многочлена
        degree (int): Степень многочлена
    """
    
    def __init__(self, coefficients: Union[List[float], Tuple[float, ...]]):
        """
        Инициализирует многочлен.
        
        Args:
            coefficients: Список коэффициентов [a_n, a_(n-1), ..., a_1, a_0]
            
        Raises:
            ValueError: Если coefficients пуст или содержит не числа
            
        Пример:
            >>> poly = Polynomial([1, 2, 3])  # x^2 + 2x + 3
        """
        if not coefficients:
            raise ValueError("Список коэффициентов не может быть пустым")
        
        if not all(isinstance(coef, (int, float)) for coef in coefficients):
            raise ValueError("Все коэффициенты должны быть числами")
        
        # Убираем ведущие нули
        self.coefficients = self._remove_leading_zeros(list(coefficients))
        self.degree = len(self.coefficients) - 1
    
    def _remove_leading_zeros(self, coeffs: List[float]) -> List[float]:
        """Удаляет ведущие нули из списка коэффициентов."""
        if not coeffs:
            return [0.0]
        
        # Находим первый ненулевой коэффициент
        first_non_zero = 0
        while first_non_zero < len(coeffs) and coeffs[first_non_zero] == 0:
            first_non_zero += 1
        
        if first_non_zero == len(coeffs):
            return [0.0]  # Все коэффициенты нулевые
        
        return coeffs[first_non_zero:]
    
    def __getitem__(self, index: int) -> float:
        """
        Возвращает коэффициент при заданной степени.
        
        Args:
            index: Степень (индекс коэффициента)
            
        Returns:
            Коэффициент при степени index
            
        Raises:
            IndexError: Если индекс вне диапазона
            
        Пример:
            >>> poly = Polynomial([1, 2, 3])
            >>> poly[2]  # коэффициент при x^2
            1.0
        """
        if index < 0 or index > self.degree:
            raise IndexError(f"Индекс {index} вне диапазона [0, {self.degree}]")
        
        return self.coefficients[self.degree - index]
    
    def __call__(self, x: float) -> float:
        """
        Вычисляет значение многочлена для заданного аргумента.
        
        Args:
            x: Значение переменной
            
        Returns:
            Значение многочлена в точке x
            
        Пример:
            >>> poly = Polynomial([1, 2, 3])  # x^2 + 2x + 3
            >>> poly(2)  # 1*4 + 2*2 + 3 = 11
            11.0
        """
        result = 0.0
        # Проходим по коэффициентам от старшей степени к младшей
        for i, coef in enumerate(self.coefficients):
            power = self.degree - i  # текущая степень x
            result += coef * (x ** power)
        return result
    
    def __add__(self, other: 'Polynomial') -> 'Polynomial':
        """
        Складывает два многочлена.
        
        Args:
            other: Другой многочлен
            
        Returns:
            Новый многочлен - сумма
            
        Пример:
            >>> p1 = Polynomial([1, 2])   # x + 2
            >>> p2 = Polynomial([1, 1])   # x + 1
            >>> p3 = p1 + p2              # 2x + 3
        """
        if not isinstance(other, Polynomial):
            return NotImplemented
        
        max_degree = max(self.degree, other.degree)
        result_coeffs = [0.0] * (max_degree + 1)
        
        for i in range(self.degree + 1):
            result_coeffs[max_degree - i] += self.coefficients[self.degree - i]
        
        for i in range(other.degree + 1):
            result_coeffs[max_degree - i] += other.coefficients[other.degree - i]
        
        return Polynomial(result_coeffs)
    
    def __iadd__(self, other: 'Polynomial') -> 'Polynomial':
        """
        Добавляет другой многочлен к текущему.
        
        Args:
            other: Другой многочлен
            
        Returns:
            self
            
        Пример:
            >>> p1 = Polynomial([1, 2])
            >>> p2 = Polynomial([1, 1])
            >>> p1 += p2
        """
        if not isinstance(other, Polynomial):
            return NotImplemented
        
        result = self + other
        self.coefficients = result.coefficients
        self.degree = result.degree
        return self
    
    def __sub__(self, other: 'Polynomial') -> 'Polynomial':
        """
        Вычитает другой многочлен из текущего.
        
        Args:
            other: Другой многочлен
            
        Returns:
            Новый многочлен - разность
            
        Пример:
            >>> p1 = Polynomial([1, 2])   # x + 2
            >>> p2 = Polynomial([1, 1])   # x + 1
            >>> p3 = p1 - p2              # 1
        """
        if not isinstance(other, Polynomial):
            return NotImplemented
        
        max_degree = max(self.degree, other.degree)
        result_coeffs = [0.0] * (max_degree + 1)
        
        for i in range(self.degree + 1):
            result_coeffs[max_degree - i] += self.coefficients[self.degree - i]
        
        for i in range(other.degree + 1):
            result_coeffs[max_degree - i] -= other.coefficients[other.degree - i]
        
        return Polynomial(result_coeffs)
    
    def __isub__(self, other: 'Polynomial') -> 'Polynomial':
        """
        Вычитает другой многочлен из текущего.
        
        Args:
            other: Другой многочлен
            
        Returns:
            self
            
        Пример:
            >>> p1 = Polynomial([1, 2])
            >>> p2 = Polynomial([1, 1])
            >>> p1 -= p2
        """
        if not isinstance(other, Polynomial):
            return NotImplemented
        
        result = self - other
        self.coefficients = result.coefficients
        self.degree = result.degree
        return self
    
    def __mul__(self, other: 'Polynomial') -> 'Polynomial':
        """
        Умножает два многочлена.
        
        Args:
            other: Другой многочлен
            
        Returns:
            Новый многочлен - произведение
            
        Пример:
            >>> p1 = Polynomial([1, 2])   # x + 2
            >>> p2 = Polynomial([1, 1])   # x + 1
            >>> p3 = p1 * p2              # x^2 + 3x + 2
        """
        if not isinstance(other, Polynomial):
            return NotImplemented
        
        result_degree = self.degree + other.degree
        result_coeffs = [0.0] * (result_degree + 1)
        
        for i in range(self.degree + 1):
            for j in range(other.degree + 1):
                result_coeffs[result_degree - (i + j)] += (
                    self.coefficients[self.degree - i] * 
                    other.coefficients[other.degree - j]
                )
        
        return Polynomial(result_coeffs)
    
    def __imul__(self, other: 'Polynomial') -> 'Polynomial':
        """
        Умножает текущий многочлен на другой.
        
        Args:
            other: Другой многочлен
            
        Returns:
            self
            
        Пример:
            >>> p1 = Polynomial([1, 2])
            >>> p2 = Polynomial([1, 1])
            >>> p1 *= p2
        """
        if not isinstance(other, Polynomial):
            return NotImplemented
        
        result = self * other
        self.coefficients = result.coefficients
        self.degree = result.degree
        return self
    
    def __truediv__(self, other: 'Polynomial') -> Tuple['Polynomial', 'Polynomial']:
        """
        Делит многочлен на другой многочлен.
        
        Args:
            other: Делитель
            
        Returns:
            Кортеж (частное, остаток)
            
        Raises:
            ZeroDivisionError: Если делитель - нулевой многочлен
            
        Пример:
            >>> p1 = Polynomial([1, 3, 2])  # x^2 + 3x + 2
            >>> p2 = Polynomial([1, 1])     # x + 1
            >>> quotient, remainder = p1 / p2  # (x + 2, 0)
        """
        if not isinstance(other, Polynomial):
            return NotImplemented
        
        if other.is_zero():
            raise ZeroDivisionError("Деление на нулевой многочлен")
        
        if self.degree < other.degree:
            return Polynomial([0]), self
        
        # Алгоритм деления многочленов
        dividend = self.coefficients.copy()
        divisor = other.coefficients
        
        quotient_degree = self.degree - other.degree
        quotient_coeffs = [0.0] * (quotient_degree + 1)
        
        for i in range(quotient_degree + 1):
            # Коэффициент частного
            factor = dividend[i] / divisor[0]
            quotient_coeffs[i] = factor
            
            # Вычитаем
            for j in range(len(divisor)):
                dividend[i + j] -= factor * divisor[j]
        
        # Остаток - это оставшаяся часть делимого
        remainder_coeffs = dividend[quotient_degree + 1:]
        remainder_coeffs = self._remove_leading_zeros(remainder_coeffs)
        
        return Polynomial(quotient_coeffs), Polynomial(remainder_coeffs)
    
    def __itruediv__(self, other: 'Polynomial') -> 'Polynomial':
        """
        Делит текущий многочлен на другой (целочисленное деление).
        
        Args:
            other: Делитель
            
        Returns:
            self (с коэффициентами частного)
            
        Raises:
            ZeroDivisionError: Если делитель - нулевой многочлен
            ValueError: Если деление с остатком
            
        Пример:
            >>> p1 = Polynomial([1, 3, 2])  # x^2 + 3x + 2
            >>> p2 = Polynomial([1, 1])     # x + 1
            >>> p1 /= p2  # p1 становится x + 2
        """
        if not isinstance(other, Polynomial):
            return NotImplemented
        
        quotient, remainder = self / other
        
        if not remainder.is_zero():
            raise ValueError("Деление с остатком не поддерживается для оператора /=")
        
        self.coefficients = quotient.coefficients
        self.degree = quotient.degree
        return self
    
    def is_zero(self) -> bool:
        """
        Проверяет, является ли многочлен нулевым.
        
        Returns:
            True если многочлен нулевой, иначе False
        """
        return len(self.coefficients) == 1 and self.coefficients[0] == 0
    
    def __str__(self) -> str:
        """
        Возвращает строковое представление многочлена.
        
        Returns:
            Строковое представление
            
        Пример:
            >>> poly = Polynomial([1, -2, 3, 0, -1])
            >>> print(poly)  # x^4 - 2x^3 + 3x^2 - 1
        """
        if self.is_zero():
            return "0"
        
        terms = []
        for i in range(self.degree, -1, -1):
            coef = self.coefficients[self.degree - i]
            
            if coef == 0:
                continue
            
            if i == 0:
                terms.append(f"{coef:g}")
            elif i == 1:
                if coef == 1:
                    terms.append("x")
                elif coef == -1:
                    terms.append("-x")
                else:
                    terms.append(f"{coef:g}x")
            else:
                if coef == 1:
                    terms.append(f"x^{i}")
                elif coef == -1:
                    terms.append(f"-x^{i}")
                else:
                    terms.append(f"{coef:g}x^{i}")
        
        # Собираем все члены
        result = terms[0]
        for term in terms[1:]:
            if term.startswith('-'):
                result += f" - {term[1:]}"
            else:
                result += f" + {term}"
        
        return result
    
    def __repr__(self) -> str:
        """
        Возвращает представление многочлена для отладки.
        
        Returns:
            Строковое представление
        """
        return f"Polynomial({self.coefficients})"
    
    def __eq__(self, other: object) -> bool:
        """
        Проверяет равенство многочленов.
        
        Args:
            other: Другой объект
            
        Returns:
            True если многочлены равны, иначе False
        """
        if not isinstance(other, Polynomial):
            return False
        
        return self.coefficients == other.coefficients


def main():
    """Демонстрация работы с многочленами."""
    print("Демонстрация работы с многочленами")
    print("=" * 40)
    
    # Создание многочленов
    p1 = Polynomial([1, -2, 3, -4])  # x^3 - 2x^2 + 3x - 4
    p2 = Polynomial([1, 1])          # x + 1
    
    print(f"p1 = {p1}")
    print(f"p2 = {p2}")
    print(f"Степень p1: {p1.degree}")
    print(f"Степень p2: {p2.degree}")
    
    # Оператор []
    print(f"\nКоэффициенты p1:")
    for i in range(p1.degree + 1):
        print(f"  x^{i}: {p1[i]}")
    
    # Вычисление значения
    x = 2
    print(f"\nЗначение p1 в точке {x}: {p1(x)}")
    print(f"Значение p2 в точке {x}: {p2(x)}")
    
    # Сложение
    p3 = p1 + p2
    print(f"\nСложение: p1 + p2 = {p3}")
    
    # Вычитание
    p4 = p1 - p2
    print(f"Вычитание: p1 - p2 = {p4}")
    
    # Умножение
    p5 = p1 * p2
    print(f"Умножение: p1 * p2 = {p5}")
    
    # Деление
    try:
        quotient, remainder = p1 / p2
        print(f"Деление: p1 / p2 = {quotient} (остаток: {remainder})")
    except ZeroDivisionError as e:
        print(f"Ошибка деления: {e}")


if __name__ == "__main__":
     main()