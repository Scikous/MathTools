from queueOps import PriorityQueueObj

def greedy_budget(wishlist: list[tuple], budget: int|float):#using a greedy algorithm to find "best" items to take
    shopping_list = []

    for item in wishlist: #get a list of all relative_utility values
        utility = item[1]
        cost = item[2]
        relative_utility = utility/cost
        shopping_list.append([item, relative_utility])

    prioritized = PriorityQueueObj(len(wishlist))
    def _priority_queue_set(shopping_list):#populate the priority queue with the items from highest to lowest priority
        while len(shopping_list) > 0:
            highest_priority = max(shopping_list, key=lambda utility_val: utility_val[1])#find highest relative_utility value
            prioritized.add(highest_priority)
            shopping_list.remove(highest_priority)
    _priority_queue_set(shopping_list)

    total_relative_utility = 0.000
    total_utility = 0
    total_cost = 0
    while not prioritized.is_empty():#get list of items to buy, their total utility and their total cost
        expense = prioritized.get()
        cost = expense[0][2]
        if budget-cost >= 0:
            budget -= cost
            shopping_list.append(expense[0][0])
            total_relative_utility += expense[1]
            total_utility += expense[0][1]
            total_cost += cost

    print(f"Names of expenses: {shopping_list}\nTotal utility: {total_utility}\nTotal relative utility: {total_relative_utility:.3f}\nTotal cost: {total_cost}")
    return shopping_list, total_cost, total_utility, total_relative_utility

if __name__ == '__main__':
    budget = 141700 #budget
    wishlist = [('Work Stations', 6600, 58400), ('Mobile Devices', 5700, 58400),
                        ('Furniture', 3700, 30000), ('Summer Cottage', 3200, 50000)]
    wishlist2 = [('Work Stations', 6600, 68400), ('Mobile Devices', 5700, 40400),
                    ('Furniture', 3700, 32800), ('Summer Cottage', 3200, 20000)]
    greedy_budget(wishlist, budget) #finds the optimal solution
    greedy_budget(wishlist2, budget) #does not find the optimal solution