# This program is to determine how much money one has to spend before he wins money.
from random import shuffle
from random import randrange

# Define the global variable
DAYS_IN_WEEK = 7


def find(number_of_days):
    # Assume that years is
    # of 365 days.
    year = int(number_of_days / 365)
    week = int((number_of_days % 365) /
               DAYS_IN_WEEK)
    days = (number_of_days % 365) % DAYS_IN_WEEK

    return year, week, days


def lotto_num():
    """
    This is a doc string for lotto num function....
    """
    numbers = list(range(10))
    finalpick = []
    for itr in range(3):
        shuffle(numbers)
        # finalpick.append(numbers.pop())
        finalpick.append(numbers[randrange(10)])
    # finalpick.sort()
    return finalpick


def pick_num():
    rand_10_pick = []
    # the value in range is number of tickets bought in that day
    for j in range(100):
        rand_10_pick.append(lotto_num())
    #    print(f"Lucky rand picked list is {rand_10_pick}")

    return rand_10_pick


total_cost_list = []

for i in range(1000):
    count = 0

    while True:
        count += 1
        code_pick = lotto_num()
        todays_pick = pick_num()

        if code_pick in todays_pick:
            break

    # while todays_pick != code_pick:
    #    code_pick = lotto_num()
    #    count += 1
    # call find function to determine how long it has taken to win the lottery.
    Y1, W1, D1 = find(count)

    print(f'Hurray you have won in the iteration {count} after {Y1} years {W1} weeks and {D1} '
          f'days with the pick {code_pick} - Total cost ${count * 100}')

    total_cost_list.append(count * 100)

print(f"Total cost of the play is ${sum(total_cost_list)} and winning amount is ${1000 * 500}")
