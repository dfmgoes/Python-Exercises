from datetime import datetime
import pandas as pd


file = "C:\\Users\\Diogo\\Desktop\\test_excel.xlsx"
current_day_hour = datetime.now().strftime("%Y-%m-%d %H-%M-%S")

def viewex():
    print('lol')

def addex():
    try: 
        
        exchanges = int(input("Do you have anything you want to add?\n"
                              "1. Yes\n"
                              "2. No\n"
                              "Choose your option."))
        
       

        if exchanges == 1:

            amount = [int(input("How much did you spend?"))]
            data = {'Date': [current_day_hour],
                    'Amount': amount}
            df = pd.DataFrame(data)
            df.to_excel(file, index=True)
            addex()



        elif exchanges == 2:
            print('Broke ass...')

        else:
            print('insert good number')

    except ValueError:
        print("that is bad number....")
            

def calcex():
    print('test')
# try:
if 1 == 1:
    userchoice1 = int(input("Hello! Welcome to Mr. Jorge's Spectacular Interest-Free* Bank! Thank you for your preference!\n"
        "*Only applies to the bank's owner.\n"
        "\nWhat would you like to do today?\n"
        "1. View Expenses\n"
        "2. Add Expenses\n"
        "3. Calculate Total Expenses\n"
        "Choose your option(1-3): "))
    
    if userchoice1 == 1: # For viewing 
        print(pd.read_excel(file))

    elif userchoice1 == 2: # For Adding
        addex()
            


    elif userchoice1 == 3: # For summing
        print('3. yup')
    
    else:
        print('That is an incorrect option! Do you need help from our accounting services? Only 0.10 per help in choosing!')
    
# except ValueError:
#     print("oh no you're fucked")