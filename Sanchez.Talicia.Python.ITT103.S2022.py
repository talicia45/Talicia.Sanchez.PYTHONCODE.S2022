JamEx Limited requires a program to calculate and print the commission received by a
salesperson. The program should process an undetermined number of salespersons and 
appropriately terminate by a predefined input. The commission rate is based on two factors, 
the amount of sales and the class to which a salesperson belongs. The input will be the 
salesperson number, sales amount and class. The commission rate will be based on the 
following criteria:
Class=1
If sales is equal to or less than $1000, the rate is 6 percent.
If sales is greater than $1000 but less than $2000, the rate is 7 percent.
If the sales is $2000 or greater, the rate is 10 percent.
Class=2
If the sales is less than $1000, the rate is 4 percent.
If the sales is $1000 or greater, the rate is 6 percent






"""
- Author: Talicia Sanchez
- Date Created: April 4, 2022
- Course: ITT103
- Purpose:To run a salesperson information and
received the commission rate of that salesperson.
"""




def commissionCalculator(_class, sale):
    Class=int(_class)
    s_amount=float(sale)
        
    match Class:
               #Enter Class 1
               #if class 1 is amount of sales is <= $1000 then commission rate is 0.6
               # or is sales >=1000,but <= 2000 >= $2000 then the comission rate is 0.10 percent.

                case 1:
                    if s_amount <= 1000.0:
                        com_rate=(s_amount*6.0)/100
                        return com_rate
                    elif s_amount > 1000.0 and Sale < 2000.0:
                        com_rate=(s_amount*7.0)/100
                        return com_rate
                    else:
                        com_rate=(s_amount*10.0)/100
                        return com_rate
  
            #Enter class 2
            #if any sales that is >
            #or < 1000 then the comission rate is 0.4 or 0.6 percent .
                case 2:
                        if s_amount < 1000:
                            com_rate=(s_amount*4.0)/100
                            return com_rate
                        elif s_amount >= 1000:
                            com_rate=(s_amount*6.0)/100
                            return com_rate
               #Enter class 3
               #All sales amount has a rate of 0.045 percent.
                case 3:
                        com_rate=(s_amount*4.5)/100
                        return com_rate
                case _:
                        print("Class error. Please input valid class: 1, 2 or 3")
                        exit(1)

#Salesperson information

def main():
    SalespersonClass=0
    SalespersonID="Unknown"
    SalesPersonSale="0"
    while True:
        try:
            userInput=input("Welcome to Commission Calculator! Enter y/Y to continue or q/Q to terminate program \n")
            if userInput == "q" or userInput =="Q":
                print("Goodbye!")
                exit(0)
            elif userInput == "y" or userInput =="y":
                SalespersonClass=int(input("\nEnter Sales Person Class: 1, 2 or 3. "))
            else:
                print("Please enter a valid input")
                continue
        except ValueError:
            print("Value must be a Whole number")
            continue
        try:
            SalesPersonSale=float(input("\nEnter Sales Person Sale: eg 1000.0 for $1000. "))   
        except ValueError:
            print("Value must be a number")
            continue
        SalespersonID=input("\nEnter Sales Person ID ")
        break
      
    thisCommission=str(commissionCalculator(SalespersonClass, SalesPersonSale))

    print(SalespersonID+" has made $"+thisCommission+" Commission on a sale of $"+str(SalesPersonSale)+".")
    

if __name__ == "__main__":
    main()
                        
