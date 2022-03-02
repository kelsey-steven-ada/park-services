# Coding Challenge: Ada’s Park Services

## Assignment
At Ada’s Park Services we need to know how much we are spending on each park compared to the income it generates for upkeep. You are going to work collaboratively with your interviewer to create a program that will help Ada track the profit from parks she maintains during your pair programming interview. You do not need to complete this solution before the interview. 

**Requirements**
- You must accept user input via the function parameters.
- You must use at least one loop or iterator.
- You must use at least one Dictionary or List to store your data. 

## Phase 1 Problem Statement
- Each park tracks the number of people who paid for parking, the number of event tickets sold, and the number of trash cans that they maintain. All values are integers.
- The function accepts 3 lists as parameters: `paid_parking_count`,  `event_ticket_count`, and `trash_can_count`
- Parking is $10, event tickets are $20, and trash cans cost $14.99 each to maintain
- Return the index of the park that made the most money after maintenance costs, along with total income, and maintenance cost.

## Phase 2 Problem Statement
Ada was able to negotiate a bulk deal for waste management. 
- Trash service in groups of 5 cans is now $60
- Trash service for individual cans is still $14.99
If a park had 8 trash cans, it would cost $60 for the first 5, and $14.99 each for the remaining 3.

Adjust the calculations for this discount and also return how much the park saved with bulk waste management.

## Further improvements: Handling ties
- When multiple parks make the same amount in profits, return a list including each of the most profitable parks.
- Print out the index of each park along with all their incomes and costs.

    ```
    Park #0
    Parking income: $200.00
    Event income: $0.00
    Costs: $120.00
    
    Park #2
    Parking income:: $100.00
    Event income: $100.00
    Costs: $120.00
    ```
