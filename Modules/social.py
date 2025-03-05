class Social:
    def __init__(self):
        # Инициализация социальных функций
        self.friends = []

    def add_friend(self, friend):
        # Метод для добавления друга
        self.friends.append(friend)

    def get_friends(self):
        # Метод для получения списка друзей
        return self.friends

