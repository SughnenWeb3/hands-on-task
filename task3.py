"""
Task 3: Pocket Money Records
You're building a small tracker for your younger sibling's weekly pocket money.
The amounts (in naira) for the past 5 weeks are stored like this:
money = [1000, 1200, 800, 1500, 1100]

1. Calculate and display the total amount received so far.
2. A mistake was made in the third week's entry (800). It should have been 1000. Fix it.
3. Display the list in reverse order to check most recent payments first.

→ Perform the corrections and computations, and print all results.
"""

money = [1000, 1200, 800, 1500, 1100]

sum = 1000 + 1200 + 800 + 1500 + 1100
print("The total amout is",sum)

money[2]= 1000
print("The new list", money)
print("The new list in reverse is ", money[::-1])
print("The final result is now ", money)
