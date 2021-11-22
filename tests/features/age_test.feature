Feature: Retirement Age Calculator
    As a potential retiree, I want to know my retirement age


  Scenario Outline: User wants to get their retirement age
    Given the user enters "<birthYear>" as birth year
    When '<birthMonth>' is entered as the month
    Then full retirement age will be '<retirementAge>'
    Examples:
      | birthYear | birthMonth | retirementAge |
      | 1955      | 2          | '66 years and 2 months' |
      | 1901      | 2          | 'You old'               |
      | 1942      | 2          | 'You old'               |
      | 1943      | 2          | '66 years and 0 months' |
      | 1954      | 2          | '66 years and 0 months' |
      | 1956      | 2          | '66 years and 4 months' |
      | 1957      | 2          | '66 years and 6 months' |
      | 1958      | 2          | '66 years and 8 months' |
      | 1959      | 2          | '66 years and 10 months'|
      | 1960      | 2          | '67 years'              |

    Scenario: User wants to get their retirement age but they're a dingus
      Given the user enters "pizza" as birth year
      When '2' is entered as the month
      Then full retirement age will be 'do it right'
