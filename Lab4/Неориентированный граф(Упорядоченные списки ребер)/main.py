"""
@file main.py
@brief Демонстрационная программа для работы с неориентированным графом
@details Показывает основные возможности класса UndirectedGraph
"""

from graph import UndirectedGraph, Vertex, Edge, print_graph
from dataclasses import dataclass


def print_separator(title: str = ""):
    """Печатает разделительную линию"""
    print("\n" + "=" * 80)
    if title:
        print(f" {title} ".center(80, "="))
        print("=" * 80)


def demo_basic_operations():
    """Демонстрация базовых операций с графом"""
    print_separator("БАЗОВЫЕ ОПЕРАЦИИ С ГРАФОМ")

    # Создание графа
    graph = UndirectedGraph[str]()
    print("\n1. Создан пустой граф")
    print(f"   Граф пуст: {graph.empty()}")

    # Добавление вершин
    print("\n2. Добавление вершин:")
    v1 = graph.add_vertex("Москва")
    v2 = graph.add_vertex("Санкт-Петербург")
    v3 = graph.add_vertex("Казань")
    v4 = graph.add_vertex("Новосибирск")
    print(f"   Добавлены вершины: {v1.value}, {v2.value}, {v3.value}, {v4.value}")
    print(f"   Количество вершин: {graph.vertex_count()}")

    # Добавление ребер
    print("\n3. Добавление ребер:")
    e1 = graph.add_edge(v1, v2)
    e2 = graph.add_edge(v1, v3)
    e3 = graph.add_edge(v2, v3)
    e4 = graph.add_edge(v3, v4)
    print(f"   Добавлено ребер: {graph.edge_count()}")

    # Проверка наличия
    print("\n4. Проверка наличия:")
    print(f"   Вершина 'Москва' есть в графе: {graph.has_vertex(v1)}")
    print(f"   Ребро Москва-Казань есть в графе: {graph.has_edge(v1, v3)}")
    print(f"   Ребро Москва-Новосибирск есть в графе: {graph.has_edge(v1, v4)}")

    # Степени
    print("\n5. Степени вершин и ребер:")
    print(f"   Степень вершины Москва: {graph.vertex_degree(v1)}")
    print(f"   Степень вершины Казань: {graph.vertex_degree(v3)}")
    print(f"   Степень ребра Москва-Казань: {graph.edge_degree(v1, v3)}")

    print("\n6. Информация о графе:")
    print(f"   {graph}")


def demo_iterators():
    """Демонстрация работы с итераторами"""
    print_separator("РАБОТА С ИТЕРАТОРАМИ")

    graph = UndirectedGraph[int]()
    vertices = [graph.add_vertex(i * 10) for i in range(1, 6)]

    # Соединяем вершины в цепь
    for i in range(len(vertices) - 1):
        graph.add_edge(vertices[i], vertices[i + 1])

    # Итератор вершин
    print("\n1. Итерация по вершинам (прямой порядок):")
    print("   ", end="")
    it = graph.vertices_begin()
    end = graph.vertices_end()
    while it != end:
        print(f"{it.current().value} ", end="")
        it.next()
    print()

    # Обратный итератор вершин
    print("\n2. Итерация по вершинам (обратный порядок):")
    print("   ", end="")
    it = graph.vertices_rbegin()
    end = graph.vertices_rend()
    while it != end:
        print(f"{it.current().value} ", end="")
        it.next()
    print()

    # Итератор ребер
    print("\n3. Итерация по ребрам:")
    for edge in graph.edges_begin():
        print(f"   {edge}")

    # Смежные вершины
    print(f"\n4. Вершины, смежные с {vertices[2].value}:")
    for v in graph.adjacent_vertices_begin(vertices[2]):
        print(f"   {v.value}")

    # Инцидентные ребра
    print(f"\n5. Ребра, инцидентные вершине {vertices[2].value}:")
    for e in graph.incident_edges_begin(vertices[2]):
        print(f"   {e}")


def demo_graph_algorithms():
    """Демонстрация простых алгоритмов на графе"""
    print_separator("ПРОСТЫЕ АЛГОРИТМЫ НА ГРАФЕ")

    graph = UndirectedGraph[str]()

    # Создаем граф социальной сети
    print("\n1. Создание графа социальной сети:")
    alice = graph.add_vertex("Алиса")
    bob = graph.add_vertex("Боб")
    charlie = graph.add_vertex("Чарли")
    david = graph.add_vertex("Дэвид")
    eve = graph.add_vertex("Ева")

    graph.add_edge(alice, bob)
    graph.add_edge(alice, charlie)
    graph.add_edge(bob, david)
    graph.add_edge(charlie, david)
    graph.add_edge(charlie, eve)
    graph.add_edge(david, eve)

    print(f"   Узлов: {graph.vertex_count()}, связей: {graph.edge_count()}")

    # Поиск наиболее связанного пользователя
    print("\n2. Поиск наиболее связанного пользователя:")
    max_degree = 0
    most_connected = None

    for vertex in graph.vertices_begin():
        degree = graph.vertex_degree(vertex)
        print(f"   {vertex.value}: {degree} связей")
        if degree > max_degree:
            max_degree = degree
            most_connected = vertex

    print(f"\n   Самый популярный: {most_connected.value} ({max_degree} связей)")

    # Друзья друзей
    print(f"\n3. Друзья {alice.value}:")
    friends = graph.get_adjacent_vertices(alice)
    for friend in friends:
        print(f"   - {friend.value}")

    print(f"\n4. Друзья друзей {alice.value}:")
    friends_of_friends = set()
    for friend in friends:
        for friend_of_friend in graph.get_adjacent_vertices(friend):
            if friend_of_friend != alice and friend_of_friend not in friends:
                friends_of_friends.add(friend_of_friend)

    for person in friends_of_friends:
        print(f"   - {person.value}")


