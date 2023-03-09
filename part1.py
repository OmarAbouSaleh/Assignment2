phones = {
    "Apple iPhone" : 120.45,
    "Android Phone" : 99.50,
    "Apple Tablet" : 75.69,
    "Android Tablet" : 65.73,
    "Windows Tablet" : 51.49,
}
sold_phones_profit = 0
week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
weekdays = []
week_days_input = int(input("1 - For specific Day" + "\n" + "2 - For the Week" + "\n" + "3 - For Week Business Days" + "\n" + "4 - For Weekend days" + "\n" + "0 - Exit" + "\n"))
product_number = 1
while week_days_input > 0:
    if week_days_input == 1:
        weekdays = 1
    elif week_days_input == 2:
        weekdays = week
    elif week_days_input == 3:
        weekdays = week[0:5]
    elif week_days_input == 4:
        weekdays = week[5:7]
    else:
        break

    for days in weekdays:
        print(f"For {days}")
        product_number = int(input("Enter product number 1-5, or enter 0 to stop: "))
        while product_number > 0:
            if product_number == 1:
                sold_phones_profit += phones["Apple iPhone"] * int(input("Enter quantity sold: "))
                product_number = int(input("Enter product number 1-5, or enter 0 to stop: "))
            elif product_number == 2:
                sold_phones_profit += phones["Android Phone"] * int(input("Enter quantity sold: "))
                product_number = int(input("Enter product number 1-5, or enter 0 to stop: "))
            elif product_number == 3:
                sold_phones_profit += phones["Apple Tablet"] * int(input("Enter quantity sold: "))
                product_number = int(input("Enter product number 1-5, or enter 0 to stop: "))
            elif product_number == 4:
                sold_phones_profit += phones["Android Tablet"] * int(input("Enter quantity sold: "))
                product_number = int(input("Enter product number 1-5, or enter 0 to stop: "))
            elif product_number == 5:
                sold_phones_profit += phones["Windows Tablet"] * int(input("Enter quantity sold: "))
                product_number = int(input("Enter product number 1-5, or enter 0 to stop: "))
            elif product_number > 5 :
                print("Invalid input, please enter a valid number")
            elif product_number == 0:
                break
            else:
                print("Invalid input, please enter a valid number")
    


print(f"Your total profit for today is: ${sold_phones_profit}")