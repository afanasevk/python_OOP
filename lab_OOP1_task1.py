# TODO: Подробно описать три произвольных класса
from typing import List


# TODO: описать класс
class Student:
    """
    Класс для описания студента.
    """

    def __init__(self, first_name: str, last_name: str, age: int, grades: List[int] = None):
        """
        Конструктор для создания объекта Student.

        :param first_name: Имя студента (str)
        :param last_name: Фамилия студента (str)
        :param age: Возраст студента (int, должен быть больше 16 лет)
        :param grades: Список оценок студента (List[int], по умолчанию пустой список)
        :raises ValueError: Если возраст меньше 16 лет
        """
        if age < 16:
            raise ValueError("Возраст студента не может быть меньше 16 лет.")

        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.grades = grades if grades is not None else []

    def __str__(self) -> str:
        return f"Студент: {self.first_name} {self.last_name}, {self.age} лет, Оценки: {', '.join(map(str, self.grades))}"

    def average_grade(self) -> float:
        """
        Возвращает среднюю оценку студента.

        :return: Средняя оценка студента (float), 0.0 если нет оценок

        Пример:
        >>> s = Student("Иван", "Петров", 18, [5, 4, 3])
        >>> s.average_grade()
        4.0
        """
        return sum(self.grades) / len(self.grades) if self.grades else 0.0

    def add_grade(self, grade: int):
        """
        Добавляет новую оценку студенту.

        :param grade: Оценка (int, должна быть от 2 до 5)
        :raises ValueError: Если оценка не в диапазоне 2-5

        Пример:
        >>> s = Student("Иван", "Иванов", 20, [4, 5])
        >>> s.add_grade(3)
        >>> s.grades
        [4, 5, 3]
        """
        if grade not in [2, 3, 4, 5]:
            raise ValueError("Оценка должна быть в диапазоне от 2 до 5.")
        self.grades.append(grade)

    def is_excellent(self, threshold: float = 4.5) -> bool:
        """
        Проверяет, является ли студент отличником.

        :param threshold: Порог для отличной успеваемости (float, по умолчанию 4.5)
        :return: True, если средняя оценка выше порога, иначе False

        Пример:
        >>> s = Student("Олег", "Сидоров", 19, [5, 5, 4, 5])
        >>> s.is_excellent()
        True
        """
        return self.average_grade() >= threshold


# TODO: описать ещё класс
class Car:
    def __init__(self, brand: str, model: str, year: int, mileage: float = 0.0, fuel_level: float = 100.0):
        """
        Конструктор для создания объекта Car.

        :param brand: Марка автомобиля (str)
        :param model: Модель автомобиля (str)
        :param year: Год выпуска (int, не может быть раньше 1886 года)
        :param mileage: Пробег (float, по умолчанию 0.0 км)
        :param fuel_level: Уровень топлива (float, по умолчанию 100.0%)
        :raises ValueError: Если год выпуска раньше 1886 года
        """
        if year < 1886:
            raise ValueError("Год выпуска не может быть раньше 1886 года.")

        self.brand = brand
        self.model = model
        self.year = year
        self.mileage = mileage
        self.fuel_level = fuel_level

    def drive(self, distance: float):
        """
        Проезжает указанное расстояние, уменьшая уровень топлива.

        :param distance: Расстояние в километрах (float)
        :raises ValueError: Если топлива недостаточно для поездки

        Пример:
        >>> car = Car("Toyota", "Corolla", 2020, 40.0)
        >>> car.drive(100)
        """
        if distance <= 0:
            raise ValueError("Расстояние должно быть положительным числом.")
        fuel_needed = distance * 0.1  # Расход топлива 10 л на 100 км
        if fuel_needed > self.fuel_level:
            raise ValueError("Недостаточно топлива для поездки.")
        self.mileage += distance
        self.fuel_level -= fuel_needed

    def refuel(self, amount: float):
        """
        Заправляет машину на указанное количество топлива.

        :param amount: Количество топлива (float, литры)
        :raises ValueError: Если количество топлива отрицательное или превышает максимальный уровень

        Пример:
        >>> car = Car("Toyota", "Corolla", 2020, 40.0)
        >>> car.refuel(30)
        >>> car.fuel_level
        70.0
        """
        if amount <= 0:
            raise ValueError("Количество топлива должно быть положительным числом.")
        self.fuel_level = min(self.fuel_level + amount, 100.0)

    def needs_service(self) -> bool:
        """
        Проверяет, нужно ли техобслуживание (если пробег > 15000 км).

        :return: True, если требуется ТО, иначе False

        Пример:
        >>> car = Car("Toyota", "Corolla", 2020, 16000)
        >>> car.needs_service()
        True
        """
        return self.mileage > 15000


# TODO: и ещё один
class BankAccount:
    def __init__(self, account_number: str, owner_name: str, currency: str, balance: float = 0.0):
        """
        Инициализирует новый банковский счет.

        :param account_number: Номер счета (str)
        :param owner_name: Имя владельца счета (str)
        :param currency: Валюта счета (str, например "USD", "EUR")
        :param balance: Начальный баланс счета (float, по умолчанию 0.0)
        """
        self.account_number = account_number
        self.owner_name = owner_name
        self.currency = currency
        self.balance = balance

    def deposit(self, amount: float):
        """
        Пополнение счета.

        :param amount: Сумма пополнения счета (float, должна быть положительной)

        Пример:
        >>> account = BankAccount("123456", "Иванов Иван", "RUB", 500)
        >>> account.deposit(200)
        >>> account.balance
        700.0
        """
        if amount <= 0:
            raise ValueError("Сумма пополнения должна быть положительной.")
        self.balance += amount

    def withdraw(self, amount: float):
        """
        Снятие средств с счета.

        :param amount: Сумма для снятия (float)
        :raises ValueError: Если на счете недостаточно средств

        Пример:
        >>> account = BankAccount("123456", "Иванов Иван", "RUB", 500)
        >>> account.withdraw(200)
        >>> account.balance
        300.0
        """
        if amount > self.balance:
            raise ValueError("Недостаточно средств на счете.")
        self.balance -= amount

    def get_balance(self) -> float:
        """
        Получение текущего баланса счета.

        :return: Текущий баланс счета (float)

        Пример:
        >>> account = BankAccount("123456", "Иванов Иван", "RUB", 500)
        >>> account.get_balance()
        500.0
        """
        return self.balance

    def get_account_info(self) -> str:
        """
        Получение информации о счете.

        :return: Строка с номером счета, владельцем, валютой и балансом (str)

        Пример:
        >>> account = BankAccount("123456", "Иванов Иван", "RUB", 500)
        >>> account.get_account_info()
        'Счет №123456, владелец: Иванов Иван, валюта: RUB, баланс: 500.00 RUB'
        """
        return (f"Счет №{self.account_number}, владелец: {self.owner_name}, "
                f"валюта: {self.currency}, баланс: {self.balance:.2f} {self.currency}")
