import time
from termcolor import colored
from data import *
from math import ceil, floor

##################### O03 #####################

def copper2silver(amount: int) -> float:
    return amount / 10

def silver2gold(amount: int) -> float:
    return amount / 5

def copper2gold(amount: int) -> float:
    return silver2gold(copper2silver(amount))

def platinum2gold(amount: int) -> float:
    return amount * 25

def getPersonCashInGold(personCash: dict) -> float:
    gold = personCash.get("gold", 0)
    if 'copper' in personCash:
        gold += copper2gold(personCash['copper'])
    if 'silver' in personCash:
        gold += silver2gold(personCash['silver'])
    if 'platinum' in personCash:
        gold += platinum2gold(personCash['platinum'])
    return gold

##################### O05 #####################

def getJourneyFoodCostsInGold(people: int, horses: int) -> float:
    people_cost = COST_FOOD_HUMAN_COPPER_PER_DAY * people
    horse_cost = COST_FOOD_HORSE_COPPER_PER_DAY * horses
    return round(copper2gold(JOURNEY_IN_DAYS * (people_cost + horse_cost)), 2)

##################### O06 #####################

def getFromListByKeyIs(lst: list, key: str, value: any) -> list:
    return [d for d in lst if d.get(key) == value]

def getAdventuringPeople(people: list) -> list:
    return getFromListByKeyIs(people, "adventuring", True)

def getShareWithFriends(friends: list) -> list:
    return getFromListByKeyIs(friends, "shareWith", True)

def getAdventuringFriends(friends: list) -> list:
    return getAdventuringPeople(getShareWithFriends(friends))

##################### O07 #####################

def getNumberOfHorsesNeeded(people: int) -> int:
    return ceil(people / 2)

def getNumberOfTentsNeeded(people: int) -> int:
    return ceil(people / 3)

def getTotalRentalCost(horses: int, tents: int) -> float:
    horse_cost = silver2gold(JOURNEY_IN_DAYS * (horses * COST_HORSE_SILVER_PER_DAY))
    tent_cost = ceil(JOURNEY_IN_DAYS / 7) * (tents * COST_TENT_GOLD_PER_WEEK)
    return round(horse_cost + tent_cost, 2)

##################### O08 #####################

def getItemsAsText(items: list) -> str:
    return_str = ""
    for i, item in enumerate(items):
        if i > 0:
            if i == len(items) - 1:
                return_str += " & "
            else:
                return_str += ", "
        return_str += f"{item['amount']}{item['unit']} {item['name']}"
    return return_str

def getItemsValueInGold(items: list) -> float:
    total_value = 0
    for item in items:
        price_type = item['price']['type']
        amount = item['amount']
        price_amount = item['price']['amount']
        if price_type == 'copper':
            price = copper2gold(price_amount)
        elif price_type == 'silver':
            price = silver2gold(price_amount)
        elif price_type == 'platinum':
            price = platinum2gold(price_amount)
        else:
            price = price_amount
        total_value += price * amount
    return float(total_value)

##################### O09 #####################

def getCashInGoldFromPeople(people: list) -> float:
    total_cash = 0
    for person in people:
        total_cash += getPersonCashInGold(person['cash'])
    return float(total_cash)

##################### O10 #####################

def getInterestingInvestors(investors: list) -> list:
    return [investor for investor in investors if investor['profitReturn'] <= 10]

def getAdventuringInvestors(investors: list) -> list:
    return [investor for investor in getInterestingInvestors(investors) if investor['adventuring']]

def getTotalInvestorsCosts(investors: list, gear: list) -> float:
    if not investors:
        return 0.0
    adventuring_investors = getAdventuringInvestors(investors)
    num_investors = len(adventuring_investors)
    rental_cost = getTotalRentalCost(num_investors, num_investors)
    food_cost = getJourneyFoodCostsInGold(num_investors, num_investors)
    items_cost = getItemsValueInGold(gear) if gear else 0
    total_cost = rental_cost + (num_investors * items_cost) + food_cost
    return float(total_cost)

##################### O11 #####################

def getMaxAmountOfNightsInInn(leftoverGold: float, people: int, horses: int) -> int:
    horse_cost_per_night = horses * copper2gold(COST_INN_HORSE_COPPER_PER_NIGHT)
    people_cost_per_night = people * silver2gold(COST_INN_HUMAN_SILVER_PER_NIGHT)
    total_cost_per_night = horse_cost_per_night + people_cost_per_night
    return floor(leftoverGold / total_cost_per_night)

def getJourneyInnCostsInGold(nightsInInn: int, people: int, horses: int) -> float:
    horse_cost_per_night = horses * copper2gold(COST_INN_HORSE_COPPER_PER_NIGHT)
    people_cost_per_night = people * silver2gold(COST_INN_HUMAN_SILVER_PER_NIGHT)
    total_cost_per_night = horse_cost_per_night + people_cost_per_night
    return round(nightsInInn * total_cost_per_night, 2)

##################### O13 #####################

def getInvestorsCuts(profitGold: float, investors: list) -> list:
    return [round(profitGold * investor['profitReturn'] / 100, 2) for investor in getInterestingInvestors(investors)]

def getAdventurerCut(profitGold: float, investorsCuts: list, fellowship: int) -> float:
    if not profitGold:
        return 0.0
    total_investor_cut = sum(investorsCuts)
    remaining_gold = profitGold - total_investor_cut
    return round(remaining_gold / fellowship, 2)

##################### O14 #####################

def getEarnigs(profitGold: float, mainCharacter: dict, friends: list, investors: list) -> list:
    people = [mainCharacter] + friends + investors
    earnings = []
    adventuringFriends = getAdventuringFriends(friends)
    interestingInvestors = getInterestingInvestors(investors)
    adventuringInvestors = getAdventuringInvestors(investors)
    investorsCuts = getInvestorsCuts(profitGold, investors)
    
    total_adventurers = 1 + len(adventuringFriends) + len(adventuringInvestors)
    total_adventurer_cut = getAdventurerCut(profitGold, investorsCuts, total_adventurers)
    
    cut_index = 0

    for person in people:
        name = person['name']
        start_cash = round(getCashInGoldFromPeople([person]), 2)
        end_cash = start_cash
        
        if person in interestingInvestors:
            end_cash += investorsCuts[cut_index]
            cut_index += 1
        elif person in adventuringFriends:
            end_cash -= 10
            for earning in earnings:
                if earning['name'] == mainCharacter['name']:
                    earning['end'] += 10
        
        if person == mainCharacter or person in adventuringInvestors or person in adventuringFriends:
            end_cash += total_adventurer_cut

        earnings.append({
            'name': name,
            'start': start_cash,
            'end': round(end_cash, 2)
        })

    return earnings

##################### view functions #####################

def print_colorvars(txt: str = '{}', vars: list = [], color: str = 'yellow') -> None:
    colored_vars = map(lambda string, color=color: colored(str(string), color, attrs=['bold']), vars)
    print(txt.format(*colored_vars))

def print_title(name: str) -> None:
    print_colorvars(vars=[f'=== [ {name} ] ==='], color='green')

def print_chapter(number: int, name: str) -> None:
    nextStep(2)
    print_colorvars(vars=[f'- CHAPTER {number}: {name} -'], color='magenta')

def nextStep(secwait: int = 1) -> None:
    print('')
    time.sleep(secwait)

def ifOne(amount: int, yes: str, no: str, single: str = 'een') -> str:
    text = yes if amount == 1 else no
    amount_str = single if amount == 1 else str(amount)
    return f'{amount_str} {text}'.lstrip()
