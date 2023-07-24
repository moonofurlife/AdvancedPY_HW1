import datetime
from application.salary import calculate_salary
from application.db.people import get_employees
from faker import Faker

def main():
    calculate_salary()
    get_employees()
    print("Current date:", datetime.date.today())

    # Пример использования пакета faker
    fake = Faker()
    for _ in range(5):
        print("Name:", fake.name(), "- Email:", fake.email())

if __name__ == '__main__':
    main()