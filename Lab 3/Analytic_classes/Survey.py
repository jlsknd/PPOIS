class Survey:
    """Класс опроса."""
    
    def __init__(self, title, questions):
        """
        Инициализация опроса.
        
        Args:
            title: Название
            questions: Список вопросов
        """
        self.title = title
        self.questions = questions
        self.responses = []
        
    def submit_response(self, customer, answers):
        """Отправить ответ."""
        self.responses.append({
            'customer': customer,
            'answers': answers,
            'submitted_at': datetime.now()
        })
        
    def get_response_count(self):
        """Получить количество ответов."""
        return len(self.responses)

