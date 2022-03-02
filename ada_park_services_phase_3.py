#
# Complete the 'calculate_profit_summary' function below.
#

SINGLE_DAY_PARKING = 10.0
SPECIAL_EVENT_TICKET = 20.0
TRASH_SERVICE = 14.99
BULK_TRASH_SERVICE = 60.0

def calculate_profit_summary(single_day_parking, event_tickets, trash_can_count):
    """
    Parameters:
        single_day_parking: The number of people who paid for parking at each park.
        event_tickets: The number of event tickets each park sold.
        trash_can_count: The number of trash cans maintained by each park.
    """

    highest_profit = None
    most_profitable_parks = []
    
    {
        "index": 0,
        "parking_income": 0.0,
        "event_income": 0.0,
        "costs": 0.0
    }
    
    for index in range(len(single_day_parking)):
        # Get income for parking & events
        parking_income = single_day_parking[index] * SINGLE_DAY_PARKING
        event_income = event_tickets[index] * SPECIAL_EVENT_TICKET
        park_total_income = parking_income + event_income

        # Get cost for trash maintenance
        discounted_groups = int(trash_can_count[index] / 5)
        discounted_trash_costs = discounted_groups * BULK_TRASH_SERVICE
        single_cans_count = trash_can_count[index] % 5
        single_can_costs = single_cans_count * TRASH_SERVICE
        total_garbage_costs = discounted_trash_costs + single_can_costs

        # Track most profitable parks after costs
        income_after_costs = park_total_income - total_garbage_costs
        if highest_profit is None or income_after_costs >= highest_profit:
            park_data = {
                "index": index,
                "parking_income": parking_income,
                "event_income": event_income,
                "costs": total_garbage_costs
            }

            if income_after_costs == highest_profit:
                most_profitable_parks.append(park_data)
            else:
                highest_profit = income_after_costs
                most_profitable_parks = [park_data]

    return most_profitable_parks

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
for park in park_data:
    print(f"Park #{park['index']}")
    print(f"Parking income: ${park['parking_income']:.2f}")
    print(f"Event income: ${park['event_income']:.2f}")
    print(f"Costs: ${park['costs']:.2f}")
    print()