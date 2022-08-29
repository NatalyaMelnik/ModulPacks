from Application.db.people import get_employees
from Application import salary
from datetime import date

if __name__ == '__main__':
    get_employees()
    salary.calculate_salary()
    present_day = date.today()
    print(present_day)
