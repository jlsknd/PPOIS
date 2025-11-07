"""
@file graph.py
@brief Модуль с реализацией неориентированного графа на основе упорядоченных списков рёбер
@details Содержит шаблонный класс графа с полным набором методов и итераторов
"""

from typing import TypeVar, Generic, Optional, List
from dataclasses import dataclass
import copy


T = TypeVar('T')


@dataclass
class Vertex(Generic[T]):
    """
    @class Vertex
    @brief Класс представляющий вершину графа
    @details Хранит значение вершины и её идентификатор
    """

    value: T  #< Значение, хранящееся в вершине
    vertex_id: int  #< Уникальный идентификатор вершины

    def __hash__(self):
        """
        @brief Хэш-функция для использования вершины в множествах и словарях
        @return Хэш вершины
        """
        return hash(self.vertex_id)

    def __eq__(self, other):
        """
        @brief Оператор равенства
        @param other Другая вершина
        @return True если вершины равны
        """
        if not isinstance(other, Vertex):
            return False
        return self.vertex_id == other.vertex_id

    def __repr__(self):
        """
        @brief Строковое представление вершины
        @return Строка с информацией о вершине
        """
        return f"Vertex(id={self.vertex_id}, value={self.value})"

    def __lt__(self, other):
        """
        @brief Оператор "меньше" для сортировки
        @param other Другая вершина
        @return True если текущая вершина меньше другой
        """
        return self.vertex_id < other.vertex_id


@dataclass
class Edge(Generic[T]):
    """
    @class Edge
    @brief Класс представляющий ребро графа
    @details Хранит пару вершин, образующих ребро
    """

    vertex1: Vertex[T]  #< Первая вершина ребра
    vertex2: Vertex[T]  #< Вторая вершина ребра

    def __hash__(self):
        """
        @brief Хэш-функция для использования ребра в множествах
        @return Хэш ребра
        """
        # Для неориентированного графа (a,b) == (b,a)
        return hash(frozenset([self.vertex1.vertex_id, self.vertex2.vertex_id]))

    def __eq__(self, other):
        """
        @brief Оператор равенства
        @param other Другое ребро
        @return True если ребра равны
        """
        if not isinstance(other, Edge):
            return False
        # Для неориентированного графа порядок вершин не важен
        return (self.vertex1 == other.vertex1 and self.vertex2 == other.vertex2) or \
               (self.vertex1 == other.vertex2 and self.vertex2 == other.vertex1)

    def __repr__(self):
        """
        @brief Строковое представление ребра
        @return Строка с информацией о ребре
        """
        return f"Edge({self.vertex1.vertex_id}--{self.vertex2.vertex_id})"

    def __lt__(self, other):
        """
        @brief Оператор "меньше" для сортировки
        @param other Другое ребро
        @return True если текущее ребро меньше другого
        """
        return (min(self.vertex1.vertex_id, self.vertex2.vertex_id),
                max(self.vertex1.vertex_id, self.vertex2.vertex_id)) < \
               (min(other.vertex1.vertex_id, other.vertex2.vertex_id),
                max(other.vertex1.vertex_id, other.vertex2.vertex_id))

    def contains_vertex(self, vertex: Vertex[T]) -> bool:
        """
        @brief Проверяет, содержит ли ребро указанную вершину
        @param vertex Вершина для проверки
        @return True если ребро содержит вершину
        """
        return self.vertex1 == vertex or self.vertex2 == vertex

    def get_other_vertex(self, vertex: Vertex[T]) -> Optional[Vertex[T]]:
        """
        @brief Получает другую вершину ребра
        @param vertex Известная вершина
        @return Другая вершина ребра или None
        """
        if self.vertex1 == vertex:
            return self.vertex2
        elif self.vertex2 == vertex:
            return self.vertex1
        return None


class GraphException(Exception):
    """
    @class GraphException
    @brief Базовое исключение для ошибок графа
    """
    pass


class VertexNotFoundException(GraphException):
    """
    @class VertexNotFoundException
    @brief Исключение для случая, когда вершина не найдена
    """
    pass


