class Coffee:
    def __init__(self, name, kind, strength, price): 
        self.name = name 
        self.kind = kind 
        self.strength = strength 
        self.price = price 

    def __str__(self) -> str:
        str1 = f"Name: {self.name}, Kind: {self.kind}, Strength: {self.strength}, Price: {self.price}"
        return str1

def same_products(crr):
    if len(crr) == 0:
        return True  # אם הרשימה ריקה, נחשיב את זה כאילו כל הקפסולות מאותו יצרן
    
    first_product_name = crr[0].name  # שם היצרן של הקפסולה הראשונה ברשימה
    
    for coffee in crr:
        if coffee.name != first_product_name:
            return False  # אם מצאנו קפסולה עם יצרן שונה, נחזיר False
    
    return True  # אם עברנו על כל הקפסולות ולא מצאנו שונות, נחזיר True

def weak_sorts(crr, num):
    weak_coffees = []  # רשימה חדשה לאחסון סוגי הקפה החלשים
    
    for coffee in crr:
        if coffee.strength < num:
            weak_coffees.append(coffee.kind)  # אם רמת החוזק של הקפסולה קטנה מ-num, נוסיף את סוג הקפה לרשימה
    
    return weak_coffees  # נחזיר את הרשימה

def most_expensive(crr):
    if len(crr) == 0:
        print("No coffees in the list.")
        return  # אם הרשימה ריקה, נדפיס הודעה ונצא מהפעולה
    
    max_price = crr[0].price  # נתחיל עם מחיר הקפסולה הראשונה כיקר ביותר
    
    for coffee in crr:
        if coffee.price > max_price:
            max_price = coffee.price  # נעדכן את המחיר היקר ביותר אם מצאנו קפסולה יקרה יותר
    
    expensive_coffees = []  # רשימה חדשה לאחסון הקפסולות היקרות ביותר
    
    for coffee in crr:
        if coffee.price == max_price:
            expensive_coffees.append(coffee)  # אם המחיר של הקפסולה שווה למחיר היקר ביותר, נוסיף אותה לרשימה
    
    for coffee in expensive_coffees:
        print(coffee)
        # נדפיס את פרטי הקפסולה


# יצירת רשימה של קפסולות לדוגמה
coffees = [
    Coffee("BrandA", "Espresso", 5, 10.0),
    Coffee("BrandA", "Americano", 4, 15.0),
    Coffee("BrandA", "Latte", 3, 15.0),
    Coffee("BrandB", "Mocha", 6, 12.0)
]

# בדיקת אם כל הקפסולות מאותו יצרן
print(same_products(coffees))  # פלט: False

# קבלת רשימת סוגי קפה שרמת החוזק שלהם קטנה מ-5
print(weak_sorts(coffees, 5))  # פלט: ['Americano', 'Latte']

# הדפסת פרטי הקפסולות היקרות ביותר
most_expensive(coffees)
# פלט:
# Name: BrandA, Kind: Americano, Strength: 4, Price: 15.0
# Name: BrandA, Kind: Latte, Strength: 3, Price: 15.0
