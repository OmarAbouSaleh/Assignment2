#Bop Somboon 000889323      Omar Abou-Saleh 000860317   Chester Laraya 000847615        March 17 2023
 
#Setting the phone prices into a dictionary which we will then call upon to extract the value (profit for each phone) later in the program.
phones = { 
    "Apple iPhone" : 120.45,
    "Android Phone" : 99.50,
    "Apple Tablet" : 75.69,
    "Android Tablet" : 65.73,
    "Windows Tablet" : 51.49,
}

#Setting the statements into a variable to make the code more readable, and to also cut down on hardcoding.
input_statement = "1 - For specific Day" + "\n" + "2 - For the Week" + "\n" + "3 - For Week Business Days" + "\n" + "4 - For Weekend days" + "\n" + "0 - Exit" + "\n"
product_statement = "Enter product number 1-5, or enter 0 to stop: "
quantity_sold_statement = "Enter quantity sold: "
good_job_statement = "You did well this period! Keep up the great work!" + "\n"
bad_job_statement = "We didn't reach our goal for this period. More work is needed." + "\n"
opening_statement = "\nWelcome to Circle Phones' Profit calculator. You can calculate your profits for a specific day, by week or you can divide the week into weekdays and the weekend." + '\n' + "\n" +  "Welcome to Circle Phones Profit calculator." + "\n"
you_can_statement = "\nYou can calculate your profits for a specific day, by week or you can divide the week into weekdays and the weekend." + "\n" + "\n"
exit_statement = "Program Ended!"

STATEMENT_THRESHOLD = 10000 #This is the threshold that we will use to determine if the user did well or not.
week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"] #This is the list of days that we will use to calculate the profit for the entire week.
weekdays = [] #This is the list that we will use to calculate the profit for the days that the user entered.

#Defining the profit for phones sold into a variable and setting it as 0 to start off with.
sold_phones_profit = 0

#Starting the program with a welcome statement and a statement that tells the user what they can do with the program.
print(opening_statement)
print(you_can_statement)
#This initializes the program to go into a while loop that will continue to run until the user enters 0 to exit the program.
week_days_input = int(input(input_statement))

#This while loop will continue to run until the user enters 0 to exit the program.
while week_days_input > 0:
    #This if statement will check if the user entered 1, 2, 3 or 4. If the user enters 1, the program will ask the user to enter a specific day. If the user enters 2, the program will calculate the profit for the entire week. If the user enters 3, the program will calculate the profit for the weekdays. If the user enters 4, the program will calculate the profit for the weekend. If the user enters a value that isn't accepted by the program, the program will ask the user to enter a valid input.
    if week_days_input == 1:
        individual_day = input("Enter a specific day [Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday]: ") #This will ask the user to enter a specific day.
        weekdays.append(individual_day) #This will take the day that the user entered and put it into the weekdays list.
    elif week_days_input == 2:
        weekdays = week #This will take the entire list of days and put it into the weekdays list.
    elif week_days_input == 3:
        weekdays = week[0:5] #This will only take the first 5 elements of the list, which are the weekdays.
    elif week_days_input == 4:
        weekdays = week[5:7] #This will only take the last 2 elements of the list, which are the weekend days.
    else:
        print("Invalid input, please enter a valid input. ")
        week_days_input = int(input(input_statement))
        break #This will break the loop and restart while loop.
    #This for loop will run for the amount of days that the user entered. If the user entered 1, the for loop will run once. If the user entered 2, the loop will run for the entire week, if the user enters 3, the loop will run for the business days, and if the user enters 4, the loop will run for only the weekend.
    for days in weekdays: #This will run for the amount of days that the user entered.
        print(f"For {days}") #This will print the day that the user entered.
        product_number = 1 #This will initialize the product number to 1.
        while product_number > 0: #This will run until the user enters 0 to stop the loop.
            product_number = int(input(product_statement)) #This will ask the user to enter a product number.
            if product_number == 0: #This will break the loop if the user enters 0.
                break
            elif product_number > 5 : #This will check if the user entered a valid product number. If the user enters a number that is greater than 5, the program will ask the user to enter a valid number.
                    print("Invalid input, please enter a valid number") 
                    continue
            else: #This will run if the user enters a valid product number.
                quantity_sold = int(input(quantity_sold_statement)) #This will ask the user to enter the quantity of the product that they sold.
                if product_number == 1:
                    sold_phones_profit += phones["Apple iPhone"] * quantity_sold #This will calculate the profit for the phones that the user sold. This will happen for all of the phones sold until the user inputs 0.
                elif product_number == 2:
                    sold_phones_profit += phones["Android Phone"] * quantity_sold 
                elif product_number == 3:
                    sold_phones_profit += phones["Apple Tablet"] * quantity_sold
                elif product_number == 4:
                    sold_phones_profit += phones["Android Tablet"] * quantity_sold
                elif product_number == 5:
                    sold_phones_profit += phones["Windows Tablet"] * quantity_sold
                elif  product_number == 0: 
                    break
    if week_days_input == 1: #This will check if the user entered 1. If the user entered 1, the program will print the profit for the day that the user entered.
        print("\n"+ f"Your total profit for today is: ${sold_phones_profit:.2f}")
        if sold_phones_profit >= STATEMENT_THRESHOLD: #This will check if the user made more than $10,000. If the user made more than $10,000, the program will print a good job statement. If the user made less than $10,000, the program will print a statement that tells the user that they need to work harder.
            print(good_job_statement)
        else: 
            print(f"More work is needed.... The last {individual_day} wasn't the best") #This will print a statement that tells the user that they need to work harder.
    else: 
        print("\n"f"Your total profit this week is: ${sold_phones_profit:.2f}") #This will print the profit for the week.
        if sold_phones_profit >= STATEMENT_THRESHOLD: #This will check if the user made more than $10,000. If the user made more than $10,000, the program will print a good job statement. If the user made less than $10,000, the program will print a statement that tells the user that they need to work harder.
            print(good_job_statement)
        else: 
            print(bad_job_statement)
            
    sold_phones_profit = 0 #This will reset the profit for the phones sold to 0.
    print(you_can_statement) #This will print the statement that tells the user what they can do with the program.
    week_days_input = int(input(input_statement)) #This will ask the user to enter a new input.
print(exit_statement) #This will print the exit statement.