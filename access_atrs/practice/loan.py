class Loan:
    def __init__(self, loan_id, amount, interest_rate, duration):
        self.amount = amount
        self.interest_rate = interest_rate
        self.duration = duration
        self.__loan_id = loan_id

    def calculate_total_repayment(self):
        return int(self.amount * (1 + self.interest_rate/100))

    def calculate_monthly_installments(self):
        return round(self.calculate_total_repayment()/self.duration, 2)

    def calculate_interest_amount(self):
        return self.calculate_total_repayment() - self.amount

class PersonalLoan(Loan):
    def __init__(self, loan_id, amount, interest_rate, duration, first_name, last_name, phone, salary):
        super().__init__(loan_id, amount, interest_rate, duration)
        self.first_name = first_name
        self.last_name = last_name
        self.phone = phone
        self.salary = salary

    def print_details(self):
        print(f"{self.last_name} {self.first_name} with salary {self.salary} got a loan")

class HomeLoan(PersonalLoan):
    def __init__(self, loan_id, amount, interest_rate, duration, first_name, last_name, phone, salary, square):
        super().__init__(loan_id, amount, interest_rate, duration, first_name, last_name, phone, salary)
        self.square = square

    def print_details(self):
        print(f"{self.last_name} {self.first_name} with salary {self.salary} got a loan for a house with square {self.square}")


personal_loan = PersonalLoan(10, 10000, 15, 36, "Anastasiia", "Andrieieva", "+380953584697", 100000)
personal_loan.print_details()

home_loan = HomeLoan(12, 10000, 12, 60, "Maria", "Terentieieva", "+380955555555", 1000000, 50)
home_loan.print_details()
print(home_loan.calculate_total_repayment())
print(home_loan.calculate_monthly_installments())
    