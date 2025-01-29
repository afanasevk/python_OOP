# TODO: импортируйте классы, созданные в ходе выполнения прошлого задания
from task_1 import Student, Car, BankAccount

if __name__ == "__main__":
    # TODO: инстанцировать все описанные классы, создав три объекта.
    student = Student("Иван", "Петров", 18, [5, 4, 3])
    car = Car("Toyota", "Corolla", 2020, 4000)
    account = BankAccount("123456", "Иванов Иван", "RUB", 500)
    try:
        student.add_grade(6)
    except ValueError:
        print("Ошибка: оценка должна быть в диапазоне от 2 до 5")

    try:
        car.drive(5000)  # Ожидаем исключение, так как топлива недостаточно
    except ValueError:
        print("Ошибка: недостаточно топлива для поездки")

    try:
        account.deposit(-100)  # Ожидаем исключение, так как сумма пополнения не может быть отрицательной
    except ValueError:
        print("Ошибка: сумма пополнения должна быть положительной")

