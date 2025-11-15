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

