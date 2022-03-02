#
# Complete the 'calculate_profit_summary' function below.
#

SINGLE_DAY_PARKING = 10.0
SPECIAL_EVENT_TICKET = 20.0
TRASH_SERVICE = 14.99

def calculate_profit_summary(single_day_parking, event_tickets, trash_can_count):
    """
    Parameters:
        single_day_parking: The number of people who paid for parking at each park.
        event_tickets: The number of event tickets each park sold.
        trash_can_count: The number of trash cans maintained by each park.
    """

    highest_profit = None
    most_profitable_park = {
        "index": 0,
        "income": 0.0,
        "costs": 0.0
    }
    
    for index in range(len(single_day_parking)):
        # Get income for parking & events
        parking_income = single_day_parking[index] * SINGLE_DAY_PARKING
        event_income = event_tickets[index] * SPECIAL_EVENT_TICKET
        park_total_income = parking_income + event_income

        # Get cost for trash maintenance
        garbage_costs = trash_can_count[index] * TRASH_SERVICE

        # Track most profitable park after costs
        income_after_costs = park_total_income - garbage_costs
        if highest_profit is None or income_after_costs > highest_profit:
            highest_profit = income_after_costs
            most_profitable_park["index"] = index
            most_profitable_park["income"] = park_total_income
            most_profitable_park["costs"] = garbage_costs

    return most_profitable_park

# Test Data
# All positive profit
# parking_input = [13, 25, 12]
# events_input = [4, 2, 1]
# trash_can_input = [5, 9, 6]

# All negative profit
# parking_input = [6, 14, 20]
# events_input = [1, 0, 1]
# trash_can_input = [8, 10, 15]

# Park #3 with negative profit
# parking_input = [10, 7, 8]
# events_input = [0, 2, 1]
# trash_can_input = [5, 4, 8]

# 2 parks have the same profit
parking_input = [12, 20, 10]
events_input = [1, 0, 5]
trash_can_input = [6, 5, 5]

# All parks have the same profit
# parking_input = [20, 0, 10]
# events_input = [0, 10, 5]
# trash_can_input = [5, 5, 5]

# Only one input
# parking_input = [16]
# events_input = [3]
# trash_can_input = [7]

# More than 3 inputs
# parking_input = [13, 25, 12, 10, 17]
# events_input = [4, 2, 1, 0, 3]
# trash_can_input = [5, 9, 6, 4, 7]

park_data = calculate_profit_summary(parking_input, events_input, trash_can_input)
print(park_data)