class EdgeNotFoundException(GraphException):
    """
    @class EdgeNotFoundException
    @brief Исключение для случая, когда ребро не найдено
    """
    pass


class VertexAlreadyExistsException(GraphException):
    """
    @class VertexAlreadyExistsException
    @brief Исключение для случая, когда вершина уже существует
    """
    pass


class EdgeAlreadyExistsException(GraphException):
    """
    @class EdgeAlreadyExistsException
    @brief Исключение для случая, когда ребро уже существует
    """
    pass


class UndirectedGraph(Generic[T]):
    """
    @class UndirectedGraph
    @brief Шаблонный класс неориентированного графа на основе упорядоченных списков рёбер
    @details Представляет неориентированный граф с возможностью хранения значений в вершинах

    Класс предоставляет:
    - Добавление/удаление вершин и ребер
    - Проверку наличия вершин и ребер
    - Итераторы для обхода вершин, ребер, смежных вершин
    - Операторы сравнения
    """

    # Type definitions
    value_type = T
    reference = T
    const_reference = T
    pointer = Optional[T]
    size_type = int

    def __init__(self):
        """
        @brief Конструктор по умолчанию
        @details Создает пустой граф
        """
        self._vertices: List[Vertex[T]] = []  # Список вершин
        self._edges: List[Edge[T]] = []  # Упорядоченный список рёбер
        self._next_vertex_id = 0

    def __copy__(self):
        """
        @brief Конструктор копирования (мелкое копирование)
        @return Копия графа
        """
        new_graph = UndirectedGraph[T]()
        new_graph._vertices = self._vertices.copy()
        new_graph._edges = self._edges.copy()
        new_graph._next_vertex_id = self._next_vertex_id
        return new_graph

    def __deepcopy__(self, memo):
        """
        @brief Глубокое копирование
        @param memo Словарь для отслеживания уже скопированных объектов
        @return Глубокая копия графа
        """
        new_graph = UndirectedGraph[T]()
        new_graph._vertices = copy.deepcopy(self._vertices, memo)
        new_graph._edges = copy.deepcopy(self._edges, memo)
        new_graph._next_vertex_id = self._next_vertex_id
        return new_graph

    def __del__(self):
        """
        @brief Деструктор
        @details Очищает все ресурсы графа
        """
        self.clear()

    def empty(self) -> bool:
        """
        @brief Проверяет, пуст ли граф
        @return True если граф не содержит вершин
        """
        return len(self._vertices) == 0

    def clear(self):
        """
        @brief Очищает граф
        @details Удаляет все вершины и ребра
        """
        self._vertices.clear()
        self._edges.clear()
        self._next_vertex_id = 0

    def __eq__(self, other) -> bool:
        """
        @brief Оператор равенства
        @param other Другой граф
        @return True если графы равны
        """
        if not isinstance(other, UndirectedGraph):
            return False

        if len(self._vertices) != len(other._vertices):
            return False

        # Сравниваем вершины
        for v1, v2 in zip(sorted(self._vertices), sorted(other._vertices)):
            if v1.value != v2.value:
                return False

        # Сравниваем ребра
        return sorted(self._edges) == sorted(other._edges)

    def __ne__(self, other) -> bool:
        """
        @brief Оператор неравенства
        @param other Другой граф
        @return True если графы не равны
        """
        return not self.__eq__(other)

    def __lt__(self, other) -> bool:
        """
        @brief Оператор "меньше"
        @param other Другой граф
        @return True если текущий граф меньше другого (по количеству вершин)
        """
        if not isinstance(other, UndirectedGraph):
            return NotImplemented
        return len(self._vertices) < len(other._vertices)

    def __le__(self, other) -> bool:
        """
        @brief Оператор "меньше или равно"
        @param other Другой граф
        @return True если текущий граф меньше или равен другому
        """
        return self.__eq__(other) or self.__lt__(other)

    def __gt__(self, other) -> bool:
        """
        @brief Оператор "больше"
        @param other Другой граф
        @return True если текущий граф больше другого
        """
        if not isinstance(other, UndirectedGraph):
            return NotImplemented
        return len(self._vertices) > len(other._vertices)

    def __ge__(self, other) -> bool:
        """
        @brief Оператор "больше или равно"
        @param other Другой граф
        @return True если текущий граф больше или равен другому
        """
        return self.__eq__(other) or self.__gt__(other)

    def __assign__(self, other):
        """
        @brief Оператор присваивания
        @param other Другой граф
        @return self
        """
        if self is other:
            return self

        self._vertices = copy.deepcopy(other._vertices)
        self._edges = copy.deepcopy(other._edges)
        self._next_vertex_id = other._next_vertex_id
        return self

    def has_vertex(self, vertex: Vertex[T]) -> bool:
        """
        @brief Проверяет присутствие вершины в графе
        @param vertex Вершина для проверки
        @return True если вершина присутствует в графе
        """
        return vertex in self._vertices

    def has_edge(self, vertex1: Vertex[T], vertex2: Vertex[T]) -> bool:
        """
        @brief Проверяет присутствие ребра между вершинами
        @param vertex1 Первая вершина
        @param vertex2 Вторая вершина
        @return True если ребро присутствует
        @throws VertexNotFoundException если одна из вершин не найдена
        """
        if not self.has_vertex(vertex1) or not self.has_vertex(vertex2):
            raise VertexNotFoundException("Одна или обе вершины не найдены в графе")

        edge = Edge(vertex1, vertex2)
        return edge in self._edges

    def vertex_count(self) -> int:
        """
        @brief Получает количество вершин в графе
        @return Количество вершин
        """
        return len(self._vertices)

    def edge_count(self) -> int:
        """
        @brief Получает количество ребер в графе
        @return Количество ребер
        """
        return len(self._edges)

    def vertex_degree(self, vertex: Vertex[T]) -> int:
        """
        @brief Вычисляет степень вершины
        @param vertex Вершина
        @return Степень вершины (количество инцидентных ребер)
        @throws VertexNotFoundException если вершина не найдена
        """
        if not self.has_vertex(vertex):
            raise VertexNotFoundException(f"Вершина {vertex} не найдена в графе")

        degree = 0
        for edge in self._edges:
            if edge.contains_vertex(vertex):
                degree += 1
        return degree

    def edge_degree(self, vertex1: Vertex[T], vertex2: Vertex[T]) -> int:
        """
        @brief Вычисляет степень ребра (сумма степеней его вершин минус 2)
        @param vertex1 Первая вершина
        @param vertex2 Вторая вершина
        @return Степень ребра
        @throws EdgeNotFoundException если ребро не найдено
        """
        if not self.has_edge(vertex1, vertex2):
            raise EdgeNotFoundException(f"Ребро между {vertex1} и {vertex2} не найдено")

        return self.vertex_degree(vertex1) + self.vertex_degree(vertex2) - 2

    def add_vertex(self, value: T) -> Vertex[T]:
        """
        @brief Добавляет вершину в граф
        @param value Значение для хранения в вершине
        @return Созданная вершина
        """
        vertex = Vertex(value, self._next_vertex_id)
        self._next_vertex_id += 1
        self._vertices.append(vertex)
        # Поддерживаем упорядоченность списка вершин
        self._vertices.sort()
        return vertex

    def add_edge(self, vertex1: Vertex[T], vertex2: Vertex[T]) -> Edge[T]:
        """
        @brief Добавляет ребро между вершинами
        @param vertex1 Первая вершина
        @param vertex2 Вторая вершина
        @return Созданное ребро
        @throws VertexNotFoundException если одна из вершин не найдена
        @throws EdgeAlreadyExistsException если ребро уже существует
        """
        if not self.has_vertex(vertex1) or not self.has_vertex(vertex2):
            raise VertexNotFoundException("Одна или обе вершины не найдены в графе")

        if vertex1 == vertex2:
            raise GraphException("Петли не поддерживаются")

        edge = Edge(vertex1, vertex2)
        if edge in self._edges:
            raise EdgeAlreadyExistsException(
                f"Ребро между {vertex1} и {vertex2} уже существует"
            )

        self._edges.append(edge)
        # Поддерживаем упорядоченность списка рёбер
        self._edges.sort()
        return edge

    def remove_vertex(self, vertex: Vertex[T]):
        """
        @brief Удаляет вершину из графа
        @param vertex Вершина для удаления
        @throws VertexNotFoundException если вершина не найдена
        """
        if not self.has_vertex(vertex):
            raise VertexNotFoundException(f"Вершина {vertex} не найдена в графе")

        # Удаляем все рёбра, инцидентные этой вершине
        self._edges = [edge for edge in self._edges if not edge.contains_vertex(vertex)]

        # Удаляем саму вершину
        self._vertices.remove(vertex)

    def remove_edge(self, vertex1: Vertex[T], vertex2: Vertex[T]):
        """
        @brief Удаляет ребро между вершинами
        @param vertex1 Первая вершина
        @param vertex2 Вторая вершина
        @throws EdgeNotFoundException если ребро не найдено
        """
        edge = Edge(vertex1, vertex2)
        if edge not in self._edges:
            raise EdgeNotFoundException(
                f"Ребро между {vertex1} и {vertex2} не найдено"
            )

        self._edges.remove(edge)

    def remove_vertex_by_iterator(self, vertex_iter: 'VertexIterator'):
        """
        @brief Удаляет вершину по итератору
        @param vertex_iter Итератор на вершину
        """
        vertex = vertex_iter.current()
        self.remove_vertex(vertex)

    def remove_edge_by_iterator(self, edge_iter: 'EdgeIterator'):
        """
        @brief Удаляет ребро по итератору
        @param edge_iter Итератор на ребро
        """
        edge = edge_iter.current()
        self.remove_edge(edge.vertex1, edge.vertex2)

    def get_adjacent_vertices(self, vertex: Vertex[T]) -> List[Vertex[T]]:
        """
        @brief Получает список смежных вершин
        @param vertex Вершина
        @return Упорядоченный список смежных вершин
        @throws VertexNotFoundException если вершина не найдена
        """
        if not self.has_vertex(vertex):
            raise VertexNotFoundException(f"Вершина {vertex} не найдена в графе")

        adjacent = []
        for edge in self._edges:
            other = edge.get_other_vertex(vertex)
            if other is not None:
                adjacent.append(other)

        # Возвращаем упорядоченный список
        return sorted(adjacent)

    def get_incident_edges(self, vertex: Vertex[T]) -> List[Edge[T]]:
        """
        @brief Получает список инцидентных ребер
        @param vertex Вершина
        @return Упорядоченный список инцидентных ребер
        @throws VertexNotFoundException если вершина не найдена
        """
        if not self.has_vertex(vertex):
            raise VertexNotFoundException(f"Вершина {vertex} не найдена в графе")

        incident = [edge for edge in self._edges if edge.contains_vertex(vertex)]
        return sorted(incident)

    # Методы для создания итераторов
    def vertices_begin(self) -> 'VertexIterator':
        """
        @brief Создает итератор на начало списка вершин
        @return Итератор вершин
        """
        return VertexIterator(self, 0)

    def vertices_end(self) -> 'VertexIterator':
        """
        @brief Создает итератор на конец списка вершин
        @return Итератор вершин
        """
        return VertexIterator(self, len(self._vertices))

    def vertices_rbegin(self) -> 'ReverseVertexIterator':
        """
        @brief Создает обратный итератор на конец списка вершин
        @return Обратный итератор вершин
        """
        return ReverseVertexIterator(self, len(self._vertices) - 1)

    def vertices_rend(self) -> 'ReverseVertexIterator':
        """
        @brief Создает обратный итератор на начало списка вершин
        @return Обратный итератор вершин
        """
        return ReverseVertexIterator(self, -1)

    def edges_begin(self) -> 'EdgeIterator':
        """
        @brief Создает итератор на начало списка ребер
        @return Итератор ребер
        """
        return EdgeIterator(self, 0)

    def edges_end(self) -> 'EdgeIterator':
        """
        @brief Создает итератор на конец списка ребер
        @return Итератор ребер
        """
        return EdgeIterator(self, len(self._edges))

    def edges_rbegin(self) -> 'ReverseEdgeIterator':
        """
        @brief Создает обратный итератор на конец списка ребер
        @return Обратный итератор ребер
        """
        return ReverseEdgeIterator(self, len(self._edges) - 1)

    def edges_rend(self) -> 'ReverseEdgeIterator':
        """
        @brief Создает обратный итератор на начало списка ребер
        @return Обратный итератор ребер
        """
        return ReverseEdgeIterator(self, -1)

    def adjacent_vertices_begin(self, vertex: Vertex[T]) -> 'AdjacentVertexIterator':
        """
        @brief Создает итератор на начало списка смежных вершин
        @param vertex Вершина
        @return Итератор смежных вершин
        """
        return AdjacentVertexIterator(self, vertex, 0)

    def adjacent_vertices_end(self, vertex: Vertex[T]) -> 'AdjacentVertexIterator':
        """
        @brief Создает итератор на конец списка смежных вершин
        @param vertex Вершина
        @return Итератор смежных вершин
        """
        adjacent = self.get_adjacent_vertices(vertex)
        return AdjacentVertexIterator(self, vertex, len(adjacent))

    def incident_edges_begin(self, vertex: Vertex[T]) -> 'IncidentEdgeIterator':
        """
        @brief Создает итератор на начало списка инцидентных ребер
        @param vertex Вершина
        @return Итератор инцидентных ребер
        """
        return IncidentEdgeIterator(self, vertex, 0)

    def incident_edges_end(self, vertex: Vertex[T]) -> 'IncidentEdgeIterator':
        """
        @brief Создает итератор на конец списка инцидентных ребер
        @param vertex Вершина
        @return Итератор инцидентных ребер
        """
        edges = self.get_incident_edges(vertex)
        return IncidentEdgeIterator(self, vertex, len(edges))

    def __repr__(self):
        """
        @brief Строковое представление графа
        @return Строка с информацией о графе
        """
        return f"UndirectedGraph(vertices={len(self._vertices)}, edges={self.edge_count()})"

    def __str__(self):
        """
        @brief Преобразование графа в строку для вывода
        @return Строковое представление
        """
        result = []
        result.append(f"Граф: {len(self._vertices)} вершин, {self.edge_count()} ребер")
        result.append("Вершины: " + ", ".join(str(v) for v in self._vertices))

        edges = []
        it = self.edges_begin()
        end = self.edges_end()
        while it != end:
            edges.append(str(it.current()))
            it.next()
        result.append("Ребра: " + ", ".join(edges) if edges else "Ребра: нет")

        return "\n".join(result)



