# interest, years, yearlyDeposit, startingBalance
def retirement(goal=None, interest=0.08, number_of_years=30, yearly_deposit=1000, starting_balance=0):
    total_interest = 0

    years = []

    interest_earned = (starting_balance + yearly_deposit) * interest
    ending_balance = starting_balance + yearly_deposit + interest_earned
    settings = {"goal": goal, "interest": interest, "startingBalance": starting_balance,
                "yearlyDeposit": yearly_deposit}

    if settings["goal"] is None:
        for no in range(1, number_of_years + 1):
            year = {
                "no": no, "startingBalance": starting_balance, "yearlyDeposit": yearly_deposit,
                "interestEarned": interest_earned, "endingBalance": ending_balance
            }
            years.append(year)
            total_interest += interest_earned

            starting_balance = ending_balance
            interest_earned = (starting_balance + yearly_deposit) * interest
            ending_balance = starting_balance + yearly_deposit + interest_earned
        settings["years"] = number_of_years
        settings["goal"] = "n/a"
        summary = {"years": years, "totalInterest": total_interest, "settings": settings}
        return summary
    else:
        x = 1

        while goal > ending_balance:
            year = {
                "no": x, "startingBalance": starting_balance, "yearlyDeposit": yearly_deposit,
                "interestEarned": interest_earned, "endingBalance": ending_balance
            }
            years.append(year)
            total_interest += interest_earned

            starting_balance = ending_balance
            interest_earned = (starting_balance + yearly_deposit) * interest
            ending_balance = starting_balance + yearly_deposit + interest_earned
            x += 1

        year = {
            "no": x, "startingBalance": starting_balance, "yearlyDeposit": yearly_deposit,
            "interestEarned": interest_earned, "endingBalance": ending_balance
        }
        years.append(year)
        settings["years"] = x
        summary = {"years": years, "totalInterest": total_interest, "settings": settings}
        return summary


if __name__ == "__main__":
    retirement_summary = retirement()
    all_years = retirement_summary["years"]

    print(retirement_summary["totalInterest"])
    print(100 * "-")
    print(retirement_summary["settings"])
    print(100 * "-")

    for y in all_years:
        print(y)
