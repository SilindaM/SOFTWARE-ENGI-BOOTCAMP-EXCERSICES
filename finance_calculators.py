import math


print("Choose either 'investment' or 'bond from the menu to proceed\n")
print("investment             -   to calculate the amount of interest you'll earn on interest")
print("bond                   -   to calculate the amount you'll have to pay on a home load ")

types=str(input("Choose your calculation\n"))

if types=="investment":
    deposit=int(input("enter money to deposit\n"))
    interestrate=int(input("enter interest rate\n"))
    deposityears=int(input("enter number of years you plan on investing for\n"))
    interest=str(input("you want simple or compound interest\n"))
    amount=1

    if(interest=="simple"):
        amount=deposit*(1+(interestrate/100)*deposityears)
        print(amount)
    elif(interest=="compound"):
        amount=deposit*(math.pow((1+(interestrate/100)),deposityears))
        print(amount)

elif types=="bond":
      value=int(input("enter value of the house\n"))
      interestrate=int(input("enter interest rate\n"))
      months=int(input("enter the months to repay\n"))
      repayment=1

      repayment=((interestrate/100)*value)/((1)-(math.pow((1+(interestrate/100)),(-months))))
      print(f"The monthly payment is {repayment} ")
