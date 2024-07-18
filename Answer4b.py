from Answer4a import Time

# פונקציה להמרת קלט למספרים שלמים עבור שעה ודקות
def get_time_input(prompt):
    hour, minutes = map(int, input(prompt).split())
    return Time(hour, minutes)

# מספר משלוחים
num_deliveries = 100

for _ in range(num_deliveries):
    print("Enter the times for delivery:")

    # קבלת זמן קבלה בחברה
    received_time = get_time_input("Enter the received time (hour minute): ")

    # קבלת זמן מסירה ללקוח
    delivered_time = get_time_input("Enter the delivered time (hour minute): ")

    # חישוב ההפרש
    diff = received_time.difference(delivered_time)

    # בדיקה אם ההבטחה התקיימה והדפסת הודעה מתאימה
    if diff <= 180:
        print("The delivery was on time.")
    else:
        print("The delivery was late.")
