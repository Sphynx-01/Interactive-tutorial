class Lessons:
    """
    Класс для управления уроками.
    """

    def __init__(self):
        """Инициализация уроков."""
        self.lessons = []

    def add_lesson(self, lesson):
        """
        Добавляет урок в список.

        :param lesson: Урок для добавления.
        """
        self.lessons.append(lesson)

    def get_lessons(self):
        """
        Получает список уроков.

        :return: Список уроков.
        """
        return self.lessons
