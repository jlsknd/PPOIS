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
