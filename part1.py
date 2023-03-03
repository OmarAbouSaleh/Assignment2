phones = {
    "Apple iPhone" : 120.45,
    "Android Phone" : 99.50,
    "Apple Tablet" : 75.69,
    "Android Tablet" : 65.73,
    "Windows Tablet" : 51.49,
}
sold_phones_profit = 0

loop_init = int(input("Enter product number 1-5, or enter 0 to stop: "))

while loop_init > 0:
    while loop_init == 1:
        sold_phones_profit += phones["Apple iPhone"] * int(input("Enter quantity sold: "))
        loop_init = int(input("Enter product number 1-5, or enter 0 to stop: "))
    while loop_init == 2:
        sold_phones_profit += phones["Android Phone"] * int(input("Enter quantity sold: "))
        loop_init = int(input("Enter product number 1-5, or enter 0 to stop: "))
    while loop_init == 3:
        sold_phones_profit += phones["Apple Tablet"] * int(input("Enter quantity sold: "))
        loop_init = int(input("Enter product number 1-5, or enter 0 to stop: "))
    while loop_init == 4:
        sold_phones_profit += phones["Android Tablet"] * int(input("Enter quantity sold: "))
        loop_init = int(input("Enter product number 1-5, or enter 0 to stop: "))
    while loop_init == 5:
        sold_phones_profit += phones["Windows Tablet"] * int(input("Enter quantity sold: "))
        loop_init = int(input("Enter product number 1-5, or enter 0 to stop: "))
    while loop_init > 5 :
        print("Invalid input, please enter a valid number")
        loop_init = int(input("Enter product number 1-5, or enter 0 to stop: "))

print(f"Your total profit for today is: ${sold_phones_profit}")
