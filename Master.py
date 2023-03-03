

phones = {
    "Apple iPhone" : 120.45,
    "Android Phone" : 99.50,
    "Apple Tablet" : 75.69,
    "Android Tablet" : 65.73,
    "Windows Tablet" : 51.49,
}


sold_phones_profit = 0
week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
week_days = week[0:5]
week_profit = 0
loop_init = 0
print("Enter:")
print("1 - For specific Day")
print("2 - For the Week")
print("3 - For Week Business Days")
print("4 - For Weekend days")
print("0 - Exit")
days = int(input(""))



if days == 1:
        day = input("Enter a specific day [Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday]: ")
        print(f"For {day}")
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
        print(f"Your total profit for today is: ${sold_phones_profit:.2f}")

if days == 2:
    loop_init = int(input("Enter product number 1-5, or enter 0 to stop: "))
    for day in week:
        print("For", day)
        sold_phones_profit = 0
        if loop_init == 0:
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
            while loop_init == 0:
                break

            week_profit += sold_phones_profit
    print(f"Your total profit for the week is: ${week_profit:.2f}")

if days == 3:
    for day in week_days:
        print("For", day)
        sold_phones_profit = 0
        if loop_init == 0:
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
            while loop_init == 0:
                break

            week_profit += sold_phones_profit
    print(f"Total Profit for the week (business days) is: ${week_profit:.2f}")

