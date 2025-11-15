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
