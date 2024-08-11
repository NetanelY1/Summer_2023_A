# List of valid prefixes
valid_prefixes = ["050", "051", "052", "053", "054", "055", "056", "057", "058"]

# Variable to count the number of strings entered
count = 0

while True:
    # Input a string from the user
    phone_number = input("Please enter a mobile number: ")
    count += 1

    # Check if the string meets the conditions
    if (len(phone_number) == 11 and
        phone_number[:3] in valid_prefixes and
        phone_number[3] == '-' and
        phone_number[4:].isdigit()):
        
        print(f"A valid mobile number has been entered: {phone_number}")
        break  # End the loop when a valid string is entered

# Print the number of strings entered
print(f"Number of strings entered: {count}")