# Классы итераторов



class VertexIterator(Generic[T]):
    """
    @class VertexIterator
    @brief Двунаправленный итератор для перебора вершин
    """

    def __init__(self, graph: UndirectedGraph[T], position: int):
        """
        @brief Конструктор итератора
        @param graph Граф
        @param position Текущая позиция
        """
        self._graph = graph
        self._position = position

    def current(self) -> Vertex[T]:
        """
        @brief Получает текущую вершину
        @return Текущая вершина
        @throws IndexError если итератор вышел за пределы
        """
        if self._position < 0 or self._position >= len(self._graph._vertices):
            raise IndexError("Итератор вышел за пределы")
        return self._graph._vertices[self._position]

    def next(self):
        """
        @brief Переходит к следующей вершине
        @return self
        """
        self._position += 1
        return self

    def prev(self):
        """
        @brief Переходит к предыдущей вершине
        @return self
        """
        self._position -= 1
        return self

    def __eq__(self, other) -> bool:
        """
        @brief Оператор равенства
        @param other Другой итератор
        @return True если итераторы равны
        """
        return (isinstance(other, VertexIterator) and
                self._graph is other._graph and
                self._position == other._position)

    def __ne__(self, other) -> bool:
        """
        @brief Оператор неравенства
        @param other Другой итератор
        @return True если итераторы не равны
        """
        return not self.__eq__(other)

    def __iter__(self):
        """
        @brief Возвращает итератор
        @return self
        """
        return self

    def __next__(self) -> Vertex[T]:
        """
        @brief Переходит к следующему элементу (для использования в циклах)
        @return Следующая вершина
        """
        if self._position >= len(self._graph._vertices):
            raise StopIteration
        vertex = self.current()
        self.next()
        return vertex


