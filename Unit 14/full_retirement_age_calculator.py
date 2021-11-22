class full_retirement_age_calculator:
    birthYear = 0
    birthMonth = 0
    benefitYear = 0
    benefitMonth = ""
    retirementAge = ""

    def __init__(self, birthYear=0, birthMonth=0, benefitYear=0,
                 benefitMonth="", retirementAge=""):
        self.retirementAge = retirementAge
        self.benefitMonth = benefitMonth
        self.benefitYear = benefitYear
        self.birthYear = birthYear
        self.birthMonth = birthMonth

    def getBirthYear(self):
        self.birthYear = int(input("What is your birth year? "))
        # program is supposed to work between 1900 - 1943 but the chart doesn't
        # specify any values for these age ranges so idk joke
        if 1900 < self.birthYear < 1943:
            self.retirementAge = "You old"
        if self.birthYear <= 1900:
            self.retirementAge = "You're a dingus"
        if not isinstance(self.birthYear, str):
            self.retirementAge = "Do it right"
        return self.birthYear

    def getBirthMonth(self):
        self.birthMonth = int(input("What is your birth month? "))
        return self.birthMonth

    def setBirthYear(self, by):
        self.birthYear = by

    def setBirthMonth(self, bm):
        self.birthMonth = bm

    def calcRetirementAge(self):
        if 1943 <= self.birthYear < 1959:
            self.benefitYear = self.birthYear + 66
            if 1943 <= self.birthYear <= 1954:
                self.retirementAge = "66 years and 0 months"
                self.benefitMonth = str(self.birthMonth)
            if self.birthYear == 1955:
                self.retirementAge = "66 years and 2 months"
                self.benefitMonth = str(self.birthMonth + 2)
            if self.birthYear == 1956:
                self.retirementAge = "66 years and 4 months"
                self.benefitMonth = str(self.birthMonth + 4)
            if self.birthYear == 1957:
                self.retirementAge = "66 years and 6 months"
                self.benefitMonth = str(self.birthMonth + 6)
            if self.birthYear == 1958:
                self.retirementAge = "66 years and 8 months"
                self.benefitMonth = str(self.birthMonth + 8)
            if self.birthYear == 1959:
                self.retirementAge = "66 years and 10 months"
                self.benefitMonth = str(self.birthMonth + 10)
        elif self.birthYear >= 1960:
            self.retirementAge = "67 years"
            self.benefitYear = self.birthYear + 67
        return self.retirementAge, self.benefitMonth, self.benefitYear

    def overFlow(self, benefit_month, benefit_year):
        self.birthMonth = int(benefit_month) - 12
        self.birthYear = int(benefit_year) + 1
        return self.birthYear, self.birthMonth
