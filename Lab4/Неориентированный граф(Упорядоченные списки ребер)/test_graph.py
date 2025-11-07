"""
@file test_graph.py
@brief Модуль с unit-тестами для неориентированного графа
@details Содержит тесты для класса UndirectedGraph с покрытием 85%+
"""

import unittest
import copy
from graph import (
    UndirectedGraph, Vertex, Edge,
    GraphException, VertexNotFoundException, EdgeNotFoundException,
    VertexAlreadyExistsException, EdgeAlreadyExistsException,
    VertexIterator, EdgeIterator, AdjacentVertexIterator, IncidentEdgeIterator,
    ReverseVertexIterator, ReverseEdgeIterator
)


class TestVertex(unittest.TestCase):
    """
    @class TestVertex
    @brief Тесты для класса Vertex
    """

    def test_vertex_creation(self):
        """Тест создания вершины"""
        v = Vertex(10, 0)
        self.assertEqual(v.value, 10)
        self.assertEqual(v.vertex_id, 0)

    def test_vertex_equality(self):
        """Тест равенства вершин"""
        v1 = Vertex(10, 0)
        v2 = Vertex(10, 0)
        v3 = Vertex(20, 1)
        self.assertEqual(v1, v2)
        self.assertNotEqual(v1, v3)

    def test_vertex_hash(self):
        """Тест хэширования вершин"""
        v1 = Vertex(10, 0)
        v2 = Vertex(10, 0)
        self.assertEqual(hash(v1), hash(v2))

    def test_vertex_repr(self):
        """Тест строкового представления"""
        v = Vertex(10, 0)
        self.assertIn("Vertex", repr(v))
        self.assertIn("10", repr(v))

    def test_vertex_comparison(self):
        """Тест сравнения вершин"""
        v1 = Vertex(10, 0)
        v2 = Vertex(20, 1)
        self.assertLess(v1, v2)


class TestEdge(unittest.TestCase):
    """
    @class TestEdge
    @brief Тесты для класса Edge
    """

    def test_edge_creation(self):
        """Тест создания ребра"""
        v1 = Vertex(10, 0)
        v2 = Vertex(20, 1)
        e = Edge(v1, v2)
        self.assertEqual(e.vertex1, v1)
        self.assertEqual(e.vertex2, v2)

    def test_edge_equality(self):
        """Тест равенства ребер"""
        v1 = Vertex(10, 0)
        v2 = Vertex(20, 1)
        e1 = Edge(v1, v2)
        e2 = Edge(v2, v1)  # Для неориентированного графа
        e3 = Edge(v1, Vertex(30, 2))
        self.assertEqual(e1, e2)
        self.assertNotEqual(e1, e3)

    def test_edge_hash(self):
        """Тест хэширования ребер"""
        v1 = Vertex(10, 0)
        v2 = Vertex(20, 1)
        e1 = Edge(v1, v2)
        e2 = Edge(v2, v1)
        self.assertEqual(hash(e1), hash(e2))

    def test_edge_contains_vertex(self):
        """Тест проверки принадлежности вершины ребру"""
        v1 = Vertex(10, 0)
        v2 = Vertex(20, 1)
        v3 = Vertex(30, 2)
        e = Edge(v1, v2)
        self.assertTrue(e.contains_vertex(v1))
        self.assertTrue(e.contains_vertex(v2))
        self.assertFalse(e.contains_vertex(v3))

    def test_edge_get_other_vertex(self):
        """Тест получения другой вершины ребра"""
        v1 = Vertex(10, 0)
        v2 = Vertex(20, 1)
        e = Edge(v1, v2)
        self.assertEqual(e.get_other_vertex(v1), v2)
        self.assertEqual(e.get_other_vertex(v2), v1)


