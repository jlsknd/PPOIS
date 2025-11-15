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