class ReverseVertexIterator(Generic[T]):
    """
    @class ReverseVertexIterator
    @brief Обратный двунаправленный итератор для перебора вершин
    """

    def __init__(self, graph: UndirectedGraph[T], position: int):
        """
        @brief Конструктор обратного итератора
        @param graph Граф
        @param position Текущая позиция
        """
        self._graph = graph
        self._position = position

    def current(self) -> Vertex[T]:
        """
        @brief Получает текущую вершину
        @return Текущая вершина
        """
        if self._position < 0 or self._position >= len(self._graph._vertices):
            raise IndexError("Итератор вышел за пределы")
        return self._graph._vertices[self._position]

    def next(self):
        """
        @brief Переходит к предыдущей вершине (в обратном направлении)
        @return self
        """
        self._position -= 1
        return self

    def prev(self):
        """
        @brief Переходит к следующей вершине (в обратном направлении)
        @return self
        """
        self._position += 1
        return self

    def __eq__(self, other) -> bool:
        """Оператор равенства"""
        return (isinstance(other, ReverseVertexIterator) and
                self._graph is other._graph and
                self._position == other._position)

    def __ne__(self, other) -> bool:
        """Оператор неравенства"""
        return not self.__eq__(other)


class EdgeIterator(Generic[T]):
    """
    @class EdgeIterator
    @brief Двунаправленный итератор для перебора ребер
    """

    def __init__(self, graph: UndirectedGraph[T], position: int):
        """
        @brief Конструктор итератора ребер
        @param graph Граф
        @param position Текущая позиция в списке рёбер
        """
        self._graph = graph
        self._position = position

    def current(self) -> Edge[T]:
        """
        @brief Получает текущее ребро
        @return Текущее ребро
        """
        if self._position < 0 or self._position >= len(self._graph._edges):
            raise IndexError("Итератор вышел за пределы")
        return self._graph._edges[self._position]

    def next(self):
        """
        @brief Переходит к следующему ребру
        @return self
        """
        self._position += 1
        return self

    def prev(self):
        """
        @brief Переходит к предыдущему ребру
        @return self
        """
        self._position -= 1
        return self

    def __eq__(self, other) -> bool:
        """Оператор равенства"""
        return (isinstance(other, EdgeIterator) and
                self._graph is other._graph and
                self._position == other._position)

    def __ne__(self, other) -> bool:
        """Оператор неравенства"""
        return not self.__eq__(other)

    def __iter__(self):
        """Возвращает итератор"""
        return self

    def __next__(self) -> Edge[T]:
        """Переходит к следующему элементу"""
        if self._position >= len(self._graph._edges):
            raise StopIteration
        edge = self.current()
        self.next()
        return edge


