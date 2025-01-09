
class SocialMedia:
    """
    Базовый класс, представляющий общую социальную медиа платформу.
    """
    def __init__(self, name: str, user_count: int) -> None:
        self.name = name
        self.user_count = user_count

    def __str__(self) -> str:
        return f"Платформа: {self.name}, Пользователей: {self.user_count}"

    def __repr__(self) -> str:
        return f"SocialMedia('{self.name}', {self.user_count})"

    def increase_users(self, count: int) -> None:
        """
        Увеличивает количество пользователей на заданное значение.
        """
        self.user_count += count


class Telegram(SocialMedia):
    """
    Подкласс, представляющий платформу Telegram.
    Расширяет функциональность базового класса SocialMedia.
    """
    def __init__(self, user_count: int, channels: int, bots: int) -> None:
        super().__init__('Telegram', user_count)
        self.channels = channels  # Количество публичных каналов
        self.bots = bots  # Количество доступных ботов

    def __str__(self) -> str:
        return (f"Платформа Telegram: Пользователей: {self.user_count}, "
                f"Каналов: {self.channels}, Ботов: {self.bots}")

    def __repr__(self) -> str:
        return f"Telegram({self.user_count}, {self.channels}, {self.bots})"

    def increase_users(self, count: int) -> None:
        """
        Переопределенный метод увеличения количества пользователей для Telegram.
        В дополнение к увеличению пользователей, увеличивается количество каналов.
        """
        super().increase_users(count)
        self.channels += count // 1000  # На каждые 1000 пользователей добавляется один канал

    def add_bot(self) -> None:
        """
        Метод добавления нового бота в Telegram.
        Уникальный метод для класса Telegram.
        """
        self.bots += 1