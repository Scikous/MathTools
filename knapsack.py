from queueOps import PriorityQueueObj

def greedy_budget(items: tuple, budget):
    prioritized = PriorityQueueObj(len(items))
    relative_utilities = []
    for item in items:
        usefulness = item[1]
        cost = item[2]
        relative_utility = usefulness/cost
        relative_utilities.append([item, relative_utility])

    def _priority_queue_set(relative_utilities):
        while len(relative_utilities) > 0:
            highest_priority = max(relative_utilities, key=lambda utility_val: utility_val[1])
            prioritized.add(highest_priority)
            relative_utilities.remove(highest_priority)
    _priority_queue_set(relative_utilities)

    expense_names = []
    total_utility = 0.00
    total_cost = 0
    while not prioritized.is_empty():
        expense = prioritized.get()
        cost = expense[0][2]
        if budget-cost >= 0:
            budget -= cost
            expense_names.append(expense[0][0])
            total_utility += expense[1]
            total_cost += cost

    print(f"Names of expenses: {expense_names}\nTotal cost: {total_cost}\nTotal utility: {total_utility}")
    return expense_names, total_cost, total_utility

B = 141700
potential_expenses = [('Work Stations', 6600, 58400), ('Mobile Devices', 5700, 58400),
                       ('Furniture', 3700, 30000), ('Summer Cottage', 3200, 50000)]
greedy_budget(potential_expenses, B)