shopping_cart = {
    "Apple": 0.99,
    "Banana": 0.49,
    "Orange": 1.29,
    "Milk": 2.99,
    "Bread": 1.99
}

total_cost = 0

for item, price in shopping_cart.items():
    print(f"Item: {item}, Price: ${price:.2f}")
    total_cost += price

print(f"\nTotal Cost: ${total_cost:.2f}")
# The print statement is:


# print(f"Item: {item}, Price: ${price:.2f}")


# Here's a breakdown:

# - print(): This is the function that prints output to the screen.
# - f"": This is a formatted string literal, also known as an f-string. It allows you to embed expressions inside string literals.
# - Item: {item}: This will print the string "Item: " followed by the value of the item variable.
# - , Price: $: This will print a comma followed by the string " Price: $".
# - {price:.2f}: This will print the value of the price variable, formatted as a floating-point number with two decimal places.

# So, if item is "Apple" and price is 0.99, the output would be:


# Item: Apple, Price: $0.99