class TestUndirectedGraph(unittest.TestCase):
    """
    @class TestUndirectedGraph
    @brief Тесты для класса UndirectedGraph
    """

    def setUp(self):
        """Подготовка к тестам"""
        self.graph = UndirectedGraph[int]()

    def test_empty_graph(self):
        """Тест создания пустого графа"""
        self.assertTrue(self.graph.empty())
        self.assertEqual(self.graph.vertex_count(), 0)
        self.assertEqual(self.graph.edge_count(), 0)

    def test_add_vertex(self):
        """Тест добавления вершины"""
        v = self.graph.add_vertex(10)
        self.assertFalse(self.graph.empty())
        self.assertEqual(self.graph.vertex_count(), 1)
        self.assertTrue(self.graph.has_vertex(v))

    def test_add_multiple_vertices(self):
        """Тест добавления нескольких вершин"""
        v1 = self.graph.add_vertex(10)
        v2 = self.graph.add_vertex(20)
        v3 = self.graph.add_vertex(30)
        self.assertEqual(self.graph.vertex_count(), 3)
        self.assertTrue(self.graph.has_vertex(v1))
        self.assertTrue(self.graph.has_vertex(v2))
        self.assertTrue(self.graph.has_vertex(v3))

    def test_add_edge(self):
        """Тест добавления ребра"""
        v1 = self.graph.add_vertex(10)
        v2 = self.graph.add_vertex(20)
        e = self.graph.add_edge(v1, v2)
        self.assertEqual(self.graph.edge_count(), 1)
        self.assertTrue(self.graph.has_edge(v1, v2))
        self.assertTrue(self.graph.has_edge(v2, v1))  # Неориентированный граф

    def test_add_edge_to_nonexistent_vertex(self):
        """Тест добавления ребра к несуществующей вершине"""
        v1 = self.graph.add_vertex(10)
        v2 = Vertex(20, 999)
        with self.assertRaises(VertexNotFoundException):
            self.graph.add_edge(v1, v2)

    def test_add_duplicate_edge(self):
        """Тест добавления дублирующегося ребра"""
        v1 = self.graph.add_vertex(10)
        v2 = self.graph.add_vertex(20)
        self.graph.add_edge(v1, v2)
        with self.assertRaises(EdgeAlreadyExistsException):
            self.graph.add_edge(v1, v2)

    def test_add_self_loop(self):
        """Тест добавления петли"""
        v1 = self.graph.add_vertex(10)
        with self.assertRaises(GraphException):
            self.graph.add_edge(v1, v1)

    def test_remove_vertex(self):
        """Тест удаления вершины"""
        v1 = self.graph.add_vertex(10)
        v2 = self.graph.add_vertex(20)
        self.graph.add_edge(v1, v2)

        self.graph.remove_vertex(v1)
        self.assertEqual(self.graph.vertex_count(), 1)
        self.assertEqual(self.graph.edge_count(), 0)
        self.assertFalse(self.graph.has_vertex(v1))

    def test_remove_nonexistent_vertex(self):
        """Тест удаления несуществующей вершины"""
        v = Vertex(10, 999)
        with self.assertRaises(VertexNotFoundException):
            self.graph.remove_vertex(v)

    def test_remove_edge(self):
        """Тест удаления ребра"""
        v1 = self.graph.add_vertex(10)
        v2 = self.graph.add_vertex(20)
        self.graph.add_edge(v1, v2)

        self.graph.remove_edge(v1, v2)
        self.assertEqual(self.graph.edge_count(), 0)
        self.assertFalse(self.graph.has_edge(v1, v2))

    def test_remove_nonexistent_edge(self):
        """Тест удаления несуществующего ребра"""
        v1 = self.graph.add_vertex(10)
        v2 = self.graph.add_vertex(20)
        with self.assertRaises(EdgeNotFoundException):
            self.graph.remove_edge(v1, v2)

    def test_clear(self):
        """Тест очистки графа"""
        v1 = self.graph.add_vertex(10)
        v2 = self.graph.add_vertex(20)
        self.graph.add_edge(v1, v2)

        self.graph.clear()
        self.assertTrue(self.graph.empty())
        self.assertEqual(self.graph.vertex_count(), 0)
        self.assertEqual(self.graph.edge_count(), 0)

    def test_vertex_degree(self):
        """Тест вычисления степени вершины"""
        v1 = self.graph.add_vertex(10)
        v2 = self.graph.add_vertex(20)
        v3 = self.graph.add_vertex(30)

        self.graph.add_edge(v1, v2)
        self.graph.add_edge(v1, v3)

        self.assertEqual(self.graph.vertex_degree(v1), 2)
        self.assertEqual(self.graph.vertex_degree(v2), 1)
        self.assertEqual(self.graph.vertex_degree(v3), 1)

    def test_edge_degree(self):
        """Тест вычисления степени ребра"""
        v1 = self.graph.add_vertex(10)
        v2 = self.graph.add_vertex(20)
        v3 = self.graph.add_vertex(30)

        self.graph.add_edge(v1, v2)
        self.graph.add_edge(v1, v3)
        self.graph.add_edge(v2, v3)

        # Степень ребра = сумма степеней вершин - 2
        degree = self.graph.edge_degree(v1, v2)
        self.assertEqual(degree, 2)  # (2 + 2) - 2 = 2

    def test_get_adjacent_vertices(self):
        """Тест получения смежных вершин"""
        v1 = self.graph.add_vertex(10)
        v2 = self.graph.add_vertex(20)
        v3 = self.graph.add_vertex(30)

        self.graph.add_edge(v1, v2)
        self.graph.add_edge(v1, v3)

        adjacent = self.graph.get_adjacent_vertices(v1)
        self.assertEqual(len(adjacent), 2)
        self.assertIn(v2, adjacent)
        self.assertIn(v3, adjacent)

    def test_get_incident_edges(self):
        """Тест получения инцидентных ребер"""
        v1 = self.graph.add_vertex(10)
        v2 = self.graph.add_vertex(20)
        v3 = self.graph.add_vertex(30)

        e1 = self.graph.add_edge(v1, v2)
        e2 = self.graph.add_edge(v1, v3)

        incident = self.graph.get_incident_edges(v1)
        self.assertEqual(len(incident), 2)

    def test_graph_equality(self):
        """Тест равенства графов"""
        g1 = UndirectedGraph[int]()
        g2 = UndirectedGraph[int]()

        v1_g1 = g1.add_vertex(10)
        v2_g1 = g1.add_vertex(20)
        g1.add_edge(v1_g1, v2_g1)

        v1_g2 = g2.add_vertex(10)
        v2_g2 = g2.add_vertex(20)
        g2.add_edge(v1_g2, v2_g2)

        self.assertEqual(g1, g2)

    def test_graph_inequality(self):
        """Тест неравенства графов"""
        g1 = UndirectedGraph[int]()
        g2 = UndirectedGraph[int]()

        g1.add_vertex(10)
        g2.add_vertex(20)

        self.assertNotEqual(g1, g2)

    def test_graph_comparison(self):
        """Тест сравнения графов"""
        g1 = UndirectedGraph[int]()
        g2 = UndirectedGraph[int]()

        g1.add_vertex(10)
        g2.add_vertex(10)
        g2.add_vertex(20)

        self.assertLess(g1, g2)
        self.assertLessEqual(g1, g2)
        self.assertGreater(g2, g1)
        self.assertGreaterEqual(g2, g1)

    def test_copy(self):
        """Тест копирования графа"""
        v1 = self.graph.add_vertex(10)
        v2 = self.graph.add_vertex(20)
        self.graph.add_edge(v1, v2)

        graph_copy = copy.copy(self.graph)
        self.assertEqual(self.graph.vertex_count(), graph_copy.vertex_count())
        self.assertEqual(self.graph.edge_count(), graph_copy.edge_count())

    def test_deepcopy(self):
        """Тест глубокого копирования графа"""
        v1 = self.graph.add_vertex([1, 2, 3])
        v2 = self.graph.add_vertex([4, 5, 6])
        self.graph.add_edge(v1, v2)

        graph_copy = copy.deepcopy(self.graph)
        self.assertEqual(self.graph.vertex_count(), graph_copy.vertex_count())
        self.assertEqual(self.graph.edge_count(), graph_copy.edge_count())


