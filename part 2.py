phones = {
    "Apple iPhone" : 120.45,
    "Android Phone" : 99.50,
    "Apple Tablet" : 75.69,
    "Android Tablet" : 65.73,
    "Windows Tablet" : 51.49,
}
sold_phones_profit = 0

weekday = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

week_profit = 0

week_init = int(input("Enter:\n 1 - For specific day \n 2 - For the Week \n 3 - for Week Business Days\n 4 - For weekends\n 0 to exit \n"))

loop_init = 0

if week_init == 2:
    for day in weekday:
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
            
        
    print(f"Total profit for the week is: ${week_profit:.2f}")

