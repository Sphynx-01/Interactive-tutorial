class Social:
    def __init__(self):
        self.friends = []

    def get_friends(self):
        """
        Получает список друзей.

        :return: Список друзей.
        """
        return self.friends

    def add_friend(self, friend_name):
        """
        Добавляет друга в список друзей.

        :param friend_name: Имя друга.
        :return: None
        """
        if friend_name not in self.friends:
            self.friends.append(friend_name)
            print(f"{friend_name} добавлен в список друзей.")
        else:
            print(f"{friend_name} уже в списке друзей.")

    def remove_friend(self, friend_name):
        """
        Удаляет друга из списка друзей.

        :param friend_name: Имя друга.
        :return: None
        """
        if friend_name in self.friends:
            self.friends.remove(friend_name)
            print(f"{friend_name} удален из списка друзей.")
        else:
            print(f"{friend_name} не найден в списке друзей.")

    def find_friend(self, friend_name):
        """
        Проверяет, есть ли друг в списке друзей.

        :param friend_name: Имя друга.
        :return: True, если друг найден, иначе False.
        """
        return friend_name in self.friends

    def display_friends(self):
        """
        Отображает список друзей.
        
        :return: None
        """
        if self.friends:
            print("Список друзей:")
            for friend in self.friends:
                print(f"- {friend}")
        else:
            print("Список друзей пуст.")