class TestVertexIterator(unittest.TestCase):
    """
    @class TestVertexIterator
    @brief Тесты для итератора вершин
    """

    def setUp(self):
        """Подготовка к тестам"""
        self.graph = UndirectedGraph[int]()
        self.v1 = self.graph.add_vertex(10)
        self.v2 = self.graph.add_vertex(20)
        self.v3 = self.graph.add_vertex(30)

    def test_vertex_iterator_iteration(self):
        """Тест итерации по вершинам"""
        vertices = []
        it = self.graph.vertices_begin()
        end = self.graph.vertices_end()

        while it != end:
            vertices.append(it.current())
            it.next()

        self.assertEqual(len(vertices), 3)

    def test_vertex_iterator_for_loop(self):
        """Тест использования итератора в цикле for"""
        vertices = []
        for v in self.graph.vertices_begin():
            vertices.append(v)

        self.assertEqual(len(vertices), 3)

    def test_vertex_iterator_prev(self):
        """Тест движения итератора назад"""
        it = self.graph.vertices_begin()
        it.next()
        it.next()
        it.prev()

        self.assertEqual(it.current(), self.v2)

    def test_reverse_vertex_iterator(self):
        """Тест обратного итератора вершин"""
        it = self.graph.vertices_rbegin()
        end = self.graph.vertices_rend()

        vertices = []
        while it != end:
            vertices.append(it.current())
            it.next()

        self.assertEqual(len(vertices), 3)
        self.assertEqual(vertices[0], self.v3)


