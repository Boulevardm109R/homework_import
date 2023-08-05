import datetime
from application.db.people import get_employees
from application.salary import *


if __name__ == '__main__':
    print("Дата:", datetime.date.today())
    get_employees()
    calculate_salary()