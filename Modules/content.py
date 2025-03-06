class Content:
    """
    Класс для управления контентом.
    """

    def __init__(self):
        """Инициализация контента."""
        self.data = []

    def add_content(self, item):
        """
        Добавляет контент в список.

        :param item: Элемент контента для добавления.
        """
        self.data.append(item)

    def get_content(self):
        """
        Получает список контента.

        :return: Список контента.
        """
        return self.data
