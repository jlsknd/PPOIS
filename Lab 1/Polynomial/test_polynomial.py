import unittest
from polynomial import Polynomial


class TestPolynomial(unittest.TestCase):
    """Тесты для класса Polynomial."""
    
    def test_initialization(self):
        """Тест инициализации многочлена."""
        # Нормальная инициализация
        p = Polynomial([1, 2, 3])
        self.assertEqual(p.coefficients, [1, 2, 3])
        self.assertEqual(p.degree, 2)
        
        # Удаление ведущих нулей
        p = Polynomial([0, 0, 1, 2])
        self.assertEqual(p.coefficients, [1, 2])
        self.assertEqual(p.degree, 1)
        
        # Нулевой многочлен
        p = Polynomial([0, 0, 0])
        self.assertEqual(p.coefficients, [0.0])
        self.assertEqual(p.degree, 0)
    
    def test_initialization_errors(self):
        """Тест ошибок инициализации."""
        with self.assertRaises(ValueError):
            Polynomial([])
        
        with self.assertRaises(ValueError):
            Polynomial([1, "2", 3])
    
    def test_getitem(self):
        """Тест оператора []."""
        p = Polynomial([1, 2, 3])  # x^2 + 2x + 3
        
        self.assertEqual(p[0], 3)  # свободный член
        self.assertEqual(p[1], 2)  # коэффициент при x
        self.assertEqual(p[2], 1)  # коэффициент при x^2
        
        with self.assertRaises(IndexError):
            _ = p[3]
        
        with self.assertRaises(IndexError):
            _ = p[-1]
    
    def test_call(self):
        """Тест вычисления значения многочлена."""
        p = Polynomial([1, 2, 3])  # x^2 + 2x + 3
        
        self.assertEqual(p(0), 3)
        self.assertEqual(p(1), 6)
        self.assertEqual(p(2), 11)
        self.assertEqual(p(-1), 2)
    
    def test_addition(self):
        """Тест сложения многочленов."""
        p1 = Polynomial([1, 2])    # x + 2
        p2 = Polynomial([1, 1])    # x + 1
        
        result = p1 + p2           # 2x + 3
        self.assertEqual(result.coefficients, [2, 3])
        
        # Сложение с нулевым многочленом
        zero = Polynomial([0])
        self.assertEqual((p1 + zero).coefficients, p1.coefficients)
    
    def test_inplace_addition(self):
        """Тест оператора +=."""
        p1 = Polynomial([1, 2])
        p2 = Polynomial([1, 1])
        
        p1 += p2
        self.assertEqual(p1.coefficients, [2, 3])
    
    def test_subtraction(self):
        """Тест вычитания многочленов."""
        p1 = Polynomial([1, 2])    # x + 2
        p2 = Polynomial([1, 1])    # x + 1
        
        result = p1 - p2           # 1
        self.assertEqual(result.coefficients, [1])
        
        # Вычитание самого себя
        result = p1 - p1
        self.assertEqual(result.coefficients, [0.0])
    
    def test_inplace_subtraction(self):
        """Тест оператора -=."""
        p1 = Polynomial([1, 2])
        p2 = Polynomial([1, 1])
        
        p1 -= p2
        self.assertEqual(p1.coefficients, [1])
    
    def test_multiplication(self):
        """Тест умножения многочленов."""
        p1 = Polynomial([1, 2])    # x + 2
        p2 = Polynomial([1, 1])    # x + 1
        
        result = p1 * p2           # x^2 + 3x + 2
        self.assertEqual(result.coefficients, [1, 3, 2])
        
        # Умножение на нулевой многочлен
        zero = Polynomial([0])
        result = p1 * zero
        self.assertEqual(result.coefficients, [0.0])
    
    def test_inplace_multiplication(self):
        """Тест оператора *=."""
        p1 = Polynomial([1, 2])
        p2 = Polynomial([1, 1])
        
        p1 *= p2
        self.assertEqual(p1.coefficients, [1, 3, 2])
    
    def test_division(self):
        """Тест деления многочленов."""
        # Деление без остатка
        p1 = Polynomial([1, 3, 2])  # x^2 + 3x + 2
        p2 = Polynomial([1, 1])     # x + 1
        
        quotient, remainder = p1 / p2
        self.assertEqual(quotient.coefficients, [1, 2])  # x + 2
        self.assertEqual(remainder.coefficients, [0.0])  # 0
        
        # Деление с остатком
        p1 = Polynomial([1, 0, 1])  # x^2 + 1
        p2 = Polynomial([1, 1])     # x + 1
        
        quotient, remainder = p1 / p2
        self.assertEqual(quotient.coefficients, [1, -1])  # x - 1
        self.assertEqual(remainder.coefficients, [2])     # 2
    
    def test_division_errors(self):
        """Тест ошибок деления."""
        p1 = Polynomial([1, 2, 3])
        zero = Polynomial([0])
        
        with self.assertRaises(ZeroDivisionError):
            _ = p1 / zero
    
    def test_inplace_division(self):
        """Тест оператора /=."""
        # Деление без остатка
        p1 = Polynomial([1, 3, 2])  # x^2 + 3x + 2
        p2 = Polynomial([1, 1])     # x + 1
        
        p1 /= p2
        self.assertEqual(p1.coefficients, [1, 2])  # x + 2
        
        # Деление с остатком должно вызывать ошибку
        p1 = Polynomial([1, 0, 1])  # x^2 + 1
        p2 = Polynomial([1, 1])     # x + 1
        
        with self.assertRaises(ValueError):
            p1 /= p2
    
    def test_is_zero(self):
        """Тест проверки нулевого многочлена."""
        zero = Polynomial([0, 0, 0])
        non_zero = Polynomial([1, 2, 3])
        
        self.assertTrue(zero.is_zero())
        self.assertFalse(non_zero.is_zero())
    
    def test_string_representation(self):
        """Тест строкового представления."""
        p = Polynomial([1, -2, 3, 0, -1])  # x^4 - 2x^3 + 3x^2 - 1
        self.assertEqual(str(p), "x^4 - 2x^3 + 3x^2 - 1")
        
        zero = Polynomial([0])
        self.assertEqual(str(zero), "0")
        
        p = Polynomial([1, 1])  # x + 1
        self.assertEqual(str(p), "x + 1")
    
    def test_equality(self):
        """Тест оператора равенства."""
        p1 = Polynomial([1, 2, 3])
        p2 = Polynomial([1, 2, 3])
        p3 = Polynomial([1, 2, 4])
        
        self.assertEqual(p1, p2)
        self.assertNotEqual(p1, p3)
        self.assertNotEqual(p1, "not a polynomial")


if __name__ == '__main__':
    unittest.main()