def demo_custom_types():
    """Демонстрация работы с пользовательскими типами"""
    print_separator("РАБОТА С ПОЛЬЗОВАТЕЛЬСКИМИ ТИПАМИ")

    @dataclass
    class City:
        name: str
        population: int

        def __repr__(self):
            return f"{self.name} ({self.population} чел.)"

    graph = UndirectedGraph[City]()

    print("\n1. Создание графа городов:")
    moscow = graph.add_vertex(City("Москва", 12_600_000))
    spb = graph.add_vertex(City("Санкт-Петербург", 5_400_000))
    kazan = graph.add_vertex(City("Казань", 1_250_000))
    nsk = graph.add_vertex(City("Новосибирск", 1_600_000))

    graph.add_edge(moscow, spb)
    graph.add_edge(moscow, kazan)
    graph.add_edge(moscow, nsk)
    graph.add_edge(kazan, nsk)

    print(f"   Городов: {graph.vertex_count()}")
    print(f"   Дорог: {graph.edge_count()}")

    print("\n2. Список городов:")
    for vertex in graph.vertices_begin():
        city = vertex.value
        degree = graph.vertex_degree(vertex)
        print(f"   {city.name}: население {city.population:,}, связей {degree}")

    print("\n3. Дороги из Москвы:")
    for adjacent_vertex in graph.adjacent_vertices_begin(moscow):
        city = adjacent_vertex.value
        print(f"   Москва → {city.name}")


def demo_graph_modifications():
    """Демонстрация модификации графа"""
    print_separator("МОДИФИКАЦИЯ ГРАФА")

    graph = UndirectedGraph[int]()

    print("\n1. Создание графа:")
    vertices = [graph.add_vertex(i) for i in range(1, 6)]

    # Создаем полный граф
    for i in range(len(vertices)):
        for j in range(i + 1, len(vertices)):
            graph.add_edge(vertices[i], vertices[j])

    print(f"   Полный граф K5: {graph.vertex_count()} вершин, {graph.edge_count()} ребер")

    print("\n2. Удаление вершины:")
    graph.remove_vertex(vertices[2])
    print(f"   После удаления вершины: {graph.vertex_count()} вершин, {graph.edge_count()} ребер")

    print("\n3. Удаление ребра:")
    graph.remove_edge(vertices[0], vertices[1])
    print(f"   После удаления ребра: {graph.vertex_count()} вершин, {graph.edge_count()} ребер")

    print("\n4. Копирование графа:")
    import copy
    graph_copy = copy.deepcopy(graph)
    print(f"   Оригинал: {graph.vertex_count()} вершин")
    print(f"   Копия: {graph_copy.vertex_count()} вершин")

    print("\n5. Очистка графа:")
    graph.clear()
    print(f"   После очистки: {graph.vertex_count()} вершин")
    print(f"   Граф пуст: {graph.empty()}")


def demo_comparison():
    """Демонстрация сравнения графов"""
    print_separator("СРАВНЕНИЕ ГРАФОВ")

    g1 = UndirectedGraph[int]()
    g2 = UndirectedGraph[int]()
    g3 = UndirectedGraph[int]()

    # Создаем одинаковые графы
    for i in range(3):
        v1 = g1.add_vertex(i * 10)
        v2 = g2.add_vertex(i * 10)

    # g1 и g2 одинаковые
    print("\n1. Сравнение пустого и заполненных графов:")
    print(f"   g1 == g2: {g1 == g2}")
    print(f"   g1 == g3 (пустой): {g1 == g3}")
    print(f"   g1 != g3: {g1 != g3}")

    print("\n2. Сравнение по размеру:")
    print(f"   g1 > g3: {g1 > g3}")
    print(f"   g3 < g1: {g3 < g1}")
    print(f"   g1 >= g2: {g1 >= g2}")
    print(f"   g1 <= g2: {g1 <= g2}")


def main():
    """Главная функция"""
    print("\n" + "=" * 80)
    print(" ДЕМОНСТРАЦИЯ РАБОТЫ НЕОРИЕНТИРОВАННОГО ГРАФА ".center(80, "="))
    print(" Реализация на основе упорядоченных списков рёбер ".center(80, "="))
    print("=" * 80)

    try:
        demo_basic_operations()
        demo_iterators()
        demo_graph_algorithms()
        demo_custom_types()
        demo_graph_modifications()
        demo_comparison()

        print_separator()
        print("\n✓ Демонстрация завершена успешно!\n")

    except Exception as e:
        print(f"\n✗ Произошла ошибка: {e}\n")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    main()

