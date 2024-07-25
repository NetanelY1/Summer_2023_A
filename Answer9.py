# תשובה מפורטת מעבר למה שנדרש בשאלה.

# לדעתי התשובה לסעיף ג היא שלילית,
# כי הפונקציה בודקת האם העצמים שווים,
# אך יתכן כמו בדוגמה שצירפתי שיהיו 2 מספרים שיוצרים אותו עצם,
# אך המספרים בעצמם אינים שווים.


class Digits:
    def __init__(self, number):
        self.arr_digits = [0] * 10
        for digit in str(number):
            self.arr_digits[int(digit)] += 1

    def equals(self, other):
        """
        Checks if two Digits objects have the same frequency of digits.
        Note: This does not account for the order of digits.
        """
        if not isinstance(other, Digits):
            return False
        return self.arr_digits == other.arr_digits

    def compare_to(self, other):
        """
        Compares two Digits objects based on the frequency of digits.
        Returns:
        1 if this object represents a larger number.
        2 if this object represents a smaller number.
        0 if the numbers are considered equal based on digit frequency.
        Note: This does not account for the order of digits.
        """
        if not isinstance(other, Digits):
            return None
        
        for i in range(9, -1, -1):
            if self.arr_digits[i] > other.arr_digits[i]:
                return 1
            elif self.arr_digits[i] < other.arr_digits[i]:
                return 2
        return 0
    
    def __str__(self):
        result = []
        for i in range(10):
            if self.arr_digits[i] > 0:
                result.append(f"{i} appears {self.arr_digits[i]} times")
        
        # Building the table representation with vertical lines
        table_header = "Digit:       | " + " | ".join(f"{i}" for i in range(10)) + " |"
        line = "             " + "+" + "---+" * 10
        table_counts = "Occurrences: | " + " | ".join(f"{self.arr_digits[i]}" for i in range(10)) + " |"
        
        return ", ".join(result) + "\n\n" + table_header + "\n" + line + "\n" + table_counts


# דוגמאות שימוש
num1 = 9922
num2 = 2299

dg1 = Digits(num1)
dg2 = Digits(num2)

print("num1: ", num1)
print("num2: ", num2)


# הצגת העצמים באמצעות __str__
print("Digits for num1:")
print(dg1)

print("Digits for num2:")
print(dg2)

# בדיקת שוויון
if dg1.equals(dg2):
    print("The numbers are equal")
else:
    print("The numbers are not equal")

# השוואה בין המספרים
comparison = dg1.compare_to(dg2)
if comparison == 1:
    print("The first number is greater than the second number.")
elif comparison == 2:
    print("The first number is less than the second number.")
else:
    print("There is no clear answer.")


# דוגמת שימוש עם קלט מהמשתמש
def main():
    num1 = int(input("first number: "))
    num2 = int(input("second number: "))

    dg1 = Digits(num1)
    dg2 = Digits(num2)

    # הצגת העצמים באמצעות __str__
    print("\nDigits for num1:")
    print(dg1)

    print("\nDigits for num2:")
    print(dg2)

    # בדיקת שוויון
    if dg1.equals(dg2):
        print("\nThe numbers are equal")
    else:
        print("\nThe numbers are not equal")

    # השוואה בין המספרים
    comparison = dg1.compare_to(dg2)
    if comparison == 1:
        print("The first number is greater than the second number.")
    elif comparison == 2:
        print("The first number is less than the second number.")
    else:
        print("There is no clear answer.")

# הרצת דוגמת השימוש
if __name__ == "__main__":
    main()