class TestEdgeIterator(unittest.TestCase):
    """
    @class TestEdgeIterator
    @brief Тесты для итератора ребер
    """

    def setUp(self):
        """Подготовка к тестам"""
        self.graph = UndirectedGraph[int]()
        self.v1 = self.graph.add_vertex(10)
        self.v2 = self.graph.add_vertex(20)
        self.v3 = self.graph.add_vertex(30)
        self.graph.add_edge(self.v1, self.v2)
        self.graph.add_edge(self.v2, self.v3)

    def test_edge_iterator_iteration(self):
        """Тест итерации по ребрам"""
        edges = []
        it = self.graph.edges_begin()
        end = self.graph.edges_end()

        while it != end:
            edges.append(it.current())
            it.next()

        self.assertEqual(len(edges), 2)

    def test_edge_iterator_for_loop(self):
        """Тест использования итератора ребер в цикле for"""
        edges = []
        for e in self.graph.edges_begin():
            edges.append(e)

        self.assertEqual(len(edges), 2)

    def test_reverse_edge_iterator(self):
        """Тест обратного итератора ребер"""
        it = self.graph.edges_rbegin()
        end = self.graph.edges_rend()

        edges = []
        while it != end:
            edges.append(it.current())
            it.next()

        self.assertEqual(len(edges), 2)


class TestAdjacentVertexIterator(unittest.TestCase):
    """
    @class TestAdjacentVertexIterator
    @brief Тесты для итератора смежных вершин
    """

    def setUp(self):
        """Подготовка к тестам"""
        self.graph = UndirectedGraph[int]()
        self.v1 = self.graph.add_vertex(10)
        self.v2 = self.graph.add_vertex(20)
        self.v3 = self.graph.add_vertex(30)
        self.graph.add_edge(self.v1, self.v2)
        self.graph.add_edge(self.v1, self.v3)

    def test_adjacent_vertex_iterator(self):
        """Тест итерации по смежным вершинам"""
        vertices = []
        it = self.graph.adjacent_vertices_begin(self.v1)
        end = self.graph.adjacent_vertices_end(self.v1)

        while it != end:
            vertices.append(it.current())
            it.next()

        self.assertEqual(len(vertices), 2)
        self.assertIn(self.v2, vertices)
        self.assertIn(self.v3, vertices)

    def test_adjacent_vertex_iterator_for_loop(self):
        """Тест использования итератора смежных вершин в цикле for"""
        vertices = []
        for v in self.graph.adjacent_vertices_begin(self.v1):
            vertices.append(v)

        self.assertEqual(len(vertices), 2)


