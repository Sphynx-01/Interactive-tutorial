def __init__(self):
        # Инициализация уроков
        self.lessons = []

    def add_lesson(self, lesson):
        # Метод для добавления урока
        self.lessons.append(lesson)

    def get_lessons(self):
        # Метод для получения списка уроков
        return self.lessons
    def print_lessons(self):
        pass
