import xml.etree.ElementTree as ET

tree = ET.parse('properties.xml')
root = tree.getroot()


def get_investments():
    data = []
    total_net_income = 0
    total_investment_cost = 0
    unit_count1 = 0
    unit_count2 = 0
    unit_count3 = 0
    unit_count4 = 0
    for child in root:
        dict = child.attrib
        dict["investmentCost"] = float(child.text)
        dict["netIncome"] = float(dict["netIncome"])
        dict["grossIncome"] = float(dict["grossIncome"])
        dict["occupancy"] = float(dict["occupancy"])
        dict["expense"] = float(dict["expense"])
        data.append(dict)
        total_net_income += float(dict["netIncome"])
        total_investment_cost += float(dict["investmentCost"])
        if dict["occupancy"] == 1:
            unit_count1 += 1
        elif dict["occupancy"] == 2:
            unit_count2 += 1
        elif dict["occupancy"] == 3:
            unit_count3 += 1
        elif dict["occupancy"] == 4:
            unit_count4 += 1

    # print(child.attrib, child.text)
    summary = {
        "count": len(data),
        "investments": data, "totalNetIncome": total_net_income, "totalInvestmentCost": total_investment_cost,
        "unitCount4": unit_count4, "unitCount3": unit_count3, "unitCount2": unit_count2, "unitCount1": unit_count1
    }
    return summary


if __name__ == "__main__":
    print(get_investments())
