employee_profile = {"name": "", "vacation_dates": ""}


def setup_profile(name, vacation_dates):
    employee_profile["name"] = name
    employee_profile["vacation_dates"] = vacation_dates


def print_application_for_leave():
    print(f"Заявление на отпуск в период {employee_profile['vacation_dates']}. {employee_profile['name']}")


def print_holiday_money_claim(amount):
    print(f"Прошу выплатить {amount} отпускных денег. {employee_profile['name']}")


def print_attorney_letter(to_whom):
    print(f"На время отпуска в период {employee_profile['vacation_dates']} моим заместителем назначается {to_whom}."
          f" {employee_profile['name']}")
