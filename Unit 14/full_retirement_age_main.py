from full_retirement_age_calculator import \
    full_retirement_age_calculator


def main():
    calculator = full_retirement_age_calculator()
    calculator.getBirthYear()
    calculator.getBirthMonth()

    retirement_age, benefit_month, benefit_year = \
        calculator.calcRetirementAge()

    months = {
        "1": "January",
        "2": "February",
        "3": "March",
        "4": "April",
        "5": "May",
        "6": "June",
        "7": "July",
        "8": "August",
        "9": "September",
        "10": "October",
        "11": "November",
        "12": "December"
    }

    if int(benefit_month) > 12:
        benefit_year, benefit_month = calculator.overFlow(benefit_month, benefit_year)

    print("Your full retirement age is", retirement_age)
    print("This will be in", months[str(benefit_month)], benefit_year)


main()
