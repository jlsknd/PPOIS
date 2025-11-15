class UndirectedGraph(Generic[T]):
    """
    @class UndirectedGraph
    @brief Шаблонный класс неориентированного графа на основе упорядоченных списков рёбер
    @details Представляет неориентированный граф с возможностью хранения значений в вершинах

    Класс предоставляет:
    - Добавление/удаление вершин, ребеер
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

