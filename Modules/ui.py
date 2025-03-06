class UserInterface:
   
    def __init__(self):
        pass

    def display(self, content):
        """
        Отображает заданный контент.

        :param content: Контент для отображения.
        """
        print(content)

    def get_input(self, prompt):
        """
        Получает ввод от пользователя.

        :param prompt: Сообщение для запроса ввода.
        :return: Ввод пользователя.
        """
        return input(prompt)
