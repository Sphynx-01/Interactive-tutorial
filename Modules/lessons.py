class GamifiedLessons:
    def __init__(self):
        # Инициализация геймифицированных уроков
        self.lessons = []

    def add_lesson(self, lesson):
        # Метод для добавления геймифицированного урока
        self.lessons.append(lesson)

    def get_lessons(self):
        # Метод для получения списка геймифицированных уроков
        return self.lessons

