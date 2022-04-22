# The total savings at the end of the year should be +- 1000$ for the cost of the house.
# Search for a number between 0-1000. Then pull it back 4 steps.

monthly_salary = float(input())
total_cost = float(input())
percentage_increase = float(input())
percentage_salary_increase = float(input())


def num_months(monthly_salary, total_cost,
               percentage_increase, percentage_salary_increase):
    number_of_months = 1
    total_cost -= monthly_salary*(guess/10000.0)
    while total_cost >= 0:
        total_cost += total_cost*percentage_increase
        total_cost -= monthly_salary*(guess/10000.0)
        number_of_months += 1
        if number_of_months % 6 == 1:
            monthly_salary += monthly_salary*percentage_salary_increase
        if monthly_salary*(guess/10000.0) >= total_cost:
            number_of_months += 1
            break
    return number_of_months


def rem_debt(monthly_salary, total_cost,
             percentage_increase, percentage_salary_increase):
    number_of_months = 1
    total_cost -= monthly_salary*(guess/10000.0)
    while total_cost >= 0:
        total_cost += total_cost*percentage_increase
        total_cost -= monthly_salary*(guess/10000.0)
        number_of_months += 1
        if number_of_months % 6 == 1:
            monthly_salary += monthly_salary*percentage_salary_increase
        if monthly_salary*(guess/10000.0) >= total_cost:
            number_of_months += 1
            break
    return total_cost


epsilon = 1000
num_guesses = 1
low = 0.0
high = 10000.0
guess = (low+high)/2.0

while abs(rem_debt(monthly_salary, total_cost,
                   percentage_increase, percentage_salary_increase)) >= 0.0 \
        and num_months(monthly_salary, total_cost,
                       percentage_increase, percentage_salary_increase) != 48:
    if num_months(monthly_salary, total_cost,
                  percentage_increase, percentage_salary_increase) > 48:
        low = guess
    elif num_months(monthly_salary, total_cost,
                    percentage_increase, percentage_salary_increase) < 48:
        high = guess
    guess = (low + high) / 2.0
    num_guesses += 1

# print("Number of months:", num_months(monthly_salary, total_cost,
#                                       percentage_increase, percentage_salary_increase))
# print("Remaining debt:", rem_debt(monthly_salary, total_cost,
#                                   percentage_increase, percentage_salary_increase))

if num_months(monthly_salary, total_cost,
              percentage_increase, percentage_salary_increase) <= 48:
    print("The best saving rate:", guess/10000)
    print("The number of steps in bisection search:", num_guesses)
else:
    print("It is not possible to buy the house in four years")

