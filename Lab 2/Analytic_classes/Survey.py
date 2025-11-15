class Survey:
    """Класс опроса."""
    
    def __init__(self, title, questions):
        """
        Инициализация опроса.
        
        Args:
            title: Название опроса
            questions: Вопросы
        """
        self.title = title
        self.questions = questions
        self.responses = []
        
    def submit_response(self, response):
        """Отправить ответ."""
        self.responses.append({
            'response': response,
            'timestamp': datetime.now()
        })
        
    def get_response_count(self):
        """Получить количество ответов."""
        return len(self.responses)
        
    def analyze_results(self):
        """Анализировать результаты."""
        return f"Проанализировано {len(self.responses)} ответов"
