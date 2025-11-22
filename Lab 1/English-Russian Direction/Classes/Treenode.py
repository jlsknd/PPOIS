class TreeNode:
    """
    Узел бинарного дерева поиска для хранения пар слово-перевод.
    
    Атрибуты:
        key (str): Английское слово
        value (str): Русский перевод
        left (Optional[TreeNode]): Левый потомок
        right (Optional[TreeNode]): Правый потомок
        height (int): Высота узла для балансировки
    """
    
    def __init__(self, key: str, value: str):
        """
        Инициализирует узел дерева.
        
        Args:
            key: Английское слово
            value: Русский перевод
        """
        self.key = key
        self.value = value
        self.left: Optional['TreeNode'] = None
        self.right: Optional['TreeNode'] = None
        self.height = 1
