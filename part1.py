phones = {
    "Apple iPhone" : 120.45,
    "Android Phone" : 99.50,
    "Apple Tablet" : 75.69,
    "Android Tablet" : 65.73,
    "Windows Tablet" : 51.49,
}

sold_phones_profit = 0
week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
week_days_input = int(input("1 - For specific Day" + "\n" + "2 - For the Week" + "\n" + "3 - For Week Business Days" + "\n" + "4 - For Weekend days" + "\n" + "0 - Exit" + "\n"))
week_profit = 0

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
        week_days_input = int(input("1 - For specific Day" + "\n" + "2 - For the Week" + "\n" + "3 - For Week Business Days" + "\n" + "4 - For Weekend days" + "\n" + "0 - Exit" + "\n"))
    for days in weekdays:
        print(f"For {days}")
        product_number = int(input("Enter product number 1-5, or enter 0 to stop: "))
        while product_number > 0:
            if product_number == 1:
                quantity_sold = int(input("Enter quantity sold: "))
                sold_phones_profit += phones["Apple iPhone"] * quantity_sold
                product_number = int(input("Enter product number 1-5, or enter 0 to stop: "))
            elif product_number == 2:
                quantity_sold = int(input("Enter quantity sold: "))
                sold_phones_profit += phones["Android Phone"] * quantity_sold
                product_number = int(input("Enter product number 1-5, or enter 0 to stop: "))
            elif product_number == 3:
                quantity_sold = int(input("Enter quantity sold: "))
                sold_phones_profit += phones["Apple Tablet"] * quantity_sold
                product_number = int(input("Enter product number 1-5, or enter 0 to stop: "))
            elif product_number == 4:
                quantity_sold = int(input("Enter quantity sold: "))
                sold_phones_profit += phones["Android Tablet"] * quantity_sold
                product_number = int(input("Enter product number 1-5, or enter 0 to stop: "))
            elif product_number == 5:
                quantity_sold = int(input("Enter quantity sold: "))
                sold_phones_profit += phones["Windows Tablet"] * quantity_sold
                product_number = int(input("Enter product number 1-5, or enter 0 to stop: "))
            elif product_number > 5 :
                print("Invalid input, please enter a valid number")
                product_number = int(input("Enter product number 1-5, or enter 0 to stop: "))
            elif  product_number == 0: 
                break
            week_profit += sold_phones_profit
    if week_days_input == 1:
        print(f"Your total profit for today is: ${week_profit}")
        if sold_phones_profit >= 10000:
            print("You did well this period! Keep up the great work!")
        else:
            print("We didn't reach our goal for this period. More work is needed.")
    elif week_days_input == 2:
        print(f"Your total profit this week is: ${week_profit}")
        if week_profit >= 10000:
            print("You did well this period! Keep up the great work!")
        else:
            print("We didn't reach our goal for this period. More work is needed.")
    elif week_days_input == 3:
        print(f"Your total profit for today is: ${week_profit}")
        if week_profit >= 10000:
            print("You did well this period! Keep up the great work!")
        else:
            print("We didn't reach our goal for this period. More work is needed.")
    elif week_days_input == 4:
        print(f"Your total profit for today is: ${week_profit}")
        if week_profit >= 10000:
            print("You did well this period! Keep up the great work!")
        else:
            print("We didn't reach our goal for this period. More work is needed.")
    week_days_input = int(input("1 - For specific Day" + "\n" + "2 - For the Week" + "\n" + "3 - For Week Business Days" + "\n" + "4 - For Weekend days" + "\n" + "0 - Exit" + "\n"))
    week_profit = 0

