#Stock Portfolio Tracker

from datetime import date

stock_prices = {
    "APPLE": 202.50,    
    "MICROSOFT": 460.75,    
    "GOOGLE": 175.20,  
    "AMAZON": 215.40,    
    "META": 680.15,   
    "NVIDIA": 142.30,    
    "TESLA": 345.80,    
    "NETFLIX": 1220.50,   
    "AMD": 165.25,     
    "INTEL": 22.40      
}

def calculate_investment():
    name = input("Enter stock name: ").upper()
    if name not in stock_prices.keys():
        print("Stock Not Found")
    else:
        try:
            quantity = int(input("Enter quantity:"))
            print(f"\033[32mStock Price are : ${stock_prices[name]}\033[0m")
            investment = stock_prices[name]*quantity
            print(f"\033[32mYour investment are : ${investment}\033[0m")
            #Saving investments in a file
            with open("investment.txt","a") as file1:
                file1.write(f"{date.today()} -- ")
                file1.write(f"{name}: ${investment}\n")
        except ValueError as e:
            print("\033[32mEnter a Valid Integer.\033[0m")
            
        
def view_investments():
    with open("investment.txt","r")as file2:
        for line in file2:
            f3=file2.read()
        if not f3:
            print("\033[32mYou have no investments\033[0m")
        else:
            print("\033[32mYour Investments are:\033[0m")
            print(f3)
    

if __name__=="__main__":
    while True:
        print("\033[33m---Welcome to Stock Portfolio Tracker---\033[0m")
        print("1.Calculate Investment Price")
        print("2.View Investments")
        print("3.Exit")

        choice = input("Enter your choice").strip()

        if choice == "1":
            calculate_investment()
        elif choice == "2":
            view_investments()
        
        elif choice == "3":
            print("\033[32mExiting...\033[0m")
            exit()
        
        else:
            print("Invalid Input")



    
    
    