class TestIncidentEdgeIterator(unittest.TestCase):
    """
    @class TestIncidentEdgeIterator
    @brief Тесты для итератора инцидентных ребер
    """

    def setUp(self):
        """Подготовка к тестам"""
        self.graph = UndirectedGraph[int]()
        self.v1 = self.graph.add_vertex(10)
        self.v2 = self.graph.add_vertex(20)
        self.v3 = self.graph.add_vertex(30)
        self.graph.add_edge(self.v1, self.v2)
        self.graph.add_edge(self.v1, self.v3)

    def test_incident_edge_iterator(self):
        """Тест итерации по инцидентным ребрам"""
        edges = []
        it = self.graph.incident_edges_begin(self.v1)
        end = self.graph.incident_edges_end(self.v1)

        while it != end:
            edges.append(it.current())
            it.next()

        self.assertEqual(len(edges), 2)

    def test_incident_edge_iterator_for_loop(self):
        """Тест использования итератора инцидентных ребер в цикле for"""
        edges = []
        for e in self.graph.incident_edges_begin(self.v1):
            edges.append(e)

        self.assertEqual(len(edges), 2)


class TestIteratorDeletion(unittest.TestCase):
    """
    @class TestIteratorDeletion
    @brief Тесты удаления через итераторы
    """

    def test_remove_vertex_by_iterator(self):
        """Тест удаления вершины через итератор"""
        graph = UndirectedGraph[int]()
        v1 = graph.add_vertex(10)
        v2 = graph.add_vertex(20)

        it = graph.vertices_begin()
        graph.remove_vertex_by_iterator(it)

        self.assertEqual(graph.vertex_count(), 1)

    def test_remove_edge_by_iterator(self):
        """Тест удаления ребра через итератор"""
        graph = UndirectedGraph[int]()
        v1 = graph.add_vertex(10)
        v2 = graph.add_vertex(20)
        graph.add_edge(v1, v2)

        it = graph.edges_begin()
        graph.remove_edge_by_iterator(it)

        self.assertEqual(graph.edge_count(), 0)


class TestComplexScenarios(unittest.TestCase):
    """
    @class TestComplexScenarios
    @brief Тесты сложных сценариев
    """

    def test_complete_graph(self):
        """Тест полного графа"""
        graph = UndirectedGraph[int]()
        vertices = [graph.add_vertex(i) for i in range(5)]

        # Создаем полный граф
        for i in range(len(vertices)):
            for j in range(i + 1, len(vertices)):
                graph.add_edge(vertices[i], vertices[j])

        # Проверяем количество ребер: n*(n-1)/2
        self.assertEqual(graph.edge_count(), 10)

    def test_string_values(self):
        """Тест с строковыми значениями"""
        graph = UndirectedGraph[str]()
        v1 = graph.add_vertex("Alice")
        v2 = graph.add_vertex("Bob")
        v3 = graph.add_vertex("Charlie")

        graph.add_edge(v1, v2)
        graph.add_edge(v2, v3)

        self.assertEqual(graph.vertex_count(), 3)
        self.assertEqual(graph.edge_count(), 2)

    def test_custom_objects(self):
        """Тест с пользовательскими объектами"""
        from dataclasses import dataclass

        @dataclass
        class Person:
            name: str
            age: int

        graph = UndirectedGraph[Person]()
        p1 = Person("Alice", 25)
        p2 = Person("Bob", 30)

        v1 = graph.add_vertex(p1)
        v2 = graph.add_vertex(p2)
        graph.add_edge(v1, v2)

        self.assertEqual(graph.vertex_count(), 2)
        self.assertEqual(graph.edge_count(), 1)


if __name__ == '__main__':
    unittest.main()

