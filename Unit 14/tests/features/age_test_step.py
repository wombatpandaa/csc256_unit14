import pytest
from pytest_bdd import scenarios, scenario, given, when, then, parsers
from full_retirement_age_calculator import full_retirement_age_calculator


CONVERTERS = {
    'birthYear': int,
    'birthMonth': int,
    'retirementAge': str,
}

scenarios('../features/age_test.feature')


@pytest.fixture
@given(parsers.cfparse('the user enters "{birthYear:Number}" as birth year',
                       extra_types=dict(Number=int)))
@given('the user enters "<birthYear>" as birth year')
def calculator(birthYear):
    return full_retirement_age_calculator(birthYear=1955)


@when(parsers.cfparse("'{birthMonth:Number}' is entered as the month",
                      extra_types=dict(Number=int)))
@when(">birthMonth> is entered as the month")
def enter_2_as_month(calculator, birthMonth):
    calculator.setBirthMonth(2)


@then(parsers.cfparse("full retirement age will be '{retirementAge}'"))
@then("full retirement age will be '<retirementAge>'")
def retirement_age_is_66_years_and_2_months(calculator, retirementAge):
    calculator.calcRetirementAge()
    assert calculator.retirementAge == "66 years and 2 months"


@scenario('../features/age_test.feature',
          'User wants to get their retirement age but they\'re a dingus')
def test_to_the_broken_thing():
    pass


@pytest.fixture
@given(parsers.cfparse('the user enters "{birthYear}" as birth year'))
def calculator(birthYear):
    return full_retirement_age_calculator(birthYear="pizza")

