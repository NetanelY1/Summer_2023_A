def check_missing_items(prices, sister_list):
    missing_items = []
    for item in sister_list:
        if item not in prices:
            missing_items.append(item)
    return missing_items

# דוגמה לשימוש בפונקציה
prices = {'apple': 10.0, 'banana': 6.5, 'milk': 6.9}
sister_list = ['milky', 'shoko', 'fries', 'apple']

missing_items = check_missing_items(prices, sister_list)
print("The products that are missing:", missing_items)