class ReverseEdgeIterator(Generic[T]):
    """
    @class ReverseEdgeIterator
    @brief Обратный двунаправленный итератор для перебора ребер
    """

    def __init__(self, graph: UndirectedGraph[T], position: int):
        """
        @brief Конструктор обратного итератора ребер
        @param graph Граф
        @param position Текущая позиция
        """
        self._graph = graph
        self._position = position

    def current(self) -> Edge[T]:
        """Получает текущее ребро"""
        if self._position < 0 or self._position >= len(self._graph._edges):
            raise IndexError("Итератор вышел за пределы")
        return self._graph._edges[self._position]

    def next(self):
        """Переходит к следующему ребру (в обратном направлении)"""
        self._position -= 1
        return self

    def prev(self):
        """Переходит к предыдущему ребру (в обратном направлении)"""
        self._position += 1
        return self

    def __eq__(self, other) -> bool:
        """Оператор равенства"""
        return (isinstance(other, ReverseEdgeIterator) and
                self._graph is other._graph and
                self._position == other._position)

    def __ne__(self, other) -> bool:
        """Оператор неравенства"""
        return not self.__eq__(other)


class AdjacentVertexIterator(Generic[T]):
    """
    @class AdjacentVertexIterator
    @brief Двунаправленный итератор для перебора смежных вершин
    """

    def __init__(self, graph: UndirectedGraph[T], vertex: Vertex[T], position: int):
        """
        @brief Конструктор итератора смежных вершин
        @param graph Граф
        @param vertex Вершина, для которой ищутся смежные
        @param position Текущая позиция
        """
        self._graph = graph
        self._vertex = vertex
        self._adjacent_vertices = graph.get_adjacent_vertices(vertex)
        self._position = position

    def current(self) -> Vertex[T]:
        """Получает текущую смежную вершину"""
        if self._position < 0 or self._position >= len(self._adjacent_vertices):
            raise IndexError("Итератор вышел за пределы")
        return self._adjacent_vertices[self._position]

    def next(self):
        """Переходит к следующей смежной вершине"""
        self._position += 1
        return self

    def prev(self):
        """Переходит к предыдущей смежной вершине"""
        self._position -= 1
        return self

    def __eq__(self, other) -> bool:
        """Оператор равенства"""
        return (isinstance(other, AdjacentVertexIterator) and
                self._graph is other._graph and
                self._vertex == other._vertex and
                self._position == other._position)

    def __ne__(self, other) -> bool:
        """Оператор неравенства"""
        return not self.__eq__(other)

    def __iter__(self):
        """Возвращает итератор"""
        return self

    def __next__(self) -> Vertex[T]:
        """Переходит к следующему элементу"""
        if self._position >= len(self._adjacent_vertices):
            raise StopIteration
        vertex = self.current()
        self.next()
        return vertex


