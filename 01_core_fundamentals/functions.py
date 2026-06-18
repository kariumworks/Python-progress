def count_goal_days(steps_list):
    total = 0
    for steps in steps_list:
        if steps > 10000:
            total += 1
    return total
steps_list = [8250, 11000, 4500, 9000, 14000]
total = count_goal_days(steps_list)
print(f"You have reached your goal of 10000 steps {total} times!")