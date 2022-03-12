bank_deposit = float(input("enter the deposit money: "))
#variable to store the amount of money in your bank account.
interest_rate = float(input("enter the interset rate per year: "))
#variable to store the interest rate .
interest_rate = interest_rate / 100
#to accept numbers like(30,40) and convert it to(30%, 40%).
num_of_years = int(input("enter number of years: "))
#variable to store num of years you want to show ur bank balance throughout.
bank_balance = 0
#variable to store the money after years from getting benefits of the interest rate.
year_counter = 2022
#variable to store the year's date to be more specific when we print it.
for year in range(num_of_years + 1):
    # a for loop to iterate num_of_years time.
    bank_deposit = bank_deposit + (bank_deposit*interest_rate)
    #the most important operation in which we update the value of this variable to make equal the new value(money after getting benefits)
    bank_balance = bank_deposit
    #updating the value of the bank_balance variable to print it.
    year_counter = year_counter + 1
    #increasing the variable value to be realistic and specific while printing it.
    print("year: ", year_counter, "\t\t\t\t\t\t\t", "this year's amount of money in ur account: ", bank_balance)
