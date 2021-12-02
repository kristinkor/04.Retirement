import RetirementLogic as r
from flask import Flask
from flask import request
from settings import get_settings
import properties as p
app = Flask(__name__)


@app.route("/settings")
def settings():
    no = request.args.get('no', default=1, type=int)

    settings = get_settings(no)

    if settings is None:
        return r.retirement()
    else:
        return r.retirement(settings['goal'], settings['interest'], settings['years'], settings['yearlyDeposit'],
                            settings['startingBalance'])


@app.route("/retirement")
def get_retirement():
    year = request.args.get('years', default=30, type=int)
    interest = request.args.get('interest', default=.08, type=float)
    deposit = request.args.get('deposit', default=1000, type=float)
    startingBalance = request.args.get('startingBalance', default=0, type=float)
    goal = request.args.get('goal', default=None, type=float)
    return r.retirement(goal=goal, interest=interest, number_of_years=year, yearly_deposit=deposit,
                        starting_balance=startingBalance)


@app.route("/properties")
def get_properties():
    return p.get_investments()

if __name__ == "__main__":
    app.run(debug=True, port=9121)
