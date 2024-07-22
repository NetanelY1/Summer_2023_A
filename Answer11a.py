def calculate_total(prices, shopping_list):
    total = 0.0
    for item, quantity in shopping_list:
        if item in prices:
            total += prices[item] * quantity
    return total

# דוגמה לשימוש בפונקציה
prices = {'apple': 10.0, 'banana': 6.5, 'milk': 6.9}
shopping_list = [('apple', 3), ('milk', 2), ('coca-cola', 3)]

total_amount = calculate_total(prices, shopping_list)
print("The total amount:", total_amount)
