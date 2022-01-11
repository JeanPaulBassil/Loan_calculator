import argparse
import math

parser = argparse.ArgumentParser()
parser.add_argument("--type")
parser.add_argument("--principal")
parser.add_argument("--periods")
parser.add_argument("--interest")
parser.add_argument("--payment")
args = parser.parse_args()
arguments = [args.type, args.principal, args.periods, args.interest, args.payment]
loan_type = arguments[0]
loan_principal = arguments[1]
periods = arguments[2]
interest = arguments[3]
annuity_payment = arguments[4]


def overpayment(number_of_months, monthly_payment, initial_loan_principal):
    final_overpayment = (int(number_of_months) * float(monthly_payment) - float(initial_loan_principal))
    print(f"Overpayment = {final_overpayment}")


def principal(loan_annuity_payment, number_of_periods, loan_interest):
    nominal_interest_rate = (float(loan_interest) / 1200)
    p = round(float(loan_annuity_payment) / (
            (nominal_interest_rate * math.pow(1 + nominal_interest_rate, int(number_of_periods))) / (
            math.pow(1 + nominal_interest_rate, int(number_of_periods)) - 1)))
    print(f"Your loan principal = {p}!")
    overpayment(number_of_periods, loan_annuity_payment, p)


def payment(payment_loan_principal, number_of_periods, loan_interest):
    nominal_interest_rate = (float(loan_interest) / 1200)
    loan_annuity_payment = math.ceil((float(payment_loan_principal) * (
            nominal_interest_rate * math.pow(1 + nominal_interest_rate, int(number_of_periods))) / (
                                              math.pow(nominal_interest_rate + 1, int(number_of_periods)) - 1)))
    print(f"Your monthly payment = {loan_annuity_payment}!")
    overpayment(number_of_periods, loan_annuity_payment, payment_loan_principal)


def months(months_loan_principal, monthly_payment, loan_interest):
    nominal_interest_rate = (float(loan_interest) / 1200)
    number_of_months = math.ceil(
        math.log(
            float(monthly_payment) / (float(monthly_payment) - (nominal_interest_rate * float(months_loan_principal))),
            1 + nominal_interest_rate)
    )
    number_of_years = math.floor(number_of_months / 12)
    number_of_months = number_of_months % 12
    if number_of_years == 0:
        print(f"It will take {number_of_months} months to repay this loan!")
    elif number_of_months == 0:
        print(f"It will take {number_of_years} years to repay this loan!")
    else:
        print(f"It will take {number_of_years} years and {number_of_months} months to repay this loan!")
    number_of_months = number_of_years * 12 + number_of_months
    overpayment(number_of_months, monthly_payment, months_loan_principal)


def annuity():
    if periods is None:
        months(loan_principal, annuity_payment, interest)
    elif annuity_payment is None:
        payment(loan_principal, periods, interest)
    elif loan_principal is None:
        principal(annuity_payment, periods, interest)


def diff(diff_interest, p, n):
    i = (float(diff_interest) / 1200)
    payments = []
    total_payment = 0
    for x in range(int(n)):
        m = x + 1
        d = math.ceil(float(p) / int(n) + i * (float(p) - ((float(p) * (m - 1)) / int(n))))
        print(f"Month {m}: payment is {d}")
        payments.append(d)
        total_payment += d
    print()
    diff_overpayment = total_payment - float(p)
    print(f"Overpayment = {diff_overpayment}")


def type_selection():
    a = 0
    for arg in arguments:
        if arg is not None:
            a += 1

    if a < 4:
        print("Incorrect parameters")
    else:
        if loan_type == "annuity":
            annuity()
        elif loan_type == "diff" and interest is not None:
            diff(interest, loan_principal, periods)
        else:
            print("Incorrect parameters")


type_selection()
