monthly_salary = float(input())
percentage_saved = float(input())
total_cost = float(input())
percentage_increase = float(input())
current_savings = 0
number_of_months = 1
total_cost -= monthly_salary*percentage_saved
while total_cost >= 0:
    total_cost += total_cost*percentage_increase
    total_cost -= monthly_salary*percentage_saved
    number_of_months += 1
    if monthly_salary*percentage_saved >= total_cost:
        number_of_months += 1
        break
print("Number of months: " + str(number_of_months))

# While making PS1, we exchanged ideas with my friend Gülnisa Yıldırım, and we did it by helping each other.
