import random
num_contributer=int(input("enter the no. of contributor"))

contributers = []
for i in range(num_contributer):
    name = input("Enter the name of contributor :",{i+1})
    contributers.append(name)
expenses=[]
for i in range(1, 11):
    title = input("Enter the title of expense : ",{i})
    amount = float(input("Enter the total amount: "))
    party = input("Enter the names : ").split(",")
    payer = input("Who paid ? : ",{', '.join(party)})

    expense = {
        "title": title,
        "amount": amount,
        "party": party,
        "payer": payer
    }
expenses.append(expense)
for expense in expenses:
    split=expense["amount"]/ len(expense["party"])
    print("title :",expense)
    print(" Payer: {expense['payer']}")
    for party in expense["party"]:
         if party==expense["payer"]:
             print(" {party} paid {expense}['amount']}")
         else:
           print(" {party} owes {expense['payer']} {split_amount:}")
           print()

   
             
              






