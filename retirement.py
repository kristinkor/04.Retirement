# interest, years, yearlyDeposit, startingBalance

def retirement():
    years = []
    total_interest = 0
    interest = 8 / 100
    starting_balance = 0
    yearly_deposit = 1_000
    interest_earned = (starting_balance + yearly_deposit) * interest
    ending_balance = starting_balance + yearly_deposit + interest_earned
    settings = {"interest": interest, "starting_balance": starting_balance, "years": 30}
    for no in range(1, 31):
        year = {
            "no": no, "startingBalance": starting_balance, "yearlyDeposit": yearly_deposit,
            "interestEarned": interest_earned, "endingBalance": ending_balance
        }
        years.append(year)
        starting_balance = ending_balance
        interest_earned = (starting_balance + yearly_deposit) * interest
        ending_balance = starting_balance + yearly_deposit + interest_earned
        total_interest += interest_earned
    summary = {"years": years, "totalInterest": total_interest, "settings": settings}
    return summary


if __name__ == '__main__':
    retirement_summary = retirement()
    all_years = retirement_summary["years"]

    print(retirement_summary["totalInterest"])
    print(100 * "-")
    print(retirement_summary["settings"])
    print(100 * "-")

for y in all_years:
    print(y)
