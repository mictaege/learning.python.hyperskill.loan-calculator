import math
import argparse

# write your code here
parser = argparse.ArgumentParser()
parser.add_argument("--payment", type=float)
parser.add_argument("--principal", type=int)
parser.add_argument("--periods", type=int)
parser.add_argument("--interest", type=float)
parser.add_argument("--type", type=str)


def nom_interest(interest):
    return interest / 12 / 100


def annuity_periods(payment, principal, interest):
    i = nom_interest(interest)
    periods = math.ceil(math.log(payment / (payment - i * principal), 1 + i))
    years = math.floor(periods / 12)
    month = periods % 12
    if years == 0:
        print(f"It will take {month} months to repay the loan")
    elif month == 0:
        print(f"It will take {years} years to repay the loan")
    else:
        print(f"It will take {years} years and {month} months to repay the loan")
    total_payment = payment * periods
    print(f"Overpayment = {total_payment - principal}")


def annuity_payment(principal, periods, interest):
    i = nom_interest(interest)
    payment = math.ceil(principal * ((i * math.pow(1 + i, periods)) / (math.pow(1 + i, periods) - 1)))
    print(f"Your monthly payment = {payment}!")
    total_payment = payment * periods
    print(f"Overpayment = {total_payment - principal}")


def diff_payment(principal, periods, interest):
    i = nom_interest(interest)
    total_payment = 0
    for m in range(1, periods + 1):
        payment = math.ceil((principal / periods) + i * (principal - (principal * (m - 1) / periods)))
        total_payment += payment
        print(f"Month {m}: payment is {payment}")
    print()
    print(f"Overpayment = {total_payment - principal}")


def annuity_principal(payment, periods, interest):
    i = nom_interest(interest)
    principal = math.floor(payment / ((i * math.pow(1 + i, periods)) / (math.pow(1 + i, periods) - 1)))
    print(f"Your loan principal = {principal}!")
    total_payment = payment * periods
    print(f"Overpayment = {total_payment - principal}")


args = parser.parse_args()
if args.type not in ["annuity", "diff"]:
    print("Incorrect parameters")
elif args.interest is None:
    print("Incorrect parameters")
elif args.type == "diff" and args.payment is not None:
    print("Incorrect parameters")
elif len(vars(args)) < 4:
    print("Incorrect parameters")
elif args.payment is not None and args.payment < 0:
    print("Incorrect parameters")
elif args.principal is not None and args.principal < 0:
    print("Incorrect parameters")
elif args.periods is not None and args.periods < 0:
    print("Incorrect parameters")
elif args.interest is not None and args.interest < 0:
    print("Incorrect parameters")
else:
    if args.type == "annuity":
        if args.periods is None:
            annuity_periods(args.payment, args.principal, args.interest)
        elif args.payment is None:
            annuity_payment(args.principal, args.periods, args.interest)
        elif args.principal is None:
            annuity_principal(args.payment, args.periods, args.interest)
    elif args.type == "diff":
        diff_payment(args.principal, args.periods, args.interest)
