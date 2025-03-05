class Content:
    def __init__(self):
        # Инициализация контента
        self.data = []

    def add_content(self, item):
        # Метод для добавления контента
        self.data.append(item)

    def get_content(self):
        # Метод для получения контента
        return self.data