class IncidentEdgeIterator(Generic[T]):
    """
    @class IncidentEdgeIterator
    @brief Двунаправленный итератор для перебора инцидентных ребер
    """

    def __init__(self, graph: UndirectedGraph[T], vertex: Vertex[T], position: int):
        """
        @brief Конструктор итератора инцидентных ребер
        @param graph Граф
        @param vertex Вершина, для которой ищутся инцидентные ребра
        @param position Текущая позиция
        """
        self._graph = graph
        self._vertex = vertex
        self._incident_edges = graph.get_incident_edges(vertex)
        self._position = position

    def current(self) -> Edge[T]:
        """Получает текущее инцидентное ребро"""
        if self._position < 0 or self._position >= len(self._incident_edges):
            raise IndexError("Итератор вышел за пределы")
        return self._incident_edges[self._position]

    def next(self):
        """Переходит к следующему инцидентному ребру"""
        self._position += 1
        return self

    def prev(self):
        """Переходит к предыдущему инцидентному ребру"""
        self._position -= 1
        return self

    def __eq__(self, other) -> bool:
        """Оператор равенства"""
        return (isinstance(other, IncidentEdgeIterator) and
                self._graph is other._graph and
                self._vertex == other._vertex and
                self._position == other._position)

    def __ne__(self, other) -> bool:
        """Оператор неравенства"""
        return not self.__eq__(other)

    def __iter__(self):
        """Возвращает итератор"""
        return self

    def __next__(self) -> Edge[T]:
        """Переходит к следующему элементу"""
        if self._position >= len(self._incident_edges):
            raise StopIteration
        edge = self.current()
        self.next()
        return edge



# Оператор вывода


def print_graph(graph: UndirectedGraph[T], stream=None):
    """
    @brief Выводит граф в поток
    @param graph Граф для вывода
    @param stream Поток вывода (по умолчанию stdout)
    """
    import sys
    if stream is None:
        stream = sys.stdout

    def print_vertex(vertex: Vertex):
        stream.write(f"{vertex.value} ")

    stream.write("Вершины: ")

    # Используем std::for_each аналог
    it = graph.vertices_begin()
    end = graph.vertices_end()
    vertices = []
    while it != end:
        vertices.append(it.current())
        it.next()

    for vertex in vertices:
        print_vertex(vertex)

    stream.write("\n")


