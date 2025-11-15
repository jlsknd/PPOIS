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

