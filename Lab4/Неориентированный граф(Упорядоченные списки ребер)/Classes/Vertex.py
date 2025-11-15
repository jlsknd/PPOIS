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

