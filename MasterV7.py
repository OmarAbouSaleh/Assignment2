# Bop Somboon 000889323      Omar Abou-Saleh 000860317   Chester Laraya 000847615        March 17 2023

# Constants to reduce hardcoding and make code more readable
TARGET_PROFIT = 10000
DAYS_OF_THE_WEEK = ["Monday", "Tuesday", "Wednesday",
            "Thursday", "Friday", "Saturday", "Sunday"]


# The supported phones and their pricing, which are used later to determine the profit for the period.
phone_prices = {
    "Apple iPhone": 120.45,
    "Android Phone": 99.50,
    "Apple Tablet": 75.69,
    "Android Tablet": 65.73,
    "Windows Tablet": 51.49,
}
phones = ["Apple iPhone",
    "Android Phone",
    "Apple Tablet",
    "Android Tablet",
    "Windows Tablet"]

week_type_statement = "1 - For specific Day" + "\n" + "2 - For the Week" + "\n" + \
    "3 - For Week Business Days" + "\n" + \
    "4 - For Weekend days" + "\n" + "0 - Exit" + "\n"
product_statement = "Enter product number 1-5, or enter 0 to stop: "
quantity_sold_statement = "Enter quantity sold: "
good_job_statement = "You did well this period! Keep up the great work!" + "\n"
bad_job_statement = "We didn't reach our goal for this period. More work is needed." + "\n"
opening_statement = "\nWelcome to Circle Phones' Profit calculator. You can calculate your profits for a specific day, by week or you can divide the week into weekdays and the weekend." + \
    '\n' + "\n" + "Welcome to Circle Phones Profit calculator." + "\n"
you_can_statement = "\nYou can calculate your profits for a specific day, by week or you can divide the week into weekdays and the weekend." + "\n" + "\n"
exit_statement = "Program Ended!"
# Constants End

# Program Start
# Starting the program with a welcome statement and a statement that tells the user what they can do with the program.
print(opening_statement)
print(you_can_statement)


# This is the list that we will use to calculate the profit for the days that the user entered.
weekdays = []
# Defining the profit for phones sold into a variable and setting it as 0 to start off with.
sold_phones_profit = 0
week_type = int(input(week_type_statement))

# This while loop will continue to run until the user enters 0 to exit the program.
while week_type > 0:
    # This if statement will check if the user entered 1, 2, 3 or 4. If the user enters 1, the program will ask the user to enter a specific day. If the user enters 2, the program will calculate the profit for the entire week. If the user enters 3, the program will calculate the profit for the weekdays. If the user enters 4, the program will calculate the profit for the weekend. If the user enters a value that isn't accepted by the program, the program will ask the user to enter a valid input.
    if week_type == 1:
        # This will ask the user to enter a specific day.
        individual_day = input(
            "Enter a specific day [" + ", ".join(DAYS_OF_THE_WEEK) + "]: ")
        # This will take the day that the user entered and put it into the weekdays list.
        weekdays.append(individual_day)
    elif week_type == 2:
        # This will take the entire list of days and put it into the weekdays list.
        weekdays = DAYS_OF_THE_WEEK
    elif week_type == 3:
        # This will only take the first 5 elements of the list, which are the weekdays.
        weekdays = DAYS_OF_THE_WEEK[0:5]
    elif week_type == 4:
        # This will only take the last 2 elements of the list, which are the weekend days.
        weekdays = DAYS_OF_THE_WEEK[5:7]
    else:
        print("Invalid input, please enter a valid input. ")
        week_type = int(input(week_type_statement))
        break  # This will break the loop and restart while loop.
    # This for loop will run for the amount of days that the user entered. If the user entered 1, the for loop will run once. If the user entered 2, the loop will run for the entire week, if the user enters 3, the loop will run for the business days, and if the user enters 4, the loop will run for only the weekend.
    for days in weekdays:  # This will run for the amount of days that the user entered.
        print(f"For {days}")  # This will print the day that the user entered.
        product_number = 1  # This will initialize the product number to 1.
        while product_number != 0:  # This will run until the user enters 0 to stop the loop.
            # This will ask the user to enter a product number.
            product_number = int(input(product_statement))
            # Error Checking
            if product_number == 0:  # This will break the loop if the user enters 0.
                break
            elif product_number > 5 or product_number < 0 :  # This will check if the user entered a valid product number. If the user enters a number that is greater than 5, the program will ask the user to enter a valid number.
                print("Invalid input, please enter a valid number")
                continue

            # This will ask the user to enter the quantity of the product that they sold.
            quantity_sold = int(input(quantity_sold_statement))
            phone_name = phones[product_number-1]
            sold_phones_profit += phone_prices[phone_name] * quantity_sold

    if week_type == 1:  # This will check if the user entered 1. If the user entered 1, the program will print the profit for the day that the user entered.
        print(
            "\n" + f"Your total profit for today is: ${sold_phones_profit:.2f}")
        if sold_phones_profit >= TARGET_PROFIT:  # This will check if the user made more than $10,000. If the user made more than $10,000, the program will print a good job statement. If the user made less than $10,000, the program will print a statement that tells the user that they need to work harder.
            print(good_job_statement)
        else:
            print(
                f"More work is needed.... The last {individual_day} wasn't the best")
    else:
        # This will print the profit for the week.
        print("\n"f"Your total profit this week is: ${sold_phones_profit:.2f}")
        if sold_phones_profit >= TARGET_PROFIT:  # This will check if the user made more than $10,000. If the user made more than $10,000, the program will print a good job statement. If the user made less than $10,000, the program will print a statement that tells the user that they need to work harder.
            print(good_job_statement)
        else:
            print(bad_job_statement)

    # This will reset the profit for the phones sold to 0.
    sold_phones_profit = 0
    print(you_can_statement)
    # This will ask the user to enter a new input.
    week_type = int(input(week_type_statement))
print(exit_statement)  # This will print the exit statement.
