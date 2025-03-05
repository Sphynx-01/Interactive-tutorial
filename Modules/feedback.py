class Feedback:
    """
    Класс для управления обратной связью.
    """

    def __init__(self):
        """Инициализация обратной связи."""
        self.feedback_list = []

    def collect_feedback(self, feedback):
        """
        Собирает обратную связь.

        :param feedback: Обратная связь для сбора.
        """
        self.feedback_list.append(feedback)

    def get_feedback(self):
        """
        Получает список собранной обратной связи.

        :return: Список обратной связи.
        """
        return self.feedback_list



