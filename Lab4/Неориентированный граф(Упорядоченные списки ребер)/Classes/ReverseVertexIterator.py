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
