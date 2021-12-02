from bs4 import BeautifulSoup


def get_settings(no=1):
    with open('retirement-settings.xml', 'r') as f:
        data = f.read()

    bs_data = BeautifulSoup(data, "xml")
    # b_unique = Bs_data.find_all('setting')
    for setting in bs_data.find_all('setting'):

        if int(setting['no']) == no:
            interest = float(setting["interest"])
            if setting['years'] == 'n/a':
                number_of_years = 0
            else:
                number_of_years = int(setting['years'])
            if setting['goal'] == 'n/a':
                goal = None
            else:
                goal = float(setting['goal'])
            starting_balance = float(setting['startingBalance'])
            yearly_deposit = float(setting['yearlyDeposit'])

            return {"goal": goal, "interest": interest, "startingBalance": starting_balance,
                    "yearlyDeposit": yearly_deposit, "years": number_of_years}

    return None
