import time
from termcolor import colored
from data import *
from math import ceil

##################### O03 #####################

def copper2silver(amount:int) -> float:
    return amount / 10

def silver2gold(amount:int) -> float:
    return amount / 5

def copper2gold(amount:int) -> float:
    return silver2gold(copper2silver(amount))

def platinum2gold(amount:int) -> float:
    return amount * 25

def getPersonCashInGold(personCash: dict) -> float:
    for item in personCash:
        if item == 'copper':
            personCash["gold"] += copper2gold(personCash[item])
        elif item == 'silver':
            personCash["gold"] += silver2gold(personCash[item])
        elif item == 'platinum':
            personCash["gold"] += platinum2gold(personCash[item])
    return personCash["gold"]

##################### O05 #####################

def getJourneyFoodCostsInGold(people:int, horses:int) -> float:
    people_cost = COST_FOOD_HUMAN_COPPER_PER_DAY * people
    horse_cost = COST_FOOD_HORSE_COPPER_PER_DAY * horses
    return round(copper2gold(JOURNEY_IN_DAYS * (people_cost + horse_cost)), 2)

##################### O06 #####################

def getFromListByKeyIs(list:list, key:str, value:any) -> list:
    sorted_list = []
    for dict in list:
        for item in dict:
            if item == key:
                if dict[item] == value:
                    sorted_list.append(dict)
    return sorted_list


def getAdventuringPeople(people:list) -> list:
    return getFromListByKeyIs(people, "adventuring", True)

def getShareWithFriends(friends:list) -> list:
    return getFromListByKeyIs(friends, "shareWith", True)

def getAdventuringFriends(friends:list) -> list:
    return getShareWithFriends(getAdventuringPeople(friends))

##################### O07 #####################

def getNumberOfHorsesNeeded(people:int) -> int:
    return ceil(people / 2)

def getNumberOfTentsNeeded(people:int) -> int:
    return ceil(people / 3)

def getTotalRentalCost(horses:int, tents:int) -> float:
    horse_cost = silver2gold(11 * (horses * COST_HORSE_SILVER_PER_DAY))
    tent_cost = 2 * (tents * COST_TENT_GOLD_PER_WEEK)
    return round(horse_cost + tent_cost, 2)

##################### O08 #####################

def getItemsAsText(items:list) -> str:
    return_str = ""
    for item in items:
        return_str += f"{item['amount']}{item['unit']} {item['name']}"
    if item == items[:-1]:
        return_str += " & "
    elif len(items) > 1:
        return_str += ", "
    return return_str

def getItemsValueInGold(items:list) -> float:
    pass

##################### O09 #####################

def getCashInGoldFromPeople(people:list) -> float:
    pass

##################### O10 #####################

def getInterestingInvestors(investors:list) -> list:
    pass

def getAdventuringInvestors(investors:list) -> list:
    pass

def getTotalInvestorsCosts(investors:list, gear:list) -> float:
    pass

##################### O11 #####################

def getMaxAmountOfNightsInInn(leftoverGold:float, people:int, horses:int) -> int:
    pass

def getJourneyInnCostsInGold(nightsInInn:int, people:int, horses:int) -> float:
    pass

##################### O13 #####################

def getInvestorsCuts(profitGold:float, investors:list) -> list:
    pass

def getAdventurerCut(profitGold:float, investorsCuts:list, fellowship:int) -> float:
    pass

##################### O14 #####################

def getEarnigs(profitGold:float, mainCharacter:dict, friends:list, investors:list) -> list:
    pass

##################### view functions #####################

def print_colorvars(txt:str='{}', vars:list=[], color:str='yellow') -> None:
    vars = map(lambda string, color=color: colored(str(string), color, attrs=['bold']) ,vars)
    print(txt.format(*vars))

def print_title(name:str) -> None:
    print_colorvars(vars=['=== [ {} ] ==='.format(name)], color='green')

def print_chapter(number:int, name:str) -> None:
    nextStep(2)
    print_colorvars(vars=['- CHAPTER {}: {} -'.format(number, name)], color='magenta')

def nextStep(secwait:int=1) -> None:
    print('')
    time.sleep(secwait)

def ifOne(amount:int, yes:str, no:str, single='een') -> str:
    text = yes if amount == 1 else no
    amount = single if amount == 1 else amount
    return '{} {}'.format(amount, text).lstrip()