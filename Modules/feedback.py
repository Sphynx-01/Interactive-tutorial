class Feedback:
    def __init__(self):
        # Инициализация обратной связи
        self.feedback_list = []

    def collect_feedback(self, feedback):
        # Метод для сбора обратной связи
        self.feedback_list.append(feedback)

    def get_feedback(self):
        # Метод для получения обратной связи
        return self.feedback_list

